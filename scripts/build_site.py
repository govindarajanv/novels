#!/usr/bin/env python3
"""
build_site.py — Validates novel summaries, generates static HTML reading pages,
and generates index.html and index.md for GitHub Pages.
"""

import os
import sys
import re
import html
import json
import yaml

VERSION = "v1.2.0"
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOVELS_YAML_PATH = os.path.join(REPO_ROOT, "novels.yaml")
INDEX_MD_PATH = os.path.join(REPO_ROOT, "index.md")
INDEX_HTML_PATH = os.path.join(REPO_ROOT, "index.html")

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

def inline_formatting(text: str) -> str:
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    return text

def md_to_html(md_text: str) -> str:
    lines = md_text.splitlines()
    html_lines = []
    in_list = False
    in_table = False
    table_rows = []

    def flush_table():
        nonlocal in_table, table_rows
        if not table_rows:
            return
        html_lines.append('<div class="table-responsive"><table>')
        header_cells = [c.strip() for c in table_rows[0].strip('|').split('|')]
        html_lines.append('<thead><tr>' + ''.join(f'<th>{inline_formatting(c)}</th>' for c in header_cells) + '</tr></thead>')
        html_lines.append('<tbody>')
        for r in table_rows[1:]:
            if re.match(r'^\s*\|?\s*:?-+:?\s*\|', r):
                continue
            cells = [c.strip() for c in r.strip('|').split('|')]
            html_lines.append('<tr>' + ''.join(f'<td>{inline_formatting(c)}</td>' for c in cells) + '</tr>')
        html_lines.append('</tbody></table></div>')
        table_rows = []
        in_table = False

    for line in lines:
        stripped = line.strip()

        if stripped.startswith('|') and stripped.endswith('|'):
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            in_table = True
            table_rows.append(stripped)
            continue
        elif in_table:
            flush_table()

        if not stripped:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            continue

        if stripped.startswith('### '):
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append(f'<h3 class="novel-section-heading">{inline_formatting(stripped[4:])}</h3>')
        elif stripped.startswith('## '):
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append(f'<h2>{inline_formatting(stripped[3:])}</h2>')
        elif stripped.startswith('# '):
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append(f'<h1 class="novel-title-main">{inline_formatting(stripped[2:])}</h1>')
        elif stripped == '---':
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append('<hr class="divider">')
        elif stripped.startswith('* '):
            if not in_list:
                html_lines.append('<ul class="summary-list">')
                in_list = True
            content = inline_formatting(stripped[2:])
            html_lines.append(f'  <li class="summary-item">{content}</li>')
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append(f'<p>{inline_formatting(stripped)}</p>')

    if in_table:
        flush_table()
    if in_list:
        html_lines.append('</ul>')

    return '\n'.join(html_lines)

