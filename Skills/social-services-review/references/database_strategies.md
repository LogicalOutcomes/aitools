# Database Search Strategies for Social Services Reviews

This document provides detailed search guidance for academic databases, Canadian-specific sources, and grey literature relevant to social services, community health, and non-profit program evaluation.

## Table of Contents

1. [Academic Database Strategies](#academic-database-strategies)
2. [Canadian-Specific Source Strategies](#canadian-specific-source-strategies)
3. [Grey Literature Search Strategies](#grey-literature-search-strategies)
4. [Search Term Banks by Domain](#search-term-banks-by-domain)
5. [Boolean Search Construction](#boolean-search-construction)

---

## Academic Database Strategies

### PsycINFO

**Access**: Subscription (via EBSCOhost, Ovid, or ProQuest)
**Coverage**: 5M+ records in psychology and behavioral sciences
**Best for**: Mental health, substance use, behavioral interventions, developmental psychology, community psychology

**Search tips**:

- Use Thesaurus terms (equivalent to MeSH): DE "Homelessness", DE "At Risk Populations"
- Field codes: TI (title), AB (abstract), DE (descriptor/subject), AG (age group)
- Age group filters: Childhood (birth-12), Adolescence (13-17), Adulthood (18+)
- Publication type filters: Peer-reviewed journal, Dissertation
- Methodology filters: Empirical Study, Qualitative Study, Meta Analysis, Literature Review

**Example search — homeless youth interventions:**

```text
(DE "Homeless" OR DE "Homelessness" OR TI "homeless*" OR AB "homeless*" OR
 AB "housing instability" OR AB "street youth" OR AB "unhoused")
AND
(DE "Adolescent Development" OR AG "Adolescence (13-17 yrs)" OR
 AG "Adulthood (18 yrs & older)" OR TI "youth" OR TI "young adult*" OR
 AB "emerging adult*" OR AB "young people")
AND
(DE "Intervention" OR DE "Treatment" OR DE "Program Evaluation" OR
 AB "program" OR AB "service*" OR AB "intervention*")
```

### CINAHL (Cumulative Index to Nursing & Allied Health Literature)

**Access**: Subscription (via EBSCOhost)
**Coverage**: 6M+ records in nursing and allied health
**Best for**: Community health nursing, health promotion, patient education, public health nursing, social determinants of health

**Search tips**:

- Use CINAHL Subject Headings (similar to MeSH)
- Field codes: MH (exact subject heading), MW (word in subject heading), TI, AB
- Subheadings available for subject headings (e.g., MH "Homelessness/PF" for psychosocial factors)

**Example search:**

```text
(MH "Homeless Persons" OR MH "Homeless Youth" OR TI "homeless*" OR AB "homeless*")
AND
(MH "Adolescence" OR MH "Young Adult" OR TI "youth" OR AB "young people")
AND
(MH "Program Evaluation" OR MH "Community Health Services" OR
 AB "intervention*" OR AB "program*")
AND
(MH "Urban Health" OR AB "urban" OR AB "city" OR AB "metropolitan")
```

### Social Work Abstracts

**Access**: Subscription (via EBSCOhost or ProQuest)
**Coverage**: Social work practice, theory, and policy
**Best for**: Direct practice, child welfare, family services, community organizing, social policy

**Search tips**:

- Smaller database — use broader search terms
- Less controlled vocabulary than PsycINFO or CINAHL
- Good for finding practice-oriented literature

### ERIC (Education Resources Information Center)

**Access**: Free at eric.ed.gov
**Coverage**: Education research and practice
**Best for**: Youth programs, school-based interventions, early childhood, family literacy, mentoring

**Search tips**:

- Use ERIC Descriptors: e.g., "At Risk Students", "Youth Programs", "Mentors"
- Filter by Source: Journal Articles, Reports (Evaluative), Reports (Research)
- Filter by Education Level: Elementary, Secondary, Postsecondary
- Free full text available for many ERIC documents

### Campbell Collaboration

**Access**: Free at campbellcollaboration.org
**Coverage**: Systematic reviews of social interventions
**Best for**: Finding existing "what works" evidence syntheses — saves time by starting with existing reviews

**Search tips**:

- Browse by Coordinating Group: Crime and Justice, Education, Social Welfare, Disability, Knowledge Translation
- Search the Campbell Library for systematic reviews and evidence/gap maps
- Check protocols for reviews in progress
- Campbell reviews are the social sciences equivalent of Cochrane reviews — high quality, rigorous methodology

### PubMed / MEDLINE

**Access**: Free at pubmed.ncbi.nlm.nih.gov
**Coverage**: 35M+ records in biomedical and health sciences
**Best for**: Health interventions, public health, epidemiology, community health

**Search tips**:

- Use MeSH terms: "Homeless Persons"[MeSH], "Adolescent"[MeSH]
- Field tags: [Title], [Title/Abstract], [MeSH Terms], [Author]
- Use MeSH browser (meshb.nlm.nih.gov) to find standardized terms
- Date filters: 2015:2026[Publication Date]
- Publication type filters: Review, Clinical Trial, Meta-Analysis

**Example search:**

```text
("Homeless Persons"[MeSH] OR "homeless*"[Title/Abstract] OR
 "housing instability"[Title/Abstract])
AND
("Adolescent"[MeSH] OR "Young Adult"[MeSH] OR "youth"[Title/Abstract])
AND
("urban"[Title/Abstract] OR "cities"[Title/Abstract])
AND
("Canada"[MeSH] OR "canada*"[Title/Abstract])
AND 2015:2026[Publication Date]
```

### Semantic Scholar

**Access**: Free API at api.semanticscholar.org
**Coverage**: 200M+ papers across all disciplines
**Best for**: Cross-disciplinary searches, discovering citation networks, finding influential papers

**API search example:**

```text
GET https://api.semanticscholar.org/graph/v1/paper/search
?query=homeless+youth+intervention+urban+canada
&fields=title,authors,year,abstract,citationCount,url
&limit=100
&year=2015-2026
```

### Google Scholar

**Access**: Free at scholar.google.com
**Coverage**: Comprehensive — includes academic papers, grey literature, theses, court opinions
**Best for**: Comprehensive searches, finding grey literature that appears alongside academic sources, citation tracking

**Search tips**:

- Use quotes for exact phrases: "Housing First" "youth"
- Use `site:` to search specific domains: `site:canada.ca "homeless youth"`
- Use "Cited by" for forward citation searching
- Advanced search allows date range, author, and publication filters
- No API — must search manually or carefully
- Export citations via "Cite" button

---

## Canadian-Specific Source Strategies

### CIHR (Canadian Institutes of Health Research)

**URL**: cihr-irsc.gc.ca
**What to find**: Funded research projects, knowledge synthesis grants, research reports
**How to search**:

- Search CIHR Funding Decisions database for funded projects by keyword
- Check CIHR Institute pages for priority areas and reports (e.g., Institute of Population and Public Health, Institute of Indigenous Peoples' Health)
- Review CIHR Evidence Briefs and Best Brains Exchanges

### PHAC (Public Health Agency of Canada)

**URL**: canada.ca/en/public-health.html
**What to find**: Best practice guidelines, surveillance reports, program evaluations, public health reports
**How to search**:

- Browse by topic: Mental Health, Substance Use, Social Determinants, etc.
- Search canada.ca with topic keywords
- Check the Canadian Best Practices Portal (cbpp-pcpe.phac-aspc.gc.ca) for intervention summaries — note: PHAC has archived this portal (site banner: "This site has been archived"); it is no longer updated but remains accessible for legacy/historical interventions
- Review Chief Public Health Officer reports

### CMHC (Canada Mortgage and Housing Corporation)

**URL**: cmhc-schl.gc.ca
**What to find**: Housing research, homelessness data, Reaching Home program reports, National Housing Strategy research
**How to search**:

- Browse Research & Data section
- Search Housing Research publications
- Check Reaching Home program evaluations and data
- Review National Housing Strategy reports and evaluations

### Statistics Canada

**URL**: statcan.gc.ca
**What to find**: Census data, survey data (Canadian Community Health Survey, General Social Survey), health indicators, social indicators
**How to search**:

- Search by topic or keyword
- Browse The Daily for recent releases
- Access data tables and profiles
- Check Health Reports and other analytical publications
- Use Census Profiles for community-level data

### Canadian Observatory on Homelessness / Homeless Hub

**URL**: homelesshub.ca
**What to find**: Research papers, reports, toolkits, program profiles, community plans
**How to search**:

- Use the Research Library search
- Browse by topic: Youth, Indigenous, Mental Health, Housing First, etc.
- Check Canadian Definition of Homelessness and related frameworks
- Review community-level reports and plans of action

### Provincial and Territorial Sources

Each province has relevant sources. Key examples:

**Ontario:**

- Health Quality Ontario / Ontario Health: ontariohealth.ca
- Ministry of Children, Community and Social Services reports
- Knowledge Institute on Child and Youth Mental Health and Addictions (formerly the Ontario Centre of Excellence for Child and Youth Mental Health; renamed 2021): cymha.ca

**British Columbia:**

- BC Housing Research Centre
- First Nations Health Authority: fnha.ca
- BC Centre on Substance Use: bccsu.ca

**Alberta:**

- Alberta Health Services evaluations
- Calgary Homeless Foundation reports
- Homeward Trust Edmonton reports

**Quebec:**

- INSPQ (Institut national de santé publique du Québec): inspq.qc.ca
- Note: Many Quebec sources are in French

**Manitoba:**

- Manitoba Centre for Health Policy: mchp-appserv.cpe.umanitoba.ca

### Other Canadian Organizations

| Organization | Focus | URL |
|-------------|-------|-----|
| Canadian Centre on Substance Use and Addiction | Substance use | ccsa.ca |
| Mental Health Commission of Canada | Mental health | mentalhealthcommission.ca |
| National Collaborating Centres for Public Health | Evidence synthesis | nccph.ca |
| Wellesley Institute | Health equity, housing | wellesleyinstitute.com |
| Maytree Foundation | Poverty reduction | maytree.com |
| Tamarack Institute | Community change | tamarackcommunity.ca |
| Canadian Evaluation Society | Evaluation practice | evaluationcanada.ca |
| Raising the Roof | Homelessness prevention | raisingtheroof.org |
| Canadian Alliance to End Homelessness | Policy, advocacy | caeh.ca |
| Assembly of First Nations | Indigenous policy | afn.ca |
| Inuit Tapiriit Kanatami | Inuit policy | itk.ca |
| Métis National Council | Métis policy | metisnation.ca |

---

## Grey Literature Search Strategies

### Systematic Approach to Grey Literature

Grey literature searching is less standardized than academic database searching, but should still be systematic and documented.

**Step 1: Organizational website searches**

- Identify 10-15 key organizations in the topic area
- Search each organization's website using their internal search and/or Google site search
- Browse publications/resources/reports sections
- Document: organization, date searched, search terms, number of results

**Step 2: Google Advanced Search**

- Use `site:` operators to search specific domains
- Use `filetype:pdf` to find reports
- Combine with topic keywords
- Example: `site:canada.ca filetype:pdf "homeless youth" "evaluation" OR "evidence"`

**Step 3: Government publication repositories**

- Government of Canada Publications: publications.gc.ca
- Provincial government publication sites
- Municipal government reports and plans

**Step 4: Research institute and think tank searches**

- RAND Corporation: rand.org
- Urban Institute: urban.org
- Brookings Institution: brookings.edu
- National Academies Press: nap.edu (US)
- Institute for Research on Public Policy: irpp.org (Canada)
- Caledon Institute: no longer active but archived publications remain cited

**Step 5: Dissertation and thesis repositories**

- ProQuest Dissertations & Theses Global
- Theses Canada (Library and Archives Canada): bac-lac.gc.ca
- Institutional repositories (university-specific)

**Step 6: Conference proceedings**

- Canadian Evaluation Society conference proceedings
- American Public Health Association (APHA) proceedings
- Society for Social Work and Research (SSWR) proceedings

**Step 7: Expert consultation**

- Contact 3-5 subject matter experts
- Ask for unpublished reports, evaluations, working papers
- Document who was contacted and what was received

### Grey Literature Documentation Template

```markdown
### Grey Literature Source: [Organization Name]
- **URL**: [website URL]
- **Date searched**: [YYYY-MM-DD]
- **Search method**: [Internal search / Google site search / Browse by topic]
- **Search terms**: [terms used]
- **Results reviewed**: [n documents reviewed]
- **Included**: [n documents included]
- **Notes**: [any relevant notes about coverage or limitations]
```

---

## Search Term Banks by Domain

### Homelessness and Housing

**Population terms**: homeless*, houseless, unhoused, rough sleep*, street-involved, precariously housed, housing instability, housing insecurity, inadequately housed, couch surfing, hidden homeless*

**Intervention terms**: Housing First, rapid rehousing, transitional housing, supportive housing, emergency shelter, outreach, case management, housing subsidy, rent supplement, eviction prevention

**Canadian-specific terms**: Reaching Home, National Housing Strategy, At Home/Chez Soi, coordinated access, Built for Zero, By-Name List

### Youth Services

**Population terms**: youth, adolescent*, young adult*, emerging adult*, teen*, young people, transition-age youth, at-risk youth, street youth, system-involved youth, aging out of care, former youth in care

**Intervention terms**: youth engagement, mentoring, life skills, independent living, education support, employment training, wraparound services, developmental assets, positive youth development, youth-centered

### Mental Health

**Population terms**: mental health, mental illness, psychiatric, psychological, emotional wellbeing, mood disorder*, anxiety, depression, trauma, PTSD, psychosis, self-harm, suicid*

**Intervention terms**: counseling, therapy, psychotherapy, cognitive behavio*, CBT, DBT, peer support, recovery-oriented, trauma-informed, early intervention, crisis intervention, assertive community treatment, ACT

### Substance Use

**Population terms**: substance use, substance abuse, addiction, drug use, alcohol use, opioid*, methamphetamine, cannabis, polysubstance, problematic substance use

**Intervention terms**: harm reduction, safe consumption, supervised injection, naloxone, overdose prevention, medication-assisted treatment, MAT, OAT, detox*, residential treatment, outpatient, recovery house, sober living

### Indigenous Health and Services

**Population terms**: Indigenous, First Nations, Métis, Inuit, Aboriginal, Native, on-reserve, off-reserve, urban Indigenous

**Approach terms**: culturally safe, cultural safety, decoloniz*, self-determination, Two-Eyed Seeing, land-based, ceremony, elder*, traditional healing, Indigenous knowledge, OCAP (ownership, control, access, possession)

**Note**: Indigenous research should follow OCAP principles and respect Indigenous data sovereignty. Prioritize Indigenous-led research and community-based participatory approaches.

### Immigrant and Refugee Services

**Population terms**: immigrant*, refugee*, newcomer*, asylum seeker*, undocumented, migrant*, settlement, resettlement, temporary foreign worker, international student

**Intervention terms**: settlement services, language training, employment bridging, credential recognition, social integration, community sponsorship, pre-arrival, cultural orientation

---

## Boolean Search Construction

### Building a Search String

**Step 1**: Identify 2-4 core concepts from your research question

Example question: "What are effective interventions for homeless youth in urban settings in Canada?"

| Concept | Terms |
|---------|-------|
| Homelessness | homeless*, housing instability, street-involved, unhoused |
| Youth | youth, adolescent*, young adult*, emerging adult*, teen* |
| Interventions | intervention*, program*, service*, treatment*, support |
| Urban | urban, city, cities, metropolitan |
| Canada | Canada, Canadian, province names |

**Step 2**: Combine synonyms with OR (broadens within a concept)

**Step 3**: Combine concepts with AND (narrows across concepts)

**Step 4**: Test and refine

- Too many results? Add more concepts with AND or use more specific terms
- Too few results? Remove a concept or add more synonyms with OR
- Check first 50 results for relevance
- Verify known relevant papers appear in results

### Adapting Searches Across Databases

Different databases use different syntax. Here's the same search adapted:

**PsycINFO (Ovid):**

```text
(homeless*.mp. OR housing instability.mp. OR street-involved.mp.)
AND (youth.mp. OR adolescent*.mp. OR young adult*.mp.)
AND (intervention*.mp. OR program*.mp. OR service*.mp.)
AND (urban.mp. OR city.mp. OR metropolitan.mp.)
AND (Canada.mp. OR Canadian.mp.)
```

**PubMed:**

```text
("Homeless Persons"[MeSH] OR homeless*[tiab] OR "housing instability"[tiab])
AND ("Adolescent"[MeSH] OR "Young Adult"[MeSH] OR youth[tiab])
AND (intervention*[tiab] OR program*[tiab] OR service*[tiab])
AND (urban[tiab] OR city[tiab] OR metropolitan[tiab])
AND ("Canada"[MeSH] OR canada*[tiab])
```

**CINAHL (EBSCOhost):**

```text
(MH "Homeless Youth" OR TI homeless* OR AB homeless* OR AB "housing instability")
AND (MH "Adolescence" OR MH "Young Adult" OR TI youth OR AB "young adult*")
AND (MH "Program Evaluation" OR AB intervention* OR AB program*)
AND (AB urban OR AB city OR AB metropolitan)
AND (AB Canada OR AB Canadian)
```

**Google Scholar:**

```text
"homeless youth" OR "homeless young" intervention program urban Canada
```

(Note: Google Scholar doesn't support full Boolean — keep it simple)

---

## Quality Control

### Before Searching

- [ ] Research question clearly defined with appropriate framework (PICO/SPIDER/PICo)
- [ ] Search terms listed with synonyms for each concept
- [ ] At least 3 academic databases selected
- [ ] Grey literature sources identified (10-15 organizations minimum)
- [ ] Canadian-specific sources identified (if applicable)
- [ ] Inclusion/exclusion criteria documented
- [ ] 3-5 known relevant papers identified to test search strategy

### During Searching

- [ ] Search string tested and refined in pilot search
- [ ] Results exported with complete metadata
- [ ] All search parameters documented (database, date, string, filters, results count)
- [ ] Grey literature searches documented by organization
- [ ] Known relevant papers found in search results (validation check)

### After Searching

- [ ] All searches documented reproducibly
- [ ] Duplicates removed
- [ ] Results from all sources aggregated
- [ ] Ready for screening
