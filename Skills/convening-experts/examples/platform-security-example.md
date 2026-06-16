# Example: Donor & Client Data Platform - Vendor vs Self-Host (Single-Round)

**User Query:** "We hold donor records and some client case data. We're choosing between a managed cloud CRM/case-management vendor (SaaS) and self-hosting an open-source stack ourselves. We have one full-time IT person and a couple of technical volunteers. Which way should we go?"

## Expert Panel: Data Platform Decision

**Panel Members:**
- Security Architect
- IT & Security Specialist
- DevOps Engineer
- Charity Lawyer
- Finance Analyst

---

### Security Architect

Frame this as a threat model, not a feature comparison. Two asset classes with very different sensitivities: donor PII (names, addresses, giving history - identity-theft and reputational value) and client case data, which is categorically more dangerous because disclosure can physically endanger people, not just embarrass the org. The case data sets the security floor; design to it.

**The "self-host = control" intuition needs to be stated precisely, because it's half-right.** Self-hosting removes a class of risk: no third party with standing access, no vendor-breach blast radius that sweeps you up, you own the encryption and access boundaries. For an org with real operational capacity, that control is a genuine advantage. But control you cannot *exercise* is not a security property - it's latent liability. The dominant breach vector is not exotic: the Verizon 2025 DBIR attributes roughly one in five breaches to exploitation of a known vulnerability, and that share has been rising. A self-hosted stack's security degrades every week patches lag. So the relevant question isn't "which architecture is more secure in principle" - it's "which posture does *this team* actually sustain over years."

**My requirements regardless of path:** encryption at rest and in transit; SSO with enforced MFA; role-based access with least privilege; tamper-evident audit logging (snooping detection is a specific regulatory expectation for case data); and a tested, documented data-export path so an exit is always available. If we go vendor, those become contractual. If we self-host, they become standing labour - which is the IT and DevOps read, so I'll defer there on feasibility.

---

### IT & Security Specialist

I'm the one full-time IT person in this scenario, so I'll be blunt: capacity is the binding constraint here, not architecture, and the proposal quietly assumes capacity we don't have.

Self-hosting a case-management stack means *I* own, indefinitely and personally: OS and dependency patching, TLS renewal, database backups *and* tested restores, log monitoring, access provisioning/deprovisioning, and incident response - for data that can endanger clients. Two volunteers whose availability I can't guarantee don't change that. The failure mode for a lean team isn't a dramatic zero-day; it's *quiet drift* - the backup job that silently stopped eight months ago, discovered the day we need it; the critical CVE that drops while I'm on leave and nobody's covering. Industry surveys keep finding that even resourced teams routinely defer patches to avoid disruption and discover patches they thought deployed never landed. A one-person team will not beat that baseline; it will do worse.

A reputable managed vendor folds patching, backups, monitoring, and physical security into the subscription - which, for a team this size, is the *only* way that baseline actually gets maintained, not a luxury. Strong lean to **managed vendor**, conditioned on the Security Architect's controls and the Charity Lawyer's, and on holding a tested export so we keep an exit.

---

### DevOps Engineer

Agreeing on capacity and pricing out what "self-host responsibly" actually entails, because the word "self-host" hides a permanent operating commitment, not a one-time build.

Minimum responsible self-host: infrastructure-as-code so the environment is reproducible after a failure; a staging environment to test upgrades before they touch production case data; automated encrypted backups with *periodic restore drills* (a backup you have never restored is a hope, not a backup); and monitoring/alerting. That's a standing on-call rotation. With under two reliable FTE you can stand it up, but you cannot *operate* it to the standard client data demands - and "stood up but unmaintained" is the worst quadrant, because it looks done while silently rotting.

**One nuance pushing the other way - against pure SaaS complacency:** vendor lock-in is real and most orgs discover it too late. Mitigate on day one - require bulk export in a documented, non-proprietary format and actually *run* a full export during the trial. A vendor that can't demonstrate clean export is disqualified. That single test also de-risks the Finance concern about switching cost.

---

### Charity Lawyer

Two legal points, and the first corrects a common misconception that would otherwise drive a wrong decision.

