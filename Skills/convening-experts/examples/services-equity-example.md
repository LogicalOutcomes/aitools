# Example: Shelter Intake No-Show Rate (Multi-Round)

**User Query:** "Our intake no-show rate is ~35%. Staff proposed an automated SMS reminder plus a rule that clients must confirm 24h ahead or the slot is released. Should we roll it out?"

> **Note on this example.** This is a soft-evidence domain — there is no equivalent of a controlled mechanism with a single discriminating test. The discipline that makes the panel useful is therefore *anchoring every claim to the best available empirical evidence and being explicit about its quality*, and forcing the disagreement onto questions that are actually empirical rather than onto competing values. Figures below are real and sourced; the panel treats survey/advocacy-sourced numbers more skeptically than RCTs, and says so.

## Expert Panel: Intake No-Show Intervention

**Panel Members:**
- Program Evaluator
- Behavioural Economist
- Frontline Social Worker
- Lived-Experience Advocate

---

## Round 1: Initial Analysis

### Program Evaluator

The proposal bundles two mechanisms with very different evidence bases; evaluate them separately.

**Reminders — strong, well-replicated.** A Cochrane review and multiple RCTs support reminders. The relevant trial here is the one that matches the population: an urban resident clinic, 95% Black, low-income, baseline no-show ~31%, where adding an SMS reminder cut no-shows from 38.1% (control) to 23.5% (intervention) — ~14.6 percentage points, p=0.04. That is a real, sizeable effect in a population demographically close to ours. The broader literature puts reminder effects in the range of a 10-38% *relative* reduction in missed visits. Low cost, low risk. I'd adopt reminders almost regardless of the rest.