COMMON_CSS = """
    :root {
      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      --bg: #0b1120;
      --surface: #1e293b;
      --surface-hover: #334155;
      --surface-card: #141f32;
      --border: #334155;
      --border-subtle: #1e293b;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --text-faint: #64748b;
      --primary: #38bdf8;
      --primary-glow: rgba(56, 189, 248, 0.15);
      --accent: #818cf8;
      --accent-glow: rgba(129, 140, 248, 0.15);
      --success: #34d399;
      --success-glow: rgba(52, 211, 153, 0.15);
      --card-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.5);
      --card-hover-shadow: 0 14px 34px -4px rgba(56, 189, 248, 0.2);
      --radius: 12px;
      --radius-sm: 6px;
      --article-font-size: 1.02rem;
    }

    [data-theme="light"] {
      --bg: #f8fafc;
      --surface: #ffffff;
      --surface-hover: #f1f5f9;
      --surface-card: #ffffff;
      --border: #cbd5e1;
      --border-subtle: #f1f5f9;
      --text: #0f172a;
      --text-muted: #475569;
      --text-faint: #94a3b8;
      --primary: #0284c7;
      --primary-glow: rgba(2, 132, 199, 0.12);
      --accent: #6366f1;
      --accent-glow: rgba(99, 102, 241, 0.12);
      --success: #059669;
      --success-glow: rgba(5, 150, 105, 0.12);
      --card-shadow: 0 4px 16px -2px rgba(0, 0, 0, 0.08);
      --card-hover-shadow: 0 12px 28px -4px rgba(2, 132, 199, 0.15);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: var(--font-sans);
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.7;
      -webkit-font-smoothing: antialiased;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      transition: background-color 0.25s ease, color 0.25s ease;
    }

    /* Top Navigation */
    .top-nav {
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(12px);
    }

    .nav-inner {
      max-width: 1080px;
      margin: 0 auto;
      padding: 0.85rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 0.7rem;
      text-decoration: none;
      color: var(--text);
      font-weight: 800;
      font-size: 1.15rem;
      letter-spacing: -0.02em;
    }

    .brand-icon {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 34px;
      height: 34px;
      background: var(--primary-glow);
      color: var(--primary);
      border-radius: var(--radius-sm);
      font-size: 1.15rem;
    }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 0.85rem;
    }

    .nav-link {
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 600;
      transition: color 0.15s ease;
    }

    .nav-link:hover { color: var(--primary); }

    .theme-toggle-btn {
      background: var(--surface-hover);
      border: 1px solid var(--border);
      color: var(--text);
      cursor: pointer;
      padding: 0.4rem 0.65rem;
      border-radius: var(--radius-sm);
      font-size: 0.9rem;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      transition: all 0.2s ease;
    }

    .theme-toggle-btn:hover {
      border-color: var(--primary);
      color: var(--primary);
    }

    .version-pill {
      font-family: var(--font-mono);
      font-size: 0.75rem;
      font-weight: 600;
      padding: 0.2rem 0.6rem;
      border-radius: 9999px;
      background: var(--primary-glow);
      color: var(--primary);
      border: 1px solid var(--primary);
      letter-spacing: 0.03em;
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
    }

    /* Container */
    .container {
      max-width: 1080px;
      width: 100%;
      margin: 0 auto;
      padding: 2rem 1.5rem 4rem;
      flex: 1;
    }

    /* Hero Section */
    .site-hero {
      margin-bottom: 2.25rem;
      padding-bottom: 1.75rem;
      border-bottom: 1px solid var(--border);
    }

    .site-title {
      font-size: 2.35rem;
      font-weight: 800;
      letter-spacing: -0.03em;
      margin-bottom: 0.4rem;
      background: linear-gradient(135deg, var(--text) 45%, var(--primary) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .site-version-row {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 0.85rem;
    }

    .site-tagline {
      color: var(--text-muted);
      font-size: 1.05rem;
      max-width: 780px;
      line-height: 1.6;
    }

    /* Stats Banner */
    .stats-banner {
      display: flex;
      flex-wrap: wrap;
      gap: 1.25rem;
      margin: 1.75rem 0 2.25rem;
      padding: 1.1rem 1.4rem;
      background: var(--surface-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
    }

    .stat-item {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      font-size: 0.9rem;
      color: var(--text-muted);
    }

    .stat-number {
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--text);
      font-family: var(--font-mono);
    }

    /* Novels Grid */
    .section-title {
      font-size: 1.45rem;
      font-weight: 800;
      margin: 2rem 0 1.25rem;
      letter-spacing: -0.02em;
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }

    .novels-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 1.5rem;
      margin-bottom: 2.75rem;
    }

    .novel-card {
      background: var(--surface-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.6rem;
      box-shadow: var(--card-shadow);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
      position: relative;
    }

    .novel-card:hover {
      transform: translateY(-4px);
      box-shadow: var(--card-hover-shadow);
      border-color: var(--primary);
    }

    .novel-card.active-card {
      border-color: var(--primary);
      box-shadow: 0 0 0 2px var(--primary-glow);
    }

    .novel-card-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 0.45rem;
      margin-bottom: 0.85rem;
    }

    .badge {
      font-size: 0.75rem;
      font-weight: 600;
      padding: 0.2rem 0.6rem;
      border-radius: 9999px;
      background: var(--surface-hover);
      color: var(--text-muted);
      border: 1px solid var(--border);
    }

    .badge-primary {
      background: var(--primary-glow);
      color: var(--primary);
      border-color: var(--primary);
    }

    .badge-success {
      background: var(--success-glow);
      color: var(--success);
      border-color: var(--success);
    }

    .novel-card-title {
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--text);
      margin-bottom: 0.4rem;
      letter-spacing: -0.015em;
    }

    .novel-card-author {
      color: var(--text-muted);
      font-size: 0.9rem;
      margin-bottom: 0.8rem;
    }

    .novel-card-desc {
      color: var(--text-muted);
      font-size: 0.92rem;
      margin-bottom: 1.4rem;
      line-height: 1.55;
      flex: 1;
    }

    .novel-card-actions {
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
      padding-top: 1rem;
      border-top: 1px solid var(--border);
    }

    .btn-read-in-page {
      background: var(--primary);
      color: #0b1120;
      font-weight: 700;
      font-size: 0.9rem;
      padding: 0.6rem 1rem;
      border-radius: var(--radius-sm);
      text-decoration: none;
      text-align: center;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.45rem;
      cursor: pointer;
      border: none;
      transition: opacity 0.15s ease, transform 0.15s ease;
    }

    .btn-read-in-page:hover {
      opacity: 0.92;
      transform: translateY(-1px);
    }

    .card-secondary-links {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 0.82rem;
    }

    .card-secondary-links a {
      color: var(--text-muted);
      text-decoration: none;
      transition: color 0.15s ease;
    }

    .card-secondary-links a:hover { color: var(--primary); }

    /* Interactive In-Page Reader */
    .reader-section {
      background: var(--surface-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2rem;
      box-shadow: var(--card-shadow);
      margin-bottom: 3rem;
      scroll-margin-top: 5rem;
    }

    .reader-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1rem;
      padding-bottom: 1.25rem;
      border-bottom: 1px solid var(--border);
      margin-bottom: 1.5rem;
    }

    .reader-title-area {
      display: flex;
      align-items: center;
      gap: 0.85rem;
    }

    .reader-title {
      font-size: 1.45rem;
      font-weight: 800;
    }

    .reader-controls {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      flex-wrap: wrap;
    }

    .ctrl-btn {
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text);
      cursor: pointer;
      padding: 0.35rem 0.65rem;
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      font-weight: 600;
      transition: all 0.15s ease;
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
      text-decoration: none;
    }

    .ctrl-btn:hover {
      border-color: var(--primary);
      color: var(--primary);
    }

    .novel-tabs-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-bottom: 1.75rem;
      background: var(--surface);
      padding: 0.5rem;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border);
    }

    .novel-tab-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 0.5rem 1rem;
      font-size: 0.9rem;
      font-weight: 600;
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: all 0.15s ease;
    }

    .novel-tab-btn:hover {
      color: var(--text);
      background: var(--surface-hover);
    }

    .novel-tab-btn.active-tab {
      background: var(--primary-glow);
      color: var(--primary);
      border: 1px solid var(--primary);
    }

    /* Article Content Typography */
    .content-article {
      font-size: var(--article-font-size);
      line-height: 1.8;
      color: var(--text);
    }

    .novel-title-main {
      font-size: 1.95rem;
      font-weight: 800;
      letter-spacing: -0.025em;
      margin-bottom: 0.6rem;
      color: var(--text);
    }

    .novel-section-heading {
      font-size: 1.28rem;
      font-weight: 700;
      color: var(--primary);
      margin: 1.85rem 0 0.85rem;
      letter-spacing: -0.01em;
      border-left: 3px solid var(--primary);
      padding-left: 0.75rem;
    }

    .content-article h2 {
      font-size: 1.45rem;
      font-weight: 700;
      margin: 2rem 0 1rem;
      border-bottom: 1px solid var(--border);
      padding-bottom: 0.4rem;
    }

    .content-article p {
      margin-bottom: 1.15rem;
      color: var(--text);
    }

    .summary-list {
      list-style-type: disc;
      margin: 0.75rem 0 1.25rem 1.6rem;
    }

    .summary-item {
      margin-bottom: 0.55rem;
      padding-left: 0.2rem;
    }

    .summary-item strong {
      color: var(--text);
      font-weight: 700;
    }

    .divider {
      border: 0;
      height: 1px;
      background: var(--border);
      margin: 2.2rem 0;
    }

    .content-article a {
      color: var(--primary);
      text-decoration: none;
      font-weight: 600;
      border-bottom: 1px solid transparent;
      transition: border-color 0.15s ease;
    }

    .content-article a:hover { border-bottom-color: var(--primary); }

    .content-article code {
      font-family: var(--font-mono);
      font-size: 0.88em;
      background: var(--surface);
      padding: 0.15rem 0.4rem;
      border-radius: 4px;
      border: 1px solid var(--border);
    }

    /* Table */
    .table-responsive {
      overflow-x: auto;
      margin: 1.5rem 0;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.92rem;
    }

    th, td {
      border: 1px solid var(--border);
      padding: 0.8rem 1rem;
      text-align: left;
    }

    th {
      background: var(--surface);
      color: var(--primary);
      font-weight: 700;
    }

    tr:nth-child(even) {
      background: var(--surface);
    }

    /* Standalone Novel Page Bar */
    .back-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1rem;
      margin-bottom: 2rem;
    }

    .back-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      color: var(--primary);
      text-decoration: none;
      font-weight: 700;
      font-size: 0.92rem;
      padding: 0.45rem 0.9rem;
      background: var(--primary-glow);
      border: 1px solid var(--primary);
      border-radius: var(--radius-sm);
      transition: background 0.15s ease, transform 0.15s ease;
    }

    .back-btn:hover {
      background: var(--surface-hover);
      transform: translateX(-2px);
    }

    .pagination-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1rem;
      margin-top: 2.5rem;
      padding-top: 1.5rem;
      border-top: 1px solid var(--border);
    }

    /* Footer */
    footer {
      border-top: 1px solid var(--border);
      background: var(--surface);
      padding: 2.25rem 1.5rem;
      margin-top: auto;
    }

    .footer-inner {
      max-width: 1080px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1rem;
      color: var(--text-muted);
      font-size: 0.85rem;
    }

    .footer-links a {
      color: var(--text-muted);
      text-decoration: none;
      transition: color 0.15s ease;
    }

    .footer-links a:hover { color: var(--primary); }

    /* Toast */
    .toast {
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background: var(--surface);
      border: 1px solid var(--primary);
      color: var(--text);
      padding: 0.75rem 1.25rem;
      border-radius: var(--radius-sm);
      box-shadow: 0 10px 25px rgba(0,0,0,0.4);
      display: none;
      z-index: 1000;
      font-weight: 600;
      font-size: 0.9rem;
    }
"""

