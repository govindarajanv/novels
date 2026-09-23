#!/usr/bin/env python3
"""
build_site.py — Validates novel summaries and generates the index.md for GitHub Pages.
"""

import os
import sys
import re
import yaml

VERSION = "v1.1.0"
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOVELS_YAML_PATH = os.path.join(REPO_ROOT, "novels.yaml")
INDEX_MD_PATH = os.path.join(REPO_ROOT, "index.md")

def slugify(title: str) -> str:
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', title.strip().lower())
    return slug.strip('-')

def load_novels():
    if not os.path.exists(NOVELS_YAML_PATH):
        print(f"Error: {NOVELS_YAML_PATH} not found.")
        sys.exit(1)

    with open(NOVELS_YAML_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not data or "novels" not in data:
        print("Error: 'novels' key missing in novels.yaml")
        sys.exit(1)

    raw_novels = data["novels"]
    if isinstance(raw_novels, dict):
        novels = [raw_novels]
    elif isinstance(raw_novels, list):
        novels = raw_novels
    else:
        print("Error: 'novels' in novels.yaml must be a dictionary or list of dictionaries.")
        sys.exit(1)

    return novels

def count_lines(filepath: str) -> int:
    with open(filepath, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)

def generate_index(novels):
    lines = [
        "---",
        "layout: default",
        "title: Novels Summary Archive",
        f"version: {VERSION}",
        "---",
        "",
        '<div class="site-hero">',
        '  <h1 class="site-title">Novels Summary Archive</h1>',
        '  <div class="site-version-row">',
        f'    <span class="version-pill">{VERSION}</span>',
        '    <span style="color: var(--text-muted); font-size: 0.85rem;">Comprehensive 100-Line Literary Analyses</span>',
        '  </div>',
        '  <p class="site-tagline">',
        '    Curated repository of high-yield, structured 100-line novel summaries. Every entry encompasses complete narrative arcs, character dossiers, cryptic motifs, and critical thematic evaluations.',
        '  </p>',
        '</div>',
        "",
        "## 📚 Catalog of Summaries",
        "",
        '<div class="novels-grid">',
    ]

    for novel in novels:
        name = novel.get("name", "Untitled")
        author = novel.get("author", "Unknown Author")
        genre = novel.get("genre", "Fiction")
        language = novel.get("language", "English")
        slug = slugify(name)
        filename = f"{slug}.md"
        filepath = os.path.join(REPO_ROOT, filename)

        status_pill = "Pending"
        line_count = 0
        if os.path.exists(filepath):
            line_count = count_lines(filepath)
            status_pill = f"✓ {line_count} Lines"

        card_html = f'''  <div class="novel-card">
    <div>
      <div class="novel-card-meta">
        <span class="badge badge-primary">{genre}</span>
        <span class="badge">{language}</span>
        <span class="badge">{status_pill}</span>
      </div>
      <h2 class="novel-card-title">{name}</h2>
      <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 0.75rem;"><strong>By:</strong> {author}</p>
      <p class="novel-card-desc">Comprehensive 100-line investigative study spanning character profiles, key plot revelations, occult mysteries, and thematic breakdown.</p>
    </div>
    <div class="novel-card-cta">
      <a href="{slug}.html" style="color: var(--primary); text-decoration: none; font-weight: 700;">Read 100-Line Summary &rarr;</a>
      <a href="{filename}" style="color: var(--text-muted); font-size: 0.8rem; text-decoration: none;">(View Markdown)</a>
    </div>
  </div>'''
        lines.append(card_html)

    lines.extend([
        '</div>',
        "",
        "---",
        "",
        "## 📋 Repository Index & Overview",
        "",
        "| Novel Name | Author | Genre | Language | Summary Link | Verification |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |",
    ])

    for novel in novels:
        name = novel.get("name", "Untitled")
        author = novel.get("author", "Unknown Author")
        genre = novel.get("genre", "Fiction")
        language = novel.get("language", "English")
        slug = slugify(name)
        filename = f"{slug}.md"
        filepath = os.path.join(REPO_ROOT, filename)
        exists = os.path.exists(filepath)
        lines_verified = f"{count_lines(filepath)} lines" if exists else "Missing"
        lines.append(f"| **{name}** | {author} | {genre} | {language} | [{name}]({slug}.html) &bull; [Markdown]({filename}) | `{lines_verified}` |")

    lines.extend([
        "",
        "---",
        "",
        "### ⚙️ How It Works",
        "1. **Catalog Definition (`novels.yaml`)**: Add novels with their title, author, genre, and language.",
        "2. **100-Line Synthesis**: A comprehensive, rigorously researched markdown summary is authored with exactly 100 lines.",
        "3. **Static Generation**: `scripts/build_site.py` validates line counts and compiles `index.md`.",
        "4. **GitHub Pages Deployment**: Automations build and deploy the archive to GitHub Pages.",
    ])

    return "\n".join(lines) + "\n"

def main():
    novels = load_novels()
    print(f"Loaded {len(novels)} novel(s) from {NOVELS_YAML_PATH}:")
    all_valid = True

    for novel in novels:
        name = novel.get("name")
        slug = slugify(name)
        filename = f"{slug}.md"
        filepath = os.path.join(REPO_ROOT, filename)

        if not os.path.exists(filepath):
            print(f"  [MISSING] {name} -> {filename} does not exist!")
            all_valid = False
        else:
            lines = count_lines(filepath)
            print(f"  [FOUND] {name} -> {filename} ({lines} lines)")
            if lines != 100:
                print(f"    WARNING: {filename} has {lines} lines, expected exactly 100 lines!")
                all_valid = False

    index_content = generate_index(novels)
    with open(INDEX_MD_PATH, "w", encoding="utf-8") as f:
        f.write(index_content)
    print(f"Generated {INDEX_MD_PATH}")

    if not all_valid:
        print("Notice: Some files are missing or do not match 100 lines.")
    else:
        print("All novel summaries are verified and exactly 100 lines!")

if __name__ == "__main__":
    main()
