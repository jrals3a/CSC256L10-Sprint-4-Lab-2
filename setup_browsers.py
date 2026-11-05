"""
setup_browsers.py — One-time browser setup for Playwright and Robot Framework.

Run ONCE per machine after `uv sync`:

    uv run python setup_browsers.py

This is NOT needed on every sync — only on first setup or new machine.
"""

import subprocess
import sys


def main():
    print("=" * 60)
    print("Task Tracker — One-Time Browser Setup")
    print("=" * 60)
    print()

    # Step 1: Install Playwright Chromium browser binaries
    print("Step 1: Installing Playwright Chromium browser...")
    print("        (Downloads ~200MB on first run — may take a few minutes)")
    print()

    result = subprocess.run(
        [sys.executable, "-m", "playwright", "install", "chromium"],
        check=False
    )

    if result.returncode != 0:
        print("ERROR: Playwright browser install failed.")
        print("Try manually: uv run python -m playwright install chromium")
        sys.exit(1)

    print()
    print("Playwright Chromium installed.")
    print()

    # Step 2: Initialize Robot Framework Browser library
    # NOT used by this course's Robot tests — Sprint 5 uses RequestsLibrary for
    # HTTP-only API acceptance tests, never the Browser library. Initialized
    # here anyway so Browser is available if you want to explore browser-driven
    # Robot tests, or work in a non-Python stack (Java/.NET) with no
    # pytest-playwright equivalent.
    # --skip-browsers reuses the Playwright Chromium installed in Step 1 —
    # no separate download needed.
    # Note: npm warnings (EBADENGINE, vulnerabilities) are expected and harmless.
    # Do NOT run npm audit fix — it may break the rfbrowser installation.
    print("Step 2: Initializing Robot Framework Browser library...")
    print("        (Not used by this course's Robot tests — RequestsLibrary instead)")
    print("        (Reuses Playwright Chromium from Step 1 — no additional download)")
    print()

    result = subprocess.run(
        ["rfbrowser", "init", "--skip-browsers"],
        check=False
    )

    if result.returncode != 0:
        print("ERROR: rfbrowser init failed.")
        print("Try manually: uv run rfbrowser init --skip-browsers")
        sys.exit(1)

    print()
    print("=" * 60)
    print("Browser setup complete.")
    print()
    print("Playwright tests:  uv run pytest -m ui -v")
    print("Robot Framework:   uv run robot tests/acceptance/robot/")
    print()
    print("You do not need to run this script again on this machine.")
    print("=" * 60)


if __name__ == "__main__":
    main()