**Data residency is a due-diligence-and-consent question, not a prohibition.** PHIPA (Ontario health information) is technology-neutral and does **not** forbid storing or processing data outside Ontario or Canada. It runs on an *accountability* model: the organization remains the custodian and stays liable; a SaaS vendor handling the data is an "agent" under PHIPA s.17 and must be bound by a written agreement to equivalent safeguards (access limits, audit logging, breach notification, no unauthorized onward transfer). PIPEDA treats cross-border transfer the same way - permitted, but you remain accountable and must ensure comparable protection by contract and disclose the transfer. So "the data can't leave Canada" is usually false; the real obligations are a signed data-processing/agent agreement, a privacy impact assessment, and transparent consent that covers any cross-border flow.

**But classify the data first, because the regime depends on it.** Donor records are PIPEDA-governed commercial-activity data. "Client case data" *may* be PHIPA-regulated personal health information if your services are health-adjacent - and that raises the bar on consent, the lockbox/withdrawal right, breach notification, and agent agreements. Which law applies changes the contract you need. Confirm classification before signing anything.

Net: a vendor is legally workable - including a US-hosted one, with the right agreement and consent - but a Canadian data-residency region, where offered, materially reduces the cross-border exposure you'd otherwise have to paper over, and is worth requiring.

---

### Finance Analyst

**Total cost of ownership, not licence price.**

**Self-host** looks cheap because the software is free, but the real cost is labour and tail risk. The standing ops burden the IT and DevOps experts described is effectively unfunded additional FTE; the contingent cost is a breach (notification, remediation, regulatory exposure, and - hardest to recover - donor trust). For a lean org the hidden labour cost typically swamps the licence savings, and the breach tail is a low-probability, high-severity line you're self-insuring.

**Managed vendor** converts that into a predictable subscription that bundles the ops labour. Residual risks are price escalation and lock-in - both manageable: negotiate a multi-year rate, hold a switching reserve, and keep the proven export path. Watch for registered-charity pricing; many vendors discount heavily, which often closes the sticker gap entirely.

**Read:** vendor has the lower *true* TCO at this team size and turns a lumpy catastrophic risk into a smooth operating line.

---

## Synthesis (RAPID Framework)

**Recommend:** Adopt a **managed vendor** for donor and client data - conditioned on: (1) data classification confirmed first, since PHIPA may apply to client case data and changes the contract; (2) a signed agent/data-processing agreement imposing equivalent safeguards (PHIPA s.17 / PIPEDA accountability), with Canadian data residency required where offered; (3) the Security Architect's controls (encryption, SSO+MFA, least-privilege RBAC, tamper-evident audit logging); and (4) a bulk-export path proven during the trial to defuse lock-in.

**Why not self-host:** Every expert converged on the same pivot - self-hosting offers real control (Security Architect) and reduces cross-border exposure (Charity Lawyer), but those advantages are only realized with operational capacity this team does not have. The decisive factor is capacity, not architecture: with known-vulnerability exploitation driving ~20% of breaches and lean teams structurally unable to sustain patch/restore discipline, an unmaintained self-hosted stack is a *worse* security and legal posture than a competent managed vendor - and it costs more once the unfunded ops labour and breach tail are counted. The "data sovereignty" argument for self-hosting is also weaker than it first appears, because residency is a contractual/consent obligation a vendor can satisfy, not a legal wall only self-hosting can clear.

**Agree:** Executive Director / board (data-custody risk owner), IT lead, Finance
**Perform:** IT & Security Specialist (vendor setup, access model), DevOps Engineer (export verification, integration)
**Input:** Security Architect (control requirements), Charity Lawyer (data classification, agent agreement, residency, consent), Finance Analyst (contract terms, charity pricing)
**Decide:** Executive Director, with board awareness given client-data sensitivity

**Live condition that would flip the recommendation (a dependency, not an unresolved dispute):** Self-host becomes correct only if **both** (a) data classification plus a specific legal constraint genuinely bars terms any suitable vendor will sign, **and** (b) the org funds real ops capacity - at least one dedicated, backed-up FTE able to sustain patching, restore drills, and incident response. Absent both, vendor stands. The panel did not disagree on this; it's the explicit boundary of the recommendation.
