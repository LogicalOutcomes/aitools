---
name: social-services-review
description: Literature reviews and evidence syntheses for non-profit, community, social, and health services. Searches academic databases AND grey literature (government reports, program evaluations, community org publications). Uses RE-AIM, Theory of Change, logic models. Outputs for funders, practitioners, and policy makers. Includes Canadian sources (CIHR, PHAC, CMHC, Statistics Canada) and social science databases (Campbell Collaboration, CINAHL, PsycINFO, ERIC). Use for literature reviews, evidence syntheses, environmental scans, scoping reviews, or program evaluation evidence in homelessness, housing, mental health, substance use, youth services, Indigenous health, immigrant services, poverty, child welfare, public health, or any non-profit domain. Also triggers on "what works" or "what's the evidence for" questions about social programs.
license: MIT
metadata:
  version: 1.1.1
  author: LogicalOutcomes
  source: https://github.com/LogicalOutcomes/aitools
  inspired_by: https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/literature-review
---

# Social Services Literature Review

## Overview

Conduct rigorous literature reviews and evidence syntheses tailored for non-profit, community, and social/health services contexts. This skill goes beyond traditional academic databases to include grey literature — government reports, program evaluations, community organization publications, and policy documents — which is where much of the evidence in social services actually lives.

The skill supports multiple review types (systematic, scoping, rapid, realist) and produces outputs that serve mixed audiences: funders reviewing grant applications, practitioners designing programs, and policy makers weighing interventions.

## Canadian Privacy Triage

**This is not legal advice — confirm with your own privacy or legal contact.**

Reviews involving client, participant, or community data may implicate Canadian privacy law. Which law applies depends on your organization type, information type, and whether data crosses a border:

- **PIPEDA** (federal) applies to private-sector organizations engaged in commercial activity involving personal information. It does **not** generally apply to non-profits and charities **unless** they engage in commercial activity. See [PIPEDA in brief](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/pipeda_brief/) and [Privacy laws in Canada](https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/02_05_d_15/) (OPC).
- **Provincial privacy laws** (e.g., PHIPA in Ontario for health information) and contractual obligations may apply regardless.
- **TCPS2 research ethics** applies when collecting or synthesizing data about human participants for research purposes.

De-identify before analysis; never paste identifiable data into a general-purpose AI assistant.

## When to Use This Skill

Use this skill when:

- Conducting a literature review on a social services intervention or program model
- Building an evidence base for a grant proposal or funding application
- Performing a scoping review or environmental scan in community health or social services
- Evaluating "what works" for a specific population or problem in a social context
- Writing a program evaluation that needs a literature grounding
- Investigating evidence-based practices in homelessness, housing, mental health, substance use, youth services, child welfare, immigrant/refugee services, Indigenous health, food security, aging, disability, poverty reduction, violence prevention, or public health
- Synthesizing both peer-reviewed and grey literature for a Canadian or North American context
- Preparing evidence briefs for boards, funders, or government stakeholders

## Low-Resource Rapid Evidence Scan (for small orgs without database access)

Many non-profits lack librarians, paid database subscriptions, and systematic-review budgets. This lighter path produces useful, honest evidence in 2–4 hours using only free and open sources. Use it explicitly when the full systematic review is impractical.

**Scope and honesty:** Label the output a **Rapid Evidence Scan**, not a systematic review. State the time invested, sources searched, and key limitations in the report.

**Free and open sources to search:**

1. Google Scholar — broad coverage; use `site:` operators for Canadian sources (e.g., `site:canada.ca`)
2. PubMed/MEDLINE (free at pubmed.ncbi.nlm.nih.gov) — health and public health evidence
3. Campbell Collaboration (campbellcollaboration.org) — free systematic reviews on social interventions
4. Cochrane Library — free systematic review abstracts
5. Government and grey literature — canada.ca publications, provincial health authority sites, Statistics Canada, CMHC, PHAC, CIHR (all free)
6. Sector hubs — homelesshub.ca, ccsa.ca, mentalhealthcommission.ca, evaluationcanada.ca
7. Google Advanced Search with `filetype:pdf` and `site:` operators for organizational reports

