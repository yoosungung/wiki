import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOGIC_PATH = ROOT / "quartz-plugins" / "km-sidebar" / "logic.js"
SIDEBAR_CSS = ROOT / "quartz-plugins" / "km-sidebar" / "sidebar.css"
QUARTZ_CONFIG = ROOT / "quartz.config.yaml"


def run_logic(fn, arg):
    script = f"""
import {{ {fn} }} from {json.dumps(LOGIC_PATH.as_posix())};
console.log(JSON.stringify({fn}({json.dumps(arg)})));
"""
    out = subprocess.check_output(["node", "--input-type=module", "-e", script], text=True)
    return json.loads(out)


class KmSidebarLogicTest(unittest.TestCase):
    def test_clamp_width_defaults_invalid(self):
        self.assertEqual(run_logic("clampWidth", "bad"), 320)

    def test_clamp_width_bounds(self):
        self.assertEqual(run_logic("clampWidth", 100), 240)
        self.assertEqual(run_logic("clampWidth", 999), 480)
        self.assertEqual(run_logic("clampWidth", 360), 360)

    def test_parse_stored_width(self):
        self.assertEqual(run_logic("parseStoredWidth", ""), 320)
        self.assertEqual(run_logic("parseStoredWidth", "400"), 400)
        self.assertEqual(run_logic("parseStoredWidth", "999"), 480)


class KmSidebarStyleTest(unittest.TestCase):
    def test_sidebar_css_has_ellipsis_and_width_var(self):
        css = SIDEBAR_CSS.read_text()
        self.assertIn("text-overflow: ellipsis", css)
        self.assertIn("--km-sidebar-width", css)
        self.assertIn(".km-sidebar-handle", css)


class QuartzConfigTest(unittest.TestCase):
    def test_footer_disabled_and_km_sidebar_plugin(self):
        config = QUARTZ_CONFIG.read_text()
        self.assertIn("source: ./content/quartz-plugins/km-sidebar", config)
        self.assertIn("github:quartz-community/footer", config)
        self.assertIn("enabled: false", config)
        self.assertIn("folderClickBehavior: collapse", config)

    def test_agents_md_excluded_from_publish(self):
        """루트 AGENTS.md는 git에 두되 공개 위키 페이지에서는 제외한다."""
        config = QUARTZ_CONFIG.read_text()
        # ignorePatterns 블록 안에서만 검사 (다른 경로 언급과 구분)
        start = config.index("ignorePatterns:")
        end = config.index("theme:", start)
        ignore_block = config[start:end]
        self.assertIn("AGENTS.md", ignore_block)


if __name__ == "__main__":
    unittest.main()
