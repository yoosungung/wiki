"""KM 자산 유지기간 정책이 AGENTS.md / 스킬 문서에 명시되어 있는지 검증한다."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENTS = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
LINTER_SKILL = (ROOT / ".agents/skills/km-linter/SKILL.md").read_text(encoding="utf-8")
RESEARCHER_SKILL = (ROOT / ".agents/skills/km-researcher/SKILL.md").read_text(
    encoding="utf-8"
)
DOTALL = re.DOTALL | re.IGNORECASE


class RetentionPolicyDocsTest(unittest.TestCase):
    def test_agents_documents_log_append_only(self):
        self.assertIsNotNone(
            re.search(
                r"log\.md.*(?:자동\s*삭제\s*없|append-only|누적|무기한)",
                AGENTS,
                DOTALL,
            ),
            msg="AGENTS.md에 log.md 자동 삭제 없음(누적/append-only) 정책이 있어야 함",
        )

    def test_agents_documents_daily_note_window(self):
        self.assertIsNotNone(
            re.search(
                r"데일리.*(D-0|오늘).*(D-1|어제).*(삭제|D-2)",
                AGENTS,
                DOTALL,
            ),
            msg="AGENTS.md에 데일리 노트 D-0/D-1 유지·이전 삭제 정책이 있어야 함",
        )

    def test_agents_documents_raw_cleanup(self):
        self.assertIsNotNone(
            re.search(r"raw/.*(?:합성.*삭제|삭제.*합성)", AGENTS, DOTALL),
            msg="AGENTS.md에 raw/ 합성 후 삭제 정책이 있어야 함",
        )

    def test_linter_skill_states_log_no_prune(self):
        self.assertIsNotNone(
            re.search(
                r"log\.md.*(삭제\s*하지\s*않|prune\s*하지\s*않|append|누적)",
                LINTER_SKILL,
                DOTALL,
            ),
            msg="km-linter 스킬에 log.md 비삭제(누적) 제약이 있어야 함",
        )

    def test_researcher_skill_keeps_daily_cleanup(self):
        self.assertIn("D-0", RESEARCHER_SKILL)
        self.assertIn("D-1", RESEARCHER_SKILL)
        self.assertIsNotNone(re.search(r"raw/.*삭제", RESEARCHER_SKILL, DOTALL))


if __name__ == "__main__":
    unittest.main()