**Time-boxed method (adapt to your deadline):**

1. Define one clear question (PICO or plain language — 10 min)
2. Run 4–6 targeted Google Scholar and PubMed searches, noting search strings (30–45 min)
3. Skim titles/abstracts; pull 8–15 relevant sources (20–30 min)
4. Search 2–3 sector hubs and one government source for grey literature (20–30 min)
5. Extract key findings into a simple table: Source | Population | Intervention | Key Finding | Quality note (30–45 min)
6. Write a 1–2 page synthesis with explicit limitations (30–45 min)

**Quality note:** always flag that subscription databases (PsycINFO, CINAHL, Social Work Abstracts) were not searched and that findings may miss important evidence. Recommend a fuller search if the stakes are high (policy decisions, major funding).

---

## Core Workflow (Full Systematic Review)

Literature reviews in social services follow a structured but flexible process. The phases below can be adapted depending on review type (systematic, scoping, rapid, or realist).

### Phase 1: Planning and Scoping

1. **Define the Research Question**

   Social services reviews benefit from multiple question frameworks depending on the nature of the inquiry:

   **PICO** (for intervention effectiveness questions):
   - Population, Intervention, Comparison, Outcome
   - Example: "What is the effectiveness of Housing First (I) for chronically homeless youth (P) compared to traditional shelter services (C) in improving housing stability (O)?"

   **SPIDER** (for qualitative and mixed-methods questions):
   - Sample, Phenomenon of Interest, Design, Evaluation, Research type
   - Example: "How do homeless youth (S) experience transitional housing programs (PI) as studied through interviews and focus groups (D), evaluating perceived barriers and facilitators (E) in qualitative research (R)?"

   **PICo** (for qualitative questions about lived experience):
   - Population, phenomenon of Interest, Context
   - Example: "How do Indigenous youth (P) navigate mental health services (I) in urban Canadian settings (Co)?"

   **Program Evaluation Framing** (for "what works" questions):
   - What intervention or program model is being examined?
   - For what population and in what setting?
   - What outcomes matter (and to whom)?
   - What contextual factors influence effectiveness?
   - What implementation considerations exist?

2. **Establish Scope and Objectives**:
   - Define clear research questions (typically 2-4)
   - Determine review type:
     - **Systematic review**: Comprehensive, reproducible search with quality assessment
     - **Scoping review**: Maps available evidence on a broad topic (PRISMA-ScR)
     - **Rapid review**: Time-limited synthesis for urgent decision-making
     - **Realist review**: Explains what works, for whom, in what circumstances, and why
     - **Narrative review**: Summarizes and interprets a body of literature
   - Set boundaries (time period, geography, populations, study types)
   - Decide whether to include grey literature (almost always yes in social services)

3. **Develop Search Strategy**:
   - Identify 2-4 main concepts from research question
   - List synonyms, abbreviations, and related terms — social services terminology varies widely across jurisdictions (e.g., "rough sleeping" vs "street homelessness," "social housing" vs "public housing")
   - Plan Boolean operators (AND, OR, NOT) to combine terms
   - Select databases — see Phase 2 for database selection guidance
   - Plan grey literature search strategy separately (see Grey Literature section)

4. **Set Inclusion/Exclusion Criteria**:
   - Date range (social services evidence evolves; 10-15 years is typical)
   - Language (English, French for Canadian reviews)
   - Publication types: peer-reviewed AND grey literature (reports, evaluations, working papers)
   - Study designs: quantitative, qualitative, AND mixed methods — social services evidence often comes from qualitative and participatory research
   - Geography: specify if Canadian-focused, North American, or international
   - Population: be specific but inclusive of subgroups
   - Document all criteria clearly

### Phase 2: Systematic Literature Search

Social services reviews must search both academic databases and grey literature sources. This is not optional — excluding grey literature misses the majority of evidence in this field.

#### Academic Databases

Select databases appropriate for the domain. Search at least 3 academic databases plus grey literature sources.

**Social Science & Health Services (Core):**

