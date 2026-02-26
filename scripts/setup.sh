#!/usr/bin/env bash
set -euo pipefail

# OpenClaw 環境セットアップスクリプト
# 使い方: bash scripts/setup.sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

info()  { echo -e "${GREEN}[INFO]${NC} $*"; }
warn()  { echo -e "${YELLOW}[WARN]${NC} $*"; }
error() { echo -e "${RED}[ERROR]${NC} $*"; exit 1; }

# ──────────────────────────────────────────────
# 1. 前提条件チェック
# ──────────────────────────────────────────────
info "前提条件を確認中..."

check_cmd() {
  if ! command -v "$1" &>/dev/null; then
    error "$1 が見つかりません。インストールしてください: $2"
  fi
  info "  $1 ... OK ($(${3:-$1 --version} 2>/dev/null | head -1))"
}

check_cmd node "brew install node@22" "node -v"
check_cmd npm "Node.js に同梱" "npm -v"
check_cmd git "brew install git" "git --version"

# Node.js バージョンチェック (>= 22)
NODE_MAJOR=$(node -v | sed 's/v//' | cut -d. -f1)
if [ "$NODE_MAJOR" -lt 22 ]; then
  error "Node.js 22 以上が必要です（現在: $(node -v)）"
fi

# pnpm
if ! command -v pnpm &>/dev/null; then
  warn "pnpm が見つかりません。インストールします..."
  npm install -g pnpm
fi
info "  pnpm ... OK ($(pnpm -v))"

# Claude Code CLI（オプション）
if command -v claude &>/dev/null; then
  info "  claude ... OK ($(claude --version 2>/dev/null | head -1))"
else
  warn "Claude Code CLI が見つかりません。タスク実行には必要です。"
  warn "  インストール: npm install -g @anthropic-ai/claude-code"
fi

# gh CLI（オプション）
if command -v gh &>/dev/null; then
  info "  gh ... OK"
else
  warn "GitHub CLI (gh) が見つかりません: brew install gh"
fi

echo ""

# ──────────────────────────────────────────────
# 2. リポジトリ取得
# ──────────────────────────────────────────────
info "リポジトリを確認中..."

clone_if_missing() {
  local dir="$1" repo="$2"
  if [ -d "$dir/.git" ]; then
    info "  $dir ... 既にクローン済み"
  elif [ -d "$dir" ]; then
    warn "  $dir は存在しますが git リポジトリではありません。スキップ。"
  else
    info "  $dir をクローン中..."
    git clone "$repo" "$dir"
  fi
}

clone_if_missing "$PROJECT_ROOT/mission-control" "https://github.com/kazuyaegusa/mission-control.git"
clone_if_missing "$PROJECT_ROOT/orchestrator" "https://github.com/kazuyaegusa/openclaw-orchestrator.git"

echo ""

# ──────────────────────────────────────────────
# 3. 依存関係インストール
# ──────────────────────────────────────────────
info "依存関係をインストール中..."

if [ -d "$PROJECT_ROOT/mission-control" ]; then
  info "  mission-control (pnpm install)..."
  (cd "$PROJECT_ROOT/mission-control" && pnpm install --frozen-lockfile 2>/dev/null || pnpm install)
fi

if [ -d "$PROJECT_ROOT/orchestrator" ]; then
  info "  orchestrator (npm install)..."
  (cd "$PROJECT_ROOT/orchestrator" && npm install)
fi

echo ""

# ──────────────────────────────────────────────
# 4. 環境変数テンプレート生成
# ──────────────────────────────────────────────
info "環境変数ファイルを確認中..."

# orchestrator/.env
if [ ! -f "$PROJECT_ROOT/orchestrator/.env" ]; then
  if [ -f "$PROJECT_ROOT/orchestrator/.env.example" ]; then
    cp "$PROJECT_ROOT/orchestrator/.env.example" "$PROJECT_ROOT/orchestrator/.env"
    info "  orchestrator/.env を .env.example からコピーしました"
    warn "  → orchestrator/.env を編集して実際の値を設定してください"
  fi
else
  info "  orchestrator/.env ... 既に存在"
fi

# mission-control/.env.local
if [ ! -f "$PROJECT_ROOT/mission-control/.env.local" ]; then
  cat > "$PROJECT_ROOT/mission-control/.env.local" <<'ENVEOF'
# Convex（npx convex dev 初回実行時に設定される）
# CONVEX_DEPLOYMENT=dev:your-project-id
# NEXT_PUBLIC_CONVEX_URL=https://your-project-id.convex.cloud
# NEXT_PUBLIC_CONVEX_SITE_URL=https://your-project-id.convex.site

# Orchestrator
ORCHESTRATOR_URL=http://localhost:3200
ORCHESTRATOR_API_KEY=changeme

# Linear（オプション）
# LINEAR_API_KEY=
# LINEAR_TEAM_ID=
ENVEOF
  info "  mission-control/.env.local を生成しました"
  warn "  → mission-control/.env.local を編集して実際の値を設定してください"
else
  info "  mission-control/.env.local ... 既に存在"
fi

echo ""

# ──────────────────────────────────────────────
# 5. TypeScript ビルド確認
# ──────────────────────────────────────────────
info "TypeScript 型チェック..."

if [ -d "$PROJECT_ROOT/orchestrator" ]; then
  (cd "$PROJECT_ROOT/orchestrator" && npx tsc --noEmit 2>/dev/null) && \
    info "  orchestrator ... OK" || \
    warn "  orchestrator 型チェック失敗（環境変数未設定の可能性あり）"
fi

echo ""

# ──────────────────────────────────────────────
# 6. 完了
# ──────────────────────────────────────────────
info "セットアップ完了！"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  次のステップ:"
echo ""
echo "  1. 環境変数を設定:"
echo "     - orchestrator/.env"
echo "     - mission-control/.env.local"
echo "     - Convex ダッシュボード (https://dashboard.convex.dev)"
echo ""
echo "  2. Convex バックエンド起動:"
echo "     cd $PROJECT_ROOT/mission-control && npx convex dev"
echo ""
echo "  3. フロントエンド起動:"
echo "     cd $PROJECT_ROOT/mission-control && pnpm dev"
echo ""
echo "  4. Orchestrator 起動:"
echo "     cd $PROJECT_ROOT/orchestrator && npm run dev"
echo ""
echo "  詳細: docs/setup-guide.md"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