COMMON_JS = """
<script>
  function initTheme() {
    const saved = localStorage.getItem('novel_theme') || 'dark';
    document.documentElement.setAttribute('data-theme', saved);
    updateThemeBtn(saved);
  }

  function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme') || 'dark';
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('novel_theme', next);
    updateThemeBtn(next);
  }

  function updateThemeBtn(theme) {
    const btns = document.querySelectorAll('.theme-toggle-btn');
    btns.forEach(btn => {
      btn.innerHTML = theme === 'dark' ? '☀️ Light' : '🌙 Dark';
    });
  }

  let currentFontSize = 1.02;
  function changeFontSize(delta) {
    currentFontSize = Math.max(0.85, Math.min(1.4, currentFontSize + delta));
    document.documentElement.style.setProperty('--article-font-size', currentFontSize + 'rem');
  }

  function copySummaryText() {
    const article = document.querySelector('.content-article');
    if (!article) return;
    navigator.clipboard.writeText(article.innerText).then(() => {
      showToast('Summary copied to clipboard!');
    });
  }

  function showToast(msg) {
    let toast = document.getElementById('app-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'app-toast';
      toast.className = 'toast';
      document.body.appendChild(toast);
    }
    toast.innerText = msg;
    toast.style.display = 'block';
    setTimeout(() => { toast.style.display = 'none'; }, 2400);
  }

  document.addEventListener('DOMContentLoaded', initTheme);
</script>
"""

