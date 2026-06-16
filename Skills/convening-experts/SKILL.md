---
name: convening-experts
description: Convenes expert panels for problem-solving through multi-round collaborative discussion. Use when the user mentions panel, experts, multiple perspectives, or wants a decision worked through several lenses — including strategic decisions, process improvement, root cause analysis, technical and security architecture, program design and evaluation, theory of change, equity and community-engagement questions, and named methods (MECE, DMAIC, RAPID, Six Sigma, RE-AIM).
license: MIT
metadata:
  version: 2.0.0
  author: LogicalOutcomes
  source: https://github.com/LogicalOutcomes/aitools
  based_on: https://github.com/oaustegard/claude-skills/blob/main/convening-experts/SKILL.md
---

# Convening Experts

Convene domain experts and methodological specialists to solve problems through multi-round collaborative discussion. Experts build on each other's insights, **challenge each other's framing**, and converge on a synthesis that preserves the disagreements worth keeping. The value is in the discussion, not in a list of parallel opinions — a flattened panel where each expert simply states a view in isolation has failed, even if every individual view is correct.

## Panel Format

### Single-Round Consultation

For simpler problems requiring multiple viewpoints:

1. **Assemble panel** (3-5 experts based on problem domain, seated for productive tension — see below)
2. **Each expert provides independent perspective** (parallel, not sequential)
3. **Synthesize recommendations** with attribution, surfacing where the experts disagreed

### Multi-Round Discussion

For complex problems requiring collaborative reasoning:

1. **Round 1**: Each expert analyzes the problem independently
2. **Round 2 (Cross-Examination)**: Experts respond to *specific* points from each other — building on, integrating, or directly challenging. This is the clash round; do not smooth it.
3. **Round 3** (if needed): Converge — resolve what can be resolved, name what cannot
4. **Final synthesis**: Integrated recommendation with a decision framework, explicitly flagging consensus vs. live disagreement

## Expert Roles

**Available expertise spans:**

- Sector & professional domain experts — non-profit operations, community & equity practice, health & science, and technical & professional roles (software, security, DevOps, data, supply chain, risk)
- Methodological & framework specialists — strategic, process improvement, innovation, systems analysis, root cause, and evaluation & behaviour

See [references/domain-experts.md](references/domain-experts.md) and [references/methodological-frameworks.md](references/methodological-frameworks.md) for the complete role catalogue.

The assistant loads the relevant reference(s) based on the problem domain. The catalogue is a starting point, not a boundary — recruit any specialist the problem genuinely calls for. A panel should reach **across** sections (e.g., a technical decision in a non-profit still needs the legal and equity lenses), not stay inside one.

## Seating for Productive Tension

A good panel is *cast*, not just assembled. After identifying the experts a problem obviously needs, deliberately seat at least one expert whose frame will challenge the others — otherwise the panel converges too early on the framing of whoever spoke first.

**Natural tension pairs** (seat both sides when the problem touches them):

- **Program Evaluator / Finance Analyst ↔ Lived-Experience Advocate** — measurable outcomes and cost-efficiency vs. how the intervention actually lands on the people it serves
- **McKinsey / BCG Consultant ↔ Anti-Oppression Practitioner** — structured prioritization vs. *who defined the problem this way and who benefits from that framing*
- **Lean Practitioner / Six Sigma Black Belt ↔ Community Engagement Specialist** — efficiency and standardization vs. non-extractive, community-led process
- **Security Architect ↔ Accessibility Specialist** — locking the system down vs. keeping it usable and inclusive (plain language, low-barrier access)
- **Security Architect / Software Engineer ↔ IT & Security Specialist (lean-team reality)** — the ideal architecture vs. what a small, stretched team can actually run and patch safely
- **Communications Strategist ↔ Lived-Experience Advocate / Anti-Oppression Practitioner** — a campaign that lands publicly vs. one that doesn't use service users as sympathetic props
- **Theory of Change Specialist ↔ Frontline Social Worker** — the clean outcome chain vs. the messy reality of the caseload

The clash is a feature. The synthesis is stronger for having survived it.

## Panel Convening Logic

The assistant selects 3-5 experts based on problem characteristics, then seats one for tension.

**Problem type → core experts + tension seat**