| Database | Coverage | Best For | Access |
|----------|----------|----------|--------|
| PsycINFO | Psychology, behavioral sciences | Mental health, substance use, behavioral interventions | Subscription |
| CINAHL | Nursing & allied health | Community health nursing, health promotion, patient education | Subscription |
| Social Work Abstracts | Social work practice & policy | Direct practice, child welfare, family services | Subscription |
| ERIC | Education literature | Youth programs, early childhood, school-based interventions | Free (eric.ed.gov) |
| Campbell Collaboration | Systematic reviews in social sciences | Evidence-based social interventions — "what works" reviews | Free (campbellcollaboration.org) |
| Cochrane Library | Systematic reviews in health | Community health interventions, public health | Free for reviews |
| Sociological Abstracts | Sociology | Social inequality, community dynamics, social policy | Subscription |
| SSRN | Working papers across social sciences | Pre-publication research, policy analysis | Free (ssrn.com) |

**Biomedical (when health outcomes are relevant):**

| Database | Best For | Access |
|----------|----------|--------|
| PubMed/MEDLINE | Health interventions, public health, epidemiology | Free (pubmed.ncbi.nlm.nih.gov) |
| PubMed Central | Full-text health research | Free |
| Global Health | International health, low-resource settings | Subscription |

**General/Cross-disciplinary:**

| Database | Best For | Access |
|----------|----------|--------|
| Semantic Scholar | Cross-disciplinary searches, citation graphs | Free API (semanticscholar.org) |
| Google Scholar | Comprehensive coverage including grey literature | Free (scholar.google.com) |
| Web of Science | Citation analysis, research impact | Subscription |
| Scopus | Broad scientific coverage, bibliometrics | Subscription |

For detailed search strategies by database, see `references/database_strategies.md`.

#### Canadian-Specific Sources

These are essential for any Canadian-focused review. See `references/database_strategies.md` for detailed search guidance.

| Source | Coverage | URL |
|--------|----------|-----|
| CIHR (Canadian Institutes of Health Research) | Funded research, knowledge syntheses | cihr-irsc.gc.ca |
| PHAC (Public Health Agency of Canada) | Public health reports, surveillance data, best practices | canada.ca/public-health |
| CMHC (Canada Mortgage and Housing Corp.) | Housing research, homelessness data | cmhc-schl.gc.ca |
| Statistics Canada | Census, surveys, health indicators, social indicators | statcan.gc.ca |
| INSPQ (Institut national de santé publique du Québec) | Public health research (QC) | inspq.qc.ca |
| Provincial health authorities | Regional health data, program evaluations | Varies by province |
| Canadian Observatory on Homelessness | Homelessness research hub | homelesshub.ca |
| Canadian Centre on Substance Use and Addiction | Substance use research and policy | ccsa.ca |
| Mental Health Commission of Canada | Mental health policy, programs, research | mentalhealthcommission.ca |
| First Nations Health Authority (BC) | Indigenous health services and data | fnha.ca |
| National Collaborating Centres for Public Health | Evidence reviews, environmental scans | nccph.ca |
| Canadian Evaluation Society | Evaluation practice, grey literature | evaluationcanada.ca |

#### Grey Literature Search Strategy

Grey literature is critical in social services — program evaluations, government reports, and community organization publications contain evidence that never appears in academic journals. Budget significant search time for this.

**Types of grey literature to search:**

- Government reports (federal, provincial/state, municipal)
- Program evaluation reports from non-profit organizations
- Reports from research institutes and think tanks
- Conference proceedings and presentations
- Theses and dissertations
- Working papers and technical reports
- Community needs assessments
- Annual reports from service organizations
- Policy briefs and white papers

**Grey literature sources:**

| Source | Type | URL |
|--------|------|-----|
| Grey Literature Report (NYAM) | Discontinued service; historical archive only (ceased ~2017). Listed for legacy citations | greylit.org |
| ProQuest Dissertations | Theses & dissertations | proquest.com |
| Government of Canada Publications | Federal reports | publications.gc.ca |
| Homeless Hub | Canadian homelessness research | homelesshub.ca |
| National Academies Press | US policy/research reports | nap.edu |
| RAND Corporation | Policy research | rand.org |
| Urban Institute | Social/economic policy | urban.org |
| Brookings Institution | Policy research | brookings.edu |
| Wellesley Institute | Health equity, housing (Toronto) | wellesleyinstitute.com |
| Maytree Foundation | Poverty reduction (Canada) | maytree.com |
| Tamarack Institute | Community change, poverty reduction | tamarackcommunity.ca |