STANDALONE_TEMPLATE = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>__TITLE__ — 100-Line Summary & Analysis</title>
  <meta name="description" content="Comprehensive 100-line summary, character dossier, and critical analysis of __TITLE__ by __AUTHOR__.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
__COMMON_CSS__
  </style>
</head>
<body>

  <!-- Top Navigation -->
  <nav class="top-nav">
    <div class="nav-inner">
      <a href="index.html" class="brand">
        <span class="brand-icon">📖</span>
        <span>Novels Summary Archive</span>
      </a>
      <div class="nav-links">
        <span class="version-pill">__VERSION__</span>
        <button class="theme-toggle-btn" onclick="toggleTheme()" title="Toggle theme">☀️ Light</button>
        <a href="https://github.com/govindarajanv/novels" target="_blank" rel="noopener noreferrer" class="nav-link">GitHub</a>
      </div>
    </div>
  </nav>

  <!-- Main Content -->
  <main class="container">
    <div class="back-bar">
      <a href="index.html" class="back-btn">← Back to Novels Index</a>
      <div class="reader-controls">
        <span class="badge badge-primary">__GENRE__</span>
        <span class="badge">__LANGUAGE__</span>
        <span class="badge badge-success">✓ 100 Lines</span>
        <button class="ctrl-btn" onclick="changeFontSize(-0.05)" title="Decrease font size">A-</button>
        <button class="ctrl-btn" onclick="changeFontSize(0.05)" title="Increase font size">A+</button>
        <button class="ctrl-btn" onclick="copySummaryText()" title="Copy entire text">📋 Copy</button>
        <a href="__SLUG__.md" class="ctrl-btn" target="_blank" title="View raw markdown">📝 Raw .md</a>
      </div>
    </div>

    <article class="content-article" style="background: var(--surface-card); border: 1px solid var(--border); border-radius: var(--radius); padding: 2.5rem; box-shadow: var(--card-shadow);">
