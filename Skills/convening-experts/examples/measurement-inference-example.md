# Example: Is the Program Effect Real? (Multi-Round)

**User Query:** "We screened clients for distress, enrolled the highest-scoring 80 into a new 6-week support program, and re-measured at the end. Mean distress fell from 72 to 58 on our scale - a 14-point drop, paired t-test p<0.001. The funder wants to scale it. Can we say the program caused this?"

## Expert Panel: Causal Inference on a Pre/Post Result

**Panel Members:**

- Data Scientist / Statistician
- Program Evaluator
- Theory of Change Specialist
- Finance Analyst

---

## Round 1: Initial Analysis

### Data Scientist / Statistician

The p-value is answering a question nobody should be asking here. p<0.001 on a paired t-test tells you the pre-post difference is unlikely to be *exactly zero*; it says nothing about whether the *program* produced it. With this design, three non-program explanations are not edge cases - they're the expected default.

**1. Regression to the mean (RTM) - this is the dominant threat and it's structural, not bad luck.** You selected the *highest-scoring* 80. Any measurement is true score plus error. Select on extreme observed scores and you have preferentially selected people whose error term was large and positive that day. On re-measurement the error component reverts toward zero *with no intervention at all*, dragging the observed mean down. The expected size of the RTM drop is a function of the test-retest reliability r: roughly, expected reversion ≈ (1 − r) × (selected mean − population mean). If your scale's r is ~0.7 and the screened group sat ~20 points above the population mean, you'd expect ~6 points of drop from RTM alone - so a meaningful fraction of your 14 could be artifact before the program does anything.

**2. No counterfactual.** You have no control group, so "what would have happened anyway" - natural recovery, crisis passing, seasonality - is entirely unmeasured and currently attributed to the program by default.

