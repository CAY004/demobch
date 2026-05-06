#!/usr/bin/env bash
set -euo pipefail

TARGET_REPO_URL="${1:-https://github.com/CAY004/totnghiep.git}"
TARGET_DIR="${2:-/workspace/totnghiep}"

if [ -d "$TARGET_DIR/.git" ]; then
  echo "Target already exists: $TARGET_DIR"
  exit 0
fi

echo "Cloning $TARGET_REPO_URL -> $TARGET_DIR"
git clone "$TARGET_REPO_URL" "$TARGET_DIR"

echo "Done. To switch environment manually:"
echo "cd $TARGET_DIR"