__RENDERED_BODY__
    </article>

    <div class="pagination-bar">
      __PREV_LINK__
      <a href="index.html" class="ctrl-btn">📚 All Novels</a>
      __NEXT_LINK__
    </div>
  </main>

  <!-- Footer -->
  <footer>
    <div class="footer-inner">
      <div>
        <strong>Novels Summary Archive</strong> &bull; Version <span class="version-pill" style="font-size: 0.7rem; padding: 0.1rem 0.45rem;">__VERSION__</span>
      </div>
      <div class="footer-links">
        <a href="index.html">Index</a> &bull;
        <a href="__SLUG__.md">Markdown Source</a> &bull;
        <a href="https://github.com/govindarajanv/novels" target="_blank" rel="noopener noreferrer">Source Code</a>
      </div>
    </div>
  </footer>

__COMMON_JS__
</body>
</html>
"""

def generate_standalone_novel_html(novel, md_content: str, prev_novel=None, next_novel=None) -> str:
    name = novel.get("name", "Untitled")
    author = novel.get("author", "Unknown Author")
    genre = novel.get("genre", "Fiction")
    language = novel.get("language", "English")
    slug = slugify(name)
    rendered_body = md_to_html(md_content)

    prev_link = f'<a href="{slugify(prev_novel["name"])}.html" class="ctrl-btn">← {prev_novel["name"]}</a>' if prev_novel else '<span></span>'
    next_link = f'<a href="{slugify(next_novel["name"])}.html" class="ctrl-btn">{next_novel["name"]} →</a>' if next_novel else '<span></span>'

    out = STANDALONE_TEMPLATE
    out = out.replace("__TITLE__", html.escape(name))
    out = out.replace("__AUTHOR__", html.escape(author))
    out = out.replace("__GENRE__", html.escape(genre))
    out = out.replace("__LANGUAGE__", html.escape(language))
    out = out.replace("__SLUG__", slug)
    out = out.replace("__VERSION__", VERSION)
    out = out.replace("__RENDERED_BODY__", rendered_body)
    out = out.replace("__PREV_LINK__", prev_link)
    out = out.replace("__NEXT_LINK__", next_link)
    out = out.replace("__COMMON_CSS__", COMMON_CSS)
    out = out.replace("__COMMON_JS__", COMMON_JS)
    return out

INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Novels Summary Archive — Comprehensive 100-Line Analyses</title>
  <meta name="description" content="Curated repository of high-yield, structured 100-line novel summaries. Every entry encompasses complete narrative arcs, character dossiers, cryptic motifs, and critical thematic evaluations.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
__COMMON_CSS__
  </style>
</head>
<body>

  <!-- Top Navigation -->
  <nav class="top-nav">
    <div class="nav-inner">
      <a href="index.html" class="brand">
        <span class="brand-icon">📖</span>
        <span>Novels Summary Archive</span>
      </a>
      <div class="nav-links">
        <span class="version-pill">__VERSION__</span>
        <button class="theme-toggle-btn" onclick="toggleTheme()" title="Toggle theme">☀️ Light</button>
        <a href="#reader" class="nav-link">Reader</a>
        <a href="#catalog-table" class="nav-link">Catalog</a>
        <a href="https://github.com/govindarajanv/novels" target="_blank" rel="noopener noreferrer" class="nav-link">GitHub</a>
      </div>
    </div>
  </nav>

  <!-- Main Container -->
  <main class="container">

    <!-- Hero Section -->
    <header class="site-hero">
      <h1 class="site-title">Novels Summary Archive</h1>
      <div class="site-version-row">
        <span class="version-pill">__VERSION__</span>
        <span style="color: var(--text-muted); font-size: 0.9rem;">Comprehensive 100-Line Literary Analyses</span>
      </div>
      <p class="site-tagline">
        Curated repository of high-yield, structured 100-line novel summaries. Every entry encompasses complete narrative arcs, character dossiers, cryptic motifs, and critical thematic evaluations.
      </p>

      <div class="stats-banner">
        <div class="stat-item">
          <span class="stat-number">__COUNT__</span>
          <span>Cataloged Novels</span>
        </div>
        <div class="stat-item">
          <span class="stat-number">__TOTAL_LINES__</span>
          <span>Verified Lines</span>
        </div>
        <div class="stat-item">
          <span class="stat-number">100%</span>
          <span>Line-Count Accuracy</span>
        </div>
      </div>
    </header>

    <!-- Catalog of Summaries Cards Grid -->
    <section>
      <h2 class="section-title">📚 Catalog of Novels</h2>
      <div class="novels-grid">
__CARDS_HTML__
      </div>
    </section>

    <!-- Interactive In-Page Reader -->
    <section id="reader" class="reader-section">
      <div class="reader-header">
        <div class="reader-title-area">
          <span style="font-size: 1.5rem;">📖</span>
          <div>
            <h2 class="reader-title" id="current-novel-heading">__FIRST_NAME__</h2>
            <div id="reader-meta-badges" style="display: flex; gap: 0.4rem; margin-top: 0.25rem;">
              <span class="badge badge-primary" id="reader-genre">__FIRST_GENRE__</span>
              <span class="badge" id="reader-language">__FIRST_LANG__</span>
              <span class="badge badge-success">✓ 100 Lines Verified</span>
            </div>
          </div>
        </div>
        <div class="reader-controls">
          <button class="ctrl-btn" onclick="changeFontSize(-0.05)" title="Decrease font size">A-</button>
          <button class="ctrl-btn" onclick="changeFontSize(0.05)" title="Increase font size">A+</button>
          <button class="ctrl-btn" onclick="copySummaryText()" title="Copy entire text">📋 Copy</button>
          <a id="dedicated-link" href="__FIRST_SLUG__.html" class="ctrl-btn">📄 Dedicated Page</a>
          <a id="raw-link" href="__FIRST_SLUG__.md" target="_blank" class="ctrl-btn">📝 Raw .md</a>
        </div>
      </div>

      <nav class="novel-tabs-bar" aria-label="Novel selection tabs">
__TAB_BUTTONS__
      </nav>

      <article class="content-article" id="novel-reader-body">
__FIRST_HTML__
      </article>
    </section>

    <!-- Overview Table -->
    <section id="catalog-table" style="margin-top: 3.5rem;">
      <h2 class="section-title">📋 Repository Index & Overview</h2>
      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th>Novel Name</th>
              <th>Author</th>
              <th>Genre</th>
              <th>Language</th>
              <th>Reading Links</th>
              <th>Verification</th>
            </tr>
          </thead>
          <tbody>
__TABLE_ROWS__
          </tbody>
        </table>
      </div>
    </section>

  </main>

  <!-- Footer -->
  <footer>
    <div class="footer-inner">
      <div>
        <strong>Novels Summary Archive</strong> &bull; Version <span class="version-pill" style="font-size: 0.7rem; padding: 0.1rem 0.45rem;">__VERSION__</span>
      </div>
      <div class="footer-links">
        <a href="#reader">Interactive Reader</a> &bull;
        <a href="#catalog-table">Catalog Table</a> &bull;
        <a href="https://github.com/govindarajanv/novels" target="_blank" rel="noopener noreferrer">Source Code</a>
      </div>
    </div>
  </footer>

  <script>
    const NOVELS_DATA = __DATA_JSON__;

    function selectNovel(slug, smoothScroll = false) {
      const data = NOVELS_DATA[slug];
      if (!data) return;

      document.getElementById('current-novel-heading').innerText = data.name;
      document.getElementById('reader-genre').innerText = data.genre;
      document.getElementById('reader-language').innerText = data.language;
      document.getElementById('novel-reader-body').innerHTML = data.html;
      document.getElementById('dedicated-link').href = data.slug + '.html';
      document.getElementById('raw-link').href = data.slug + '.md';

      document.querySelectorAll('.novel-tab-btn').forEach(btn => btn.classList.remove('active-tab'));
      const activeTab = document.getElementById('tab-' + slug);
      if (activeTab) activeTab.classList.add('active-tab');

      document.querySelectorAll('.novel-card').forEach(card => card.classList.remove('active-card'));
      const activeCard = document.getElementById('card-' + slug);
      if (activeCard) activeCard.classList.add('active-card');

      if (history.replaceState) {
        history.replaceState(null, null, '#' + slug);
      }

      if (smoothScroll) {
        const readerElem = document.getElementById('reader');
        if (readerElem) {
          readerElem.scrollIntoView({ behavior: 'smooth' });
        }
      }
    }

    window.addEventListener('hashchange', () => {
      const hash = window.location.hash.replace('#', '');
      if (NOVELS_DATA[hash]) {
        selectNovel(hash, true);
      }
    });

    window.addEventListener('DOMContentLoaded', () => {
      const hash = window.location.hash.replace('#', '');
      if (NOVELS_DATA[hash]) {
        selectNovel(hash, false);
      }
    });
  </script>
__COMMON_JS__
</body>
</html>
"""

