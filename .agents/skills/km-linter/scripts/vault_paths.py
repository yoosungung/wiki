"""Vault root detection for KM scripts."""
import os


def find_vault_root(start: str | None = None) -> str:
    """Walk up from *start* (or this file) to find the repo/vault root."""
    path = os.path.abspath(start or os.path.dirname(__file__))
    for _ in range(12):
        if os.path.isdir(os.path.join(path, "wiki")) and os.path.isdir(
            os.path.join(path, ".agents")
        ):
            return path
        parent = os.path.dirname(path)
        if parent == path:
            break
        path = parent
    raise RuntimeError("Could not find vault root (expected wiki/ and .agents/)")
