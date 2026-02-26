# セッションサマリー: 自律型AIエージェント基盤構築

> 作成日: 2026-02-16
> ステータス: converter パイプライン完成 → 次フェーズ（オーケストレーター）設計待ち

---

## 1. 本日の成果: カタログ → OpenClaw スキル自動変換パイプライン

### 完成物

claude_research リポジトリの AI ツールカタログ（4,484件）から、OpenClaw 互換の SKILL.md を自動生成するパイプラインを構築した。

```
claude_research/skills.json (4,484件)
  ↓ フィルタ（カテゴリ・品質スコア・セキュリティ・重複除去）
  ↓ → 430件 → 上限50件/回
候補リスト
  ↓ GitHub API で README / SKILL.md を取得
  ↓
OpenClaw SKILL.md を自動生成（Jinja2テンプレート）
  ↓
skills/{slug}/SKILL.md に配置
  ↓
fork にコミット & プッシュ（launchd で毎日10:00自動実行）
```

### ファイル一覧

| ファイル | 役割 |
|---------|------|
| `skill-converter/convert.py` | メイン変換スクリプト（`--dry-run`, `--verbose`） |
| `skill-converter/fetch_catalog.py` | GitHub API 経由カタログ取得、README/SKILL.md 取得 |
| `skill-converter/filter.py` | カテゴリ・品質・セキュリティでフィルタリング |
| `skill-converter/generator.py` | README → SKILL.md 生成、既存SKILL.mdアダプト |
| `skill-converter/config.yaml` | パイプライン設定 |
| `skill-converter/templates/skill.md.j2` | OpenClaw SKILL.md テンプレート |
| `convert-skills.sh` | 自動実行シェルスクリプト（コミット＆プッシュ付き） |
| `~/Library/LaunchAgents/com.kazuyaegusa.openclaw-skill-convert.plist` | launchd 定義（毎日10:00） |

### dry-run 検証結果

```
カタログ取得: 4,484件
条件フィルタ後: 430件
重複除去後: 422件
上限適用後: 50件
既存スキル除外: 52件の既存スキルは保護
```

正常動作を確認。launchd にも登録済み。

---

## 2. 8891_screen_shot リポジトリの全体像

### リポジトリ概要

**kazuyaegusa/8891_screen_shot** は、macOS 上で画面操作を記録・再生し、AIエージェントが GUI アプリケーションを自律操作するための基盤技術を開発するプロジェクト。

### コアコンセプト: Screen Action Recorder

```
[記録フェーズ]                    [再生フェーズ]
ユーザーがアプリ操作              記録データ（JSON + スクショ）
    ↓                              ↓
CGEventTap でクリック/入力検知      AI が要素を再検索
    ↓                              ↓
Accessibility API で UI要素取得     identifier > value > description > 座標
    ↓                              ↓
JSON + スクリーンショット保存      見つからない場合 → AI画像認識（Phase 3）
    ↓
パラメータ化して「スキル」に変換
```

### 技術スタック

| レイヤー | 技術 | 状態 |
|---------|------|------|
| イベント監視 | `CGEventTap` (Quartz) | 完了 |
| UI要素取得 | `AXUIElement` (Accessibility API) | 完了 |
| スクリーンショット | `mss` + `Pillow` | 完了 |
| クリック実行 | `CGEventCreateMouseEvent` | 完了 |
| キーボード入力 | `CGEventCreateKeyboardEvent` | 完了 |
| 要素検索（再生） | identifier/value/description/role | 完了 |
| JSON保存 | capture_id, element, app, browser 等 | 完了 |
| AI画像認識フォールバック | Claude Vision API | 未着手 |
| ブラウザDOM対応 | Chrome Extension | 未着手 |
| スキルエディタ | Web UI | 未着手 |

### 検証状況

```
V1 クリック記録    ████████████ 完了
V2 クリック再生    ████████████ 完了
V3 キーボード取得  ████████████ 完了
V4 キーボード再生  ████████████ 完了
V5 日本語入力      ████████████ 完了（制約あり: IME前のkeycode記録）
V6 統合動作        ███░░░░░░░░░ 実装完了、テスト未了
V7 スキル化        ░░░░░░░░░░░░ 未着手
V8 AI補完          ░░░░░░░░░░░░ 未着手
```

### アプリ種別ごとの再生信頼度

