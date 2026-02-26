#!/bin/bash
# OpenClaw 上流リポジトリ自動同期スクリプト
# 本家 (origin) から最新を取得し、フォーク (fork) にプッシュする
#
# 使い方:
#   手動実行: bash ~/KEWORK/OpenClaw/sync-upstream.sh
#   launchd で自動実行: com.kazuyaegusa.openclaw-sync.plist

set -euo pipefail

REPO_DIR="/Users/kazuyaegusa/KEWORK/OpenClaw/OpenClaw-repo"
LOG_DIR="/Users/kazuyaegusa/KEWORK/OpenClaw/logs"
LOG_FILE="${LOG_DIR}/sync-$(date +%Y%m%d).log"
LOCK_FILE="/tmp/openclaw-sync.lock"

mkdir -p "$LOG_DIR"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

# 多重起動防止
if [ -f "$LOCK_FILE" ]; then
  pid=$(cat "$LOCK_FILE" 2>/dev/null || echo "")
  if [ -n "$pid" ] && kill -0 "$pid" 2>/dev/null; then
    log "ERROR: 別の同期プロセスが実行中 (PID: $pid)。スキップします。"
    exit 1
  fi
  rm -f "$LOCK_FILE"
fi
echo $$ > "$LOCK_FILE"
trap 'rm -f "$LOCK_FILE"' EXIT

log "===== 同期開始 ====="

cd "$REPO_DIR" || { log "ERROR: リポジトリディレクトリが見つかりません: $REPO_DIR"; exit 1; }

# 現在のブランチを記録
CURRENT_BRANCH=$(git branch --show-current)
log "現在のブランチ: $CURRENT_BRANCH"

# 上流から最新を取得
log "origin (本家) から fetch..."
git fetch origin --prune 2>&1 | tee -a "$LOG_FILE"

# main ブランチを同期
log "main ブランチを同期中..."
git checkout main 2>&1 | tee -a "$LOG_FILE"
git merge origin/main --ff-only 2>&1 | tee -a "$LOG_FILE" || {
  log "WARNING: fast-forward merge できません。rebase を試みます..."
  git rebase origin/main 2>&1 | tee -a "$LOG_FILE" || {
    log "ERROR: rebase 失敗。main ブランチを origin/main にリセットします。"
    git rebase --abort 2>/dev/null || true
    git reset --hard origin/main 2>&1 | tee -a "$LOG_FILE"
  }
}

# フォークにプッシュ
log "fork (kazuyaegusa/openclaw) にプッシュ中..."
git push fork main 2>&1 | tee -a "$LOG_FILE" || {
  log "WARNING: 通常プッシュ失敗。force-with-lease で再試行..."
  git push fork main --force-with-lease 2>&1 | tee -a "$LOG_FILE" || {
    log "ERROR: フォークへのプッシュに失敗しました。"
  }
}

# 元のブランチに戻る
if [ "$CURRENT_BRANCH" != "main" ] && [ -n "$CURRENT_BRANCH" ]; then
  log "元のブランチ ($CURRENT_BRANCH) に戻します..."
  git checkout "$CURRENT_BRANCH" 2>&1 | tee -a "$LOG_FILE" || {
    log "WARNING: ブランチ切り替え失敗。main のままです。"
  }
fi

# 古いログファイルを削除（30日以上前）
find "$LOG_DIR" -name "sync-*.log" -mtime +30 -delete 2>/dev/null || true

log "===== 同期完了 ====="
