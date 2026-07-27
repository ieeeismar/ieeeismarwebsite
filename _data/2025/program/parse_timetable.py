import pandas as pd
import re
from datetime import datetime

# https://docs.google.com/spreadsheets/d/e/2PACX-1vQrmgHgmh-sZFvt8d_Wz2Ma69b1l4xsuwLbSiNrNKH2BgJmTFTEPLN7fw6HqHWjLKJK7i48kBKjE-K9/pubhtml?gid=801352381&single=true&widget=true&headers=false&chrome=false&range=A10:I22

# The Google Sheets CSV URLs
urls = [
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vQrmgHgmh-sZFvt8d_Wz2Ma69b1l4xsuwLbSiNrNKH2BgJmTFTEPLN7fw6HqHWjLKJK7i48kBKjE-K9/pub?gid=801352381&single=true&output=csv&range=A10:I22",
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vQrmgHgmh-sZFvt8d_Wz2Ma69b1l4xsuwLbSiNrNKH2BgJmTFTEPLN7fw6HqHWjLKJK7i48kBKjE-K9/pub?gid=801352381&single=true&output=csv&range=A24:I35",
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vQrmgHgmh-sZFvt8d_Wz2Ma69b1l4xsuwLbSiNrNKH2BgJmTFTEPLN7fw6HqHWjLKJK7i48kBKjE-K9/pub?gid=801352381&single=true&output=csv&range=A37:I47"
]

def normalize_day(header: str) -> str:
    s = header.replace('\n', ' ').strip()
    s = re.sub(r'\s*\(.*?\)\s*', '', s).strip()
    dt = datetime.strptime(s.replace(',', ''), '%b %d %Y')
    return f"{dt.strftime('%B')} {dt.day} {dt.year}"

def parse_time_range(cell: str):
    if not isinstance(cell, str):
        return None, None
    parts = re.split(r'\s*~\s*', cell.strip())
    if len(parts) != 2:
        return None, None
    return parts[0], parts[1]

def clean_title(val):
    if pd.isna(val):
        return None
    s = str(val).strip()
    if s in {'`', "''", '""'} or len(s) == 0:
        return None
    return s

def parse_url(url: str) -> pd.DataFrame:
    df = pd.read_csv(url)
    day_header = df.columns[0]
    time_col = 'Time' if 'Time' in df.columns else df.columns[1]
    day_str = normalize_day(day_header)
    candidate_locs = [c for c in df.columns if c not in {day_header, time_col} and not c.lower().startswith('unnamed')]
    rows = []
    for _, row in df.iterrows():
        start, end = parse_time_range(row.get(time_col))
        if not start:
            continue
        for loc in candidate_locs:
            title = clean_title(row.get(loc))
            if title:
                rows.append({
                    'Session Title': title,
                    'Session Location': loc,
                    'Session Day': day_str,
                    'Session Start Time': start,
                    'Session End Time': end,
                })
    return pd.DataFrame(rows)

# Process all URLs
all_data = [parse_url(u) for u in urls]
flat = pd.concat(all_data, ignore_index=True)

# Sort
flat['_sort_day'] = flat['Session Day'].apply(lambda s: datetime.strptime(s, '%B %d %Y'))
flat = flat.sort_values(by=['_sort_day', 'Session Start Time', 'Session Location']).drop(columns=['_sort_day'])

# Save final CSV
flat.to_csv("ismar_sessions_flat.csv", index=False)

print(flat.head(20).to_string(index=False))
print("Saved to ismar_sessions_flat.csv")
