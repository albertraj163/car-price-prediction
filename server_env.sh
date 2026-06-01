#!/usr/bin/env bash
export PORT="${PORT:-5554}"
export HOST="${HOST:-0.0.0.0}"
export SERVER_IP=$(hostname -I | tr ' ' '\n' | grep '^192\.' | head -1)
if [ -z "$SERVER_IP" ]; then
  export SERVER_IP=$(hostname -I | awk '{print $1}')
fi
