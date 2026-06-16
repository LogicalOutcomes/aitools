---
name: evaluation-framework-builder
description: Drafts complete program evaluation plans using the LogicalOutcomes evaluation framework (Kerr & Llewelyn, 2024) — logic model, evaluation questions, indicators, interest groups analysis, project roles, schedule, and meeting agendas. Use this skill whenever someone asks for an evaluation plan, evaluation framework, logic model, theory of change, indicators, outcome measures, M&E plan, or performance measurement for a nonprofit or community program — or asks to review or improve an existing evaluation framework, or mentions that a funder requires evaluation or outcome reporting. Also use it when someone asks to "measure outcomes" or design a survey for a program; the framework replaces most surveys with better methods.
license: MIT
metadata:
  version: 1.1.0
  author: LogicalOutcomes
  source: https://github.com/LogicalOutcomes/aitools
---

# Evaluation framework builder

Help nonprofit organizations create practical, focused evaluation plans following the LogicalOutcomes evaluation framework ([Kerr & Llewelyn, 2024](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4815131)). The framework treats evaluation as an intervention that improves services — not a reporting exercise. Every part of the plan exists to change what the program does, not to document it.

## Workflow

Gather information → research → generate plan → review with user → deliver. Adapt to what the user brings:

- **Detailed description (with or without a URL):** Start immediately. If you need one or two specifics (e.g., participant tracker status), ask alongside your first research step — don't gate on them.
- **Minimal information:** Ask 2–3 focused questions: what the program does, who it serves, what it aims to achieve, and what tracking they already keep on participants. Never more than 3 questions before starting.
- **Existing framework pasted or uploaded:** Review it against the framework rules below and suggest specific improvements. Don't regenerate from scratch unless asked.
- **Partial request (just a logic model, just indicators):** Provide that section alone, well enough to stand on its own, with a one-line note on how it fits the full 10-section plan. Don't generate the rest unless asked.

If tracker status is unknown, assume a weak/partial tracker (the common case) and design accordingly — see "Working with the tracker they actually have."

### Serve all three reasons for evaluating — don't pick one

A core design principle: **one plan serves all three reasons people evaluate at the same time** — funder accountability, management/Board concerns, and staff service-improvement. The basic framework already covers the core questions all three care about. So identifying the driver does **not** mean choosing a template or narrowing the plan; it means deciding where to add **emphasis** and whether a specific question needs an **add-on module** (below). Never drop coverage of the other two groups.

- **Funder requirement** — emphasize the funder's questions and keep burden low, while still using the data to improve services. If a funder mandates a survey or metric that conflicts with this framework, don't silently comply: acknowledge the requirement, recommend the tracker-and-interviews approach as primary, offer the funder-required method as supplementary, and document the limitation.
- **Management/Board concern** — emphasize the specific issue with targeted interviews and the relevant process metrics. If the question is one the basic framework can't answer on its own, add the matching module below rather than bending participant-outcome measures to fit it.
- **Staff / service improvement** — emphasize participant feedback, process analysis, and team problem-solving.

Most evaluations mix all three; that is expected, not a problem to resolve. Driver-fit detail is in `references/evaluation-services-guide.md`.

### Add a module when a question exceeds the basic framework

The basic framework gives useful but often *suggestive* findings. When the evaluation needs to answer a question it isn't built for, add a focused module rather than over-stretching the standard indicators or quietly ignoring the question. Name the module in the plan and state plainly what it adds; if it materially changes effort or cost, say so. From the handbook appendix:

| If they need to… | Add |
|---|---|
| Understand *why* a problem is happening (e.g., rising staff turnover or participant drop-out) | "Five Whys" + targeted staff/participant interviews; employee-engagement review |
| Justify or improve program design from evidence | Brief literature review (e.g., a Consensus search) |
| Confirm the program is delivered as intended | Implementation-fidelity measures tied to the program model |
| Examine equity in depth | Equity/DEI audit; community-based participatory methods; community-defined outcomes |
| Assess cost-effectiveness or process efficiency | Business-process analysis, participant journey mapping, cost-benefit |
| Demonstrate long-term impact | Rigorous design (comparison groups, longitudinal data) — flag scope and cost honestly |
| Compare against other programs | Common data standards (e.g., Common Impact Data Standard) and case-mix adjustment |

