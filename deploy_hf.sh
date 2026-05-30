#!/usr/bin/env bash
# Deploy app to Hugging Face Spaces (free live link for GitHub Pages)

set -e
export PATH="$HOME/.local/bin:$PATH"
SPACE="albertraj163/car-price-prediction"

pip install -q huggingface_hub

if ! huggingface-cli whoami >/dev/null 2>&1; then
  echo "Hugging Face login required (free):"
  echo "  1. https://huggingface.co/join — account create"
  echo "  2. https://huggingface.co/settings/tokens — token create"
  echo "  3. Run: huggingface-cli login"
  exit 1
fi

huggingface-cli repo create car-price-prediction --type space --space_sdk docker 2>/dev/null || true

git remote remove huggingface 2>/dev/null || true
git remote add huggingface "https://huggingface.co/spaces/$SPACE"

echo "Pushing to Hugging Face Space..."
git push huggingface main --force

echo ""
echo "Live app (GitHub Pages backend):"
echo "  https://albertraj163-car-price-prediction.hf.space"
echo ""
echo "GitHub Pages (after deploy):"
echo "  https://albertraj163.github.io/car-price-prediction/"
