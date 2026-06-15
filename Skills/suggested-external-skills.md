# LO Approved External Skills

This is LO's short list of **outside skills we've looked at and approved** — skills built and kept by other people that are worth using at LO. It exists so we can benefit from good work elsewhere without copying it (copies go stale) and without sending people into someone's whole repository of hundreds of unrelated skills.

This file lives in the `aitools` repo, in the `Skills/` folder, next to LO's own skills list. It is the single source of truth — edit it here to add or retire an approved skill, and the change takes effect everywhere with no repackaging.

**How this is used:** when someone asks for help and a skill on this list fits, Claude recommends it and handles fetching it from the source. Nobody has to run anything.

**How to maintain it (plain version):** to add a skill, look at it, and if it's good and right for LO, add a few lines below — its name, what it does, and the link. To retire one, delete its lines. Keep the list short and deliberate; that's the point. When in doubt about whether something belongs, leave it off.

Each entry below has been reviewed and approved for LO use. Last reviewed: 2026-06-14.

---

## Research and evidence

### literature-review
- **What it does:** runs systematic literature reviews across academic databases (PubMed, arXiv, Semantic Scholar, and others), and produces formatted documents/PDFs with checked citations in styles like APA and Vancouver.
- **Why it's here:** directly useful for LO's evidence work; complements our own social-services-review skill (this one is broader/biomedical, ours is tuned to social services and grey literature).
- **From:** https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/literature-review

### scholar-evaluation
- **What it does:** scores a piece of scholarly work against a structured framework (problem, methods, analysis, writing) and gives quantitative ratings plus feedback.
- **Why it's here:** quick structured way to judge the quality of a study or report.
- **From:** https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/scholar-evaluation

### scientific-critical-thinking
- **What it does:** assesses how trustworthy a scientific claim is — study design, biases, confounders — using evidence-grading frameworks (GRADE, Cochrane Risk of Bias).
- **Why it's here:** strong fit for weighing evidence in evaluations and reviews. Pairs with peer-review (below).
- **From:** https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/scientific-critical-thinking

### peer-review
- **What it does:** writes a structured, checklist-based review of a manuscript or grant, including reporting-standard checks (CONSORT/STROBE).
- **Why it's here:** useful when LO is asked to formally review someone else's research or proposal.
- **From:** https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/peer-review

## Writing and ideation

### scientific-writing
- **What it does:** drafts research manuscripts in flowing prose (not bullet points), using a standard IMRAD structure and proper citations.
- **Why it's here:** helps turn findings into publishable/funder-ready written prose.
- **Good to know:** it's designed to lean on a companion data-gathering tool ("research-lookup") from the same collection. It still works without it, but expect to supply sources yourself.
- **From:** https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/scientific-writing

### scientific-brainstorming
- **What it does:** open-ended idea generation — exploring angles, challenging assumptions, finding gaps — for the early, pre-plan stage of a project.
- **Why it's here:** handy at the start of designing a study or program before anything is fixed.
- **From:** https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/scientific-brainstorming

### market-research-reports
- **What it does:** produces long (50+ page) consulting-style market research reports with strategic frameworks (Porter Five Forces, PESTLE, SWOT, BCG matrix).
- **Why it's here:** useful for environmental scans and sector analyses.
- **Good to know:** it's built to use several companion tools from the same collection (for data lookup, charts, and images). Without those, you'll get the report structure and analysis but may need to add data and visuals by hand. Heavier than most entries here — reach for it only for genuinely large reports.
- **From:** https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/market-research-reports

## Working with Claude itself

### crafting-instructions
- **What it does:** helps write good instructions for Claude — project setups, prompts, or new skills.
- **Why it's here:** useful when LO staff are building their own Claude projects or skills.
- **From:** https://github.com/oaustegard/claude-skills/tree/main/crafting-instructions

---

### A note on the two source collections

Most entries above come from one large scientific collection (`K-Dense-AI/scientific-agent-skills`), and one from a general collection (`oaustegard/claude-skills`). We deliberately do **not** point people at those whole collections — they hold hundreds of skills, most irrelevant to LO, and they mix carefully-reviewed work with community contributions of unknown quality. This list is how we take the few good ones and leave the rest. Add to it only after looking at a skill yourself.