**Grey literature search tips:**

- Use Google Advanced Search with site-specific operators (e.g., `site:canada.ca "homeless youth" evaluation`)
- Search organizational websites directly — many don't index well in Google
- Check reference lists of known reports for additional sources
- Contact subject matter experts and program staff for unpublished evaluations
- Search conference proceedings from relevant associations (e.g., Canadian Evaluation Society, APHA)

#### Document Search Parameters

For each database or source searched, document:

```markdown
## Search Strategy

### Database: PsycINFO
- **Date searched**: [YYYY-MM-DD]
- **Date range**: [start] to [end]
- **Search string**: [exact string used]
- **Filters**: English or French, Peer-reviewed
- **Results**: [N] articles

### Grey Literature: Canadian Observatory on Homelessness
- **Date searched**: [YYYY-MM-DD]
- **Search terms**: [terms]
- **Method**: Website search + browse by topic
- **Results**: [N] reports
```

### Phase 3: Screening and Selection

1. **Deduplication**: Remove duplicate records across databases (by DOI or title match)

2. **Title and Abstract Screening**:
   - Apply inclusion/exclusion criteria
   - In social services, be inclusive at this stage — titles in grey literature are often less descriptive than academic papers
   - Document number excluded and reasons

3. **Full-Text Screening**:
   - Obtain full texts (grey literature may require direct website downloads or author contact)
   - Apply all criteria rigorously
   - Document specific reasons for exclusion

4. **Create PRISMA Flow Diagram**:

   ```text
   Academic databases: n = [X]
   Grey literature sources: n = [Y]
   ├─ Total records: n = [X+Y]
   ├─ After deduplication: n = [Z]
   ├─ After title/abstract screening: n = [A]
   ├─ After full-text screening: n = [B]
   └─ Included in review: n = [C]
       ├─ Peer-reviewed: n = [D]
       └─ Grey literature: n = [E]
   ```

### Phase 4: Data Extraction and Quality Assessment

1. **Extract Key Data** from each included source:
   - Source metadata (authors, year, organization, DOI or URL)
   - Source type (peer-reviewed article, program evaluation, government report, etc.)
   - Study/evaluation design and methods
   - Population and setting characteristics
   - Intervention or program model description
   - Outcomes measured and key findings
   - Implementation context and considerations
   - Limitations noted
   - Funding source

2. **Assess Quality**:

   Social services evidence comes from diverse study types. Use the appropriate quality assessment tool:

   | Study Type | Quality Tool |
   |-----------|-------------|
   | Randomized controlled trials | Cochrane Risk of Bias (RoB 2.0) |
   | Quasi-experimental studies | ROBINS-I |
   | Observational studies | Newcastle-Ottawa Scale |
   | Qualitative studies | CASP Qualitative Checklist or JBI Qualitative |
   | Mixed-methods studies | Mixed Methods Appraisal Tool (MMAT) |
   | Program evaluations | Evaluation-specific criteria (see below) |
   | Systematic reviews | AMSTAR 2 |
   | Grey literature reports | AACODS Checklist (Authority, Accuracy, Coverage, Objectivity, Date, Significance) |

   **Program evaluation quality criteria:**
   - Was the evaluation design appropriate for the questions asked?
   - Were outcomes clearly defined and measured?
   - Was the comparison group adequate (if applicable)?
   - Were contextual factors documented?
   - Was fidelity of implementation assessed?
   - Were participant perspectives included?
   - Was the sample size adequate?
   - Were limitations acknowledged?

3. **Organize by Themes**:
   - Identify 3-6 major themes across sources
   - Consider organizing by: intervention type, population subgroup, outcome domain, implementation factor, or setting
   - Note patterns, consensus, contradictions, and gaps

