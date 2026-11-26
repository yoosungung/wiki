"""org-wiki 레이아웃 계약 (INDEX.md · inbox/{agent}/ · Quartz inbox/raw 제외)."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUARTZ_CONFIG = ROOT / "quartz.config.yaml"
DEPLOY = ROOT / ".github" / "workflows" / "deploy.yml"

INBOX_AGENTS = ("pm", "km", "ta", "qa", "aa", "sw-factory", "nl2sql")


def _ignore_block(config: str) -> str:
    start = config.index("ignorePatterns:")
    end = config.index("theme:", start)
    return config[start:end]


class OrgWikiLayoutTest(unittest.TestCase):
    def test_index_md_exists_at_root(self):
        self.assertTrue(
            (ROOT / "INDEX.md").is_file(),
            msg="루트에 INDEX.md가 있어야 함 (org-knowledge wiki-layout)",
        )

    def test_inbox_agent_dirs_exist(self):
        for agent in INBOX_AGENTS:
            path = ROOT / "inbox" / agent
            self.assertTrue(
                path.is_dir(),
                msg=f"inbox/{agent}/ 디렉터리가 있어야 함",
            )

    def test_no_inbox_archived_dir(self):
        self.assertFalse(
            (ROOT / "inbox" / "_archived").exists(),
            msg="inbox/_archived/는 사용하지 않음 — promote 후 git rm",
        )

    def test_quartz_ignores_inbox_and_raw(self):
        config = QUARTZ_CONFIG.read_text(encoding="utf-8")
        ignore_block = _ignore_block(config)
        self.assertRegex(ignore_block, r"(?m)^\s*-\s+inbox\b")
        self.assertRegex(ignore_block, r"(?m)^\s*-\s+raw\b")

    def test_deploy_excludes_inbox_and_raw(self):
        deploy = DEPLOY.read_text(encoding="utf-8")
        self.assertIn("inbox", deploy)
        self.assertIn("raw", deploy)
        # Prepare Content rsync가 inbox·raw를 제외해야 함
        self.assertIsNotNone(
            re.search(r"rsync.*--exclude=['\"]?inbox", deploy, re.DOTALL),
            msg="deploy Prepare Content rsync에 --exclude=inbox 필요",
        )
        self.assertIsNotNone(
            re.search(r"rsync.*--exclude=['\"]?raw", deploy, re.DOTALL),
            msg="deploy Prepare Content rsync에 --exclude=raw 필요",
        )

    def test_wiki_frontmatter_no_column0_flow_close(self):
        """Quartz: multiline `key: [ … ]` with `]` at column 0 → deficient indentation."""
        bad_pat = re.compile(
            r"(?m)^[A-Za-z0-9_-]+:\s*\[\s*\n(?:[ \t]+.+\n)+^\]\s*$"
        )
        wiki = ROOT / "wiki"
        offenders = []
        for path in wiki.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            if not text.startswith("---"):
                continue
            end = text.find("\n---", 3)
            if end < 0:
                continue
            if bad_pat.search(text[: end + 4]):
                offenders.append(str(path.relative_to(ROOT)))
        self.assertEqual(
            offenders,
            [],
            msg="multiline flow frontmatter with column-0 `]` breaks Quartz build",
        )


if __name__ == "__main__":
    unittest.main()
