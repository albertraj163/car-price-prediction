#!/usr/bin/env bash
# Easy GitHub push - minimum questions only

export PATH="$HOME/.local/bin:$PATH"
cd "$(dirname "$0")"

echo ""
echo "=========================================="
echo "  GitHub-ku Upload - Easy Steps"
echo "=========================================="
echo ""

if ! gh auth status >/dev/null 2>&1; then
  echo "STEP 1: Browser open aagum"
  echo "STEP 2: GitHub login pannunga"
  echo "STEP 3: Terminal la code kudukum - adha browser la paste pannunga"
  echo "STEP 4: 'Authorize' click pannunga"
  echo "STEP 5: Terminal ku vandhu Enter press pannunga"
  echo ""
  gh auth login --hostname github.com --git-protocol https --web
fi

echo ""
echo "Uploading to GitHub..."
gh repo create car-price-prediction --public --source=. --remote=origin --push 2>/dev/null || git push -u origin main

echo ""
echo "SUCCESS! Repo ready:"
gh repo view --json url -q .url 2>/dev/null || echo "https://github.com/YOUR_USERNAME/car-price-prediction"
echo ""
