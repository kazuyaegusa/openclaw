# OpenClaw 環境セットアップガイド

別のデバイスで OpenClaw の開発・運用環境を再現するための手順書。

---

## 1. 前提条件

| ツール | バージョン | インストール |
|--------|-----------|-------------|
| Node.js | >= 22.x | `brew install node@22` or [nvm](https://github.com/nvm-sh/nvm) |
| pnpm | >= 10.x | `npm install -g pnpm` |
| npm | >= 10.x | Node.js に同梱 |
| Git | latest | `brew install git` |
| GitHub CLI | latest | `brew install gh` |
| Claude Code CLI | latest | `npm install -g @anthropic-ai/claude-code` |

Claude Code CLI はタスク実行の中核。`claude --version` で動作確認すること。

---

## 2. アーキテクチャ概要

```
┌─────────────────┐     ┌──────────────────────┐     ┌──────────────┐
│  mission-control │────▶│    Convex Cloud       │◀────│  orchestrator│
│  (Next.js:3000)  │     │  (リアルタイムDB/API)   │     │  (Express:3200)│
└─────────────────┘     └──────────────────────┘     └──────┬───────┘
                                                            │
                                                     ┌──────▼───────┐
                                                     │ Claude Code   │
                                                     │ CLI × 3並行    │
                                                     └──────────────┘
```

- **mission-control**: 管理ダッシュボード（タスクボード、承認、コンテキスト受信箱）
- **Convex Cloud**: リアルタイムデータベース + サーバーレスバックエンド
- **orchestrator**: 承認済みタスクをポーリングし、Claude Code CLI で並行実行（最大3件）
- **Linear**: タスクの双方向同期

---

## 3. リポジトリ取得

```bash
# 作業ディレクトリ
mkdir -p ~/KEWORK && cd ~/KEWORK

# OpenClaw メタリポジトリ（このガイドが入っているリポジトリ）
# ※ git init されていない場合は個別にクローン

# mission-control
git clone https://github.com/kazuyaegusa/mission-control.git OpenClaw/mission-control

# orchestrator
git clone https://github.com/kazuyaegusa/openclaw-orchestrator.git OpenClaw/orchestrator
```

---

## 4. 環境変数の設定

### 4.1 mission-control

```bash
cd ~/KEWORK/OpenClaw/mission-control
cp .env.local.example .env.local  # なければ手動作成
```

`.env.local` に以下を設定:

```env
# Convex（npx convex dev 初回実行時に自動設定される）
CONVEX_DEPLOYMENT=dev:rugged-rabbit-145
NEXT_PUBLIC_CONVEX_URL=https://rugged-rabbit-145.convex.cloud
NEXT_PUBLIC_CONVEX_SITE_URL=https://rugged-rabbit-145.convex.site

# Orchestrator 連携
ORCHESTRATOR_URL=http://localhost:3200
ORCHESTRATOR_API_KEY=<orchestrator と同じキーを設定>

# Linear（オプション）
LINEAR_API_KEY=<Linear OAuth トークン>
LINEAR_TEAM_ID=<Linear チーム ID>
```

### 4.2 orchestrator

```bash
cd ~/KEWORK/OpenClaw/orchestrator
cp .env.example .env
```

`.env` に以下を設定:

```env
PORT=3200

# Convex（mission-control と同じプロジェクト）
CONVEX_URL=https://rugged-rabbit-145.convex.cloud

# Linear
LINEAR_ACCESS_TOKEN=<Linear API トークン>
LINEAR_TEAM_ID=<Linear チーム ID>

# Claude Code CLI
CLAUDE_BIN=claude
DEFAULT_REPO_PATH=~/KEWORK

# プロジェクト→リポジトリ マッピング
MAPPING_FILE_PATH=<パス（任意）>

# API 認証キー（mission-control と一致させる）
ORCHESTRATOR_API_KEY=<ランダム生成した 64 文字 hex>

# JWT（オプション）
JWT_SECRET=<ランダム文字列>

# 並行タスク実行数（デフォルト: 3）
MAX_CONCURRENT_TASKS=3
```

**API キー生成例:**
```bash
openssl rand -hex 32
```

### 4.3 Convex 環境変数（サーバーサイド）

Convex ダッシュボード（https://dashboard.convex.dev）で以下を設定:

| 変数名 | 用途 |
|--------|------|
| `ORCHESTRATOR_API_KEY` | orchestrator からのリクエスト認証 |
| `LINEAR_API_KEY` | Linear API 連携 |
| `LINEAR_TEAM_ID` | Linear チーム ID |
| `ANTHROPIC_API_KEY` | Claude API（Convex 内 AI 処理用） |

---

## 5. 依存関係インストール

```bash
# mission-control
cd ~/KEWORK/OpenClaw/mission-control
pnpm install

# orchestrator
cd ~/KEWORK/OpenClaw/orchestrator
npm install
```

---

## 6. 起動

### 6.1 mission-control（ターミナル 1）

```bash
cd ~/KEWORK/OpenClaw/mission-control
npx convex dev    # Convex バックエンド（自動デプロイ）
```

### 6.2 mission-control フロントエンド（ターミナル 2）

```bash
cd ~/KEWORK/OpenClaw/mission-control
pnpm dev          # Next.js → http://localhost:3000
```

### 6.3 orchestrator（ターミナル 3）

```bash
cd ~/KEWORK/OpenClaw/orchestrator
npm run dev       # tsx watch → http://localhost:3200
```

**バックグラウンド起動（推奨）:**
```bash
cd ~/KEWORK/OpenClaw/orchestrator
nohup npx tsx watch src/index.ts > /tmp/orchestrator.log 2>&1 &
```

ログ確認: `tail -f /tmp/orchestrator.log`

---

## 7. 動作確認

### 7.1 Orchestrator 疎通

```bash
curl -s http://localhost:3200/status | jq .
```

### 7.2 Convex 接続

mission-control の画面（http://localhost:3000）でタスクボードが表示されればOK。

### 7.3 並行実行確認

1. ダッシュボードからタスクを複数件承認
2. `tail -f /tmp/orchestrator.log` でログを監視
3. 「タスク実行開始 ... (実行中: N/3)」が複数件同時に出ればOK

---

## 8. 主要設定リファレンス

### 並行タスク実行

| 設定 | ファイル | デフォルト |
|------|---------|-----------|
| `MAX_CONCURRENT_TASKS` | `orchestrator/.env` | 3 |

- `TaskPoller` が10秒間隔でポーリングし、空きスロット分だけタスクをclaim
- Claude Code CLI を子プロセスとして並行起動

### ポーリング間隔

`orchestrator/src/services/task-poller.ts` の `POLL_INTERVAL_MS`（デフォルト: 10000ms）

### Claude Code CLI タイムアウト

`orchestrator/src/claude/executor.ts` の `PROMPT_TIMEOUT_MS`（デフォルト: 30分）

---

## 9. トラブルシューティング

| 症状 | 原因 | 対処 |
|------|------|------|
| ポート 3200 が使用中 | 旧プロセスが残留 | `lsof -ti :3200 \| xargs kill` |
| タスクが In Progress にならない | orchestrator が旧コードで起動 | プロセスを再起動 |
| Convex 接続エラー | 環境変数未設定 or Convex dev 未起動 | `.env.local` を確認し `npx convex dev` を起動 |
| Claude CLI タイムアウト | 30分超のタスク | タスクを分割するか `PROMPT_TIMEOUT_MS` を変更 |
| `EADDRINUSE` エラー | ポート競合 | 該当ポートのプロセスを kill |

---

## 10. 技術スタック一覧

| カテゴリ | 技術 |
|----------|------|
| フロントエンド | Next.js 16 / React 19 / Tailwind CSS 4 / shadcn/ui |
| リアルタイム DB | Convex Cloud |
| バックエンド | Express.js (TypeScript) |
| AI 実行 | Claude Code CLI (Sonnet) |
| タスク管理 | Linear (双方向同期) |
| パッケージ管理 | pnpm (mission-control) / npm (orchestrator) |
| 開発ツール | tsx (TypeScript 実行) / Vitest (テスト) |
| 言語 | TypeScript |
