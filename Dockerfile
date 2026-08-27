# Python実行用のベースイメージ（Colab環境に合わせて 3.12.13 に固定）
FROM python:3.12.13-slim

# Pythonの出力をバッファリングせず、.pycを作らない
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# 作業ディレクトリ
WORKDIR /app

# 依存関係を先にコピーしてインストール（キャッシュ活用）
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースをコピー
COPY . .

# デフォルトの起動コマンド（必要に応じて変更）
CMD ["python"]