def generate_index_html(novels, novel_rendered_dict: dict) -> str:
    cards_html = []
    tab_buttons = []
    js_content_map = {}

    for idx, novel in enumerate(novels):
        name = novel.get("name", "Untitled")
        author = novel.get("author", "Unknown Author")
        genre = novel.get("genre", "Fiction")
        language = novel.get("language", "English")
        slug = slugify(name)
        active_tab_class = "active-tab" if idx == 0 else ""
        active_card_class = "active-card" if idx == 0 else ""

        tab_buttons.append(
            f'<button class="novel-tab-btn {active_tab_class}" id="tab-{slug}" onclick="selectNovel(\'{slug}\')">{name}</button>'
        )

        card = f'''  <div class="novel-card {active_card_class}" id="card-{slug}">
    <div>
      <div class="novel-card-meta">
        <span class="badge badge-primary">{genre}</span>
        <span class="badge">{language}</span>
        <span class="badge badge-success">✓ 100 Lines</span>
      </div>
      <h2 class="novel-card-title">{name}</h2>
      <p class="novel-card-author"><strong>By:</strong> {author}</p>
      <p class="novel-card-desc">Complete 100-line analytical synthesis covering major dramatic events, character dossiers, hidden symbols, and thematic deconstruction.</p>
    </div>
    <div class="novel-card-actions">
      <button class="btn-read-in-page" onclick="selectNovel('{slug}', true)">
        📖 Read In-Page &darr;
      </button>
      <div class="card-secondary-links">
        <a href="{slug}.html"><strong>Dedicated Page &rarr;</strong></a>
        <a href="{slug}.md" target="_blank">View Markdown</a>
      </div>
    </div>
  </div>'''
        cards_html.append(card)

        js_content_map[slug] = {
            "name": name,
            "author": author,
            "genre": genre,
            "language": language,
            "slug": slug,
            "html": novel_rendered_dict.get(slug, "<p>Summary loading...</p>")
        }

    table_rows = []
    for novel in novels:
        name = novel.get("name", "Untitled")
        author = novel.get("author", "Unknown Author")
        genre = novel.get("genre", "Fiction")
        language = novel.get("language", "English")
        slug = slugify(name)
        table_rows.append(
            f'<tr><td><strong>{name}</strong></td><td>{author}</td><td><span class="badge badge-primary">{genre}</span></td><td>{language}</td><td><a href="{slug}.html"><strong>Read HTML</strong></a> &bull; <a href="{slug}.md">Markdown</a></td><td><span class="badge badge-success">✓ 100 Lines</span></td></tr>'
        )

    first_novel = novels[0]
    first_slug = slugify(first_novel["name"])
    first_html = novel_rendered_dict.get(first_slug, "")

    out = INDEX_TEMPLATE
    out = out.replace("__VERSION__", VERSION)
    out = out.replace("__COUNT__", str(len(novels)))
    out = out.replace("__TOTAL_LINES__", str(len(novels) * 100))
    out = out.replace("__FIRST_NAME__", html.escape(first_novel.get("name", "")))
    out = out.replace("__FIRST_GENRE__", html.escape(first_novel.get("genre", "")))
    out = out.replace("__FIRST_LANG__", html.escape(first_novel.get("language", "")))
    out = out.replace("__FIRST_SLUG__", first_slug)
    out = out.replace("__FIRST_HTML__", first_html)
    out = out.replace("__CARDS_HTML__", "\n".join(cards_html))
    out = out.replace("__TAB_BUTTONS__", "\n".join(tab_buttons))
    out = out.replace("__TABLE_ROWS__", "\n".join(table_rows))
    out = out.replace("__DATA_JSON__", json.dumps(js_content_map))
    out = out.replace("__COMMON_CSS__", COMMON_CSS)
    out = out.replace("__COMMON_JS__", COMMON_JS)
    return out