- **Technical / architecture / security decision** → Domain technical expert (Software Engineer, Security Architect, DevOps) + Finance Analyst + **IT & Security Specialist** (lean-reality check) + legal/privacy lens (Charity Lawyer) where personal data is involved
- **Strategic decision** → McKinsey Consultant + relevant domain experts + SWOT Analyst + a standpoint seat (Lived-Experience Advocate or Anti-Oppression Practitioner) where the decision affects service users
- **Process improvement** → Six Sigma Black Belt + Lean Practitioner + domain operations expert + **Community Engagement Specialist** where the "process" touches participants
- **Program / service design** → Theory of Change Specialist + Program Evaluator + Frontline Social Worker + **Lived-Experience Advocate** (always, for anything client-facing) + Behavioural Economist where uptake matters
- **Evaluation / measurement** → Program Evaluator + Data Scientist/Statistician + Theory of Change Specialist + equity-disaggregation lens
- **Root cause analysis** → Domain expert + Five Whys Facilitator + Systems Thinker
- **Funding / revenue / campaign** → Philanthropy Advisor or Grant Strategist + Communications Strategist + McKinsey Consultant + an equity/standpoint seat where service users would be featured
- **Cross-functional problem** → Relevant domain experts + Bain Consultant (RAPID) + Systems Thinker

## Response Format

Refer to experts by **role title only** — never invent personal names or personas. Keep the exchange alive through the *specificity* of engagement (an expert naming the exact point they are building on or challenging), not through invented characters.

### Single-Round Format

```text
## Expert Panel: [Topic]

**Panel Members:**
- [Expert 1 Role]
- [Expert 2 Role]
- [Expert 3 Role]

---

### [Expert 1 Role]
[Independent analysis and recommendations]

### [Expert 2 Role]
[Independent analysis and recommendations]

### [Expert 3 Role]
[Independent analysis and recommendations]

---

## Synthesis
[Integrated recommendation with decision framework. State where the panel agreed
and where it did not — do not manufacture consensus.]
```

### Multi-Round Format

```text
## Expert Panel: [Topic]

**Panel Members:**
- [Expert 1 Role]
- [Expert 2 Role]
- [Expert 3 Role]

---

## Round 1: Initial Analysis

### [Expert 1 Role]
[Initial perspective]

### [Expert 2 Role]
[Initial perspective]

### [Expert 3 Role]
[Initial perspective]

---

## Round 2: Cross-Examination

### [Expert 1 Role] responds to [Expert 2 Role]
[Builds on or directly challenges a specific named point]

### [Expert 2 Role] responds to [Expert 3 Role]
[Integration or disagreement]

### [Expert 3 Role] responds to [Expert 1 Role]
[Synthesis attempt — or a sharpened disagreement]

---

## Round 3: Convergence (if needed)

[Experts resolve what they can and name what they can't]

---

## Final Synthesis
[Integrated recommendation, highlighting consensus AND the disagreements that
remain live and why they matter to the decision]
```

## Expert Behaviour Guidelines

**Domain Experts:**

- Apply real-world operating context (lean budgets, regulatory constraints, the actual caseload)
- Use domain-appropriate terminology without over-explanation
- Prioritize practical implementation over theoretical perfection
- Flag domain-specific risks and constraints

**Framework Experts:**

- Apply frameworks systematically (show the structure)
- Adapt frameworks to problem context (not rigid application)
- Explain "why this framework" for this problem
- Integrate domain context when applying generic frameworks

**Equity & Standpoint Experts (Anti-Oppression Practitioner, Lived-Experience Advocate, Accessibility Specialist, Africentric Practice Specialist, Indigenous Engagement Advisor):**

- Challenge *who defined the problem* and *who benefits* from the proposed framing, not only the proposed solution
- Test every recommendation against how it lands for the people it claims to serve
- Name extraction, tokenism, and proxy speech when they appear in the other experts' proposals
- These experts are expected to disagree with efficiency- and compliance-framed recommendations; that disagreement is the point, not a failure to align

**Cross-Panel Interaction:**

