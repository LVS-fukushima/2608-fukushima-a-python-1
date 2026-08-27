# Python_basic_tasks

Python の基礎構文を学ぶ演習（Q1〜Q100）に取り組むためのリポジトリです。
**Python 3.12.13** の Docker 環境で実行できます。

## ディレクトリ構成

```
Python_basic_tasks/
├── Dockerfile            # Python 3.12.13 の実行環境定義
├── docker-compose.yml    # ビルド／起動をまとめて管理
├── requirements.txt      # 追加ライブラリ（現状は標準ライブラリのみで空）
├── Questions/            # 問題ファイル Q1.py 〜 Q100.py（問題文はコメントで記載）
└── static/               # Q94〜100 で使うデータ（example.txt, students.csv, sales.csv）
```

## 前提

- Docker Desktop がインストール済みであること
  - インストール方法は [こちら](https://respawn.littleheroes.jp/w/courses/596/1357) を参照してください
- 以降のコマンドはプロジェクトルート（この README がある場所）で実行します

## リポジトリの準備

### 1. リポジトリの作成

「Use this template」ボタンをクリック

<img width="676" height="98" alt="image" src="https://github.com/user-attachments/assets/50fbee88-c21f-46a4-b2ec-43422d082eac" />

「Repository name」を入力して「Create repository」ボタンをクリックして作成

リポジトリ名は [リポジトリ命名規則](https://github.com/KIR-SHARE-ISSUES/template?tab=readme-ov-file#-%E3%83%AA%E3%83%9D%E3%82%B8%E3%83%88%E3%83%AA%E5%91%BD%E5%90%8D%E8%A6%8F%E5%89%87) を参照

<img width="667" height="361" alt="image" src="https://github.com/user-attachments/assets/153f3a15-91e4-49c2-88e6-9bd5c9ceb023" />

### 2. リポジトリのクローン

Mac はターミナル、Windows は WSL ターミナルを開いて、ホームディレクトリへ移動

```bash
cd ~
```

クローン

```bash
git clone [url]
```

## 開発環境構築

### 1. クローンしたリポジトリへ移動

```bash
cd [リポジトリ名]
```

### 2. VSCode でのターミナルの開き方

以下のいずれかの方法で、VSCode 内にターミナルを開けます。

- メニューバーから **「ターミナル」→「新しいターミナル」** を選択する
- ショートカットキー **`Control` + `` ` ``（バッククォート）** を押す

開いたターミナルが `クローンしたリポジトリ` のディレクトリになっていることを確認してから、各コマンドを実行してください。
（VSCode でこのプロジェクトフォルダを開いていれば、通常はそのディレクトリでターミナルが開きます）

## Docker の起動方法

### 前提

#### コマンドの実行場所

このドキュメントに出てくる次のようなコマンドは、すべて **`リポジトリ名` ディレクトリ配下**で実行してください。

```bash
docker compose build
```

ターミナルのプロンプトが `リポジトリ名` になっている状態（例）で実行します。

```text
apple@MacBook-Pro-3 リポジトリ名 %
```

> 別のディレクトリにいる場合は `cd` で移動してください。
>
> ```bash
> cd path/to/リポジトリ名
> ```

### 1. イメージのビルド

初回、または `Dockerfile` / `requirements.txt` を変更したときに実行します。

```bash
docker compose build
```

### 2. コンテナの起動

バックグラウンドでコンテナを常駐させます。

```bash
docker compose up -d
```

> **課題に取り組んでいる間は、コンテナが常に起動している必要があります。**
> 起動したままにしておき、各問題を実行してください。

起動確認（Python バージョンが 3.12.13 であること）:

```bash
docker compose exec app python --version
# => Python 3.12.13
```

### 3. コンテナの停止

**コンテナの停止は、課題がすべて終了したときに行ってください。**
課題の途中では停止せず、起動したままにしておきます。

```bash
docker compose down
```

> カレントディレクトリを丸ごとマウントしているため、ローカルでコードを編集すれば
> 再ビルドなしにコンテナへ即反映されます。

## 課題ファイル（Q1.py〜Q100.py）

### 回答について

- 各課題ファイル（Q1.py〜Q100.py）には問題文がコメントアウトで記載されています。（必要なものはimportまで記載）
- 回答は記載されている問題文(およびimport)の下に追記して下さい。
- また、回答を記載したら後述の「実行方法」でファイルの動作が正常であることを確認して下さい。

### 実行方法

コンテナを起動した状態（`docker compose up -d` 済み）で、`docker compose exec` を使って実行します。

```bash
# 例: Q1 を実行
docker compose exec app python Questions/Q1.py

# 例: Q68 を実行
docker compose exec app python Questions/Q68.py
```

> Q90〜93 を実行すると `static/` 配下に出力ファイル
> （`fruits.txt`, `students_A.csv`, `total_sales.csv`, `static.zip`）が生成されます。

## コンテナを起動せずに単発実行する場合

`docker compose up -d` を使わず、都度使い捨てのコンテナで実行することもできます。

```bash
# 通常の問題
docker compose run --rm app python Questions/Q1.py

# Q94〜100（static を作業ディレクトリに）
docker compose run --rm --workdir /app/static app python /app/Questions/Q89.py
```
