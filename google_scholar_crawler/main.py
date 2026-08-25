import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from scholarly import scholarly


def normalize_scholar_id(value: str) -> str:
    value = value.strip()
    if value.startswith(("http://", "https://")):
        value = parse_qs(urlparse(value).query).get("user", [""])[0]
    if not value:
        raise ValueError(
            "GOOGLE_SCHOLAR_ID must be a Google Scholar user ID or profile URL"
        )
    return value


def main() -> None:
    scholar_id = normalize_scholar_id(os.environ["GOOGLE_SCHOLAR_ID"])
    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(
        author, sections=["basics", "indices", "counts", "publications"]
    )

    cited_by = author.get("citedby")
    if not isinstance(cited_by, int):
        raise RuntimeError("Google Scholar response did not contain a citation count")

    publications = author.get("publications", [])
    author["publications"] = {
        publication["author_pub_id"]: publication
        for publication in publications
        if publication.get("author_pub_id")
    }
    author["updated"] = datetime.now(timezone.utc).isoformat()

    results_dir = Path(__file__).resolve().parent / "results"
    results_dir.mkdir(exist_ok=True)
    with (results_dir / "gs_data.json").open("w", encoding="utf-8") as output:
        json.dump(author, output, ensure_ascii=False)

    badge_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(cited_by),
    }
    with (results_dir / "gs_data_shieldsio.json").open(
        "w", encoding="utf-8"
    ) as output:
        json.dump(badge_data, output, ensure_ascii=False)

    print(f"Fetched {cited_by} citations and {len(author['publications'])} publications")


if __name__ == "__main__":
    main()
