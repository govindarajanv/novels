---
layout: default
title: Novels Summary Archive
version: v1.1.0
---

<div class="site-hero">
  <h1 class="site-title">Novels Summary Archive</h1>
  <div class="site-version-row">
    <span class="version-pill">v1.1.0</span>
    <span style="color: var(--text-muted); font-size: 0.85rem;">Comprehensive 100-Line Literary Analyses</span>
  </div>
  <p class="site-tagline">
    Curated repository of high-yield, structured 100-line novel summaries. Every entry encompasses complete narrative arcs, character dossiers, cryptic motifs, and critical thematic evaluations.
  </p>
</div>

## 📚 Catalog of Summaries

<div class="novels-grid">
  <div class="novel-card">
    <div>
      <div class="novel-card-meta">
        <span class="badge badge-primary">Crime</span>
        <span class="badge">English</span>
        <span class="badge">✓ 100 Lines</span>
      </div>
      <h2 class="novel-card-title">The Murder Artist</h2>
      <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 0.75rem;"><strong>By:</strong> John Case</p>
      <p class="novel-card-desc">Comprehensive 100-line investigative study spanning character profiles, key plot revelations, occult mysteries, and thematic breakdown.</p>
    </div>
    <div class="novel-card-cta">
      <a href="the-murder-artist.html" style="color: var(--primary); text-decoration: none; font-weight: 700;">Read 100-Line Summary &rarr;</a>
      <a href="the-murder-artist.md" style="color: var(--text-muted); font-size: 0.8rem; text-decoration: none;">(View Markdown)</a>
    </div>
  </div>
  <div class="novel-card">
    <div>
      <div class="novel-card-meta">
        <span class="badge badge-primary">bildungsroman</span>
        <span class="badge">English</span>
        <span class="badge">✓ 100 Lines</span>
      </div>
      <h2 class="novel-card-title">The Adventures of Tom Sawyer</h2>
      <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 0.75rem;"><strong>By:</strong> Mark Twain</p>
      <p class="novel-card-desc">Comprehensive 100-line investigative study spanning character profiles, key plot revelations, occult mysteries, and thematic breakdown.</p>
    </div>
    <div class="novel-card-cta">
      <a href="the-adventures-of-tom-sawyer.html" style="color: var(--primary); text-decoration: none; font-weight: 700;">Read 100-Line Summary &rarr;</a>
      <a href="the-adventures-of-tom-sawyer.md" style="color: var(--text-muted); font-size: 0.8rem; text-decoration: none;">(View Markdown)</a>
    </div>
  </div>
  <div class="novel-card">
    <div>
      <div class="novel-card-meta">
        <span class="badge badge-primary">bildungsroman</span>
        <span class="badge">English</span>
        <span class="badge">✓ 100 Lines</span>
      </div>
      <h2 class="novel-card-title">Adventures of Huckleberry Finn</h2>
      <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 0.75rem;"><strong>By:</strong> Mark Twain</p>
      <p class="novel-card-desc">Comprehensive 100-line investigative study spanning character profiles, key plot revelations, occult mysteries, and thematic breakdown.</p>
    </div>
    <div class="novel-card-cta">
      <a href="adventures-of-huckleberry-finn.html" style="color: var(--primary); text-decoration: none; font-weight: 700;">Read 100-Line Summary &rarr;</a>
      <a href="adventures-of-huckleberry-finn.md" style="color: var(--text-muted); font-size: 0.8rem; text-decoration: none;">(View Markdown)</a>
    </div>
  </div>
</div>

---

## 📋 Repository Index & Overview

| Novel Name | Author | Genre | Language | Summary Link | Verification |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **The Murder Artist** | John Case | Crime | English | [The Murder Artist](the-murder-artist.html) &bull; [Markdown](the-murder-artist.md) | `100 lines` |
| **The Adventures of Tom Sawyer** | Mark Twain | bildungsroman | English | [The Adventures of Tom Sawyer](the-adventures-of-tom-sawyer.html) &bull; [Markdown](the-adventures-of-tom-sawyer.md) | `100 lines` |
| **Adventures of Huckleberry Finn** | Mark Twain | bildungsroman | English | [Adventures of Huckleberry Finn](adventures-of-huckleberry-finn.html) &bull; [Markdown](adventures-of-huckleberry-finn.md) | `100 lines` |

---

### ⚙️ How It Works
1. **Catalog Definition (`novels.yaml`)**: Add novels with their title, author, genre, and language.
2. **100-Line Synthesis**: A comprehensive, rigorously researched markdown summary is authored with exactly 100 lines.
3. **Static Generation**: `scripts/build_site.py` validates line counts and compiles `index.md`.
4. **GitHub Pages Deployment**: Automations build and deploy the archive to GitHub Pages.
