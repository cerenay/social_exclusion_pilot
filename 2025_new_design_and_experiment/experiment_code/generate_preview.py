#!/usr/bin/env python3

import os
import re
from datetime import date

# ── Paths ──────────────────────────────────────────────────────────────────────
SCRIPT_DIR      = os.path.dirname(os.path.abspath(__file__))
EXPERIMENT_DIR  = os.path.join(SCRIPT_DIR, "social_exc_2025")
PAGE_HTML       = os.path.join(EXPERIMENT_DIR, "_templates", "global", "Page.html")
OUTPUT_DIR      = os.path.join(SCRIPT_DIR, "screenshots")
OUTPUT_FILE     = os.path.join(OUTPUT_DIR, "experiment_preview.html")

# Screens in experiment order: (app_name, screen_label, template_path_relative_to_EXPERIMENT_DIR)
SCREENS = [
    ("painting_choice",  "Screen 1 · Welcome & Consent",
     "painting_choice/Welcome.html"),
    ("painting_choice",  "Screen 2 · Part 1 Introduction",
     "painting_choice/Intro.html"),
    ("painting_choice",  "Screen 3 · Painting Preferences",
     "painting_choice/PaintingChoice.html"),
    ("painting_choice",  "Screen 4 · Group Assignment",
     "painting_choice/Transition.html"),
    ("painting_choice",  "Screen 5 · Reasons for Choice",
     "painting_choice/Explanation.html"),
    ("counting_matrix",  "Screen 6 · Part 2 Instructions (all treatments)",
     "counting_matrix/Instructions.html"),
    ("counting_matrix",  "Screen 7 · Slider Practice Round",
     "counting_matrix/SliderExample.html"),
    ("counting_matrix",  "Screen 8 · Slider Task",
     "counting_matrix/MatrixTask.html"),
    ("counting_matrix",  "Screen 9 · Slider Task Results",
     "counting_matrix/Results.html"),
    ("dictator",         "Screen 10 · Part 3 Introduction",
     "dictator/Introduction.html"),
    ("dictator",         "Screen 11 · Round 1 – Baseline Allocation",
     "dictator/offer_1.html"),
    ("dictator",         "Screen 12 · Round 2 – Group-Identity Scenarios",
     "dictator/offer_2.html"),
    ("dictator",         "Screen 13 · Round 3 – Task-Difficulty Scenarios",
     "dictator/offer_3.html"),
    ("dictator",         "Screen 14 · Part 3 Results",
     "dictator/Results.html"),
    ("dictator",         "Screen 15 · Total Payoffs & Exchange Rate",
     "dictator/totPayoffs.html"),
    ("postExp_survey",   "Screen 16 · Survey – Familiarity with Artists",
     "postExp_survey/Postexp_surv1.html"),
    ("postExp_survey",   "Screen 17 · Survey – Group & Task Feelings",
     "postExp_survey/Postexp_surv2.html"),
    ("postExp_survey",   "Screen 18 · Survey – Emotions",
     "postExp_survey/Postexp_surv2b.html"),
    ("postExp_survey",   "Screen 19 · Survey – Allocation Task Questions",
     "postExp_survey/Postexp_surv3.html"),
    ("postExp_survey",   "Screen 20 · Demographics",
     "postExp_survey/Demo.html"),
    ("postExp_survey",   "Screen 21 · Thank You",
     "postExp_survey/EndSurvey.html"),
]


