#!/usr/bin/env bash
source "$(dirname "$0")/server_env.sh"

if pgrep -f "gunicorn app:app" >/dev/null; then
  echo "Server is RUNNING"
  echo "Open: ${APP_URL}"
else
  echo "Server is NOT running. Start with: ./run_server.sh"
fi
