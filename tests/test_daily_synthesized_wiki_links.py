"""데일리 노트 SYNTHESIZED_WIKI 항목은 클릭 가능한 [[wiki/...]] 링크여야 한다."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DAILY_NOTE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}\.md$")
# SYNTHESIZED_WIKI 블록: 헤더 다음 bullet들 (다음 **KEY** 또는 EOF까지)
SYNTH_BLOCK_RE = re.compile(
    r"-\s*\*\*SYNTHESIZED_WIKI[^*]*\*\*[^\n]*\n((?:[ \t]+-[^\n]*\n)*)",
    re.MULTILINE,
)
WIKI_LINK_RE = re.compile(r"\[\[wiki/[^\]]+\]\]")
BACKTICK_WIKI_RE = re.compile(r"`wiki/[^`]+`")


def daily_notes():
    return sorted(p for p in ROOT.glob("????-??-??.md") if DAILY_NOTE_RE.match(p.name))


def synthesized_blocks(text: str) -> list[str]:
    return [m.group(1) for m in SYNTH_BLOCK_RE.finditer(text)]


class DailySynthesizedWikiLinksTest(unittest.TestCase):
    def test_daily_notes_exist(self):
        self.assertTrue(daily_notes(), "루트에 YYYY-MM-DD.md 데일리 노트가 있어야 함")

    def test_synthesized_wiki_uses_wikilinks_not_backticks(self):
        for note in daily_notes():
            text = note.read_text(encoding="utf-8")
            blocks = synthesized_blocks(text)
            self.assertTrue(
                blocks,
                f"{note.name}: SYNTHESIZED_WIKI 블록이 없음",
            )
            for block in blocks:
                self.assertFalse(
                    BACKTICK_WIKI_RE.search(block),
                    f"{note.name}: SYNTHESIZED_WIKI에 backtick wiki 경로가 남아 있음:\n{block}",
                )
                # 경로성 bullet( wiki/ 를 언급하는 줄)은 [[wiki/...]] 이어야 함
                path_lines = [
                    ln
                    for ln in block.splitlines()
                    if "wiki/" in ln or WIKI_LINK_RE.search(ln)
                ]
                self.assertTrue(
                    path_lines,
                    f"{note.name}: SYNTHESIZED_WIKI에 wiki 경로/링크가 없음:\n{block}",
                )
                for ln in path_lines:
                    self.assertTrue(
                        WIKI_LINK_RE.search(ln),
                        f"{note.name}: wiki 경로가 [[wiki/...]] 링크가 아님: {ln.strip()}",
                    )

    def test_synthesized_wiki_links_resolve(self):
        for note in daily_notes():
            text = note.read_text(encoding="utf-8")
            for block in synthesized_blocks(text):
                for m in WIKI_LINK_RE.finditer(block):
                    target = m.group(0)[2:-2]  # strip [[ ]]
                    # alias 지원: path|alias
                    path = target.split("|", 1)[0].strip()
                    self.assertTrue(
                        (ROOT / path).is_file(),
                        f"{note.name}: 깨진 링크 {m.group(0)} → {path}",
                    )


if __name__ == "__main__":
    unittest.main()
