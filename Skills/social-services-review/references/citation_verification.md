# Citation Verification Protocol

This is the shared, platform-neutral verification protocol for the
social-services-review skill. Both the public and internal versions of
`SKILL.md` point here so the standard cannot drift between them. It is referenced
from Phase 6 (Citation Verification) of the review workflow.

Citation accuracy is non-negotiable. A fabricated or unverifiable reference is a
failure of the whole review, not a cosmetic defect.

## The binding rule

> **No reference appears in the output unless, in THIS working session, a live
> web retrieval returned a record whose title, first author, year, and venue
> match the citation. Anything that cannot be confirmed against a retrieved
> record is excluded, or explicitly flagged `[unverified]` — never filled in
> from the model's prior knowledge.**

The same standard applies to every statistic, percentage, and effect size: each
must trace to a retrieved source, or it is flagged `[unverified]` or omitted.

## Primary path — live web verification

This is the path that actually works inside an AI assistant. Do not delegate
verification to the bundled script as your primary check: it depends on
doi.org/CrossRef, which a hosted code sandbox usually cannot reach (see
"Optional offline second pass" below).

Your assistant almost certainly has two relevant capabilities, though the names
differ by platform — a **web-search tool** (to find a source) and a **fetch or
browse tool** (to open a specific page and read its content). The protocol uses
both. For every source you intend to cite:

1. **Search** for the source using your assistant's web-search capability.
2. **Open** an authoritative record with the fetch/browse capability — the
   DOI or publisher landing page, PubMed, the journal's own page, or (for grey
   literature) the issuing organization's own page.
3. **Read** title, authors, year, venue, and identifier *off the opened page* —
   not from the model's memory. Build the reference from that metadata.
4. If any field can't be confirmed, re-search or drop the source. A DOI that
   does not resolve is the classic signature of a fabricated reference — drop it.
5. Apply the same standard to every figure you cite.

If your assistant has no web access at all, you cannot verify citations in the
session. In that case, either (a) supply sources yourself and have the assistant
synthesize only from what you provide, or (b) run the review without inline
references and verify every citation by hand before the report is used.

## Provenance table (required)

Append a short appendix mapping each reference to the exact URL opened and a
confirmed/flagged status, so the work can be audited:

```markdown
| # | Reference (short) | URL opened | Confirmed |
|---|-------------------|------------|-----------|
| 1 | Thurber et al. (2007) | https://doi.org/10.1007/s10964-006-9142-6 | yes |
```

## Grey literature and URLs

Confirm each URL resolves and record an access date. Archive important pages via
web.archive.org if link rot is a concern. Grey-literature references need:
Author/Organization, Year, Title, Publisher/Organization, URL.

## Optional offline second pass

On a machine with open internet access (a local terminal, not a network-blocked
AI sandbox), `python scripts/verify_citations.py my_review.md` can batch-check
DOIs against CrossRef. It fails loud and exits non-zero when it cannot reach the
verifier, and flags non-resolving DOIs separately from unchecked ones — it never
reports success it did not earn. It is a supplement to, not a replacement for,
the live protocol above.

## Citation formatting

Format citations consistently. APA 7th is the social-sciences default; see
`references/citation_styles.md`.
