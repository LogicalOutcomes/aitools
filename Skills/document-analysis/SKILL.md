---
name: document-analysis
description: >-
  Analyze documents the user already has — evaluation reports, program documents, interview
  transcripts, research papers, strategic plans, data files. Use this skill whenever the user
  uploads a document and wants to understand it rather than create something new: "summarize
  this report", "what are the themes in these transcripts", "does this evaluation's conclusion
  follow from its findings", "what's missing from this plan", "compare these two reports",
  "check its internal logic", "pull out the quotes about X", "first-pass coding", "evidence
  map", "gap analysis", "review this before my meeting", or just an uploaded report with "take
  a look at this". Also use it when a user has interview transcripts, focus group notes, or
  qualitative data to analyze, or asks whether a document's claims are supported by its
  evidence. If the task is to understand, assess, synthesize, or extract from existing
  documents, this is the skill — even if the user never says "analyze".
license: MIT
metadata:
  version: 1.0.0
  author: LogicalOutcomes
  source: https://github.com/LogicalOutcomes/aitools
---

# Document Analysis

> ⚠️ **Do not upload documents containing identifiable information about real people to a general-purpose AI assistant.** This includes names, contact details, health data, case notes, or any other information that could identify a client, participant, employee, or donor. De-identify documents before uploading — replace names and identifiers with codes (P1, P2, "one program manager"). See the Canadian privacy triage note below.

Support for deep work with complex, multi-page documents: surfacing patterns, extracting
themes, identifying gaps, flagging contradictions, and distinguishing what a document says,
what it implies, and what it leaves out. The user is the analyst; this skill helps them
understand what they already have. Analysis outputs are working notes to inform the user's own
thinking and writing — not text to copy straight into deliverables.

Ground all examples and illustrative scenarios in the nonprofit and community sector: program evaluations, community
health, youth services, settlement services, food security, mental health, public health
interventions. Avoid corporate, manufacturing, banking, or retail examples — they read as
foreign to most nonprofit clients.

## Canadian Privacy Triage

**This is not legal advice — confirm with your own privacy or legal contact.**

Which privacy law applies depends on your organization type, what information you are handling, and whether it crosses a border:

- **PIPEDA** (federal) applies to private-sector organizations engaged in commercial activity involving personal information. It does **not** generally apply to non-profits and charities **unless** they engage in commercial activity. See [PIPEDA in brief](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/pipeda_brief/) and [Privacy laws in Canada](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/02_05_d_15/) (OPC).
- **Provincial privacy laws** (e.g., PHIPA in Ontario for health information, PIPA in Alberta and BC) and contractual obligations may apply regardless.
- **TCPS2 research ethics** applies when you are collecting or using data about human participants for research purposes.

Operational defaults: de-identify before analysis; never paste identifiable data into a general-purpose AI assistant; confirm that participants provided informed consent for this use of their information.

## Which Tool is Canonical for What

- **Systematic qualitative coding of interview transcript sets** (a full study's transcripts,
  coded consistently against a codebook): for formal, study-wide coding against a fixed
  codebook, a dedicated coding tool or repeatable pipeline (de-identification → coding →
  synthesis) is more reliable than conversational analysis. Use this skill for exploratory
  first-pass work, for transcript questions arising inside a broader document conversation, or
  when the user explicitly wants conversational analysis.

## Workflow: Orient First, Then Go Deep

When a document arrives, don't dive straight into analysis. A brief orientation catches
upload problems (truncation, wrong file), confirms shared understanding, and lets the user
steer before tokens are spent on the wrong analysis:

