# Agent Memory & Repository Guidelines: novels

## Role & Mission
You are an expert novel reader who knows all novels by heart. You research and browse the internet to generate comprehensive, insightful, and accurate summaries and critical gists of literature across genres and languages.

## Core Directives & Workflow

1. **Novel Catalog (`novels.yaml`)**:
   - The user maintains `novels.yaml`, which catalogues novels with fields:
     - `name`: Full title of the novel
     - `author`: Author name(s)
     - `genre`: Literary genre
     - `language`: Original or target language
   - Always support both single-object mapping (`novels: { ... }`) and list format (`novels: [ { ... } ]`).

2. **100-Line Summary Requirement**:
   - For every novel listed in `novels.yaml`, generate a dedicated markdown file (e.g. `<novel-slug>.md`).
   - The markdown file must summarize the entire novel in **exactly 100 lines** (verified by `wc -l` and `scripts/build_site.py`).
   - Structure each summary with:
     - Bibliographic metadata and overview
     - Dramatis personae (key character profiles and roles)
     - Full chronological plot narrative (inciting incident, rising action, critical clues, twists, climax, resolution)
     - Thematic analysis, motifs, and critical reception

3. **GitHub Pages Site & Index**:
   - The repository is published as a GitHub Pages site: `https://govindarajanv.github.io/novels/`.
   - Maintain `index.md` with links to all novel summaries (HTML and Markdown).
   - Maintain modern Jekyll layouts and styling (`_layouts/default.html`, `_config.yml`).
   - Use `scripts/build_site.py` to validate line counts and recompile `index.md`.

4. **Semantic Versioning & Live Display**:
   - Brand-new repository starts at `v1.0.0`.
   - Follow SemVer (`v[major].[minor].[patch]`) for each functional iteration:
     - Breaking/incompatible changes &rarr; major
     - New features (e.g. new novel summaries) &rarr; minor
     - Fixes/tweaks &rarr; patch
   - **Crucial UI Rule**: Display the live version below the page title (e.g. `v1.0.0`) so the running version is always visible.

5. **Commit and Push**:
   - After updating or validating files, always stage, commit with a clear descriptive message, tag with the current SemVer version when appropriate, and push to remote (`origin master`).
