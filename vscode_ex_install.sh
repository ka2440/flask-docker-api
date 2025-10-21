#!/bin/bash

# 拡張機能のIDリスト
extensions=(
    "ms-python.python"
    "ms-python.vscode-pylance"
    "ms-python.debugpy"
    "mhutchie.git-graph"
)

# 各拡張機能をインストール
for extension in "${extensions[@]}"; do
    code --install-extension $extension
done