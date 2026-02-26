#!/bin/bash
# カタログ → OpenClaw SKILL.md 自動変換スクリプト
# claude_research の skills.json から SKILL.md を生成し、フォークにコミット＆プッシュ
#
# 使い方:
#   手動実行: bash ~/KEWORK/OpenClaw/convert-skills.sh
#   launchd で自動実行: com.kazuyaegusa.openclaw-skill-convert.plist

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CONVERTER_DIR="${SCRIPT_DIR}/skill-converter"
REPO_DIR="/Users/kazuyaegusa/KEWORK/OpenClaw/OpenClaw-repo"
LOG_DIR="/Users/kazuyaegusa/KEWORK/OpenClaw/logs"
LOG_FILE="${LOG_DIR}/convert-$(date +%Y%m%d).log"
LOCK_FILE="/tmp/openclaw-convert.lock"

mkdir -p "$LOG_DIR"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

# 多重起動防止
if [ -f "$LOCK_FILE" ]; then
  pid=$(cat "$LOCK_FILE" 2>/dev/null || echo "")
  if [ -n "$pid" ] && kill -0 "$pid" 2>/dev/null; then
    log "ERROR: 別の変換プロセスが実行中 (PID: $pid)。スキップします。"
    exit 1
  fi
  rm -f "$LOCK_FILE"
fi
echo $$ > "$LOCK_FILE"
trap 'rm -f "$LOCK_FILE"' EXIT

log "===== スキル変換開始 ====="

# Python 依存パッケージの確認
python3 -c "import yaml, jinja2" 2>/dev/null || {
  log "ERROR: 必要なパッケージが不足しています。pip install pyyaml jinja2 を実行してください。"
  exit 1
}

# 変換実行
log "変換パイプライン実行中..."
cd "$CONVERTER_DIR"
python3 convert.py --config "${CONVERTER_DIR}/config.yaml" 2>&1 | tee -a "$LOG_FILE"
CONVERT_EXIT=$?

if [ $CONVERT_EXIT -ne 0 ]; then
  log "ERROR: 変換パイプラインがエラーで終了 (exit: $CONVERT_EXIT)"
  exit 1
fi

# 新規ファイルがあるか確認
cd "$REPO_DIR"
NEW_FILES=$(git status --porcelain skills/ 2>/dev/null | grep "^?" | wc -l | tr -d ' ')

if [ "$NEW_FILES" = "0" ]; then
  log "新規スキルなし。コミット不要です。"
  log "===== スキル変換完了 ====="
  exit 0
fi

log "新規スキル検出: ${NEW_FILES} ファイル"

# Git コミット＆プッシュ
log "新規スキルをコミット中..."
git add skills/*/SKILL.md 2>&1 | tee -a "$LOG_FILE"

COMMIT_MSG="自動生成: カタログから ${NEW_FILES} 件のスキルを追加 ($(date +%Y-%m-%d))"
git commit -m "$COMMIT_MSG" 2>&1 | tee -a "$LOG_FILE" || {
  log "WARNING: コミット失敗。変更がないか確認してください。"
  log "===== スキル変換完了 ====="
  exit 0
}

log "fork にプッシュ中..."
git push fork main 2>&1 | tee -a "$LOG_FILE" || {
  log "ERROR: プッシュ失敗。手動で確認してください。"
  exit 1
}

# 古いログファイルを削除（30日以上前）
find "$LOG_DIR" -name "convert-*.log" -mtime +30 -delete 2>/dev/null || true

log "===== スキル変換完了 ====="