A module is a scoped addition to the standard plan, not a replacement for it.

### Research

Use web search to find the organization's website, understand similar program models and their evidence base, and identify evaluation approaches used with comparable programs. Use the organization's own language for the people they serve (e.g., "survivors," "youth," "families") — check their website, and never substitute generic or deficit-based terms. If research turns up little, proceed with what the user provided and note where more information would strengthen the plan. Don't fabricate references or statistics; claims about evidence come from search results or are flagged as needing verification.

### Generate

Before writing the plan, read both reference files:

1. **`references/plan-structure.md`** — the required 10-section structure, table formats, and verification checklist.
2. **`references/sample-plan.md`** — a complete exemplar (newcomer employment program). Match its depth, tone, and table formats exactly. Sections 7–10 in your plan deserve the same depth as sections 1–6.

After those two, consult these only when relevant (don't load them every time):

- **`references/evaluation-services-guide.md`** — driver-fit and funder-negotiation detail, data-collection priorities, and the roles/measures tables.
- **`references/evaluation-principles.md`** — the rationale, and the test for when a survey is appropriate.
- **`references/evaluation-planning-handbook.md`** — the methodology source of truth; check it on any point of dispute, and for the full menu of add-on modules.

### Review and deliver

Present the draft in Markdown and invite corrections — offer to adjust indicators, outcomes, or interest groups. Markdown is the default deliverable. If the user wants a polished client-facing document, offer a Word version (use the docx skill) or the print-styled HTML in `assets/html-template.html` (copy the head template verbatim; follow the body structure and table patterns in its comments).

## Framework rules (non-negotiable)

These override generic evaluation practice. They exist because LogicalOutcomes has watched hundreds of evaluations succeed or stall, and these are the patterns that separate the two.

1. **Minimize surveys; default to tracker data and small-sample interviews.** In programs serving 20–200 participants, surveys typically get too few responses to be useful (response rates of 10–30% are common), and staff often don't find the results credible enough to act on. Use small-sample interviews (5–15 people) where qualitative understanding matters. A survey is appropriate only when at least one of these holds: the sampling method and response rate support statistical validity; the results are built into service delivery and used to improve it; a standardized instrument is needed for benchmarking; or a funder requires one. When a survey is used, keep it brief, prefer validated questions (e.g., Statistics Canada / CCHS items), and still build the framework around tracker data and interviews. Apply the same test to every survey as to every other measure: *what will we change based on this?*
2. **Participant tracker first.** The tracker (case management data) is the primary data source for every measure — it has a near-100% response rate because collection is integrated into service delivery. Most organizations have only a weak or partial tracker; plan for the one they have — see "Working with the tracker they actually have."
3. **Every measure leads to action.** Each indicator must connect to a specific program change. If data won't be discussed in staff meetings and acted on, don't collect it.
4. **Evaluation is an intervention.** The goal is program change, not documentation.
5. **Build capacity incrementally.** The progression is tracker → outputs → short-term → mid-term → long-term (only after 2+ years of mid-term data). Never recommend long-term measures unless mid-term collection is already happening.
6. **Long-term outcomes are aspirational.** They appear in the logic model to show direction but are not directly measured; progress is inferred from mid-term patterns over 2+ years.
7. **Evaluation is a project.** Without a Project Owner (accountable for quality) and a Project Manager (day-to-day coordination), evaluation becomes nobody's priority and stalls. Every plan assigns both functions — though in a small organization one person may hold more than one role (see "Right-size to capacity").
8. **Disaggregate for equity — but only where the data supports it.** Where feasible, break down outputs and outcomes by population group (e.g., demographics, geography, language) to check whether the program works differently for different groups, and compare intake and drop-out against the target population. Draw disaggregation from the participant tracker (collected with consent), or from interviews or surveys whose response rate and design actually support the breakdown. Do not disaggregate small or self-selected samples in ways that imply more certainty than the data warrants, and never report cells small enough to identify an individual.

## Working with the tracker they actually have

Assume the realistic case: **most organizations do not have an adequate participant tracker, and few evaluations will build a new one.** Plan for the tracker that exists, not an ideal one. Three situations:

- **Adequate tracker / CMS** — use it as the primary source. This unlocks the handbook's richer questions: completion rates by site and population gro