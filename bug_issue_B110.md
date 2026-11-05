# Bug issue to file on GitHub (Phase 5, Part 4): copy-paste

**Title:** `[BUG] Silent exception handling in UI complete/delete routes (B110)`
**Labels:** `bug`, `bandit`, `low-priority`   ·   **Leave the issue open.**

**Description** (the lab's text, with the line numbers corrected to match the real bandit output):

```
## What Was Found

Bandit security scan flagged two B110 findings in app/routes/ui.py:
- Line 50: complete_task() handler — try/except/pass
- Line 59: delete_task() handler — try/except/pass

Both handlers silently catch all exceptions and redirect to the task
list without logging the error. If a task operation fails for any
reason, the failure is invisible — no log, no user feedback, no trace.

## Bandit Output

Issue: [B110:try_except_pass] Try, Except, Pass detected.
Severity: Low   Confidence: High
Location: app/routes/ui.py:50:4

Issue: [B110:try_except_pass] Try, Except, Pass detected.
Severity: Low   Confidence: High
Location: app/routes/ui.py:59:4

## Expected Behavior

Exceptions should be logged so failures are visible in development
and production. Silent failures make debugging extremely difficult.

## Acceptance Criteria

- [ ] complete_task() logs exception with task_id context
- [ ] delete_task() logs exception with task_id context
- [ ] bandit scan shows 0 B110 findings in app/routes/ui.py
- [ ] All existing tests continue to pass

## SQA Decision

Severity: Low
Priority: Low — deferred to backlog
Reason: No data loss, no crash, no security exposure. UI redirects
correctly even when the operation fails. Acceptable risk for current
sprint. Will be addressed before acceptance testing phase.
```

> The lab's description says "Line 54" and "Line 64", but its own bandit block (and the real scan on this code) says 50:4 and 59:4. I used 50 and 59. Run `uv run bandit -r app/` in your repo and use whatever line numbers it prints for you.
