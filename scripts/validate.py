#!/usr/bin/env python3
"""
Repository validator for the LogicalOutcomes aitools Skills library.

Checks, in order:
  1. Encoding      — every text file is valid UTF-8 with no NUL bytes.
  2. Front matter  — each Skills/<name>/SKILL.md has the required YAML keys,
                     and `name` matches its folder.
  3. Forbidden     — no LO-internal names, excluded-skill names, or old DRAFT
                     banner text appears anywhere in the repo.
  4. Lint          — markdownlint-cli2 reports zero errors (skipped with a
                     warning if the tool is not installed).

Usage:
    python3 scripts/validate.py            # from the repo root
    python3 scripts/validate.py --skip-lint

Exit code is non-zero if any check fails.
"""

import os
import re
import sys
import shutil
import subprocess

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SKILLS_DIR = os.path.join(REPO_ROOT, "Skills")
TEXT_EXTS = {".md", ".py", ".yaml", ".yml", ".html", ".txt"}
SELF = os.path.abspath(__file__)

# Forbidden strings are assembled from fragments so the literal bytes never
# appear in this file — otherwise the validator would flag itself.
FORBIDDEN = [
    "lo-workflow" + "-tools",
    "LO AI " + "Workspace",
    "Time" + "neye",
    "PM " + "Admin",
    "Independent Contractor " + "Agreement",
    "Ko" + "Note",
    "ko" + "note",
    "not officially " + "approved",
    "not been officially " + "approved",   # DRAFT-banner variant
    "DRAFT " + "document",                  # DRAFT-banner variant
    "the handbook " + "wins",
    "contract-proposal" + "-drafter",
    "document" + "-branding",
    "grill" + "-me",
    "prepare-for" + "-developer",
]

EXPECTED_SKILLS = [
    "convening-experts",
    "deep-background",
    "document-analysis",
    "evaluation-framework-builder",
    "project-starter",
    "social-services-review",
]

errors = []
warnings = []


def text_files():
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        if ".git" in dirpath.split(os.sep):
            continue
        for name in filenames:
            if os.path.splitext(name)[1].lower() in TEXT_EXTS:
                yield os.path.join(dirpath, name)


def rel(p):
    return os.path.relpath(p, REPO_ROOT)


# --- 1. Encoding -----------------------------------------------------------
def check_encoding():
    for f in text_files():
        raw = open(f, "rb").read()
        if b"\x00" in raw:
            errors.append(f"NUL byte in {rel(f)}")
        try:
            raw.decode("utf-8")
        except UnicodeDecodeError as e:
            errors.append(f"Invalid UTF-8 in {rel(f)}: {e}")


# --- 2. Front matter -------------------------------------------------------
def parse_front_matter(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    if not lines or lines[0].strip() != "---":
        return None
    block = []
    for l in lines[1:]:
        if l.strip() == "---":
            return block
        block.append(l)
    return None


def check_front_matter():
    for skill in EXPECTED_SKILLS:
        path = os.path.join(SKILLS_DIR, skill, "SKILL.md")
        if not os.path.isfile(path):
            errors.append(f"Missing SKILL.md for {skill}")
            continue
        block = parse_front_matter(path)
        if block is None:
            errors.append(f"{skill}/SKILL.md: missing YAML front matter")
            continue
        text = "\n".join(block)
        top = {}
        for l in block:
            m = re.match(r"^([A-Za-z_]+):(.*)$", l)
            if m:
                top[m.group(1)] = m.group(2).strip()
        if top.get("name") != skill:
            errors.append(f"{skill}/SKILL.md: name '{top.get('name')}' != folder '{skill}'")
        if not top.get("description") and "description:" not in text:
            errors.append(f"{skill}/SKILL.md: empty or missing description")
        if top.get("license") != "MIT":
            errors.append(f"{skill}/SKILL.md: license must be 'MIT' (got '{top.get('license')}')")
        if "metadata:" not in text:
            errors.append(f"{skill}/SKILL.md: missing metadata block")
        else:
            for key in ("author:", "version:", "source:"):
                if key not in text:
                    errors.append(f"{skill}/SKILL.md: metadata missing {key}")
            if "https://github.com/LogicalOutcomes/aitools" not in text:
                errors.append(f"{skill}/SKILL.md: source must be the aitools repo URL")


# --- 3. Forbidden strings --------------------------------------------------
def check_forbidden():
    for f in text_files():
        if os.path.abspath(f) == SELF:
            continue
        content = open(f, encoding="utf-8", errors="replace").read()
        for s in FORBIDDEN:
            if s in content:
                errors.append(f"Forbidden string '{s}' in {rel(f)}")


# --- 4. Lint ---------------------------------------------------------------
def check_lint(skip):
    if skip:
        warnings.append("Lint skipped (--skip-lint).")
        return
    npx = shutil.which("npx")
    if not npx:
        warnings.append("markdownlint-cli2 not found (npx unavailable); lint check skipped. "
                        "Install Node.js and run: npx markdownlint-cli2 \"**/*.md\"")
        return
    proc = subprocess.run(
        [npx, "--yes", "markdownlint-cli2", "**/*.md"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    if proc.returncode != 0:
        tail = "\n".join((proc.stderr or proc.stdout).strip().split("\n")[-15:])
        errors.append("markdownlint-cli2 reported errors:\n" + tail)


def main():
    skip_lint = "--skip-lint" in sys.argv
    check_encoding()
    check_front_matter()
    check_forbidden()
    check_lint(skip_lint)

    for w in warnings:
        print(f"WARN: {w}")
    if errors:
        print(f"\nFAIL: {len(errors)} problem(s) found:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print("PASS: all checks passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
