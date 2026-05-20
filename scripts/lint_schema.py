#!/usr/bin/env python3
"""Schema lint checker for LLM Wiki pages."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

REQUIRED_FRONTMATTER = {
    "entity": ["type", "aliases", "tags", "created", "updated", "source_count"],
    "concept": ["type", "aliases", "tags", "created", "updated", "source_count"],
    "source": ["type", "source_path", "title", "author", "date", "tags", "created"],
    "synthesis": ["type", "question", "tags", "created", "updated"],
}

REQUIRED_SECTIONS = {
    "entity": [
        "## Identity",
        "## Aliases",
        "## Key Attributes",
        "## Evidence",
        "## Related",
        "## Open Questions",
    ],
    "concept": [
        "## Definition",
        "## Scope",
        "## Contrasts",
        "## Evidence",
        "## Related",
        "## Open Questions",
    ],
    "source": [
        "## Summary",
        "## Key Claims",
        "## Notable Quotes",
        "## Entities Mentioned",
        "## Concepts Mentioned",
        "## Follow-ups",
    ],
    "synthesis": [
        "## Question / Purpose",
        "## Answer / Analysis",
        "## Citations",
        "## Implications",
        "## Follow-up Questions",
    ],
}

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


@dataclass
class Issue:
    code: str
    severity: str
    file: str
    message: str

    def to_dict(self) -> dict[str, str]:
        return {
            "code": self.code,
            "severity": self.severity,
            "file": self.file,
            "message": self.message,
        }


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, text

    frontmatter_block = parts[0][4:]
    body = parts[1]
    frontmatter: dict[str, Any] = {}

    for line in frontmatter_block.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, raw_value = line.split(":", 1)
        key = key.strip()
        value = raw_value.strip()
        if value.startswith("[") and value.endswith("]"):
            items = [v.strip().strip('"\'') for v in value[1:-1].split(",") if v.strip()]
            frontmatter[key] = items
        elif value in {"[]", ""}:
            frontmatter[key] = [] if value == "[]" else ""
        else:
            frontmatter[key] = value.strip('"\'')

    return frontmatter, body


def page_name(md_file: Path) -> str:
    return md_file.stem


def wiki_content_files(root: Path) -> list[Path]:
    allowed = {"entities", "concepts", "sources", "syntheses"}
    files = []
    for path in root.rglob("*.md"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if rel.parts and rel.parts[0] in allowed:
            files.append(path)
    return files


def build_page_index(root: Path) -> set[str]:
    return {page_name(path) for path in wiki_content_files(root)}


def related_section_links(body: str) -> list[str]:
    lines = body.splitlines()
    in_related = False
    chunk: list[str] = []
    for line in lines:
        if line.startswith("## "):
            if line.strip() == "## Related":
                in_related = True
                continue
            if in_related:
                break
        if in_related:
            chunk.append(line)
    text = "\n".join(chunk)
    return [m.group(1).strip() for m in WIKILINK_RE.finditer(text)]


def check_file(md_file: Path, wiki_root: Path, known_pages: set[str]) -> list[Issue]:
    issues: list[Issue] = []
    rel = md_file.relative_to(wiki_root.parent).as_posix()
    text = md_file.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text)

    page_type = frontmatter.get("type")
    if not page_type:
        issues.append(Issue("missing_frontmatter", "high", rel, "Missing frontmatter or `type` key."))
        return issues

    if page_type not in REQUIRED_FRONTMATTER:
        issues.append(Issue("invalid_type", "high", rel, f"Unsupported type `{page_type}`."))
        return issues

    for key in REQUIRED_FRONTMATTER[page_type]:
        if key not in frontmatter:
            issues.append(Issue("missing_frontmatter_key", "high", rel, f"Missing required frontmatter key `{key}` for type `{page_type}`."))

    for section in REQUIRED_SECTIONS[page_type]:
        if section not in body:
            issues.append(Issue("missing_section", "high", rel, f"Missing required section heading `{section}` for type `{page_type}`."))

    if page_type == "source":
        source_path = str(frontmatter.get("source_path", ""))
        if not (source_path.startswith("raw/sources/") or source_path.startswith("raw/assets/")):
            issues.append(Issue("invalid_source_path", "high", rel, "`source_path` must be under `raw/sources/` or `raw/assets/`."))

    if "## Related" in body:
        links = related_section_links(body)
        if not links:
            issues.append(Issue("missing_related_links", "medium", rel, "`## Related` section has no wikilinks."))
        else:
            for link in links:
                if link not in known_pages:
                    issues.append(Issue("broken_related_link", "medium", rel, f"Related link `[[{link}]]` does not resolve to an existing page."))
    elif page_type in {"entity", "concept"}:
        issues.append(Issue("missing_related_links", "medium", rel, "Page requires a `## Related` section with at least one wikilink."))

    return issues


def lint_wiki(wiki_root: Path) -> dict[str, Any]:
    files = wiki_content_files(wiki_root)
    known_pages = build_page_index(wiki_root)
    issues: list[Issue] = []

    for md_file in sorted(files):
        issues.extend(check_file(md_file, wiki_root, known_pages))

    summary = {
        "files_scanned": len(files),
        "issues_total": len(issues),
        "high": sum(i.severity == "high" for i in issues),
        "medium": sum(i.severity == "medium" for i in issues),
        "low": sum(i.severity == "low" for i in issues),
    }

    return {"summary": summary, "issues": [i.to_dict() for i in issues]}


def print_human_report(result: dict[str, Any]) -> None:
    summary = result["summary"]
    print("Schema Lint Report")
    print("=" * 18)
    print(f"Files scanned: {summary['files_scanned']}")
    print(f"Total issues: {summary['issues_total']} (high={summary['high']}, medium={summary['medium']}, low={summary['low']})")
    print()

    if not result["issues"]:
        print("No schema issues found.")
        return

    by_file: dict[str, list[dict[str, str]]] = {}
    for issue in result["issues"]:
        by_file.setdefault(issue["file"], []).append(issue)

    for file, file_issues in by_file.items():
        print(f"- {file}")
        for issue in file_issues:
            print(f"  [{issue['severity'].upper()}] {issue['code']}: {issue['message']}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate wiki schema and produce lint reports.")
    parser.add_argument("--wiki-root", default="wiki", help="Path to wiki root directory (default: wiki)")
    parser.add_argument("--json-out", help="Write machine-readable JSON report to this path")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero when any issue is found")
    args = parser.parse_args()

    wiki_root = Path(args.wiki_root)
    if not wiki_root.exists() or not wiki_root.is_dir():
        print(f"wiki root not found: {wiki_root}")
        return 2

    result = lint_wiki(wiki_root)
    print_human_report(result)

    if args.json_out:
        out = Path(args.json_out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    if args.strict and result["summary"]["issues_total"] > 0:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
