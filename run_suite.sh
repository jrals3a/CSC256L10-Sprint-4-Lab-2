#!/bin/bash
# usage: run_suite.sh LOGFILE [pytest args...]   (runs from task-tracker; starts Flask on 5050 because AirPlay holds 5000)
cd "$(dirname "$0")/task-tracker" || exit 1
LOG="$1"; shift; case "$LOG" in /*) ;; *) LOG="$(cd "$(dirname "$0")" && pwd)/$LOG";; esac
sed -i '' 's/127.0.0.1:5000/127.0.0.1:5050/' tests/api/test_tasks_api.py tests/api/conftest.py
(uv run flask --app app run --port 5050 >/dev/null 2>&1 &) ; 
for i in $(seq 1 30); do curl -s http://127.0.0.1:5050/api/health >/dev/null && break; sleep 1; done
uv run python -m pytest "$@" 2>&1 | tee "$LOG"
pkill -f "flask --app app run --port 5050" || true
git checkout -- tests/api
