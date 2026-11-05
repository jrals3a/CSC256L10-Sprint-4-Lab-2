# S4_2 Lab: Database Layer and Web UI (verified solution)

Every phase was built in `task-tracker/` and tested for real, starting from the instructor's S4_2 starter.
Final state on `main`: **74 tests passing · 85% coverage · `mypy app/` clean · `ruff check .` clean · bandit: exactly the 2 expected B110 findings**.

Branches (one commit per lab step, with the lab's commit messages):

| Branch | Lab phase |
|---|---|
| `feature/rf011-database-repository` | 2: `SQLAlchemyTask`, `DatabaseTaskRepository`, `create_app(use_db=True, config=)`, `tasks.db` in `.gitignore`, 10 DB contract tests, `db_client` fixture |
| `feature/us012-web-ui` | 3: `base.html`, `add_task.html`, `task_list.html`, `style.css`, `ui.py` Blueprint, registration, `test_app_factory.py` |

The `Merge …` commits are a **local simulation** of the PR merges. Nothing was pushed, there are no PRs or issues on GitHub, and I took no screenshots for you.

## What's in this folder

- `task-tracker/`: the finished repo, with `images/s4/kahsai-S4_2-screenshots.md` (template; name and date filled in, repo URL and screenshots are yours).
- `evidence/`: raw pytest/bandit output from my runs, named after the screenshots they match (for checking your own results).
- `bug_issue_B110.md`: the bug issue text, ready to paste (see discrepancy 4).
- `run_suite.sh`: the helper I used to run the suite with the Flask server (see discrepancy 1).

## Test progression

| Step | Result |
|---|---|
| Baseline (Phase 1, Screenshot 10) | 64 passed |
| DB contract tests (Screenshot 11) | 10 passed |
| After the DB layer (Screenshot 12) | 74 passed |
| After the UI Blueprint (Screenshot 13) | 74 passed (`test_app_factory.py` replaced, same test count) |
| Coverage (Screenshot 19) | 85%; `app/routes/ui.py` is only 37% (only the home redirect is unit-tested; the rest is the manual US033 check) |
| Bandit (Screenshot 21) | 2 × B110 Low/High at `app/routes/ui.py:50:4` and `:59:4`; nothing else |

## Manual UI check (Phase 4 / US033): I ran this in the browser pane

I added Buy groceries, Study for exam and Call dentist; submitted an empty title and got "Title is required."; clicked Complete on Buy groceries and saw strikethrough with the Complete button gone; clicked Delete on Study for exam and it disappeared. All as the lab describes.
The screenshots must still come from **your** browser on `http://127.0.0.1:5000`, because they're your acceptance evidence for US033.
Cosmetic: the lab's CSS puts each Complete/Delete button in its own light-gray padded box (the `form` style hits the inline forms). That is how the lab's code looks. It isn't a bug in your copy.

## Screenshot map: commands for YOU in your own terminal (project root)

| # | File | When / command | You should see |
|---|---|---|---|
| 10 | `10_s4_2_start.png` | Phase 1, server running in Terminal 1: `uv run python -m pytest -v` | 64 passed, **0 skipped** |
| 11 | `11_db_contract_tests_green.png` | `uv run python -m pytest tests/repositories/test_database_task_repository.py -v` | 10 passed |
| 12 | `12_full_suite_after_db.png` | `uv run python -m pytest -v` (after Part 4, before conftest, same count after) | 74 passed |
| 13 | `13_full_suite_after_ui.png` | `uv run python -m pytest -v` | 74 passed |
| 14–18 | `14_ui_add_task_form.png`, `15_ui_task_list.png`, `16_ui_validation_error.png`, `17_ui_task_completed.png`, `18_ui_task_deleted.png` | Phase 4 steps 2–6, in the browser | Add form; 3 tasks; "Title is required."; strikethrough with no Complete button; list without Study for exam |
| 19 | `19_full_coverage.png` | `uv run python -m pytest --cov=app --cov-report=term-missing -v` | 85% |
| 20 | `20_coverage_html.png` | `… --cov-report=html -v`, open `htmlcov/index.html` | per-file table |
| 21 | `21_bandit_findings.png` | `uv run bandit -r app/` | 2 × B110 (Low severity, High confidence) |
| 22 | `22_bug_issue_filed.png` | GitHub: file the issue from `bug_issue_B110.md` | the issue, open, with 3 labels |

## Discrepancies I found

1. **Port 5000 / macOS AirPlay (important for you).** Control Center's AirPlay Receiver holds port 5000 and answers `403`, so on your Mac `uv run python -m app` can't serve on 5000, the 3 E2E tests **fail** instead of skipping, and the browser steps would show a 403. Fix: System Settings → General → AirDrop & Handoff → turn **AirPlay Receiver** off. I verified everything on port 5050 instead, with the E2E URLs temporarily swapped and restored (`git checkout`). The final files use 5000, as the lab says.
2. **Screenshot 12 timing.** After Part 4 the suite is already 74 passed; Part 5 only adds a fixture, so the count doesn't change.
3. **`db_client` is never used.** The lab adds the `db_client` fixture but no test uses it, so the `use_db=True` branch of `create_app()` is covered only through the contract tests, not through the app. I did check by hand that `create_app(use_db=True, config={"DATABASE_URL": "sqlite:///:memory:"})` wires `DatabaseTaskRepository`.
4. **Bug-issue line numbers.** The lab's issue text says "Line 54" and "Line 64", but its own bandit block says `50:4` and `59:4`, and the real scan agrees with the latter. `bug_issue_B110.md` uses 50 and 59.
5. **The UI runs on the file backend.** `python -m app` calls `create_app()` with no arguments, so the browser UI uses `tasks.json`, not the SQLite database. `use_db=True` is wired and tested, but nothing starts the app that way yet. That is also how the lab is written.
6. **Docs say "Sprint plan frozen".** Not touched here. The S4_2 agile docs are in `L10 S4_2 Assignment`.

## Your GitHub Desktop / GitHub.com part (same boundary as every lab)

- Create each branch from `main`, commit (messages are in `git log`), publish, open the PRs with the titles in the lab, and use `Closes #N` with your RF011 / US012 / US036 issue numbers. Merge, **do not click Delete branch**.
- File the bug issue (labels `bug`, `bandit`, `low-priority`) and **leave it open**.
- Export `kahsai-S4_2-screenshots.md` to PDF as `kahsai-S4_2-screenshots.pdf` and submit it on Blackboard under **S4_2 Lab**. The S4_2 Agile Documentation assignment and the Reflection are separate.