### Phase 5: Synthesis and Analysis

1. **Write Thematic Synthesis** (NOT source-by-source summaries):

   Social services syntheses should integrate evidence from both academic and grey literature, noting the source type where relevant.

   Example structure:

   ```markdown
   #### 3.4.1 Theme: Housing First Approaches for Youth

   Housing First models adapted for youth have been examined in [N] studies
   and [N] program evaluations across Canadian cities. The evidence suggests
   that youth-specific adaptations — including developmental supports,
   education/employment connections, and flexible case management — are
   associated with higher housing retention rates ([X–Y%]) compared to
   adult-focused models ([Author, Year]; [Organization, Year]). However,
   several evaluations noted challenges with program fidelity when scaling
   across sites ([Author, Year]; [Organization, Year]).

   (Placeholders above are illustrative only. Every figure and citation in a
   real synthesis must come from a verified source — never invent author names,
   organizations, years, or statistics to fill the pattern.)
   ```

2. **Evaluation Frameworks for Synthesis**:

   When synthesizing evidence about program effectiveness, consider organizing findings using one of these frameworks:

   **RE-AIM** (Reach, Effectiveness, Adoption, Implementation, Maintenance):
   - How many people does the intervention reach?
   - How effective is it?
   - How widely is it adopted by organizations?
   - How well is it implemented?
   - How well are effects maintained over time?

   **Theory of Change / Logic Model**:
   - What are the inputs, activities, outputs, and outcomes?
   - What assumptions underlie the program theory?
   - Does the evidence support the causal pathway?

   **OECD-DAC Evaluation Criteria**:
   - Relevance, Coherence, Effectiveness, Efficiency, Impact, Sustainability

3. **Critical Analysis**:
   - Evaluate methodological quality across studies
   - Assess strength and consistency of evidence
   - Note where grey literature fills gaps left by academic research
   - Identify equity considerations — who is included/excluded from the evidence?
   - Consider transferability across contexts (e.g., US findings applied to Canadian settings)
   - Flag potential biases (publication bias, funder influence, organizational self-evaluation)

4. **Write for Mixed Audiences**:

   The review output should serve funders, practitioners, and policy makers. This means:
   - Include a plain language summary at the top
   - Translate findings into actionable practice recommendations
   - Discuss policy implications explicitly
   - Note implementation considerations and costs where available
   - Use the review template in `assets/review_template.md`

### Phase 6: Citation Verification

Citation accuracy is non-negotiable. A fabricated or unverifiable reference is a
failure of the whole review, not a cosmetic defect.

**Follow the shared protocol in [`references/citation_verification.md`](references/citation_verification.md).** In brief:

- No reference goes in the output unless, in this session, a live web retrieval returned a record whose title, first author, year, and venue match the citation. Never fill a citation in from the model's prior knowledge.
- Use your assistant's **web-search capability** to locate each source, and its **fetch/browse capability** to open the authoritative record (DOI or publisher page, PubMed, the journal site, or the issuing organization's own page for grey literature). Read the metadata off the opened page, not from memory.
- A DOI that does not resolve is the classic signature of a fabricated reference — drop it.
- Apply the same standard to every statistic, percentage, and effect size.
- Append the required **provenance table** mapping each reference to the URL opened and a confirmed/flagged status.

The bundled `scripts/verify_citations.py` is an **optional offline second pass** only. It needs open internet access to doi.org/CrossRef, which most hosted AI code sandboxes block, so it cannot be your primary check — verify live in-session as above.

### Phase 7: Document Generation

1. **Generate the review** using the template in `assets/review_template.md`

2. **Generate PDF** if needed:

   ```bash
   python scripts/generate_pdf.py my_review.md \
     --citation-style apa \
     --output my_review.pdf
   ```

