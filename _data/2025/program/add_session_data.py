import io
import sys
import csv
import requests
import pandas as pd
from collections import Counter
from typing import Optional, Tuple

# ----------------------------
# Helpers
# ----------------------------

def load_google_sheet_as_csv(sheet_id: str, gid: Optional[str] = None) -> pd.DataFrame:
    """
    Download a Google Sheet as CSV with explicit UTF-8 handling.
    Cleans up potential encoding issues in text fields.
    """
    base = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
    url = f"{base}&gid={gid}" if gid else base

    resp = requests.get(url)
    resp.raise_for_status()

    csv_text = resp.content.decode("utf-8")
    df = pd.read_csv(io.StringIO(csv_text), dtype=str, keep_default_na=False)

    # Clean all text fields for common UTF-8 misreads such as stray Â and Â°
    df = df.applymap(clean_text_encoding)
    return df

def clean_text_encoding(value: str) -> str:
    """
    Fix common misdecoded characters from UTF-8 to Latin-1 confusion.
    """
    if isinstance(value, str):
        value = value.replace("Â°", "°")
        value = value.replace("Â", "")
        return value
    return value

def normalize_text(s):
    if pd.isna(s):
        return s
    return " ".join(str(s).strip().split())

def most_frequent_session_row(df: pd.DataFrame) -> pd.Series:
    """
    Select the most frequent quadruple of
    Session Day, Session Start Time, Session End Time, Session Location
    for a given Session Title. Ties break deterministically.
    """
    quads = list(
        map(
            tuple,
            df[["Session Day", "Session Start Time", "Session End Time", "Session Location"]]
            .to_records(index=False),
        )
    )
    counts = Counter(quads)
    best = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[0][0]
    return pd.Series(
        {
            "Session Day": best[0],
            "Session Start Time": best[1],
            "Session End Time": best[2],
            "Session Location": best[3],
        }
    )

def any_missing(df: pd.DataFrame, cols: Tuple[str, ...]) -> pd.Series:
    """
    Identify rows with missing values for any of the given columns.
    Treat NaN and empty strings as missing.
    """
    mask = False
    for c in cols:
        mask = mask | df[c].isna() | (df[c].astype(str).str.strip() == "")
    return mask

# ----------------------------
# Main
# ----------------------------

def main():
    # Inputs
    flat_sessions_path = "ismar_sessions_flat.csv"  # Local CSV with session metadata
    google_sheet_id = "1Cfo14TFRp_zsGoGzODodnzPRTEob--MRpxzlSYGEbZQ"  # ProgramISMAR_restructured
    google_gid = None  # Use a string such as "0" if targeting a specific tab

    # Output
    output_csv = "ProgramISMAR_with_sessions.csv"

    # Load sources
    flat = pd.read_csv(flat_sessions_path, dtype=str, keep_default_na=False)
    # Clean any misdecoded characters in the flat file as well, for safety
    flat = flat.applymap(clean_text_encoding)

    program = load_google_sheet_as_csv(google_sheet_id, google_gid)

    # Validate program columns
    expected_program_cols = ["Paper ID", "Paper Title", "Session Title"]
    missing_program = [c for c in expected_program_cols if c not in program.columns]
    if missing_program:
        raise ValueError(f"Google Sheet is missing columns: {missing_program}")

    # Validate flat sessions columns
    needed_cols = [
        "Session Title",
        "Session Day",
        "Session Start Time",
        "Session End Time",
        "Session Location",
    ]
    missing_flat = [c for c in needed_cols if c not in flat.columns]
    if missing_flat:
        raise ValueError(f"{flat_sessions_path} is missing columns: {missing_flat}")

    # Normalize titles
    flat["Session Title"] = flat["Session Title"].map(normalize_text)
    program["Session Title"] = program["Session Title"].map(normalize_text)

    # Keep only sessions that appear in the Google Sheet
    valid_titles = set(program["Session Title"].dropna().unique())
    flat = flat[flat["Session Title"].isin(valid_titles)]

    # Drop exact duplicate rows in flat data
    flat = flat.drop_duplicates()

    # Collapse to one row per Session Title by most frequent quadruple
    resolved = (
        flat.groupby("Session Title", as_index=False)
        .apply(most_frequent_session_row)
        .reset_index(drop=True)
    )

    # Merge into program
    merged = program.merge(
        resolved,
        on="Session Title",
        how="left",
        validate="m:1"  # many papers to one session row
    )

    # Identify rows with missing session info including location
    required_cols = ("Session Day", "Session Start Time", "Session End Time", "Session Location")
    missing_mask = any_missing(merged, required_cols)
    num_missing = int(missing_mask.sum())

    # Print clear warning and list excluded rows
    if num_missing > 0:
        print("\n" + "=" * 78)
        print("WARNING: Some papers are missing session information including location")
        print(f"Total rows with missing session data: {num_missing}")
        print("These rows will be EXCLUDED from the final output")
        print("=" * 78 + "\n")

        missing_cols_display = list(required_cols)
        show_cols = ["Paper ID", "Paper Title", "Session Title"] + missing_cols_display
        missing_rows = merged.loc[missing_mask, show_cols].fillna("")
        print("Rows excluded:\n")
        for _, row in missing_rows.iterrows():
            print(
                f"Paper ID: {row['Paper ID']}, "
                f"Title: {row['Paper Title']}, "
                f"Session Title: {row['Session Title']}, "
                f"Session Day: {row['Session Day']}, "
                f"Start: {row['Session Start Time']}, "
                f"End: {row['Session End Time']}, "
                f"Location: {row['Session Location']}"
            )
        print("\n" + "=" * 78 + "\n")

    # Filter out rows without complete session info
    merged_clean = merged[~missing_mask].copy()

    # Diagnostics
    unique_sessions_in_program = program["Session Title"].nunique(dropna=True)
    unique_sessions_resolved = resolved["Session Title"].nunique(dropna=True)
    print(f"Program unique session titles: {unique_sessions_in_program}")
    print(f"Resolved session titles available: {unique_sessions_resolved}")
    print(f"Rows in final merged output: {len(merged_clean)}")

    # Write CSV with UTF-8 encoding
    merged_clean.to_csv(output_csv, index=False, quoting=csv.QUOTE_MINIMAL, encoding="utf-8")
    print(f"\nDone. Clean merged file written to: {output_csv}\n")

if __name__ == "__main__":
    main()
