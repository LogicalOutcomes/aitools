# Command Templates

Read this file when the user invokes a command. Each command can be invoked at any point in a session.

Adapted from Mike Caulfield's Deep Background / SIFT Toolbox prompt (openly published for reuse): <https://checkplease.neocities.org/sift-toolbox/index.html>

The first five commands below (`another round`, `sources table`, `context report`, `read the room`, `discourse map`) are canonical to Caulfield's prompt. The last two (`plain-language summary`, `explain this with an animation`) are extensions listed in SKILL.md but not present in Caulfield's original; their templates here are reasonable defaults, not canonical text.

---

## `another round`

Run additional searches deliberately structured to surface conflicting views, then "fact-check the fact-check" — push on the weakest points of the initial assessment to find errors and blind spots.

It is fine for individual sources to be biased as long as the *set* of searches surfaces a range of viewpoints (e.g. pair an "X is true" search with an "X is false" search). If possible, find:

* one source that conflicts with the majority view,
* one source that supports the majority view,
* one source with a completely different answer.

Update the sources table with what you find. A pattern where low-quality sources say one thing and high-quality sources say another is worth noting explicitly.

Finish with a **Post-round update**: summarize what new information came to light and whether (and how) it changes the view of the issue. If the round discovered nothing new, say so plainly — admit it mostly reinforced the previous searches.

---

## `sources table`

Build a table of sources that hold conflicting positions on the chosen question, written with a fact-checking ethic.

1. Find strong links with conflicting information on the question or topic.
2. Present them in a markdown table: `| Source | Description of position on issue | Link |`.
3. Format links as hot markdown links.
4. Search for additional conflicting links and update the table.
5. Add columns for an **Initial Usefulness Rating** (1–5) and for the **specificity of claims** (does the source give a date? a place? a reference? testimony?).
6. On `another round`, apply the conflicting-source search structure above and update the table; note any quality-vs-position pattern.

---

## `context report`

Produce a structured summary of everything learned about the subject or artifact, using EXACTLY this format and headers — add no extra sections.

```text
## Core Context
- 4–6 bullets capturing the most essential information (1–3 sentences each)
- Focus on authenticity, origin, and common misconceptions
- Include source citations in markdown link format: ([Source Name](URL))
- First bullet: how the artifact is commonly presented or misrepresented
- Final bullets: establish the factual reality

## Expanded Context

**What does this appear to be / how is it described online?**
1–2 paragraphs on how the artifact is presented online — how it is framed, described, contextualised, with citations. Use "commonly presented" only if you have seen it in multiple places; otherwise "has been presented".

**What does this mean to its primary audience/audiences online?**
1 paragraph on how different audiences interpret it, what narratives it reinforces, what responses it generates.

**What is the actual story or deeper background?**
1–2 paragraphs on the factual origin, context, and history, directly addressing misconceptions identified earlier. Multiple citations.

**What does the actual picture/graphic look like?** (for images)
1 paragraph describing the authentic version compared with the misrepresented one, with specific visual details and citations.

**What is (some of) the larger discourse context?**
1–3 unnumbered bullets on broader media/communication/information patterns this example illustrates.

**What is (some of) the larger topical context?**
5–10 keywords or short phrases, comma-separated, for categorizing the artifact.
```

---

## `read the room`

Summarize the structure of expert and public opinion using the five categories defined in `references/frameworks.md` — **Competing theories**, **Majority/minority**, **Consensus**, **Uncertainty**, **Fringe** — naming each explicitly. Read those definitions before applying the labels; the minority-vs-fringe distinction in particular must be applied correctly.

---

## `discourse map`

Build an interactive d3.js artifact mapping the discourse space.

* Map the claims, the evidence supporting them, the issues/concerns those claims relate to, and the discourse participants involved.
* Place the core claim at the centre; use JavaScript logic to cluster nodes within the available viewport.
* On hover, do not move the node — show a popup describing it in detail. For evidence nodes, describe the type(s) of backing and what the evidence shows; for claim nodes, give more detail.

---

## `plain-language summary`

*(Extension — not in Caulfield's original prompt.)*

Produce a plain-language version of the findings for a lay or community audience: short sentences, no jargon, define any unavoidable technical terms inline, and keep the structure simple (what the claim was, what's actually true, why it matters). Preserve the substance and the verdict; drop the tables and formal apparatus.

---

## `explain this with an animation`

*(Extension — not in Caulfield's original prompt.)*

Build a self-contained interactive artifact that animates the key finding or mechanism (e.g. a timeline, a process, or how a misconception arose versus what actually happened). Keep it accurate to the verified facts, label sources where a claim is shown, and favour a single clear mechanism over visual flourish.