- Reference other experts' points specifically ("Building on the Systems Thinker's observation about the reinforcing loop...")
- Challenge constructively ("The Program Evaluator's metric misses what I see daily, because...")
- Synthesize across disciplines ("This connects the Security Architect's data-residency constraint with the Charity Lawyer's PHIPA obligation...")
- Flag tensions between perspectives explicitly

**Disagreement Handling:**

- Make disagreements productive (what assumptions differ?)
- Present multiple valid approaches when consensus isn't required
- Identify the decision criteria that would resolve a disagreement
- A disagreement that changes the final recommendation is a sign the panel worked — preserve it in the synthesis
- Escalate to the user when expert consensus genuinely can't be reached

## Decision Frameworks

When the panel must recommend action:

**RAPID (Bain)**

- **Recommend**: Panel's recommendation with rationale
- **Agree**: Which stakeholders must agree
- **Perform**: Who implements
- **Input**: Who provides input
- **Decide**: Who makes the final decision

**Weighted Decision Matrix**

- Criteria (importance weighted)
- Options scored on each criterion
- Total score with sensitivity analysis

**Risk-Benefit Analysis**

- Upside potential (probability × impact)
- Downside risk (probability × impact)
- Mitigation strategies
- Decision under uncertainty

## Organizational Context

Apply the operating context of a mission-driven / non-profit organization automatically, and adapt it to the specific problem rather than assuming every question is a frontline-services question. This organization spans **programs and services, community and equity practice, and technical and operational functions** — a question may sit in any of these, or across them.

**Common constraints:**

- Lean budgets and stretched, multi-hatted teams; capacity is often the binding constraint, not ideas
- Canadian regulatory and governance context where relevant (CRA charitable compliance, ONCA/CNCA, privacy under PIPEDA/PHIPA, accessibility under AODA)
- Bilingual (EN/FR) and plain-language obligations for public-facing work
- Donor and client data protection; data residency and consent

**Cultural factors:**

- Equity and community trust are first-order considerations, not add-ons
- Decisions are judged by how they land on the people served, not only by efficiency or cost
- Evidence and lived experience are both legitimate forms of knowledge, and they sometimes conflict

Do **not** flatten "non-profit" into "social services only." A non-profit also builds software, defends a threat model, runs a campaign, models a budget, and manages a supply chain — recruit accordingly.

## Evidentiary Standard

The panel exists to push past what the user could get from one capable hire — so the discussion must be *more* rigorous than a generalist's, not a confident-sounding average of one. This is the difference between a useful panel and a flattered one.

- **Claims are specific and, where possible, quantified.** "Reminders reduce no-shows" is weak; "an SMS reminder cut no-shows from 38% to 24% in a demographically comparable RCT" is the standard. Prefer mechanisms, effect sizes, named methods, and concrete thresholds over adjectives.
- **State evidence quality, don't hide it.** Distinguish RCT/meta-analytic evidence from single-site observational results from survey/advocacy figures from expert judgment. An expert who cites a soft number *and flags it as soft* is more credible than one who launders it.
- **In soft-evidence domains** (most social-program questions), rigor means anchoring to the best evidence that exists, forcing the disagreement onto *empirical* questions (what would falsify this? what does the data actually show?) rather than competing values, and being explicit about what is genuinely a value choice.
- **In hard domains** (security, statistics, software, finance, law), the bar is technical correctness an actual domain expert would not catch out. Get the mechanism, the legal provision, the statistical assumption exactly right. A plausible-but-wrong claim (e.g., "PHIPA bars cross-border storage" — it doesn't; it's an accountability regime) is worse than no claim.
- **Avoid the predictable.** If an expert's contribution is what a reader could already guess that role would say, it adds nothing. The value is in the non-obvious — the counterintuitive-but-correct point, the concession against interest, the disagreement that *changes* the recommendation. When grounding a claim in current facts, figures, or law, verify rather than reciting from memory.

The worked panels in `examples/` are the standard to match. Each anchors its claims to the
best available evidence, states evidence quality honestly (RCT vs. single-site vs. survey),
forces the disagreement onto *empirical* questions rather than competing values, and ends
with at least one disagreement preserved rather than smoothed.

### Example 1: Program / Service Design (Multi-Round) — `services-equity-example.md`

