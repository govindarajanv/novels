#!/usr/bin/env python3
"""
build_all_summaries.py — Generates all 17 new novel summaries with strict 100-line validation.
"""

import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def create_summary(slug, title, author, genre, year, setting, chars, s3, s4, s5, s6, s7, s8, themes):
    # Ensure sections 3-8 have exactly 43 bullets total
    sec_bullets = [s3, s4, s5, s6, s7, s8]
    total_b = sum(len(b[1]) for b in sec_bullets)
    if total_b != 43:
        raise ValueError(f"{slug} has {total_b} bullets across sec 3-8, expected 43!")

    lines = []
    lines.append(f"# {title} — Comprehensive Novel Summary & Critical Analysis")
    lines.append("")
    lines.append(f"**Author:** {author} | **Genre:** {genre} | **Language:** English (Published: {year})")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Sec 1 (6 bullets)
    lines.append("### 1. Bibliographic Metadata & Overview")
    lines.append(f"* **Title:** {title}")
    lines.append(f"* **Author:** {author}")
    lines.append(f"* **Publication Date:** {year}")
    lines.append(f"* **Protagonist:** {chars[0][0]} — {chars[0][1].split('.')[0]}")
    lines.append(f"* **Geographic Setting:** {setting}")
    lines.append(f"* **Core Literary Mode:** {genre} exploring character dynamics, systemic conflicts, and human nature")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Sec 2 (8 bullets)
    lines.append("### 2. Dramatis Personae")
    for c_name, c_desc in chars:
        lines.append(f"* **{c_name}:** {c_desc}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Sec 3
    lines.append(f"### 3. {s3[0]}")
    for b in s3[1]:
        lines.append(f"* {b}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Sec 4
    lines.append(f"### 4. {s4[0]}")
    for b in s4[1]:
        lines.append(f"* {b}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Sec 5
    lines.append(f"### 5. {s5[0]}")
    for b in s5[1]:
        lines.append(f"* {b}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Sec 6
    lines.append(f"### 6. {s6[0]}")
    for b in s6[1]:
        lines.append(f"* {b}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Sec 7
    lines.append(f"### 7. {s7[0]}")
    for b in s7[1]:
        lines.append(f"* {b}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Sec 8
    lines.append(f"### 8. {s8[0]}")
    for b in s8[1]:
        lines.append(f"* {b}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Sec 9 (4 bullets)
    lines.append("### 9. Thematic Analysis & Critical Legacy")
    for t_name, t_desc in themes:
        lines.append(f"* **{t_name}:** {t_desc}")

    content = "\n".join(lines) + "\n"
    actual_lines = len(content.splitlines())
    if actual_lines != 100:
        raise ValueError(f"{slug} generated {actual_lines} lines instead of exactly 100!")
    
    filepath = os.path.join(REPO_ROOT, f"{slug}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✓ Generated {slug}.md (exactly 100 lines)")

print("Script template ready")
