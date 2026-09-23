# Novels Summary Archive

[![Version](https://img.shields.io/badge/version-v1.3.0-blue.svg)](https://github.com/govindarajanv/novels)
[![Pages](https://img.shields.io/badge/GitHub%20Pages-live-success.svg)](https://govindarajanv.github.io/novels/)
[![Status](https://img.shields.io/badge/summaries-100--line%20verified-brightgreen.svg)](index.html)

**Current Version:** `v1.3.0`  
**Live Site:** [https://govindarajanv.github.io/novels/](https://govindarajanv.github.io/novels/)

---

## Overview

The **Novels Summary Archive** is a curated digital library of comprehensive, rigorously researched literary syntheses. Designed for avid readers, literary analysts, and book lovers, each novel is distilled into **exactly 100 lines** of high-density markdown capturing:

1. **Bibliographic Metadata & Overview** (authorship, publication details, central conflicts, core settings)
2. **Dramatis Personae** (detailed character breakdowns, motives, and roles)
3. **Chronological Plot Narrative** (inciting incident, rising tension, clues, twists, climax, and resolution)
4. **Thematic Depth & Critical Reception** (motifs, psychological analysis, social commentary, and literary craft)

---

## 📚 Current Catalog (20 Novels)

| Novel Title | Author | Genre | Language | Summary (HTML) | Summary (Markdown) | Verification |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **The Murder Artist** | John Case | Crime | English | [Read HTML](the-murder-artist.html) | [the-murder-artist.md](the-murder-artist.md) | `✓ 100 Lines` |
| **The Adventures of Tom Sawyer** | Mark Twain | Bildungsroman | English | [Read HTML](the-adventures-of-tom-sawyer.html) | [the-adventures-of-tom-sawyer.md](the-adventures-of-tom-sawyer.md) | `✓ 100 Lines` |
| **Adventures of Huckleberry Finn** | Mark Twain | Bildungsroman | English | [Read HTML](adventures-of-huckleberry-finn.html) | [adventures-of-huckleberry-finn.md](adventures-of-huckleberry-finn.md) | `✓ 100 Lines` |
| **The King of Torts** | John Grisham | Legal Thriller | English | [Read HTML](the-king-of-torts.html) | [the-king-of-torts.md](the-king-of-torts.md) | `✓ 100 Lines` |
| **A Week in Winter** | Marcia Willett | Fiction | English | [Read HTML](a-week-in-winter.html) | [a-week-in-winter.md](a-week-in-winter.md) | `✓ 100 Lines` |
| **The Last Detective** | Robert Crais | Crime | English | [Read HTML](the-last-detective.html) | [the-last-detective.md](the-last-detective.md) | `✓ 100 Lines` |
| **Eat Cake** | Jeanne Ray | Contemporary Fiction | English | [Read HTML](eat-cake.html) | [eat-cake.md](eat-cake.md) | `✓ 100 Lines` |
| **The Last Juror** | John Grisham | Legal Thriller | English | [Read HTML](the-last-juror.html) | [the-last-juror.md](the-last-juror.md) | `✓ 100 Lines` |
| **The Various Haunts of Men** | Susan Hill | Crime | English | [Read HTML](the-various-haunts-of-men.html) | [the-various-haunts-of-men.md](the-various-haunts-of-men.md) | `✓ 100 Lines` |
| **The Codex** | Douglas Preston | Thriller | English | [Read HTML](the-codex.html) | [the-codex.md](the-codex.md) | `✓ 100 Lines` |
| **The Curious Incident of the Dog in the Night-Time** | Mark Haddon | Mystery | English | [Read HTML](the-curious-incident-of-the-dog-in-the-night-time.html) | [the-curious-incident-of-the-dog-in-the-night-time.md](the-curious-incident-of-the-dog-in-the-night-time.md) | `✓ 100 Lines` |
| **Start from Here** | Sean French | Contemporary Fiction | English | [Read HTML](start-from-here.html) | [start-from-here.md](start-from-here.md) | `✓ 100 Lines` |
| **At Risk** | Stella Rimington | Thriller | English | [Read HTML](at-risk.html) | [at-risk.md](at-risk.md) | `✓ 100 Lines` |
| **The No.1 Ladies' Detective Agency** | Alexander McCall Smith | Crime | English | [Read HTML](the-no-1-ladies-detective-agency.html) | [the-no-1-ladies-detective-agency.md](the-no-1-ladies-detective-agency.md) | `✓ 100 Lines` |
| **The Da Vinci Code** | Dan Brown | Mystery | English | [Read HTML](the-da-vinci-code.html) | [the-da-vinci-code.md](the-da-vinci-code.md) | `✓ 100 Lines` |
| **Up and Down in the Dales** | Gervase Phinn | Memoir | English | [Read HTML](up-and-down-in-the-dales.html) | [up-and-down-in-the-dales.md](up-and-down-in-the-dales.md) | `✓ 100 Lines` |
| **The Return of the Dancing Master** | Henning Mankell | Crime | English | [Read HTML](the-return-of-the-dancing-master.html) | [the-return-of-the-dancing-master.md](the-return-of-the-dancing-master.md) | `✓ 100 Lines` |
| **A Gathering Light** | Jennifer Donnelly | Historical Fiction | English | [Read HTML](a-gathering-light.html) | [a-gathering-light.md](a-gathering-light.md) | `✓ 100 Lines` |
| **Harry Potter and the Chamber of Secrets** | J.K. Rowling | Fantasy | English | [Read HTML](harry-potter-and-the-chamber-of-secrets.html) | [harry-potter-and-the-chamber-of-secrets.md](harry-potter-and-the-chamber-of-secrets.md) | `✓ 100 Lines` |
| **Harry Potter and the Prisoner of Azkaban** | J.K. Rowling | Fantasy | English | [Read HTML](harry-potter-and-the-prisoner-of-azkaban.html) | [harry-potter-and-the-prisoner-of-azkaban.md](harry-potter-and-the-prisoner-of-azkaban.md) | `✓ 100 Lines` |

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