# ── CSS extractor ──────────────────────────────────────────────────────────────
def extract_css(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        src = f.read()
    m = re.search(r"<style>(.*?)</style>", src, re.DOTALL)
    if m:
        return m.group(1).strip()
    raise ValueError(f"No <style> block found in {path}")


# ── Template parser ────────────────────────────────────────────────────────────
def _get_block(html: str, block_name: str) -> str:
    """Extract the body of a named block (oTree {{ }} or Jinja2 {% %} style)."""
    patterns = [
        rf'\{{\{{\s*block\s+{block_name}\s*\}}\}}(.*?)\{{\{{\s*endblock\s*\}}\}}',
        rf'\{{%\s*block\s+{block_name}\s*%\}}(.*?)\{{%\s*endblock\s*%\}}',
    ]
    for pat in patterns:
        m = re.search(pat, html, re.DOTALL)
        if m:
            return m.group(1).strip()
    return ""


def _strip_for_loops(html: str) -> str:
    """Remove for/endfor tags, keep loop body once, add ⋯ note.
    Works from innermost loop outward (up to 6 nesting levels)."""
    loop_re = re.compile(
        r'\{%-?\s*for\s+[^%]+?-?%\}'   # {% for ... %}
        r'((?:(?!\{%-?\s*for\s).)*?)'   # body (no nested for)
        r'\{%-?\s*endfor\s*-?%\}',      # {% endfor %}
        re.DOTALL,
    )
    for _ in range(6):
        new = loop_re.sub(
            lambda m: m.group(1).rstrip()
                      + '\n<span class="preview-loop">⋯ repeats for each item ⋯</span>\n',
            html,
        )
        if new == html:
            break
        html = new
    return html


def _strip_conditionals(html: str) -> str:
    """Remove if/elif/else/endif block tags; keep all branch content."""
    for pat in [
        r'\{%-?\s*if\s+[^%]+?-?%\}',
        r'\{%-?\s*elif\s+[^%]+?-?%\}',
        r'\{%-?\s*else\s*-?%\}',
        r'\{%-?\s*endif\s*-?%\}',
    ]:
        html = re.sub(pat, '', html)
    return html


def _replace_known_tags(html: str) -> str:
    """Swap oTree shorthand tags for preview-friendly HTML."""
    # {{ next_button }}
    html = re.sub(
        r'\{\{\s*next_button\s*\}\}',
        '<button class="btn-primary" disabled>Next →</button>',
        html,
    )
    # {{ formfields }}
    html = re.sub(
        r'\{\{\s*formfields?\s*\}\}',
        '<p class="preview-placeholder"><em>[oTree renders form fields here]</em></p>',
        html,
    )
    # {{ formfield_errors 'X' }}
    html = re.sub(r"\{\{\s*formfield_errors\s+['\"]?\w+['\"]?\s*\}\}", '', html)
    # {{ load otree }}
    html = re.sub(r'\{\{\s*load\s+otree\s*\}\}', '', html)
    # {{ forloop.counter }} / {{ forloop.counter0 }}
    html = re.sub(r'\{\{\s*forloop\.counter0\s*\}\}',
                  '<span class="preview-var">0</span>', html)
    html = re.sub(r'\{\{\s*forloop\.counter\s*\}\}',
                  '<span class="preview-var">1</span>', html)
    return html


def _replace_variables(html: str) -> str:
    """Replace {{ var }} and {{ form.X }} with styled placeholders."""
    # {{ form.X.label }}
    html = re.sub(
        r'\{\{\s*form\.(\w+)\.label\s*\}\}',
        lambda m: f'<em>[{m.group(1)} label]</em>',
        html,
    )
    # {{ form.X }} (widget)
    html = re.sub(
        r'\{\{\s*form\.(\w+)\s*\}\}',
        lambda m: f'<span class="preview-var">[{m.group(1)} field]</span>',
        html,
    )
    # {{ word.word }} or {{ word }}
    html = re.sub(
        r'\{\{\s*([\w][\w.]*)\s*\}\}',
        lambda m: f'<span class="preview-var">[{m.group(1)}]</span>',
        html,
    )
    # catch-all for anything left like {{ 'x' if ... else 'y' }}
    html = re.sub(
        r'\{\{[^}]+\}\}',
        '<span class="preview-var">[expr]</span>',
        html,
    )
    return html


def _remove_scripts(html: str) -> str:
    """Strip <script> blocks (they don't run in the static preview)."""
    return re.sub(r'<script\b[^>]*>.*?</script>', '', html,
                  flags=re.DOTALL | re.IGNORECASE)


def _remove_remaining_tags(html: str) -> str:
    """Remove any leftover {% ... %} tags."""
    return re.sub(r'\{%[^%]*%\}', '', html)


def parse_template(filepath: str):
    """Read an oTree template and return (title: str, body_html: str)."""
    with open(filepath, encoding="utf-8") as f:
        src = f.read()

    title = _get_block(src, "title") or "Page"
    body  = _get_block(src, "content") or src

    # Apply transformations in order
    body = _strip_for_loops(body)
    body = _strip_conditionals(body)
    body = _replace_known_tags(body)
    body = _replace_variables(body)
    body = _remove_scripts(body)
    body = _remove_remaining_tags(body)

    # Collapse excessive blank lines
    body = re.sub(r'\n{3,}', '\n\n', body).strip()

    return title.strip(), body


# ── HTML builder ───────────────────────────────────────────────────────────────
def build_screen(label: str, title: str, body: str) -> str:
    return f"""
<div class="screen-label">{label}</div>
<div class="page-shell">
  <h2 class="page-title">{title}</h2>
  <div class="page-body">
    {body}
  </div>
</div>
"""


def build_divider(app_name: str) -> str:
    return f"""
<div class="app-divider">
  <hr><span>{app_name}</span><hr>
</div>
"""


PREVIEW_EXTRA_CSS = """
/* ── Preview shell ── */
body {
  background: #E8E8EC !important;
  padding: 40px 20px !important;
}
.page-shell {
  max-width: 760px;
  margin: 0 auto 8px;
  background: var(--bg);
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 4px 24px rgba(0,0,0,0.12);
}
.page-title {
  font-size: 1.45rem !important;
  font-weight: 600 !important;
  color: var(--text-main) !important;
  text-align: center !important;
  padding: 30px 36px 22px !important;
  margin: 0 !important;
  border-bottom: 1px solid var(--border) !important;
  background: var(--card-bg) !important;
}
.page-body {
  padding: 28px 36px 32px;
  background: var(--bg);
}
.screen-label {
  max-width: 760px;
  margin: 48px auto 6px;
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #6366F1;
}
.screen-label:first-of-type { margin-top: 0; }

/* ── App divider ── */
.app-divider {
  max-width: 760px;
  margin: 56px auto 12px;
  display: flex;
  align-items: center;
  gap: 14px;
}
.app-divider span {
  font-size: 0.82rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: #52525B;
  white-space: nowrap;
}
.app-divider hr {
  flex: 1;
  border: none;
  border-top: 1px solid #C4C4CC;
  margin: 0;
}

/* ── Preview helpers ── */
.preview-var {
  display: inline-block;
  background: #EEF2FF;
  color: #4338CA;
  border: 1px solid #C7D2FE;
  border-radius: 4px;
  padding: 1px 6px;
  font-size: 0.8rem;
  font-family: monospace;
  vertical-align: middle;
}
.preview-loop {
  display: block;
  color: var(--text-muted);
  font-size: 0.8rem;
  font-style: italic;
  margin: 4px 0 8px 0;
}
.preview-placeholder {
  color: var(--text-muted);
  font-style: italic;
  font-size: 0.88rem;
}

/* ── Button override for preview (not real buttons) ── */
.btn-primary {
  background: var(--accent) !important;
  border: none !important;
  border-radius: 8px !important;
  padding: 10px 28px !important;
  font-size: 0.95rem !important;
  font-weight: 500 !important;
  color: #fff !important;
  cursor: default !important;
  margin-top: 24px !important;
  display: inline-block !important;
  opacity: 0.85 !important;
}

/* ── Footer ── */
.preview-footer {
  max-width: 760px;
  margin: 56px auto 0;
  text-align: center;
  font-size: 0.78rem;
  color: var(--text-muted);
  padding-bottom: 40px;
}
"""


def build_html(theme_css: str, sections: list) -> str:
    body = "\n".join(sections)
    today = date.today().strftime("%B %Y")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Social Exclusion Experiment – Full Preview</title>
<style>
/* ── Theme (auto-read from _templates/global/Page.html) ── */
{theme_css}

{PREVIEW_EXTRA_CSS}
</style>
</head>
<body>

{body}

<div class="preview-footer">
  Social Exclusion Experiment &middot; Full Preview &middot; {today}<br>
  <span style="font-size:0.72rem;">
    Static text is read directly from your template files.
    <span class="preview-var" style="font-size:0.72rem;">[placeholders]</span>
    mark dynamic oTree variables filled at runtime.
  </span>
</div>

</body>
</html>
"""


# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    # 1. Read CSS
    print(f"Reading CSS from:  {PAGE_HTML}")
    css = extract_css(PAGE_HTML)
    print("  ✓ CSS extracted.\n")

    # 2. Parse each template
    sections = []
    current_app = None

    for app, label, rel_path in SCREENS:
        filepath = os.path.join(EXPERIMENT_DIR, rel_path)

        if app != current_app:
            sections.append(build_divider(app))
            current_app = app

        if not os.path.exists(filepath):
            print(f"  ⚠  File not found, skipping: {rel_path}")
            continue

        title, body = parse_template(filepath)
        sections.append(build_screen(label, title, body))
        print(f"  ✓  {rel_path}")

    # 3. Write output
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    html = build_html(css, sections)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\nPreview saved to:\n  {OUTPUT_FILE}")
    print("\nDone! Open experiment_preview.html in your browser.")


if __name__ == "__main__":
    main()