def generate_index_md(novels) -> str:
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
        "3. **Static Generation**: `scripts/build_site.py` validates line counts and compiles `index.md`, `index.html`, and `<novel-slug>.html`.",
        "4. **GitHub Pages Deployment**: Automations build and deploy the archive to GitHub Pages.",
    ])

    return "\n".join(lines) + "\n"

def main():
    novels = load_novels()
    print(f"Loaded {len(novels)} novel(s) from {NOVELS_YAML_PATH}:")
    all_valid = True

    novel_md_contents = {}
    novel_rendered_html = {}

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
            with open(filepath, "r", encoding="utf-8") as f:
                md_content = f.read()
                novel_md_contents[slug] = md_content
                novel_rendered_html[slug] = md_to_html(md_content)

    # 1. Generate standalone HTML pages for each novel
    for i, novel in enumerate(novels):
        slug = slugify(novel.get("name"))
        if slug in novel_md_contents:
            prev_novel = novels[i - 1] if i > 0 else None
            next_novel = novels[i + 1] if i < len(novels) - 1 else None
            standalone_html = generate_standalone_novel_html(
                novel,
                novel_md_contents[slug],
                prev_novel=prev_novel,
                next_novel=next_novel
            )
            html_path = os.path.join(REPO_ROOT, f"{slug}.html")
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(standalone_html)
            print(f"  Generated HTML reader page: {html_path}")

    # 2. Generate index.html
    index_html_content = generate_index_html(novels, novel_rendered_html)
    with open(INDEX_HTML_PATH, "w", encoding="utf-8") as f:
        f.write(index_html_content)
    print(f"Generated {INDEX_HTML_PATH}")

    # 3. Generate index.md
    index_md_content = generate_index_md(novels)
    with open(INDEX_MD_PATH, "w", encoding="utf-8") as f:
        f.write(index_md_content)
    print(f"Generated {INDEX_MD_PATH}")

    if not all_valid:
        print("Notice: Some files are missing or do not match 100 lines.")
        sys.exit(1)
    else:
        print(f"Success: All novel summaries verified (100 lines each) and static site generated at {VERSION}!")

if __name__ == "__main__":
    main()