**The "confirm or lose the slot" rule - this is not a reminder, it's a conditional-access policy, and it must be evaluated as one.** It will reduce the *recorded* no-show rate. The mechanism by which it does so is the whole question, and it splits into two:
- *Genuine behaviour change* (people attend who otherwise wouldn't), or
- *Denominator manipulation* (people who don't confirm are removed from the schedule before they can be counted as no-shows).

These are not the same thing and the headline metric cannot distinguish them. I want this designed so we can.

**Measurement I'd require before rollout (RE-AIM frame):** Reach (who can actually receive and act on an SMS - phone access is unstable in this population); Effectiveness measured as *attendance and total unique people served*, not the no-show rate; Implementation fidelity (is the rule applied consistently or selectively at the desk); Maintenance (does any effect survive past the novelty window). Disaggregated by risk group, for reasons the Lived-Experience Advocate will sharpen.

---

### Behavioural Economist

I want to complicate the instinct that "any pressure is harmful," because the evidence doesn't support that blanket claim - and the nuance is the useful part.

**Loss-framing in the *message* can work.** Two UK NHS RCTs (~10,000 and ~9,800 patients) found that an SMS stating the *cost of a missed appointment to the health system* cut the Did-Not-Attend rate from 11.1% to 8.4% (OR 0.74, 95% CI 0.61-0.89) versus the standard reminder, replicated in the second trial. So a well-designed normative/loss-framed *reminder* is among the most cost-effective levers available - it's free to send.

**But that is categorically different from a loss-framed *access penalty*.** The NHS effect operates through salience and social norm at zero cost to the patient. "Confirm or lose your slot" operates through threatened loss of *access to the service itself*. Same psychological lever (loss aversion), completely different target - one nudges attention, the other gates care. Conflating them is the error I'd guard against.

**Design principles:** reduce friction rather than add a hurdle (a confirmation *requirement* is a hurdle); prefer an opt-out default (silence = "held"; "reply STOP if you can't make it") over opt-in ("reply YES or lose it"), because the two collect the same scheduling signal but the opt-in version's failure mode is *losing the silent, hardest-to-reach tail*. My recommendation: keep the loss-framed *information* (it works), drop the loss-framed *penalty*.

---

### Frontline Social Worker

Let me describe what a no-show *is* in this population, because the proposal treats it as a choice and the data says it largely isn't a free one.

The strongest predictor of a future no-show is a *history* of no-shows - which means we're targeting a stable, identifiable group, not random forgetfulness. And that group is structured: non-attendance is independently associated with low income (one oncology-access study found an adjusted OR around 2.9) and with being Black or Latino (OR around 3.3), plus homelessness and unstable housing. The people with the highest no-show rates are disproportionately the people in the most precarity - unstable phones, crises, competing survival demands, no transit fare.

**Operationally:** a 24-hour confirmation window assumes a stable phone, the executive function to track a deadline mid-crisis, and a reason to trust we'll hold up our end. The clients who fail that test are not the marginal forgetters - they're our highest-need cases. The reminder I support fully. The penalty cleans the spreadsheet by pushing the hardest cases back out the door, and it does it precisely to the people the shelter exists for.

One thing I'll concede against my own position: empty held slots when there's a waitlist are a real cost, and staff do need a capacity signal. So I'm against the *penalty*, not against collecting a confirmation.

---

### Lived-Experience Advocate

I'll start by granting the uncomfortable thing, because ducking it would weaken the case: penalty policies *can* lower the recorded number. A community health center that barred persistently-missing patients until formal reinstatement dropped its no-show rate from 34% to 11% over two years. So I'm not going to argue "it won't work." I'm going to argue about *what "work" counted*.

That same policy required roughly 20 staff-hours a week to administer, and "barred until reinstated" means the people who fell off didn't show up in the no-show column because they weren't on the schedule at all. That is the denominator point the Evaluator raised, lived from the other side: when you've been in the system, "confirm by this time or lose it" reads as *we were looking for a reason to give your bed to someone easier*, and people respond by not trying to book - which moves the failure upstream, before intake, where your metrics can't see it. There's survey evidence in the fee literature that fear of a penalty makes people *avoid* booking rather than attend; treat the exact percentages skeptically (they're survey-sourced, not RCTs), but the direction is consistent with what I've watched happen.

And notice who designed this. The fix optimizes the *staff's* scheduling pain. Nobody who has missed an intake because their phone was stolen was in the room when "confirm or lose the slot" got written. That's the framing to fix first.

---

## Round 2: Cross-Examination

### Program Evaluator responds to the Lived-Experience Advocate

The Advocate's upstream point is the one that changes my evaluation design, and I want to be precise about why. I was going to measure attendance among people who reach intake. But if "the slot disappears" suppresses people from *booking in the first place*, that effect is entirely outside my denominator - I'd record a falling no-show rate *and* a rising attendance rate while the program quietly shrinks at the front door. The 34%->11% community-health-center result is consistent with exactly that: we don't know from the headline figure how much was attendance gain versus roster attrition, and the 20-hours/week tells me the "improvement" had a large administrative-exclusion component.

So I'm revising the primary endpoint away from the no-show rate entirely. Primary: *total unique people served* and *time-to-intake* against a pre-period baseline. The no-show rate becomes a monitored secondary, explicitly flagged as gameable. Only this framing can catch a penalty that "works" on the rate while serving fewer people.

### Frontline Social Worker responds to the Behavioural Economist

The Economist's distinction between loss-framed *information* and a loss-framed *penalty* is the hinge, and it dissolves most of my operational objection. The NHS "cost of a missed appointment" wording is just a better reminder - it costs the client nothing and I'd run it. My objection was always to gating access, not to telling people their slot matters.

So I can support collecting the confirmation *signal* on the Economist's opt-out design - silence defaults to "held," "reply if you can't" - because that gives the desk the capacity information without the exclusion. One desk-level condition: an opt-out reply ("can't make it") has to trigger an *offered re-book*, not a quiet removal, or opt-out just becomes a politer exit for the same tail.

### Lived-Experience Advocate responds to the Program Evaluator

Building on the Evaluator's revised endpoint - measuring total people served is right, but *disaggregate it or it will hide the harm*. The whole worry is that the penalty filters a specific tail: the OR ~2.9 (low income) and ~3.3 (Black/Latino) groups the Social Worker cited are precisely who gets removed, and an aggregate "people served" number can hold steady or rise while that tail is pushed out and replaced by easier-to-serve clients. I want no-show, attendance, and people-served broken out by those risk groups, with the affected community at the table defining what "doing worse" looks like - because a statistician and I might draw that line differently.

---

## Round 3: Convergence

### Program Evaluator
Converged: separate the mechanisms; adopt the loss-framed reminder; reject the access penalty; collect confirmation as an opt-out signal; and measure on disaggregated total-people-served and time-to-intake, with the no-show rate demoted to a gameable secondary.

### Behavioural Economist
Agreed. We keep the lever the evidence supports (loss-framed *information*, NHS-replicated) and drop the lever that aims loss aversion at access. Pilot the opt-out wording in EN and FR before scaling - message phrasing has measurable effects, so it shouldn't be guessed.

### Frontline Social Worker
Agreed, with the two desk conditions: silence defaults to held; any "can't make it" triggers an offered re-book. That's a workflow I can run and defend to a client's face.

### Lived-Experience Advocate
I can support this version: the exclusion mechanism is gone and the measurement will actually see the tail. The condition I won't drop - affected clients help set the success criteria *before* this scales. If that step gets cut for speed, my agreement doesn't transfer to the scaled version.

---

## Final Synthesis

**Recommendation:** Adopt the **SMS reminder**, using NHS-style loss/normative framing ("a missed appointment costs the shelter a bed-night someone else needed"), which the RCT evidence supports as cost-free and effective. **Do not** adopt the "confirm 24h or lose the slot" penalty. Replace it with an **opt-out confirmation** (silence = held; "reply if you can't make it" -> offered re-book), piloted in EN and FR before any full rollout.

**Why the proposal changed:** The penalty would reduce the *recorded* no-show rate substantially - the 34%->11% community-health-center precedent is real - but the panel established that this works largely through denominator attrition (removing the high-risk tail from the schedule) and upstream booking suppression, at a documented ~20 staff-hours/week, falling hardest on the low-income and racialized groups with the highest baseline non-attendance (adjusted ORs ~2.9 and ~3.3). It optimizes the organization's scheduling pain, not client attendance. The opt-out redesign preserves the capacity signal leadership wanted without the exclusion.

**Decision Framework (RAPID):**
- **Recommend:** Loss-framed reminder + opt-out confirmation + offered re-book; no slot-release penalty
- **Agree:** Program leadership; intake staff (workflow); client/community representatives (success criteria)
- **Perform:** Intake team (workflow), IT (opt-out SMS logic, EN/FR), Evaluator (measurement plan)
- **Input:** Lived-Experience Advocate and affected clients on wording and success definition; Charity Lawyer on consent for SMS contact
- **Decide:** Program Director

**Measurement (revised, the panel's core technical output):** Primary endpoints are *total unique people served* and *time-to-intake* vs. baseline, **disaggregated** by the high-risk groups most likely to be filtered out. The no-show rate is retained only as a monitored secondary, explicitly labelled as gameable via denominator effects. Pilot phrasing in EN and FR.

**Live disagreement preserved:** Support from the Lived-Experience Advocate is conditional and does **not** extend to a scaled rollout if affected clients are excluded from defining the success criteria for speed. This is a gate on scaling, not a resolved point.

**Evidence-quality flags (stated, not buried):** Reminder effects and the NHS loss-framing effect are RCT-grade. The 34%->11% penalty result and the 20-hours/week figure are single-site observational. The "fees suppress care-seeking" figures are survey/advocacy-sourced and treated as directional only. The disaggregation ORs are from outpatient/oncology populations, not shelters - directionally relevant, not a precise transfer.

**Key insight:** The original metric (no-show rate) and the original mechanism (slot-release penalty) were mutually reinforcing in the wrong direction - the penalty most improves the one metric least able to detect the harm it causes, because both run through the same denominator. Fixing the measurement and fixing the mechanism turned out to be the same move.
