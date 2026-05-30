#!/usr/bin/env bash
# Deploy app to Hugging Face Spaces (free — GitHub Pages predict ku backend)

set -e
SPACE="albertraj163/car-price-prediction"

pip install -q huggingface_hub

if ! hf auth whoami >/dev/null 2>&1; then
  echo ""
  echo "Hugging Face login (free, one time):"
  echo "  1. https://huggingface.co/join"
  echo "  2. https://huggingface.co/settings/tokens → New token"
  echo "  3. Run: hf auth login"
  echo ""
  exit 1
fi

hf repo create "$SPACE" --type space --space_sdk docker 2>/dev/null || true

git remote remove huggingface 2>/dev/null || true
git remote add huggingface "https://huggingface.co/spaces/$SPACE"

echo "Uploading to Hugging Face..."
git push huggingface main --force

echo ""
echo "Done! Links:"
echo "  GitHub Pages: https://albertraj163.github.io/car-price-prediction/"
echo "  Live API:     https://albertraj163-car-price-prediction.hf.space"
