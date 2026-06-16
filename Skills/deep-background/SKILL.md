---
name: deep-background
description: >-
  Meticulous fact-checking, claim analysis, and contextualization using Mike
  Caulfield's Deep Background methodology. Use this skill whenever the user
  asks to fact-check, verify, debunk, or contextualize a claim, quote, statistic,
  news story, screenshot, meme, viral post, photo, or historical artifact —
  including questions like "is this true?", "is this real?", "what's the story
  behind this?", "check this", or "where does this photo come from?". Also use
  it when the user uploads an image of a social media post, headline, placard,
  or document and wants it assessed, or asks for photo provenance, source
  reliability assessment, a "sources table", a "context report", a "discourse
  map", or to "read the room" on a controversy. Trigger even if the user
  doesn't use the word "fact-check" — any request to assess whether something
  is accurate, misleading, or missing context belongs here.
license: MIT
metadata:
  version: 1.0.0
  author: LogicalOutcomes
  source: https://github.com/LogicalOutcomes/aitools
---

# Deep Background: Fact-Checking and Contextualization

This skill implements Mike Caulfield's "Deep Background" methodology: a structured, self-critical process for verifying claims, identifying errors, providing context, and assessing source reliability. The goal is not just true/false verdicts but giving the user the context needed to understand a claim, image, or artifact — and to make decisions about it.

Core stance: even when certain about something, look for what might be missing. Always ask whether cited sources are real and appropriate to the question. Be meticulous and self-critical.

## Quick-Check Mode (for busy staff and simple claims)

For simple, low-controversy claims where a full report is unnecessary, use this streamlined 3-step method:

1. **Stop and assess.** What exactly is being claimed? What is the likely overarching claim behind it (moderate and strong version)? Could this be misleading even if technically true?
2. **Find better coverage.** Run 1-2 targeted searches. Prefer authoritative sources (government, established news outlets, peer-reviewed databases). If initial results are thin, try one alternative framing.
3. **Deliver a verdict.** One-sentence bottom line, 2-3 sentences of support with citations, one note on evidence quality. Flag if the full-report method is needed.

**When to use quick-check:** a single verifiable claim, low stakes, user is time-pressed. If the claim is contested, politically charged, involves an image, or the quick search surfaces conflicting results, switch to the full method below.

## First Response in a Full Session

1. **Establish the current date.** Get the real date from whatever is available — the environment, a date tool, or system context. Display it in the output header — never guess or omit it.
2. **Identify the user's informational need** from what they've uploaded or stated. If an image is uploaded, describe it and transcribe any text *first*, then ask the user to correct any errors in the description/transcription before continuing analysis.
3. **Identify the overarching claim** (see below) to guide investigation. Only offer the user a menu of options if their informational need is genuinely unclear.
4. If during initial searches a clearer overarching claim emerges (e.g., a common misconception is identified), switch to that overarching claim. If there are no misconceptions, provide the context needed to understand the claim, quote, or media.

If the session starts with no claim or image to analyze, give a brief welcome message explaining the skill's function and ask for a claim, image, or artifact to explore.

## The Overarching Claim

Facts are usually presented as evidence *of* something bigger. Before researching, identify and state the likely overarching claim in two versions:

- **Moderate version**: the restrained inference (e.g., "this weather event was unusually severe"; "the missed anniversary shows carelessness")
- **Strong version**: the expansive inference, if the framing cues support it (e.g., "climate change is causing these events"; "the marriage is failing")

Read each factual claim through the lens of the overarching claim to understand its meaning and relevance.

## Search Discipline

Before searching: preview four possible searches, critique how they might bias results (loaded terms, one-sided framings, recency bias, language limits), then run four real searches designed to overcome those flaws. It is fine if individual sources are biased as long as the set of searches together surfaces a range of viewpoints (e.g., pair "X is true" framings with "X debunked" framings).

If results are thin or the topic is regional, search in additional relevant languages.

Verify that links cited in the response lead directly to real, existing pages — use web_fetch to spot-check when uncertain. Never cite a URL you have not seen in search results or fetched. If only a search link is available, find a better direct link where possible.

## Response Structure for a Fact-Check

**Always lead with a one-line bottom-line verdict** — the plain answer to the question — before any tables or sections.

Then match the depth to the question:

- **Compact check** (default for a single, simple, low-controversy claim): the verdict line, a short paragraph of support with citations, and a brief source note. Skip the full table apparatus.
- **Full report** (for contested, high-stakes, or multi-claim questions, or whenever the user asks for it): the verdict line, then all sections below in this exact order (all sections include citations where available):

```text
__Generated [current date], may be out of date if significantly later.__
__AI-Generated: Will likely contain errors; treat this as one input into a human-checked process__

1. ✅ Verified Facts (table)
2. ⚠️ Errors and Corrections (table)
3. 📌 Corrections Summary:
4. 📌 Potential Leads
5. 🛑 Assessment of Source Usefulness: (table)
6. 📗 Revised Summary (Corrected & Contextualized):
7. 🧭 Notes on the Information Environment:
8. 💡 Tip Suggestion:

__Core commands: `another round`, `context report`, `sources table`, `read the room`. Also try: `discourse map`, `plain-language summary`, `explain this with an animation`__
```

(If an image was uploaded, the describe-transcribe-confirm step happens *before* this structure is produced.)

### Section Specifications

**1. Verified Facts Table** — headers exactly:
`| Statement | Status | Clarification & Correction | Confidence (1–5) |`
Statement is a direct quote or paraphrase of a verified claim; Status is "✅ Correct"; add context/minor clarifications with cited evidence; confidence 1–5 with 5 highest.

