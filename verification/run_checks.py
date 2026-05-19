#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTATION_FILES = [
    ROOT / "verification" / "ingest-fixture.expect.json",
    ROOT / "verification" / "query-fixture.expect.json",
    ROOT / "verification" / "lint-fixture.expect.json",
]


def read_text(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def extract_wikilinks(text: str):
    return re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", text)


def run_check(check: dict):
    content = read_text(check["file"])
    ctype = check["type"]

    if ctype == "contains":
        ok = check["pattern"] in content
    elif ctype == "contains_all":
        ok = all(p in content for p in check["patterns"])
    elif ctype == "regex":
        ok = re.search(check["pattern"], content) is not None
    elif ctype == "wikilinks_known":
        links = extract_wikilinks(content)
        allowed = set(check["known_pages"])
        ok = len(links) > 0 and all(link in allowed for link in links)
    else:
        return False, f"unsupported check type: {ctype}"

    if ok:
        return True, "ok"
    return False, check.get("failure_message", "expectation not met")


def main():
    total = 0
    failed = 0

    for expect_file in EXPECTATION_FILES:
        spec = json.loads(expect_file.read_text(encoding="utf-8"))
        print(f"\n== {spec['name']} ==")
        for check in spec["checks"]:
            total += 1
            ok, detail = run_check(check)
            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {check['id']}: {check['description']} ({detail})")
            if not ok:
                failed += 1

    print(f"\nSummary: {total - failed}/{total} passed")
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
