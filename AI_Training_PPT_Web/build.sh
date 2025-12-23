#!/bin/bash

# ========================================
# Cloudflare Pages Build Script
# ========================================

set -e  # 遇到错误立即退出

echo "Starting build process..."

# 尝试使用 python3,如果不存在则使用 python
if command -v python3 &> /dev/null; then
    echo "Using python3..."
    python3 tools/build.py
elif command -v python &> /dev/null; then
    echo "Using python..."
    python tools/build.py
else
    echo "Error: Python not found!"
    exit 1
fi

echo "Build completed successfully!"
