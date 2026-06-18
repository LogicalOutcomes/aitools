# LogicalOutcomes AI Tools — Skills

Practical AI "skills" for the non-profit and community sector, shared by
[LogicalOutcomes](https://logicaloutcomes.net), a Canadian non-profit.

We share most of our tools openly because the sector is stronger when good methods are passed
around. Take these, adapt them to your work, and improve them.

## What is a "skill"?

A skill is a plain-language instruction sheet for an AI assistant. Each one lives in its own
folder and is mostly just a written document — what the task is, how to do it well, and when to
use it — sometimes with a few example templates or helper files alongside.

You don't need to be technical to read one. Open the `SKILL.md` file in any folder here and
you'll find ordinary writing describing how an experienced person would approach the task. That
makes a skill useful in three ways: you can **use it** with an AI assistant, you can **read it**
to learn how we do the work, or you can **adapt it** into your own materials.

The skill format is **open and not tied to any one company's AI**. The format was introduced in Claude, but the same skills work with any up to date AI chat platform. Nothing here is locked to a single product. However, you may need to tweak the skills to fit  your own context and model; test them and see.

## What's in here

The skills cover the work we do with non-profits: planning program evaluations,
reviewing the research evidence behind a program, making sense of documents and interview notes,
working through a tough decision from several angles, and setting up a new project. They're
written for real non-profit conditions — tight budgets, grant deadlines, equity considerations,
and the duty to protect people's personal information.

The table below is generated automatically from each skill's own description, so it stays
accurate as skills change. The full, authoritative description of any skill is the `SKILL.md`
inside its folder.

<!-- SKILLS-INDEX:START -->
| Skill | What it does |
| --- | --- |
| [`convening-experts`](Skills/convening-experts/) | Convenes expert panels for problem-solving through multi-round collaborative discussion. |
| [`deep-background`](Skills/deep-background/) | Meticulous fact-checking, claim analysis, and contextualization using Mike Caulfield's Deep Background methodology. |
| [`document-analysis`](Skills/document-analysis/) | Analyze documents the user already has — evaluation reports, program documents, interview transcripts, research papers, strategic plans, data files. |
| [`evaluation-framework-builder`](Skills/evaluation-framework-builder/) | Drafts complete program evaluation plans using the LogicalOutcomes evaluation framework (Kerr & Llewelyn, 2024) — logic model, evaluation questions, indicators, interest groups analysis, project roles, schedule, and meeting agendas. |
| [`project-starter`](Skills/project-starter/) | Sets up new nonprofit projects using bundled handbook-style templates — drafts the project charter from a proposal, SOW, contract, email, or rough notes; assigns project roles; drafts role-and-terms emails for contractors and employees; and prepares client and internal kick-off meeting agendas. |
| [`social-services-review`](Skills/social-services-review/) | Literature reviews and evidence syntheses for non-profit, community, social, and health services. |
<!-- SKILLS-INDEX:END -->

## Skills we recommend but don't copy

Some good skills are looked after by other people. Rather than copy them here, where they would fall out of date, we keep a short, reviewed list of recommendations at
[`Skills/suggested-external-skills.md`](Skills/suggested-external-skills.md), with a link to the
original of each.

## How to use these skills

**The simplest way — just read it.** Open a skill's `SKILL.md` and use it as a checklist or
guide for the task yourself, or paste relevant parts into whatever AI assistant you already use,
along with your own request. This works with any assistant and needs no setup.

**With an AI assistant that supports skills.** Many assistants let you add a skill so it loads on
its own when your request matches. Copy the skill's folder from this repository (or download the
repository and use the folder you need) and add it through your assistant's skills or capabilities
settings. After that, you describe your task in plain language and the assistant follows the skill —
you don't have to mention it by name. The exact menu wording differs between tools, so check your
assistant's help if you're unsure.

**Adapt it for your organization.** These are starting points, not rules. Several skills contain
blanks to fill in (like `[ORGANIZATION]` or a sample fee) and templates you should match to your
own policies before relying on them — especially anything about contracts, pay, or handling
personal data. Edit freely; treat your own organization's policies as the final word.

## Please check the results

A skill helps an AI assistant do good work, but the assistant can still get things wrong. Before
you rely on anything it produces, check the facts, make sure any figures and quotes are real, and
confirm that sources actually exist. When you're working with real information about clients or
research participants, remove personal details first — never paste people's identifiable
information into a general-purpose AI assistant.

## Crediting and reuse

Everything here is released under the **MIT licence** (see the [`LICENSE`](LICENSE) file) — you're
free to use, change, and share it, including commercially, as long as you keep the copyright and
licence notice. Each skill also carries its own `license:` line in its `SKILL.md`, so the terms
travel with the skill no matter which tool you use it in.

Some of these build on others' work, credited in the skill's front matter and here:

- **`convening-experts`** is derived from Oskar Austegard's
  [convening-experts skill](https://github.com/oaustegard/claude-skills/blob/main/convening-experts/SKILL.md)
  (MIT).
- **`social-services-review`** was partly inspired by K-Dense AI's
  [literature-review skill](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/literature-review)
  (MIT).
- **`deep-background`** builds on Mike Caulfield's *SIFT* fact-checking method
  ([source](https://checkplease.neocities.org/sift-toolbox/index.html)).
- **`evaluation-framework-builder`** draws on the *LogicalOutcomes Evaluation Planning Handbook*
  (Kerr & Llewelyn, 2024), which is itself shared under CC BY 4.0
  ([read it on SSRN](https://ssrn.com/abstract=4815131)).
