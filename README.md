# Novels Summary Archive

[![Version](https://img.shields.io/badge/version-v1.2.0-blue.svg)](https://github.com/govindarajanv/novels)
[![Pages](https://img.shields.io/badge/GitHub%20Pages-live-success.svg)](https://govindarajanv.github.io/novels/)
[![Status](https://img.shields.io/badge/summaries-100--line%20verified-brightgreen.svg)](index.html)

**Current Version:** `v1.2.0`  
**Live Site:** [https://govindarajanv.github.io/novels/](https://govindarajanv.github.io/novels/)

---

## Overview

The **Novels Summary Archive** is a curated digital library of comprehensive, rigorously researched literary syntheses. Designed for avid readers, literary analysts, and book lovers, each novel is distilled into **exactly 100 lines** of high-density markdown capturing:

1. **Bibliographic Metadata & Overview** (authorship, publication details, central conflicts, core settings)
2. **Dramatis Personae** (detailed character breakdowns, motives, and roles)
3. **Chronological Plot Narrative** (inciting incident, rising tension, clues, twists, climax, and resolution)
4. **Thematic Depth & Critical Reception** (motifs, psychological analysis, social commentary, and literary craft)

---

## 📚 Current Catalog

| Novel Title | Author | Genre | Language | Summary (Pages) | Summary (Markdown) | Verification |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **The Murder Artist** | John Case | Crime | English | [Read Summary](https://govindarajanv.github.io/novels/the-murder-artist.html) | [the-murder-artist.md](the-murder-artist.md) | `✓ 100 Lines` |
| **The Adventures of Tom Sawyer** | Mark Twain | Bildungsroman | English | [Read Summary](https://govindarajanv.github.io/novels/the-adventures-of-tom-sawyer.html) | [the-adventures-of-tom-sawyer.md](the-adventures-of-tom-sawyer.md) | `✓ 100 Lines` |
| **Adventures of Huckleberry Finn** | Mark Twain | Bildungsroman | English | [Read Summary](https://govindarajanv.github.io/novels/adventures-of-huckleberry-finn.html) | [adventures-of-huckleberry-finn.md](adventures-of-huckleberry-finn.md) | `✓ 100 Lines` |

---

## 🚀 How to Add a New Novel

1. **Update `novels.yaml`**: Add the new novel metadata to `novels.yaml`:
   ```yaml
   novels:
     - name: 'The Murder Artist'
       author: 'John Case'
       genre: 'Crime'
       language: 'English'
     - name: 'New Novel Title'
       author: 'Author Name'
       genre: 'Genre'
       language: 'Language'
   ```

2. **Generate the 100-Line Summary**:
   Create `<novel-slug>.md` with **exactly 100 lines** summarizing the novel across narrative arcs, character dossiers, twists, and themes.

3. **Validate & Build**:
   ```bash
   python3 scripts/build_site.py
   ```
   This will verify that all summaries have exactly 100 lines and regenerate `index.md`.

4. **Commit & Push**:
   ```bash
   git add novels.yaml index.md <novel-slug>.md
   git commit -m "Add 100-line summary for <novel-name>"
   git push origin master
   ```

---

## 🛠️ Technology Stack

- **Static Site Engine**: Jekyll (GitHub Pages)
- **Validation & Compilation**: Python 3 (`scripts/build_site.py`)
- **Deployment**: GitHub Actions (`.github/workflows/pages.yml`)
- **Typography & Theme**: Responsive layout with automatic dark/light theme support
