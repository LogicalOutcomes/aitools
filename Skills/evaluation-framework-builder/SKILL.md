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

## Canadian Privacy Triage

**This is not legal advice — confirm with your own privacy or legal contact.**

Evaluation plans involving client, participant, donor, or employee data may implicate Canadian privacy law. Which law applies depends on your organization type, information type, and whether data crosses a border:

- **PIPEDA** (federal) applies to private-sector organizations engaged in commercial activity involving personal information. It does **not** generally apply to non-profits and charities **unless** they engage in commercial activity. See [PIPEDA in brief](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/pipeda_brief/) and [Privacy laws in Canada](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/02_05_d_15/) (OPC).
- **Provincial privacy laws** (e.g., PHIPA in Ontario for health information) and contractual obligations may apply regardless.
- **TCPS2 research ethics** applies when collecting data about human participants for research.

Operational defaults: de-identify before analysis; never paste identifiable data into a general-purpose AI assistant; confirm that participants provided informed consent for this use of their information; check that your use of AI tools is consistent with any ethics approval in place.

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
| Justify or improve program design from evidence | Verified evidence scan (see Research step); or the `social-services-review` skill (in this same repository) for a full review |
| Confirm the program is delivered as intended | Implementation-fidelity measures tied to the program model |
| Examine equity in depth | Equity/DEI audit; community-based participatory methods; community-defined outcomes |
| Assess cost-effectiveness or process efficiency | Business-process analysis, participant journey mapping, cost-benefit |
| Demonstrate long-term impact | Rigorous design (comparison groups, longitudinal data) — flag scope and cost honestly |
| Compare against other programs | Common data standards (e.g., Common Impact Data Standard) and case-mix adjustment |

A module is a scoped addition to the standard plan, not a replacement for it.

### Research

Use web search to find the organization's website, understand similar program models and their evidence base, and identify evaluation approaches used with comparable programs. Use the organization's own language for the people they serve (e.g., "survivors," "youth," "families") — check their website, and never substitute generic or deficit-based terms. If research turns up little, proceed with what the user provided and note where more information would strengthen the plan.

This step also produces the report's References (Section 10), so it carries a hard accuracy rule. Earlier versions of this skill dropped citations because they were hallucinated; citations are included again **only** under the discipline below. (The discipline assumes your assistant can open web pages. If it cannot browse, do not write citations from memory — instead flag each evidence claim for human verification and keep only the fixed framework source in Section 10.)

The discipline governs the **evidence-scan sources only**. The framework source (the handbook SSRN link) and the LogicalOutcomes Evaluation Planner link are fixed, permanently stable references — cite them exactly as given, and never re-open or re-verify them.

- **Open-to-cite.** Cite a source only if, in this session, you opened its authoritative record — the DOI/publisher landing page, PubMed, the journal, or (for grey literature) the issuing organization's own page — and confirmed its title, first author, year, and venue *from that page*, not from memory. If you have not opened the page, do not cite it.
- **Match the record, don't just resolve a link.** A dead link is an obvious fabrication signal, but the more common and more dangerous error is a *live* link to the wrong record: a near-identical title, an adjacent year, a preprint standing in for the version of record, or one entry in a multi-year report series. Confirm the page you opened reports the *same* title, authors, and year as the citation you are writing. Where several similar records exist — government evaluations and report series are the usual traps — pin down the specific one you actually drew on and cite that, not a sibling.
- **Verified, not padded — fewer is fine, including none.** This is a focused scan, not a literature review, so the quality gate is absolute and there is no minimum count. Cite only what you confirmed by opening the record; if that is two sources, cite two; if the scan turns up nothing confirmable, the references section carries only the framework source and says the scan found no citable evidence. Never add a source to reach a number, and stop at roughly six to eight even when more exist. For a fuller synthesis, use the `social-services-review` skill (in this same repository) instead of expanding this step.
- **Evidence is advisory.** Findings inform the indicators the plan already has; they do not expand the outcome set. The literature shows what is *associated with* outcomes — it cannot override what this organization can feasibly track and act on (capacity outranks evidence).
- **Flag, don't fabricate.** Any evidence claim, statistic, or effect size that can't be tied to a source you opened is flagged `[needs verification]` or omitted — never invented. This applies to references and numbers alike.

