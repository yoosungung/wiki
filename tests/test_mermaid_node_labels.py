"""Mermaid fence 안 노드 라벨 선두 `N.` / `- ` 를 금지한다.

Quartz(Mermaid11)는 따옴표 안에서도 선두 `1.` / `- item` 을 markdown list로
파싱해 `Unsupported markdown: list` 로 노드를 깨뜨릴 수 있다.
허용: `["1: …"]`, `["1\\. …"]`, `["• …"]` 등.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"

MERMAID_FENCE = re.compile(r"```mermaid\s*\n(.*?)```", re.DOTALL | re.IGNORECASE)
# square-bracket node label text (optional quotes) starting with digits+dot
LEADING_ORDERED = re.compile(r'\["?](\d+)\.')
# quoted or unquoted label text starting with markdown bullet "- "
LEADING_BULLET = re.compile(r'\["?-\s')


def _offenders() -> list[str]:
    hits: list[str] = []
    for path in sorted(WIKI.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for block in MERMAID_FENCE.findall(text):
            for rx, kind in (
                (LEADING_ORDERED, "ordered N."),
                (LEADING_BULLET, "bullet -"),
            ):
                for m in rx.finditer(block):
                    rel = path.relative_to(ROOT).as_posix()
                    snippet = block[m.start() : m.start() + 40].replace("\n", " ")
                    hits.append(f"{rel} [{kind}]: {snippet}…")
    return hits


class MermaidNodeLabelsTest(unittest.TestCase):
    def test_no_leading_list_markers_in_mermaid_labels(self):
        hits = _offenders()
        self.assertEqual(
            hits,
            [],
            msg=(
                "Mermaid 노드 라벨 선두에 N. 또는 - 금지 "
                "(대신 1: / 1\\. / • 사용). "
                f"(hits={len(hits)}):\n" + "\n".join(hits)
            ),
        )


if __name__ == "__main__":
    unittest.main()
