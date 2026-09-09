#!/usr/bin/env python3
"""Grade which skill description should win. No live Claude / MCP."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SKILLS = ROOT / "skills"
FIXTURES = HERE / "fixtures" / "triggers.json"
STOP = frozenset(
    {
        "the",
        "and",
        "for",
        "use",
        "when",
        "with",
        "from",
        "this",
        "that",
        "not",
        "load",
        "or",
        "a",
        "an",
        "to",
        "of",
        "on",
        "in",
        "is",
        "do",
        "via",
    }
)
TOKEN = re.compile(r"[a-z0-9][a-z0-9_./:-]{1,}", re.I)
FRONT = re.compile(r"^---\s*\n(.*?)\n---", re.S)
DESC = re.compile(r"^description:\s*>\s*\n((?:  .*\n)+)", re.M)


def description(skill: str) -> str:
    text = (SKILLS / skill / "SKILL.md").read_text(encoding="utf-8")
    block = FRONT.search(text)
    if not block:
        return ""
    match = DESC.search(block.group(1) + "\n")
    if not match:
        return ""
    return " ".join(line.strip() for line in match.group(1).splitlines())


def tokens(text: str) -> set[str]:
    out = set()
    for raw in TOKEN.findall(text.lower()):
        if raw in STOP or len(raw) < 3:
            continue
        out.add(raw)
        if raw.startswith("blazium-"):
            out.add(raw.removeprefix("blazium-"))
    return out


def score(prompt: str, desc: str) -> int:
    p = tokens(prompt)
    d = tokens(desc)
    overlap = len(p & d)
    bonus = 0
    for needle in (
        "6506",
        "6507",
        "6508",
        "39218",
        "justamcp",
        "user-blazium-mcp",
        "user-blazium-game",
        "res://mcp",
        "mcp.blazium.games",
        "hub-remote",
        "blazium-cli",
        "toolchain",
        "project.blazium",
        "packedscene",
        "autoload",
        "n64",
        "doctor",
    ):
        if needle in prompt.lower() and needle in desc.lower():
            bonus += 4
    return overlap + bonus


def main() -> int:
    data = json.loads(FIXTURES.read_text(encoding="utf-8"))
    default_catalog = data["catalog"]
    failures = 0
    for case in data["cases"]:
        catalog = case.get("catalog") or default_catalog
        expected = case["expected"]
        needed = set(catalog) | {expected} | set(case.get("not") or [])
        missing = [name for name in needed if not (SKILLS / name / "SKILL.md").is_file()]
        if missing:
            print(f"FAIL {case['id']}: missing skills {missing}", file=sys.stderr)
            failures += 1
            continue
        ranked = sorted(
            ((score(case["prompt"], description(name)), name) for name in catalog),
            reverse=True,
        )
        winner = ranked[0][1]
        denied = case.get("not") or []
        if winner != expected:
            print(
                f"FAIL {case['id']}: expected {expected}, winner {winner} {ranked[:3]}",
                file=sys.stderr,
            )
            failures += 1
            continue
        expected_score = next(s for s, n in ranked if n == expected)
        bad = [name for name in denied if name in catalog and score(case["prompt"], description(name)) >= expected_score]
        if bad:
            print(f"FAIL {case['id']}: {bad} tied or beat {expected}", file=sys.stderr)
            failures += 1
            continue
        print(f"ok {case['id']} -> {expected}")
    if failures:
        print(f"{failures} trigger smoke failure(s)", file=sys.stderr)
        return 1
    print(f"passed {len(data['cases'])} trigger smoke case(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