| アプリ種別 | 代表例 | 再生信頼度 | 備考 |
|-----------|--------|-----------|------|
| macOSネイティブ | システム設定, テキストエディット | 高 | identifier が豊富 |
| macOSシステム | Finder, 通知センター | 中〜高 | 右クリックメニューも対応 |
| チャットアプリ | LINE | 中 | IDなし、表示テキストで補助 |
| Electron系 | Cursor, Discord | 低 | 識別情報なし → AI補完必要 |

### 既存スキル（03_sample/skills/）

- **app-automation**: homerow スタイルのアプリ自動化（scan/click/copy/workflow）
- **line-chat-saver**: LINE トーク履歴の AppleScript 自動保存

### リポジトリ構造

```
8891_screen_shot/
├── claude/                     # メイン開発ディレクトリ
│   ├── src/                    # 本番コード
│   │   ├── capture_loop.py     # 常駐キャプチャ（timer/event モード）
│   │   ├── window_detector.py  # Linux ウィンドウ検出
│   │   ├── window_detector_mac.py  # macOS ウィンドウ検出
│   │   └── window_screenshot.py    # 赤枠描画 + JSON保存
│   ├── docs/                   # API仕様書（src と 1:1 対応）
│   ├── setup/                  # インストール・デーモン設定
│   └── old/                    # 旧バージョン退避
├── 03_sample/                  # Screen Action Recorder
│   ├── mvp_click_recorder.py   # 操作記録ツール
│   ├── mvp_action_player.py    # 操作再生ツール
│   ├── docs/                   # 設計書・進捗レポート
│   │   ├── AUTONOMOUS_AGENT_VISION.md  # 自律型AI設計書
│   │   ├── SCREEN_ACTION_RECORDER_DESIGN.md
│   │   ├── SCREEN_ACTION_RECORDER_SUMMARY.md
│   │   └── PROGRESS_REPORT.md
│   └── skills/                 # スキル定義
├── 03_e2e/                     # E2Eテスト（Playwright）
└── 100_IMPORT/                 # 外部API参照（Gemini, OpenAI）
```

---

## 3. 統合ビジョン: 全プロジェクトの接続

### 保有アセット

```
┌─────────────────────────────────────────────────────────────────┐
│                    kazuyaegusa エコシステム                      │
│                                                                 │
│  [claude_research]         [8891_screen_shot]     [OpenClaw]    │
│  AI ツール収集 4,484件     GUI 操作の記録・再生   スキル管理    │
│  日次自動更新              Accessibility API       52+ スキル   │
│  カテゴリ・品質分類        クリック/入力/スクショ  SKILL.md形式  │
│                                                                 │
│  ─────────── 今回接続 ──────────────                            │
│  skill-converter が claude_research → OpenClaw を自動変換        │
│                                                                 │
│  ─────────── 未接続 ───────────────                             │
│  8891_screen_shot の操作スキルが OpenClaw に統合されていない      │
│  「スキルを使って仕事をする」オーケストレーターが存在しない      │
└─────────────────────────────────────────────────────────────────┘
```

### 目指す姿: 自律型AIエージェント

AUTONOMOUS_AGENT_VISION.md で描かれているアーキテクチャ:

```
┌─────────────────────────────────────────────────────────────────┐
│                      【AIエージェント】                         │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    オーケストレーター                    │   │
│  │  「何をすべきか判断し、スキルを組み合わせて実行する」    │   │
│  └─────────────────────────────────────────────────────────┘   │
│           │                    │                    │          │
│           ▼                    ▼                    ▼          │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │
│  │ 思考スキル   │    │ 操作スキル   │    │ 通信スキル   │      │
│  │              │    │              │    │              │      │
│  │ 分析・要約   │    │ GUI操作      │    │ API呼出      │      │
│  │ 計画・判断   │    │ クリック     │    │ メール送信   │      │
│  │ コード生成   │    │ キーボード   │    │ Slack投稿    │      │
│  └──────────────┘    └──────────────┘    └──────────────┘      │
│   OpenClaw スキル     8891 Screen        claude_research       │
│   + claude_research   Action Recorder    + 既存API             │
│     から自動生成                                               │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                  スキル成長サイクル                      │   │
│  │  社員操作 → 記録 → スキル化 → 蓄積 → AI活用 → 改善     │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. 現在地と次のステップ

### 完了したもの

| # | 項目 | 状態 |
|---|------|------|
| 1 | claude_research: AI ツールカタログ収集（4,484件） | 稼働中 |
| 2 | OpenClaw: スキル管理基盤（52+スキル） | 稼働中 |
| 3 | skill-converter: カタログ → SKILL.md 自動変換 | 完成・launchd登録済み |
| 4 | 8891: クリック記録・再生（V1-V2） | 完了 |
| 5 | 8891: キーボード記録・再生（V3-V5） | 完了 |
| 6 | 8891: レコーダー/プレイヤー統合 | 実装完了・テスト待ち |

### 未完了・次のステップ

| # | 項目 | 依存 | 優先度 |
|---|------|------|--------|
| A | V6: 統合テスト（LINE入力+送信、Safari URL等） | V5完了 | 高 |
| B | V7: スキル化（記録→パラメータ化→再利用） | V6完了 | 高 |
| C | V8: AI画像認識フォールバック（Electron対応） | V7完了 | 中 |
| D | オーケストレーター設計・実装 | B + skill-converter | 高 |
| E | 8891 操作スキル → OpenClaw 統合 | B | 中 |
| F | 常時稼働エージェント（イベント駆動） | D | 中 |

### 提案: 次フェーズの順序

```
[即座]
  V6 統合テスト実施 → 技術基盤の最終確認

