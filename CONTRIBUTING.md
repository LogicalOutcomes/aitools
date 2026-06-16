# Contributing to LogicalOutcomes AI Tools

Thanks for helping improve these skills. This guide covers how a skill is
structured, what its front matter must contain, and how to validate and lint a
change before opening a pull request.

## What a skill is

Each skill lives in its own folder under `Skills/` and is centred on a single
`SKILL.md` — a plain-language instruction sheet describing the task, how to do it
well, and when to use it. A skill folder may also include:

- `references/` — background material the assistant reads on demand.
- `assets/` — templates and output scaffolds.
- `examples/` — worked examples.
- `scripts/` — helper scripts (Python 3).

Skills are platform-neutral. Write instructions for "the assistant" or "the
agent" rather than naming a specific AI product.

## SKILL.md front matter

Every `SKILL.md` must begin with a YAML front matter block delimited by `---`
lines. Required keys:

```yaml
---
name: your-skill-name            # must exactly match the folder name
description: >-                   # non-empty; this populates the README table
  One or more sentences describing what the skill does and when to use it.
license: MIT                      # exactly this value
metadata:
  version: 1.0.0                  # semantic version
  author: LogicalOutcomes
  source: https://github.com/LogicalOutcomes/aitools
---
```

If a skill is derived from or inspired by someone else's work, credit it in the
metadata with `based_on:` (direct derivation) or `inspired_by:` (looser
influence), pointing at the original, and add a matching note to the README
"Crediting and reuse" section.

## Privacy and accuracy

Skills that handle real documents or personal data must carry the Canadian
privacy triage note (PIPEDA / OPC links, the nonprofit/commercial-activity
caveat, and a "this is not legal advice" line). Templates that carry legal or
employment weight must tell the user to adapt them and seek their own legal or
HR review before use.

## Validate before you commit

From the repo root:

```bash
python3 scripts/validate.py
```

`validate.py` checks encoding (valid UTF-8, no NUL bytes), SKILL.md front matter,
forbidden strings (LO-internal names and excluded-skill names), and runs the
Markdown linter. It exits non-zero if anything fails. Use `--skip-lint` to skip
the lint step when Node.js is not available.

## Markdown lint

Markdown is linted with [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2)
using the rules in [`.markdownlint-cli2.yaml`](.markdownlint-cli2.yaml) at the
repo root. Run it directly with:

```bash
npx markdownlint-cli2 "**/*.md"
```

The config disables rules that conflict with long-form instruction sheets and
reusable templates (line length, inline HTML, single-H1, and similar) and keeps
the rules that catch real defects: fenced code blocks must declare a language
(MD040), URLs must be linked rather than bare (MD034), and headings and lists
must be surrounded by blank lines (MD022, MD032). Every fenced code block needs
a language tag (` ```text `, ` ```python `, etc.). The target is zero errors.

## Pull requests

Keep changes scoped to one skill where possible, run `scripts/validate.py`, and
note any new attribution in both the front matter and the README.
