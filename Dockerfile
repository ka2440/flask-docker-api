FROM python:3.12

# workspaceディレクトリ作成、移動
WORKDIR /workspace

# プロジェクトディレクトリにコピー
COPY requirements.txt /workspace

# 必要モジュールのインストール
RUN pip install --upgrade pip
RUN pip install -r requirements.txt