[短期: 1-2週]
  オーケストレーター設計
    ├── タスクキュー: AIが「次に何をすべきか」を判断
    ├── スキルルーター: タスク→最適なスキルの選択
    ├── 実行エンジン: Claude Code エージェントチームとして実行
    └── 成果物配信: PR作成、通知、レポート

[中期: 2-4週]
  V7 スキル化 + OpenClaw 統合
    ├── 8891 操作記録 → OpenClaw SKILL.md として登録
    ├── 操作スキル + 思考スキル + 通信スキルの連携
    └── スキル成長サイクルの確立

[長期]
  常時稼働 + 自律改善
    ├── イベント駆動（cron→webhook/監視ベース）
    ├── 失敗検知 → 自動リトライ/再記録
    └── 「使うほど賢くなる」フィードバックループ
```

---

## 5. 「売れる仕組み」へのパス

### 現状の課題

今は「素材を集めて棚に並べている」段階。以下が欠けている:

1. **アクション実行層**: 情報は集まるが、それに基づく「行動」が自動化されていない
2. **スキル連携**: 個々のスキルは動くが、組み合わせたワークフローがない
3. **判断の自動化**: 「何をすべきか」の判断自体を AI に任せる仕組みがない
4. **常時稼働**: cron の定期実行ではなく、イベント駆動で 24 時間反応する仕組みがない

### 価値提案

```
「社員が働くほど、AIが対応できる業務範囲が拡大し続ける」

  社員10人 × 1ヶ月 → 数百の操作スキルが自然に蓄積
  新しいアプリ導入 → そのアプリのスキルも自動追加
  AI は使えば使うほど、対応できる業務の幅が広がり続ける
```

これを実現するための技術基盤は揃いつつある:
- **カタログ収集**: claude_research（稼働中）
- **スキル管理**: OpenClaw + converter（本日完成）
- **GUI操作**: 8891 Screen Action Recorder（V1-V5完了）
- **不足**: オーケストレーター（次フェーズ）

---

## 付録: コマンドリファレンス

### skill-converter

```bash
# dry-run（ファイル書き出しなし）
python3 ~/KEWORK/OpenClaw/skill-converter/convert.py --dry-run

# 本番実行（SKILL.md 生成のみ）
python3 ~/KEWORK/OpenClaw/skill-converter/convert.py

# フル実行（生成 + コミット + プッシュ）
bash ~/KEWORK/OpenClaw/convert-skills.sh

# launchd 操作
launchctl load ~/Library/LaunchAgents/com.kazuyaegusa.openclaw-skill-convert.plist
launchctl unload ~/Library/LaunchAgents/com.kazuyaegusa.openclaw-skill-convert.plist
launchctl list | grep openclaw
```

### 8891 Screen Action Recorder

```bash
# 操作記録
cd 8891_screen_shot/03_sample
python3 mvp_click_recorder.py

# 再生（シミュレーション）
python3 mvp_action_player.py mvp_output/session_xxx.json --dry-run

# 再生（本番）
python3 mvp_action_player.py mvp_output/session_xxx.json --delay 2.0

# 常駐キャプチャ（スクリーンショット + UI要素JSON）
cd 8891_screen_shot/claude/src
python3 capture_loop.py --trigger event
```

### OpenClaw 同期

```bash
# 上流同期
bash ~/KEWORK/OpenClaw/sync-upstream.sh

# ログ確認
ls ~/KEWORK/OpenClaw/logs/
```
