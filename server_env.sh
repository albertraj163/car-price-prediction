#!/usr/bin/env bash
export PORT="${PORT:-$(python3 -c 'from config import PORT; print(PORT)')}"
export HOST="${HOST:-$(python3 -c 'from config import HOST; print(HOST)')}"
export SERVER_IP=$(hostname -I | tr ' ' '\n' | grep '^192\.' | head -1)
if [ -z "$SERVER_IP" ]; then
  export SERVER_IP=$(hostname -I | awk '{print $1}')
fi
export APP_URL="http://${SERVER_IP}:${PORT}"
