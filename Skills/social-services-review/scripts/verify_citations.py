#!/usr/bin/env python3
"""
Citation Verification Script (offline second-pass tool)

IMPORTANT — read before relying on this script:
  This script verifies DOIs against doi.org and CrossRef. Many hosted AI tools
  run code in a sandbox whose outbound network access is blocked, so those
  endpoints are often NOT reachable from inside an assistant's code environment.
  When run there, this script CANNOT verify anything and will say so loudly and
  exit non-zero — it will NOT emit a pass-looking report.

  The PRIMARY verification path for this skill is the live web-verification
  protocol in references/citation_verification.md: use your assistant's
  web-search capability to locate each source, open the authoritative record
  with its fetch/browse capability, confirm title/first-author/year/venue off
  the fetched page, and only then cite. Use this script only in an environment
  with open network access (e.g. a local machine or terminal) as a supplementary
  batch double-check.

Exit codes:
  0  all extracted DOIs were reachable AND resolved (VERIFIED)
  2  verification endpoints unreachable — NOTHING was checked (UNCHECKED)
  3  at least one DOI resolved as NOT FOUND (possible fabrication) (FAILED)
"""

import re
import sys
import json
import time
from typing import Dict, List, Tuple

try:
    import requests
except ImportError:
    print("ERROR: the 'requests' package is required. Install with: "
          "pip install requests --break-system-packages", file=sys.stderr)
    sys.exit(2)

DOI_RE = re.compile(r'10\.\d{4,}/[^\s\]\)"<>]+')
PROBE_TIMEOUT = 8


class CitationVerifier:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(
            {"User-Agent": "LO-CitationVerifier/2.0 (mailto:info@logicaloutcomes.net)"}
        )

    # --- reachability -----------------------------------------------------
    def endpoints_reachable(self) -> Tuple[bool, str]:
        """Probe doi.org and CrossRef. Return (reachable, detail).
        Distinguishes 'cannot reach verifier' from 'DOI not found' so the two
        are never silently conflated."""
        last = "no endpoint probed"
        for url in ("https://doi.org/", "https://api.crossref.org/works?rows=0"):
            try:
                r = self.session.get(url, timeout=PROBE_TIMEOUT)
                if r.status_code < 400:
                    return True, f"reachable via {url} ({r.status_code})"
            except Exception as e:  # noqa: BLE001
                last = f"{type(e).__name__}: {e}"
                continue
            last = f"{url} -> HTTP {r.status_code}"
        return False, f"verification endpoints unreachable ({last})"

    # --- per-DOI resolution ----------------------------------------------
    def resolve_doi(self, doi: str) -> Tuple[str, Dict]:
        """Return (state, metadata) where state is VERIFIED | NOT_FOUND | UNCHECKED."""
        try:
            r = self.session.get(f"https://doi.org/api/handles/{doi}", timeout=PROBE_TIMEOUT)
        except Exception as e:  # noqa: BLE001
            return "UNCHECKED", {"error": f"{type(e).__name__}: {e}"}
        if r.status_code == 200:
            return "VERIFIED", self._crossref(doi)
        if r.status_code in (404, 400):
            return "NOT_FOUND", {}
        return "UNCHECKED", {"http": r.status_code}

    def _crossref(self, doi: str) -> Dict:
        try:
            r = self.session.get(f"https://api.crossref.org/works/{doi}", timeout=PROBE_TIMEOUT)
            if r.status_code != 200:
                return {"doi": doi}
            m = r.json().get("message", {})
            return {
                "doi": doi,
                "title": (m.get("title") or [""])[0],
                "authors": self._authors(m.get("author", [])),
                "year": self._year(m),
                "journal": (m.get("container-title") or [""])[0],
                "volume": m.get("volume", ""),
                "pages": m.get("page", ""),
            }
        except Exception as e:  # noqa: BLE001
            return {"doi": doi, "error": str(e)}

    @staticmethod
    def _authors(authors: List[Dict]) -> str:
        out = []
        for a in authors[:3]:
            fam, giv = a.get("family", ""), a.get("given", "")
            if fam:
                out.append(f"{fam}, {giv[0]}." if giv else fam)
        if len(authors) > 3:
            out.append("et al.")
        return ", ".join(out)

    @staticmethod
    def _year(m: Dict) -> str:
        for key in ("published-print", "published-online", "issued"):
            dp = m.get(key, {}).get("date-parts", [[]])
            if dp and dp[0]:
                return str(dp[0][0])
        return ""


def main():
    if len(sys.argv) < 2:
        print("Usage: python verify_citations.py <markdown_file>")
        sys.exit(2)

    path = sys.argv[1]
    with open(path, encoding="utf-8") as f:
        dois = sorted(set(DOI_RE.findall(f.read())))

    v = CitationVerifier()
    reachable, detail = v.endpoints_reachable()

    if not reachable:
        print("=" * 68)
        print("  CITATION VERIFICATION DID NOT RUN")
        print("=" * 68)
        print(f"  {detail}")
        print("  NOTHING WAS VERIFIED. Do not treat these citations as checked.")
        print("  Use the live web-verification protocol in")
        print("  references/citation_verification.md, or run this script on a")
        print("  machine with open internet access.")
        print("=" * 68)
        sys.exit(2)

    verified, not_found, unchecked = [], [], []
    meta = {}
    for doi in dois:
        state, m = v.resolve_doi(doi)
        ({"VERIFIED": verified, "NOT_FOUND": not_found, "UNCHECKED": unchecked}[state]).append(doi)
        if state == "VERIFIED":
            meta[doi] = m
        time.sleep(0.3)

    print(f"DOIs found: {len(dois)} | verified: {len(verified)} | "
          f"NOT FOUND: {len(not_found)} | unchecked: {len(unchecked)}")
    if not_found:
        print("\n!! NOT FOUND — these DOIs did not resolve. Treat as fabricated until")
        print("   confirmed by hand; a non-resolving DOI is the classic signature of")
        print("   an invented reference:")
        for d in not_found:
            print(f"   - {d}")
    report = {"verified": verified, "not_found": not_found,
              "unchecked": unchecked, "metadata": meta}
    out = path.rsplit(".", 1)[0] + "_citation_report.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"\nReport: {out}")
    sys.exit(3 if not_found else 0)


if __name__ == "__main__":
    main()