1. Say what the document appears to be ("a 24-page program evaluation report for a youth
   mentorship initiative").
2. Describe its structure (sections, data tables, number of interviews referenced).
3. Note anything that limits analysis — truncated content, missing sections, unclear
   methodology, small samples — *before* presenting findings, not after.
4. Ask a focusing question: summarize, themes, gaps, or something specific?

For long documents, ask about scope before producing a lengthy analysis. For data files,
describe the structure (rows, columns, types) before analyzing content. For interview
transcripts, note participant count, approximate length, and visible structure. For multiple
long documents, summarize each individually before attempting cross-document synthesis — it
is more reliable than synthesizing everything at once.

## Privacy and De-identification Defaults

Uploaded documents may contain participant names, health data, case details, or client
information. Your organization's de-identification policy governs; sensible operational defaults are:

- **In all outputs** — summaries, thematic analyses, coding summaries, evidence maps — use
  participant codes (P1, P2) or role descriptors ("one program manager", "a youth
  participant") rather than any names in the source, even when the user hasn't asked. This
  stops identifying details propagating into deliverables, where they are much harder to
  recall.
- **If a document appears to contain identifying information**, flag it: "I notice this
  document contains what appear to be real names [or health data, or case details]. I can
  work with it, but you may want to consider whether this data should be de-identified before
  analysis. I can help you create a de-identification plan if that would be useful."
- Offer to design de-identification plans (what to redact, what coding scheme to use).
- For documents from research involving human participants, remind the user to verify that
  their use of AI tools is consistent with their ethics approval.

## Analysis Capabilities

**Document summary** — concise orientation: key findings, methodology, conclusions,
limitations, structure.

**Pattern and theme identification** — for each theme: a clear theme statement; supporting
evidence (quotes or references with page/section locations); how prominently it appears; and
counter-evidence or exceptions within the document.

**Gap analysis** — what is missing, unclear, or contradictory: topics claimed but not
adequately addressed; questions the evidence raises that the document doesn't answer;
contradictions between sections or between claims and evidence; missing context needed to
interpret findings.

**Cross-document synthesis** — across multiple documents: areas of agreement; disagreement or
contradiction; complementary findings that together tell a fuller story; gaps no document
addresses.

**Data interpretation** — for tables and quantitative content: trends and anomalies;
potential issues (small samples, missing data, unclear measures); where the data supports or
contradicts the document's narrative; what the numbers show without overstating what they
prove.

**Evaluation and research document analysis** — assess internal logic: is the logic model's
causal chain plausible; are findings supported by the evidence presented; is the methodology
rigorous and appropriate; do conclusions follow from findings; are recommendations actionable
and grounded in evidence. For health program evaluations and evidence syntheses, also assess
study design, biases and confounders, and consistency of findings across studies. The test is
always whether the report's own evidence justifies its own conclusions — not whether the
findings are "right" in some absolute sense.

Situate each document in the consulting document lifecycle (program description → evaluation
plan → instruments → raw data → findings report → final report; follow your organization's
evaluation document lifecycle guidance). An evaluation plan needs feasibility-and-alignment analysis; a findings
report needs evidence-quality analysis.

## Qualitative Analysis

Qualitative analysis is interpretive work — it requires understanding context, culture, power
dynamics, and lived experience. This skill supports it but cannot replace the analyst's
judgement. **Before doing any qualitative analysis (coding, themes, transcript work), read
`references/qualitative-analysis.md`** — it defines what to do and, more importantly, the
boundaries: where description ends and the analyst's interpretation begins, what cannot be
seen in transcript text, and the transparency notes every qualitative output needs.

The headline rules, in brief: suggest rather than assert (themes are "potential themes for
your review", always marked as draft); ground every theme in quotes with locations; describe
what participants said before interpreting what it means; and invite the analyst's contextual
knowledge.

### Counting Theme Frequency

When counts matter ("how many participants raised cost?"), **compute them programmatically**:
search the source files with code, count matches against the coded segments, and report the
verified number with the code used to produce it available for inspection. Counts estimated
from reading long documents in context are unreliable — the predecessor tool banned numeric
counts entirely for this reason. Code removes that failure mode; use it. When counts aren't
needed or the corpus is too unstructured to count meaningfully, use descriptive frequency
language: "a recurring theme across most interviews", "raised by a few participants", "one
participant offered a distinct perspective". Never report a specific count you have not
verified programmatically or by directly enumerable inspection (e.g., three short excerpts).

## Epistemic Discipline: States / Implies / Infers

In every substantive analysis, label which of three things each claim is:

- What the document **states** — direct claims and data. "The report states that..."
- What the document **implies** — reasonable inferences from the text. "The data in Table 3
  implies that..."
- What you **infer** — analysis going beyond the text. "Based on the gap between the stated
  methodology and the reported findings, it appears that..."

This discipline must hold across long conversations, not just the first exchange — drift
toward unlabeled inference is the main way document analysis quietly becomes fabrication.

Flag when documents are **ambiguous** (text supports multiple interpretations),
**incomplete** (missing sections, partial data, truncation), **contradictory** (incompatible
claims), or **methodologically limited** (small samples, unclear measures, missing comparison
groups). Note data limitations before interpreting data: a finding based on 8 interviews
carries different weight than one based on 200 survey responses.

## External Sources

Web access is available. Fetching external standards, frameworks, or published benchmarks to
analyze a document against is fine (e.g., comparing a report's methods section to RE-AIM or
to a funder's reporting requirements). But **every claim about what a document contains must
come from the document itself** — never let fetched material blur into "the report says".
Keep the two evidence streams labeled.

## Citing the Document

Every claim about a document must reference a specific location: page numbers, section
headers, direct quotes for key claims, table/figure references. "On page 12, under
'Stakeholder Perspectives,' the report states..." is useful. "The report mentions stakeholder
perspectives" is not — it can't be checked.

## Output Formats

Match the format to the question; offer alternatives when the best fit is unclear. The six
standard formats (document summary, thematic analysis, gap analysis, cross-document
comparison, evidence map, coding summary) are specified in `references/output-formats.md` —
**read it before producing a structured output**, and use the fill-in skeletons in
`assets/output-templates.md` when producing one as a file. Thematic analyses and coding
summaries are always marked as drafts for analyst review.

## Working Style

- Be thorough but structured — dense analysis is fine; disorganized analysis is not.
- Ask before assuming scope on long documents.
- Invite the user's expertise: they know the context; ask questions that leverage it.
- If a document is truncated or partially uploaded, state what you have, work with it, and
  note what additional content would strengthen the analysis.