Record the confirmed sources (with the links that resolved to the matching record) for Section 10. Do the verification; do not narrate it in the plan — the deliverable carries the references themselves, not a sentence asserting they were checked (a self-attestation a reader can't verify and that reads as AI boilerplate). If you want an audit trail, keep it in working notes outside the client document.

### Generate

Before writing the plan, read both reference files:

1. **`references/plan-structure.md`** — the required 10-section structure, table formats, and verification checklist.
2. **`references/sample-plan.md`** — a complete exemplar (newcomer employment program). Match its depth, tone, and table formats exactly. Sections 7–10 in your plan deserve the same depth as sections 1–6.

After those two, consult these only when relevant (don't load them every time):

- **`references/evaluation-services-guide.md`** — driver-fit and funder-negotiation detail, data-collection priorities, and the roles/measures tables.
- **`references/evaluation-principles.md`** — the rationale, and the test for when a survey is appropriate.
- **`references/evaluation-planning-handbook.md`** — the methodology source of truth; check it on any point of dispute, and for the full menu of add-on modules.

### Review and deliver

Present the draft in Markdown and invite corrections — offer to adjust indicators, outcomes, or interest groups. Markdown is the default deliverable. If the user wants a polished client-facing document, offer a Word version (if your assistant can produce one) or the print-styled HTML in `assets/html-template.html`, which prints cleanly to PDF (copy the head template verbatim; follow the body structure and table patterns in its comments).

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

- **Adequate tracker / CMS** — use it as the primary source. This unlocks the handbook's richer questions: completion rates by site and population group, average/median sessions attended, and short-term outcomes by group.
- **Weak or partial tracker (the common case)** — keep whatever exists as the backbone and **add only a few high-value fields**: participant goals in their own words, sessions attended, goal progress, and a demographic field or two collected with consent. Where the tracker can't yet support an outcome, **estimate it from staff interviews and document review** — less precise, but, per the handbook, still credible and useful for decisions. Do **not** make a system build a precondition for outcome work, and do not over-promise precision the data can't deliver.
- **No tracker at all** — start the lightest possible one: a SharePoint List (Microsoft 365) or shared sheet with name, contact, start date, goals in their words, sessions attended, and progress notes. Add a monthly staff review, a quarterly check-in with 3–5 participants, and one documented service change per cycle. Until something exists to record in, limit the framework to outputs, process measures, and small-sample interviews.

Scale outcome measurement to what the tracking can bear — neither forbid it nor over-promise it.

## Right-size to capacity

Match the weight of the plan to the organization's staff time. For very small programs (e.g., ≤2 FTE): combine roles — one person is often both Liaison and Project Owner; reduce the six meetings to the two or three that matter most (define objectives and roles; monthly data review; annual recommendations); and lighten the reporting cadence. The four roles and six meetings are a maximum to draw from, not a minimum every organization must staff. Keeping the plan runnable matters more than completeness — an unrun plan improves nothing.

## Don't drift to generic evaluation

This framework is deliberately a minority approach; the mainstream monitoring-and-evaluation playbook is the very thing it replaces. When you notice yourself reaching for any of the following, substitute the framework's move instead:

- a baseline/endline or pre-post survey → tracker data + small-sample interviews (a survey only under rule 1)
- a "theory of change" or a multi-domain outcome framework → the two-table logic model; add no extra domains
- a SMART-target KPI dashboard *as the deliverable* → measures exist to trigger a service change, not to populate a scorecard
- measuring long-term outcomes directly → aspirational only; inferred from mid-term patterns over 2+ years
- "to be comprehensive, let's also measure…" → every added measure must pass *what will we change based on this?* Default to fewer.

## Terminology

Always use: **"interest groups"** (never "stakeholders"), **"participants"** (or the organization's own term), **"participant tracker"** (never "database" or "CRM"). Default to **"small-sample interviews"** for qualitative understanding; use "survey"/"questionnaire" only in the conditions set out in framework rule 1, and never reach for a "client satisfaction survey" as a default. Never use: "stakeholder," "comprehensive assessment," "multi-domain outcome framework."

## Placeholder language

Don't invent specifics the user hasn't provided. Meeting schedules → "To be determined by organization"; staff names → role titles only; target numbers → "Number of..." or "to be determined"; calendar dates → "Weeks 1–4" style; specific tools → "participant tracker" or "staff meeting notes."

## Before presenting: verify

Run the full checklist at the end of `references/plan-structure.md`. The most common failures: a combined 6-column logic model instead of two 3-column tables; surveys used as a default instead of tracker data and interviews (or without meeting any rule-1 condition); generic (non-customized) evaluation objectives; thin sections 7–10; banned terminology; invented names/dates/numbers; outcome indicators that depend on tracker fields the organization doesn't have (estimate from interviews/document review instead); and a plan heavier than the organization can run.

## Pointers

- Methodology source: [LogicalOutcomes Evaluation Planning Handbook](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4815131) (Kerr & Llewelyn, 2024). A full copy is bundled at `references/evaluation-planning-handbook.md` for offline reference.
- **Source-of-truth hierarchy.** The handbook governs *methodology and principles* — evaluation as an intervention, participant-informed practice, minimizing burden, building capacity incrementally, serving all three reasons for evaluating at once. LogicalOutcomes' current operationalization governs *output structure and terminology*: the 10-section plan, the two-table logic model, and the current vocabulary ("interest groups," "participant tracker") deliberately update the 2024 handbook's wording (which still says "stakeholders" and "CMS"). So follow this skill for structure and terms; defer to the handbook on method. If the skill and handbook disagree on **methodology**, the handbook wins — flag the discrepancy rather than silently diverging.

<!-- END OF FILE: evaluation-framework-builder/SKILL.md — if you do not see this line, the file was truncated in transit. -->