**3. The estimate is also imprecise in a way the p-value hides.** n=80 selected from a screen gives you a single arm; the confidence interval on the *causal* effect (which you can't compute from these data) would be far wider than the CI on the raw difference. Don't let p<0.001 launder a fragile design into a precise claim.

**What I'd want:** the scale's test-retest reliability (to bound the RTM component), and ideally a comparison group.

---

### Program Evaluator

I agree the causal claim is unsupported as stated, and I want to add the evaluation-design version of the Statistician's point, because it has a name and a fix.

**Selection on a transient spike is Ashenfelter's Dip.** In program evaluation this is classic: people enter a program precisely when they're at a low point (that's *why* they were screened in), and they would have partially recovered regardless. Pre-post comparison then systematically overstates the effect. It's the same phenomenon as RTM viewed through the enrollment process rather than the measurement error.

**The design fix is a comparison group, and you may already have one.** You screened more than 80 people to select 80. The clients who scored *just below* the enrollment cutoff are a natural comparison - similar distress, similar context, didn't get the program. That's a regression-discontinuity setup, and it's far stronger than pre-post. Alternatively, if the program rolls out in waves, a difference-in-differences design using the not-yet-enrolled wave as control.

**One caution on my own suggestion:** difference-in-differences only identifies the effect if the two groups would have followed *parallel trends* absent the program. With an Ashenfelter Dip, the enrolled group is on a steeper recovery trajectory by construction - that *violates* parallel trends and would bias DiD too, unless we use the pre-period data to model and adjust for the differential trend. So I'm not offering DiD as a free pass; it has its own assumption that this selection mechanism actively threatens.

---

### Theory of Change Specialist

Step back from the estimator for a moment, because even a clean causal number would leave the funder's real question unanswered.

**A 14-point drop on the distress scale is an *outcome* measurement, but the theory of change is what tells you whether it's the *right* outcome and whether it will persist.** Two questions the statistics can't reach:

1. **Mechanism.** What in the 6-week program is *supposed* to reduce distress, and is there evidence that mechanism fired? If the logic model says "peer connection reduces isolation reduces distress," did isolation actually change? An outcome that moves without its hypothesized mediator moving is a warning sign that you're measuring something else (like RTM).
2. **Endpoint timing.** You measured at week 6 - program end. If distress drops during a supportive program and rebounds after, you've measured the *presence of support*, not a durable change. The theory of change should specify a maintenance window and a follow-up measurement; without it, "it worked" means "it worked while we were doing it."

I'm not contradicting the Statistician - I'm saying that fixing the design to get a clean effect, but measuring the wrong endpoint at the wrong time, gives you a rigorous answer to a question the funder didn't ask.

---

### Finance Analyst

The decision in front of us is a scaling decision, so frame the statistics as a question of *risk on capital*, not academic purity.

Scaling commits recurring cost - staff, space, per-client delivery - against an effect estimate that the Statistician and Evaluator say is materially inflated by RTM and selection. If half the observed 14-point drop is artifact, the cost-per-real-unit-of-improvement is double what the headline implies, and a program that looks cost-effective at face value may not clear the bar against alternatives.

**But I'll push back on "just run an RCT before scaling," before someone proposes it.** A full trial has real cost and delay, and the program may be denying a plausibly-helpful service to a control group in the meantime. The proportionate move is the cheapest design that *materially* reduces the inference risk: the Evaluator's just-below-cutoff comparison group uses data we're *already* collecting at near-zero marginal cost. I'd fund that before I'd fund either a blind scale-up or an expensive standalone trial. Spend the evaluation dollar where it buys the most reduction in decision risk.

---

## Round 2: Cross-Examination

### Program Evaluator responds to the Data Scientist / Statistician

The Statistician's RTM quantification is the number that should anchor this whole discussion, and I want to operationalize it. If we pull the scale's test-retest reliability - even from the instrument's published validation, if we don't have our own - we can put an *expected RTM drop* on the board before arguing about anything else. If that expected artifact is ~6 of the 14 points, the conversation changes from "did it work" to "is the residual ~8 points real, and is *that* worth scaling." That reframes the funder conversation honestly without pretending the effect is zero.

### Data Scientist / Statistician responds to the Program Evaluator

The regression-discontinuity idea is the strongest thing said so far, and it's better than I initially credited - because the enrollment cutoff is a *known, sharp* threshold, which is exactly the condition RD needs. Clients just above and just below a distress cutoff are plausibly exchangeable, so comparing their week-6 scores estimates a local causal effect with far weaker assumptions than pre-post.

I'll sharpen the Evaluator's own caution back at them, though: RD identifies the effect only *at the cutoff* - it tells us whether the program helps people near the enrollment threshold, not necessarily the most severe cases deep above it. If the funder wants to scale to the whole screened population, the RD estimate is a lower-anxiety but *local* answer. Worth being explicit that we'd be generalizing from the margin.

### Theory of Change Specialist responds to the Finance Analyst

The Finance framing - buy the cheapest design that most reduces decision risk - is right, and it actually *strengthens* my endpoint point rather than competing with it. The single highest-value, lowest-cost addition is a follow-up measurement at, say, 12 weeks post-program. It costs one more data-collection round on people we already have contact with, and it directly tests the artifact-vs-durable question: RTM and a support-presence effect both predict *rebound* after the program ends, whereas a real durable change predicts the gain holds. So one cheap follow-up wave discriminates between the very explanations the Statistician and I are each worried about. That's a high information-per-dollar measurement, by the Finance Analyst's own criterion.

---

## Round 3: Convergence

### Data Scientist / Statistician

Converged. The pre-post result cannot support a causal claim; RTM and selection are expected to inflate it. Two cheap design upgrades fix most of this: a regression-discontinuity comparison using the just-below-cutoff group (data already collected), and a post-program follow-up wave to test durability.

### Program Evaluator

Agreed, and I'll add the honest interim statement for the funder: quantify the expected RTM component from the scale's reliability, report the *residual* as the candidate effect with appropriate uncertainty, and label the current number as not-yet-causal rather than either "proven" or "nothing."

### Theory of Change Specialist

Agreed, with the maintenance-window follow-up as a non-negotiable, because it simultaneously tests durability and discriminates artifact from effect. And confirm at least one mediator moved, or we don't know what we changed.

### Finance Analyst

Agreed. Fund the RD analysis and the follow-up wave - both near-zero marginal cost - before any scaling commitment. Hold the scale-up decision until the residual effect and its durability are estimated. This is cheaper than scaling on an inflated number and cheaper than a standalone RCT.

---

## Final Synthesis

**Recommendation:** Do **not** tell the funder the program "caused" the 14-point drop, and do **not** scale on the current evidence. The pre-post design cannot separate program effect from regression to the mean and selection (Ashenfelter's Dip), both of which are expected here by construction and likely account for a substantial share of the observed change.

**Before any scaling decision, run two low-cost design upgrades using data largely already in hand:**

1. **Regression-discontinuity** comparison using clients who scored just below the enrollment cutoff as controls - a far stronger causal design than pre-post, valid at the cutoff. (Generalizes to near-threshold clients, not automatically to the most severe.)
2. **A post-program follow-up wave** (e.g., 12 weeks out) to test durability - which also discriminates a real, durable effect (gain holds) from RTM / support-presence artifact (gain rebounds).
3. Quantify the **expected RTM component** from the scale's test-retest reliability, and report the **residual** as the candidate effect with honest uncertainty. Confirm at least one **hypothesized mediator** moved.

**Decision Framework (RAPID):**

- **Recommend:** RD analysis + follow-up wave + RTM quantification before scaling; honest interim reporting to the funder
- **Agree:** Executive Director, funder (on the revised evidence bar)
- **Perform:** Data Scientist (RD model, RTM estimate), Program Evaluator (follow-up wave, reporting), Theory of Change Specialist (mediator check)
- **Input:** Finance Analyst (cost-per-real-effect once the residual is estimated)
- **Decide:** Executive Director, in conversation with the funder

**Live disagreement preserved (a real, unresolved technical point):** The panel did not fully resolve *generalizability*. The regression-discontinuity estimate is rigorous but *local to the cutoff*; the funder wants to scale across the whole screened distress range. Whether a margin-estimated effect justifies scaling to the most severe clients is a genuine inference gap that RD alone cannot close - flagged explicitly rather than smoothed, because closing it would require either a stronger design or an accepted assumption the panel won't make silently.

**Key insight:** The headline statistic (p<0.001) was real but answered the wrong question - statistical significance of a raw difference, not causal attribution. Every expert converged on the same move: the cheapest credible *design* (RD + a follow-up wave on data already being collected) buys far more decision-relevant certainty than either the existing significance test or an expensive standalone trial. Rigor here was about the design, not the p-value.
