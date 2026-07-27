# IEEE ISMAR Website Repository  

This repository hosts multiple years of the IEEE ISMAR conference website. The **2024** site is a static HTML website, while from **2025** onward, the site is managed using Jekyll to enable dynamic page generation, templating, and easier maintenance.  

The website is available at: [https://www.ieeeismar.net/](https://www.ieeeismar.net/). 

For any questions, please contact: **ieeeismarpublicity@gmail.com**.

---

## Website Structure  

- **ISMAR 2024 (`/2024`):** A static HTML site that is served as-is. No Jekyll processing is applied.  
- **ISMAR 2025 and beyond:** Jekyll processes markdown files in each year's folder (e.g., `2025/`), automatically generating HTML pages based on their filenames and directory structure.  

Year-specific components such as layouts, includes, and structured data are stored in dedicated directories (`_layouts/2025`, `_includes/2025`, `_data/2025`), allowing customization for each conference year while maintaining a shared structure.  

---

## Editing Common Website Elements for a Specific Year  

To modify shared website elements such as headers, footers, or navigation menus for a given year, update the corresponding files in the `_includes/<year>/` directory.  

For example, to edit the **header for 2025**, modify:  

`_includes/2025/header.html`

Changes here will automatically apply to all pages that use the `header.html` include.

Similarly, to modify the **layout of all pages for a specific year**, update the appropriate file in `_layouts/<year>/`. For example:  

`_layouts/2025/default.html`

This file determines the overall structure of 2025 pages.

---

## Adding a New Page for a Specific Year  

For years managed by Jekyll (starting with 2025), new pages are created as markdown (`.md`) files in the corresponding year’s folder.  

### 1. **Create a New Markdown File**  
To add a page for **2025**, create a markdown file in `2025/`, e.g.,  

`2025/new-page.md`

### 2. **Automatic URL Generation**  
Jekyll automatically determines the URL of a page based on its filename and directory. For example:  
- `2025/about.md` → **`ieeeismar.net/2025/about`**  
- `2025/contribute/papers.md` → **`ieeeismar.net/2025/contribute/papers`**  

> [!TIP]  
> If you want the page to have a custom URL, you can define a **permalink** in the front matter.

### 3. **Custom Permalinks**  
If a page needs a specific URL, define it in the front matter at the top of the markdown file:  
```yaml
---
title: "Custom Page"
layout: "default"
permalink: "/2025/custom-page"
---
```

### 4. **Redirecting Old URLs**  
If a page’s URL structure changes but old links need to remain functional, use `redirect_from`:
```yaml
---
title: "Legacy Page"
redirect_from:
  - "/old-page.html"
---
```
This ensures users visiting the old URL will be redirected to the new one.

---

## Adding a New Jekyll Website for a New Year  

To create a new Jekyll-based website for a future conference year (e.g., 2026):

### 1. **Create a New Year Directory**  
Create a new folder for the year inside the repository:

`2026/`

This will store all markdown pages for that year’s website.

### 2. **Set Up Year-Specific Resources**  
If the new year requires custom templates or includes, create:

- `_layouts/2026/`       # Custom layouts for 2026
- `_includes/2026/`      # Custom reusable elements for 2026
- `_data/2026/`          # Structured data (YAML files) for 2026
- `assets/2026/`         # Year-specific assets (CSS, JS, images)

### 3. **Update _config.yml to Define a New Collection**  
Jekyll processes pages for each year using collections. Add a new collection for the new year in `_config.yml`:
```yaml
collections:
  year2026:
    output: true
    permalink: /2026/:path/
```
This ensures Jekyll correctly processes the markdown files in the `2026/` folder and assigns the correct URLs.

> [!IMPORTANT]
> Without adding the new collection in `_config.yml`, Jekyll will not generate the pages for the new year.

### 4. **Make the New Year the Default Homepage**  
To automatically forward `ieeeismar.net/` to the new year’s homepage, add the following front matter to `2026/index.md`:
```yaml
---
title: "IEEE ISMAR 2026"
redirect_from:
  - "/"
---
```
This ensures visitors accessing the base URL are directed to the latest conference site.

---

## Local Development  

To preview the website locally before pushing changes:

### 1. **Install Jekyll and Dependencies**  
Make sure you have Ruby and Bundler installed. Then, in the repository root, run:
```sh
bundle install
```

### 2. **Start the Local Server**  
Run the following command to build the site and start a local server:
```sh
bundle exec jekyll serve
```
This will generate the website and serve it at `http://localhost:4000`. Any changes you make will be reflected automatically.

### 3. **Stopping the Server**  
Press `CTRL+C` in the terminal to stop the local server.

> [!TIP]
> Running Jekyll locally allows you to preview changes before pushing them to GitHub Pages.

---

## Important Notes for Web Chairs  

> [!WARNING]
> If you are the web chair for a specific year’s conference, please do not edit the content of previous years.

Each year’s website is meant to remain unchanged once the conference has concluded. If an update is necessary for a past year (e.g., fixing broken links), coordinate with the repository maintainers before making changes.

---

## Contact  

For any questions or assistance, please contact: ieeeismarpublicity@gmail.com. The initial author of this README is **[Nels Numan](https://nels.dev)** (Web Co-Chair 2025).