**2. Errors and Corrections Table** — headers exactly:
`| Statement | Issue | Correction | Correction Confidence (1–5) |`
Issue markers: ❌ Incorrect (factual error), 💭 opinion, ❓ unable to substantiate. Corrections cite evidence; note opinions as outside the scope of the check.

**3. Corrections Summary** — H3 header "📌 Corrections Summary:". Bullet points, each led by a bold label for the correction type (e.g., **Placard Text Correction**). Concise but complete; focus on the most significant errors.

**4. Potential Leads** — H3 header "📌 Potential Leads:". Table formatted like the Verified Facts table. Unconfirmed-but-not-debunked claims that might reward future investigation, each with a plausibility rating and a link (e.g., "Photo is possibly Salma Hayek" with a link to the post suggesting it). If no direct link exists, provide a search link.

**5. Source Usefulness Assessment** — headers exactly:
`| Source | Usefulness Assessment | Notes | Rating |`
Source names in **bold**; usefulness uses ✅ or ⚠️ plus a brief assessment; notes give source type and verification status; rating 1–5 with 5 highest. State-controlled media (controlled, not merely funded) get an asterisk and a note below the table: *State-controlled media, not a reliable source on anything that intersects with its national interests or interest of ruling party.*

**6. Revised Summary** — H3 header "📗 Revised Summary (Corrected & Contextualized):". 2–3 corrected paragraphs integrating all verified facts and corrections, neutral scholarly tone, no speculation unsupported by reliable sources, inline citations.

**7. Notes on the Information Environment** — H3 header "🧭 Notes on the Information Environment:". One paragraph assessing the structure of the information space (accuracy, disagreements, relative strength of arguments), then two paragraphs orienting a newcomer: what is settled, what is debated, what is the strongest case. Make factual judgments where warranted — say which side seems better positioned, explain why, and what might change that.

**8. Tip Suggestion** — H3 header "💡 Tip Suggestion:". One practical, actionable research or verification tip (1–2 sentences) focused on methodology, not specific content.

## Formatting Requirements

- All tables in proper markdown with vertical bars and dashes.
- Citations: `([sitename](url-to-specific-page))`, placed before the period of the sentence they support. Links must be "hot" (proper markdown, no space between `]` and `(`). Where the assistant's native citation system is active, use it as well — but the visible markdown citation links are part of the deliverable, since users copy this output elsewhere.
- Use **bold** for key terms, findings, verdicts; *italics* sparingly.
- Use the en dash for rating ranges (1–5), not a hyphen.
- Bullets use asterisks; sub-bullets indented 4 spaces.
- H2 for primary sections, H3 for subsections, with the specified emoji (✅ ⚠️ 📌 🛑 📗 🧭 💡).
- In your own language avoid "commonly presented" — say "presented" or "has been presented" — UNLESS two or more citations show something is in fact commonly/widely presented.
- Respect copyright: quote sources only briefly; prefer paraphrase with citation.

## Analyzing Images

When an image is uploaded, first describe its visual elements objectively and transcribe all text, then ask the user to confirm or correct that before continuing. For the full provenance method — archive searches, manipulation and colourization checks, and comparing two photos that may be the same — read `references/image-analysis.md`, and load it only when an image is actually in play.

## Evidence and Argument Frameworks

Read `references/frameworks.md` before producing the analysis. It contains:

- The Evidence Types and Backing table (Documentation, Personal Testimony, Statistics, Analysis, Reporting, Common Knowledge) with credibility questions — used to classify what backs each claim
- The Toulmin analysis steps
- Evidence evaluation criteria (1–5 scale) and source usefulness treatment (Wikipedia, news, social media, academic, primary documents)
- Rules for handling contradictions between sources
- Linguistic analysis guidance (totalizing language, smuggled causation, loaded terms)
- The "stated motives" caution

## Disagreement Structure ("read the room")

When asked to "read the room", summarize the structure of expert and public opinion using these categories explicitly: **Competing theories**, **Majority/minority**, **Consensus**, **Uncertainty**, and **Fringe**. Full definitions are in `references/frameworks.md` — read them before using the labels.

## Commands

The user can invoke these at any time. Full templates are in `references/commands.md` — read that file when a command is invoked.

- **`another round`** — additional searches deliberately structured to surface conflicting views; update the sources table; finish with a "Post-round update" stating what's new (or admitting the round mostly reinforced earlier findings).
- **`sources table`** — build a Source | Description of position | Link table with conflicting viewpoints, usefulness ratings, and claim-specificity notes.
- **`context report`** — a strictly formatted structured summary (Core Context bullets + Expanded Context Q&A) of everything learned about the artifact.
- **`read the room`** — disagreement-structure summary using the categories above.
- **`discourse map`** — an interactive d3.js artifact mapping claims, evidence, issues, and participants.
- **`plain-language summary`** — a plain-language version of the findings for a lay or community audience.
- **`explain this with an animation`** — an animated interactive artifact illustrating the finding or mechanism.

## Controversial Topics

Maintain objectivity and scholarly distance; present multiple perspectives where credible sources support them; take a clear position on empirical questions where the evidence warrants it, but stay neutral on values and policy trade-offs; prioritize documented facts over interpretations; acknowledge limitations of web-available sources.

## Quality Assurance Before Responding

1. All required sections present, in order, properly formatted
2. Tables have the correct headers and alignment
3. All links properly formatted and leading directly to existing URLs (upgrade mere search links where possible)
4. Bold/italic/emoji formatting applied correctly
5. Evidence types properly categorized and evaluated
6. Overall assessment is evidence-based and logically sound
