#!/usr/bin/env bash
if pgrep -f "gunicorn app:app" >/dev/null; then
  echo "Server is RUNNING on port 5050"
  pgrep -af "gunicorn app:app"
else
  echo "Server is NOT running. Start with: ./run_server.sh"
fi
