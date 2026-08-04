"""Mermaid 노드 라벨 선두 `N.` 이 markdown list로 오인되지 않게 따옴표로 감싼다.

Quartz(Mermaid)에서 unquoted `[1. …]` → `Unsupported markdown: list` 렌더 깨짐.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"

MERMAID_FENCE = re.compile(r"```mermaid\s*\n(.*?)```", re.DOTALL | re.IGNORECASE)
# square-bracket node text starting with digits+dot, not preceded by a quote
UNQUOTED_ORDERED_LABEL = re.compile(r'(?<!")\[(\d+)\.')


def _offenders() -> list[str]:
    hits: list[str] = []
    for path in sorted(WIKI.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for block in MERMAID_FENCE.findall(text):
            for m in UNQUOTED_ORDERED_LABEL.finditer(block):
                rel = path.relative_to(ROOT).as_posix()
                snippet = block[m.start() : m.start() + 40].replace("\n", " ")
                hits.append(f"{rel}: {snippet}…")
    return hits


class MermaidNodeLabelsTest(unittest.TestCase):
    def test_no_unquoted_ordered_list_labels_in_mermaid(self):
        hits = _offenders()
        self.assertEqual(
            hits,
            [],
            msg=(
                "Mermaid 노드 라벨 선두 N. 은 [\"N. …\"] 처럼 따옴표로 감싸야 함 "
                f"(hits={len(hits)}):\n" + "\n".join(hits)
            ),
        )


if __name__ == "__main__":
    unittest.main()
