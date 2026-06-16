# Qualitative Analysis: Methodology and Boundaries

Read this before any qualitative work — first-pass coding, theme identification, transcript
organization, evidence assembly. The can/can't boundaries here are the heart of the skill:
qualitative analysis is interpretive work requiring understanding of context, culture, power
dynamics, and lived experience that is not fully present in transcript text. The model
supports the analyst; it does not replace the analyst's judgement.

Note: for systematic coding of a full transcript set against a codebook, the qual-analysis
coding tool or repeatable pipeline is more reliable than conversational analysis — see SKILL.md.

## What the model can do

**First-pass coding support**: Read transcripts and suggest potential themes or codes. This
is equivalent to a research assistant's first pass — useful for saving time, but every
suggestion must be reviewed and validated by the analyst.

**Consistency support**: Across multiple transcripts, flag where the same concept appears in
different language. This helps ensure coding consistency across a data set.

**Organization and structuring**: Take unstructured notes or transcripts and organize content
by theme, question, or participant group. Useful for getting an overview before deep
analysis.

**Counter-evidence surfacing**: Once a theme is identified, search for disconfirming evidence
or exceptions. Humans tend to underweight disconfirming evidence — the model can
systematically look for it.

**Evidence assembly**: Gather all quotes and references related to a specific theme or code
across multiple documents. Saves the manual work of combing through transcripts.

**Question generation**: Based on the data, suggest questions that might warrant further
investigation, areas where data is thin, or topics where participants disagree.

**Verified counting**: When theme or code frequencies matter, compute them programmatically
from the source files (see "Counting" below) rather than estimating.

## Boundaries — and what to do instead

Be transparent about these limitations. Each comes with positive guidance.

**Interpretive depth is the analyst's job.** Report what participants said and how they said
it. When patterns suggest a possible interpretation, present it as a question: "Several
participants described feeling unheard during consultations — does this connect to the power
dynamics you observed in the sessions?" Let the analyst supply the interpretive layer.

**Focus on what is on the page.** Silences, hesitations, and avoidance are often the most
important data in qualitative research, but they are not visible in transcript text. Focus on
what participants explicitly stated. If a topic was raised in interview questions but not
addressed in participants' responses, flag this as a potential area of interest — but note
that you are observing an absence in the text, not interpreting the reason for it.

**Support interpretive frameworks, but don't claim to perform them.** Grounded theory,
phenomenological analysis, and narrative analysis require human judgement. When a user
requests these, organize the data in ways that support the approach (e.g., open coding
suggestions for grounded theory, chronological narrative structures for narrative analysis)
and be clear: "I've organized the data to support your [approach] — the interpretive work is
yours."

**Name what you can't see.** The model may miss leading questions, social desirability
effects, or meaning that depends on cultural context, community norms, or local knowledge not
present in the text. Every qualitative output includes a brief limitations note: "This
analysis is based on the text as written. It does not account for interviewer effects,
non-verbal communication, or contextual factors not captured in the transcripts."

## Counting theme frequency

When describing how often themes appear, two valid modes:

1. **Verified counts** — when counts matter, compute them with code: search the transcript
   files for the coded segments, count programmatically, and report the verified figure. A
   count is also acceptable when the corpus is small enough to enumerate directly and
   checkably (e.g., 3 short excerpts visibly in context).
2. **Descriptive frequency language** — otherwise: "a recurring theme across most
   interviews," "raised by a few participants," "one participant offered a distinct
   perspective."

Never report a specific count ("7 out of 12") produced by impression from reading — counts
recalled from long-context reading are systematically unreliable, which is why the
predecessor tool banned them outright. Verified-by-code or descriptive: nothing in between.

## How to approach qualitative work

When a user asks for qualitative analysis, ask which approach they prefer — thematic
analysis, content analysis, framework analysis, or a general first-pass review. If they are
unsure, default to thematic analysis (identifying patterns across the data).

1. **Start with structure**: Offer to organize the data (by question, by participant, by
   topic) before attempting thematic analysis
2. **Suggest, don't assert**: Present themes as "potential themes for your review", not as
   findings
3. **Always show the evidence**: Every theme must be grounded in specific quotes with
   locations
4. **Flag uncertainty**: When a passage is ambiguous, present multiple possible
   interpretations
5. **Invite the analyst's judgement**: "You know the context better than I do — does this
   grouping reflect what you heard in the interviews?"
6. **Separate description from interpretation**: Describe what participants said before
   offering any interpretation of what it might mean

**Transparency note for all qualitative outputs:** Suggested codes and themes reflect
patterns in the text as the model processes it. They may systematically favour clearly stated
themes over subtle or implicit ones. The analyst should review them against their own reading
of the data.
