import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(__file__))
from vault_paths import find_vault_root


class TestVaultPaths(unittest.TestCase):
    def test_find_vault_root_from_scripts_dir(self):
        scripts_dir = os.path.dirname(os.path.abspath(__file__))
        root = find_vault_root(scripts_dir)
        self.assertTrue(os.path.isdir(os.path.join(root, "wiki")))
        self.assertTrue(os.path.isdir(os.path.join(root, ".agents")))
        self.assertTrue(os.path.isfile(os.path.join(root, "AGENTS.md")))


if __name__ == "__main__":
    unittest.main()