```text
User: Our intake no-show rate is ~35%. Staff proposed an SMS reminder plus a
rule that clients must confirm 24h ahead or the slot is released.

The assistant convenes:
- Program Evaluator (RE-AIM; the denominator-artifact problem)
- Behavioural Economist (loss-framed information vs. loss-framed access penalty)
- Frontline Social Worker (operational reality, non-attendance predictors)
- Lived-Experience Advocate (tension seat; concedes the penalty lowers the
  recorded rate, then attacks what "worked" actually counted)

Format: Multi-round. Soft-evidence domain — rigor comes from anchoring to real
effect sizes and being explicit about evidence quality.
```

### Example 2: Technical / Security Decision (Single-Round) — `platform-security-example.md`

```text
User: We hold donor and client data. Managed vendor CRM, or self-host an
open-source stack, with one IT person and two volunteers?

The assistant convenes:
- Security Architect (threat model; control you can't exercise is liability)
- IT & Security Specialist (tension seat — lean-team patch/restore capacity)
- DevOps Engineer (what "self-host responsibly" actually costs to operate)
- Charity Lawyer (PHIPA accountability model — corrects the residency myth)
- Finance Analyst (true TCO, breach tail)

Format: Single-round → RAPID framework synthesis
```

### Example 3: Causal Inference / Measurement (Multi-Round) — `measurement-inference-example.md`

```text
User: Distress fell 72→58 pre/post in our new program, paired t-test p<0.001.
Can we tell the funder the program caused it and scale?

The assistant convenes:
- Data Scientist / Statistician (regression to the mean, no counterfactual)
- Program Evaluator (Ashenfelter's Dip; regression-discontinuity fix)
- Theory of Change Specialist (mechanism + endpoint-timing/durability)
- Finance Analyst (cheapest design that most reduces decision risk)

Format: Multi-round (the causal claim must be challenged, then repaired)
```

See the `examples/` directory for the full worked panels.

## Constraints

**Never:**

- Use fictional or personal names for experts (use role titles only: "Software Engineer", not "Dr. John Smith, Software Engineer")
- Invent organization-specific facts beyond general domain knowledge
- Apply frameworks rigidly without problem context
- Create artificial consensus when legitimate disagreements exist — a synthesis that erases a real, recommendation-changing disagreement has flattened the panel
- Reduce a multi-expert panel to a list of parallel monologues with no cross-reference
- Include experts who add no value (quality over quantity)
- Make experts repeat each other (each should contribute uniquely)

**Always:**

- Select experts genuinely relevant to the problem, and seat at least one for productive tension
- Reach across roster sections when the problem does (technical + legal + equity, etc.)
- Make cross-expert references specific and substantive — quote the actual point being engaged
- Show framework structure when applying methodological methods
- Provide decision-ready synthesis (not "here are perspectives, you decide")
- Preserve and explain disagreements that remain live after the discussion
- Acknowledge uncertainty explicitly when present

## Activation Decision Tree

```text
Is the problem complex with multiple valid approaches?
├─ Yes → Expert panel
│   ├─ Spans multiple domains or needs a view challenged? → Multi-round discussion
│   └─ Needs diverse but independent perspectives? → Single-round consultation
└─ No → Direct answer (don't force panel format)

Does the decision affect the people the organization serves?
├─ Yes → Seat a standpoint/equity expert (Lived-Experience Advocate, Anti-Oppression
│        Practitioner, Accessibility Specialist) as a tension seat
└─ No → Domain + framework experts as appropriate

Requires a systematic framework?
├─ Yes → Include the matching framework expert and show its structure
└─ No → Domain experts only
```

## Quality Indicators

**Good panel:**

- Each expert contributes a unique insight
- Cross-references are specific and substantive (they name the point being engaged)
- At least one genuine disagreement surfaces, and it is engaged rather than smoothed
- Framework application shows structure and reasoning
- The synthesis is decision-ready and honest about what remained contested
- Where the decision touches service users, their standpoint visibly shaped the outcome

**Poor panel (flattened):**

- Experts state views in isolation and never engage each other
- Generic advice not grounded in a framework or domain
- No synthesis or integration across perspectives
- Consensus forced despite legitimate disagreement
- The equity/standpoint seat is present but ignored in the synthesis
- Panel format used when a direct answer would have served better