3. **Quality Checklist**:
   - [ ] Research question clearly stated
   - [ ] Both academic AND grey literature searched
   - [ ] Canadian-specific sources included (if applicable)
   - [ ] Search methodology fully documented
   - [ ] Inclusion/exclusion criteria clearly stated
   - [ ] PRISMA flow diagram included
   - [ ] Quality assessment completed (appropriate tools for each study type)
   - [ ] Results organized thematically (not source-by-source)
   - [ ] Practice recommendations included
   - [ ] Policy implications discussed
   - [ ] Plain language summary provided
   - [ ] Equity considerations addressed
   - [ ] All DOIs and URLs verified
   - [ ] Citations formatted consistently (APA 7th recommended)
   - [ ] Limitations of the review acknowledged

## Equity and Inclusion Considerations

Social services reviews should explicitly address equity. Consider:

- **Who is represented** in the evidence? Are there populations missing (Indigenous peoples, racialized communities, LGBTQ2S+ individuals, people with disabilities, immigrants/refugees)?
- **Who defined the outcomes?** Were community members involved in determining what "success" looks like?
- **Whose knowledge counts?** Indigenous knowledge, lived experience perspectives, and community-based participatory research should be valued alongside traditional academic evidence.
- **Intersectionality**: How do overlapping identities (e.g., Indigenous + youth + homeless) shape experiences and outcomes?
- **Context matters**: An intervention that works in one setting may not transfer. Document the conditions under which evidence was generated.

## Common Domains and Search Term Suggestions

For detailed search strategies, see `references/database_strategies.md`. Quick reference for common domains:

| Domain | Key Search Terms |
|--------|-----------------|
| Homelessness | homeless*, housing instability, rough sleeping, shelter, Housing First, transitional housing |
| Youth services | youth, adolescent*, young adult*, emerging adult*, at-risk youth, street youth |
| Mental health | mental health, psychiatric, psychological, counseling, therapy, wellbeing |
| Substance use | substance use, addiction, harm reduction, recovery, opioid, alcohol |
| Indigenous health | Indigenous, First Nations, Métis, Inuit, Aboriginal, decoloniz* |
| Immigrant/refugee | immigrant*, refugee*, newcomer*, settlement, integration |
| Food security | food security, food bank, nutrition, hunger, food access |
| Child welfare | child welfare, child protection, foster care, kinship care |
| Poverty | poverty, low-income, social assistance, income support |
| Violence prevention | domestic violence, intimate partner violence, gender-based violence |
| Disability | disability, accessibility, inclusion, accommodation |
| Aging | older adult*, senior*, aging, elder care, long-term care |

## Bundled Scripts

This skill bundles these helper scripts — no separate literature-review skill is required:

- `scripts/verify_citations.py` — Optional offline DOI batch-check (needs open internet; fails loud and exits non-zero if it cannot reach the verifier). Primary verification is the live protocol in `references/citation_verification.md`
- `scripts/generate_pdf.py` — Convert markdown to professional PDF
- `scripts/parse_exported_results.py` — Process and deduplicate exported search results (note: this script processes results you export from a database; it does not search databases directly)

## Resources

### Bundled Resources

- `assets/review_template.md` — Review template adapted for social services
- `references/citation_styles.md` — Citation formatting guide (APA, Vancouver, etc.)
- `references/database_strategies.md` — Detailed database search strategies for social science and Canadian sources
- `references/citation_verification.md` — Shared, platform-neutral citation-verification protocol (used by Phase 6)

### External Resources

- PRISMA (Systematic Reviews): <https://www.prisma-statement.org/>
- PRISMA-ScR (Scoping Reviews): <https://www.equator-network.org/reporting-guidelines/prisma-scr/>
- Campbell Collaboration: <https://www.campbellcollaboration.org/>
- Cochrane Handbook: <https://training.cochrane.org/handbook>
- CASP Checklists: <https://casp-uk.net/casp-tools-checklists/>
- MMAT (Mixed Methods): <https://mixedmethodsappraisaltoolpublic.pbworks.com/>
- AACODS (Grey Literature): <https://fac.flinders.edu.au/dspace/api/core/bitstreams/e94a96eb-0334-4300-8880-c836d4d9a676/content>
- RE-AIM Framework: <https://re-aim.org/>
- Canadian Observatory on Homelessness: <https://www.homelesshub.ca/>
- Canadian Evaluation Society: <https://evaluationcanada.ca/>
