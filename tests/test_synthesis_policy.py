"""inbox→wiki 합성 정책: 재사용 지식·일반화 제목·진행정보 제외 (#51)."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SYNTHESIZER = ROOT / ".agents" / "skills" / "km-synthesizer" / "SKILL.md"
AGENTS = ROOT / "AGENTS.md"
POLICY = (
    ROOT
    / "wiki"
    / "Engineering"
    / "AI-Native-Engineering"
    / "Wiki-Synthesis-Policy.md"
)
PLAYWRIGHT_PATTERN = (
    ROOT
    / "wiki"
    / "Engineering"
    / "AI-Native-Engineering"
    / "Playwright-Frontend-UI-Smoke-Pattern.md"
)
LEGACY_PLAYWRIGHT = (
    ROOT
    / "wiki"
    / "Engineering"
    / "AI-Native-Engineering"
    / "nl2sql-Playwright-E2E-Smoke.md"
)

# 내부 진행 로그로 보이는 패턴 (업스트림 OSS PR URL은 본 테스트 대상 아님)
INTERNAL_PROGRESS_RE = re.compile(
    r"(?i)(PR#\s*\d+|티켓\s*#\s*\d+|ticket\s*#\s*\d+|Waiting for Approval|pm-owned)",
)


class SynthesisPolicyTest(unittest.TestCase):
    def test_synthesizer_skill_has_reuse_and_exclude_rules(self):
        text = SYNTHESIZER.read_text(encoding="utf-8")
        self.assertIn("REUSABLE_KNOWLEDGE", text)
        self.assertIn("GENERALIZED_PATH", text)
        self.assertIn("EXCLUDE_PROGRESS", text)

    def test_agents_md_mentions_synthesis_policy(self):
        text = AGENTS.read_text(encoding="utf-8")
        self.assertRegex(text, r"재사용|일반화|진행\s*정보")
        self.assertIn("Wiki-Synthesis-Policy", text)

    def test_policy_wiki_page_exists(self):
        self.assertTrue(POLICY.is_file(), msg="합성 정책 canonical 페이지 필요")
        text = POLICY.read_text(encoding="utf-8")
        self.assertIn("EXCLUDE_PROGRESS", text)
        self.assertIn("GENERALIZED_PATH", text)

    def test_playwright_page_renamed_and_scrubbed(self):
        self.assertTrue(
            PLAYWRIGHT_PATTERN.is_file(),
            msg="일반화 파일명 Playwright-Frontend-UI-Smoke-Pattern.md 필요",
        )
        self.assertFalse(
            LEGACY_PLAYWRIGHT.exists(),
            msg="제품/PR 묶인 nl2sql-Playwright-E2E-Smoke.md 는 제거·이전해야 함",
        )
        text = PLAYWRIGHT_PATTERN.read_text(encoding="utf-8")
        self.assertIsNone(
            INTERNAL_PROGRESS_RE.search(text),
            msg="Playwright 패턴 노트에 내부 PR#/티켓# 진행 로그가 있으면 안 됨",
        )


if __name__ == "__main__":
    unittest.main()
