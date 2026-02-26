```text
あなたは既存コードベースに機能追加する実装AIです。以下をそのまま実装してください。

## 目的
`/Users/kazuyaegusa/KEWORK/OpenClaw` の既存「コンテキスト収集→解析→タスク分解→承認→実行」フローに対して、入力を「URL貼り付け」「プレーンテキスト貼り付け」「URL+テキスト混在」のどれでも扱えるようにする。  
X投稿は例に過ぎず、媒体非依存の汎用入力にすること。

## 対象リポジトリ
- `/Users/kazuyaegusa/KEWORK/OpenClaw/mission-control`
- 必要なら `/Users/kazuyaegusa/KEWORK/OpenClaw/orchestrator` も最小変更で連携

## 実装要件（MVP）
1. 入力UIを1つに統合
- ファイル候補:
  - `/Users/kazuyaegusa/KEWORK/OpenClaw/mission-control/src/components/inbox/context-create-dialog.tsx`
- ユーザーは1つの大きな入力欄に何でも貼れるようにする。
- プレースホルダ例: 「URLだけでも、テキストだけでも、両方でもOK」
- 送信前に以下を軽く表示:
  - 検出URL件数
  - テキスト文字数
  - 入力モード (`url_only` / `text_only` / `mixed`)

2. 受け取り時に正規化処理を追加
- ファイル候補:
  - `/Users/kazuyaegusa/KEWORK/OpenClaw/mission-control/convex/http.ts`
  - `/Users/kazuyaegusa/KEWORK/OpenClaw/mission-control/convex/contexts.ts`
  - `/Users/kazuyaegusa/KEWORK/OpenClaw/mission-control/convex/contextProcessor.ts`
- 生入力からURLを抽出（複数可、MVPで最大3件程度まで処理）。
- URLを除いた残りを`plainText`として保持。
- 判定:
  - URLのみ: `url_only`
  - テキストのみ: `text_only`
  - 両方あり: `mixed`
- 保存項目（既存スキーマに追記）:
  - `rawInput`
  - `inputMode`
  - `detectedUrls`
  - `plainText`
  - `normalizedText`（解析に使う最終テキスト）
  - `sourceSnapshots`（URLごとの title/text/status/error を持つ配列）

3. URL本文の取得（失敗しても処理継続）
- 取得失敗時は`status=failed`で保存し、`plainText`のみで解析を継続。
- タイムアウトを短めに設定（例: 8秒）。
- 取得できた本文は`normalizedText`に連結する。
- `normalizedText`の構築順:
  - `plainText`
  - 各URLの抽出本文（URLごとに区切り見出し付き）
- 必ず「入力が不完全でも落ちない」実装にする。

4. 既存解析・分解フローに接続
- `contextProcessor`は`normalizedText`を最優先で解析するよう変更。
- 既存の`task_request`判定とorchestrator分解連携は壊さない。
- 既存コンテキスト種別との後方互換性を維持する。

5. コピー実装リスクの明示（軽量ガード）
- 解析時に`riskFlags`を追加（例: `copyright_risk`）。
- URL由来本文がある場合、タスク生成時に「抽象化して再実装する」注意書きをメタに残す。
- 自動実行を止めるまでは不要だが、承認画面で人が確認できる情報として保存する。

6. テスト追加
- URL抽出と入力モード判定のユニットテスト。
- URL取得失敗時のフォールバックテスト。
- `normalizedText`優先で解析されることのテスト。
- 既存フローの回帰テスト（最低1本）。

7. ドキュメント更新
- 変更内容を以下へ追記:
  - `/Users/kazuyaegusa/KEWORK/OpenClaw/mission-control/README.md`
  - 必要なら `/Users/kazuyaegusa/KEWORK/OpenClaw/docs/setup-guide.md`
- 「URLのみ/テキストのみ/混在」の利用例を追加。

## 制約
- 破壊的変更禁止。既存データが読めること。
- 大規模リファクタ禁止。MVPとして最短で実装。
- 新規外部APIキー必須の設計は避ける（まずはHTTP取得ベースで十分）。
- エラー時は常に「保存して次へ進む」方針。

## 完了条件
- 1つの入力欄にURL/テキスト/混在を貼って保存できる。
- 保存されたコンテキストが`normalizedText`で解析される。
- 既存の承認・分解・実行フローが継続動作する。
- テストが通る。
- 変更ファイル一覧と検証結果を最後に報告する。

既存APIの入出力契約・既存ステータス遷移・既存UI挙動は変更禁止。新機能はすべて後方互換な加算（optional field追加、分岐追加）で実装すること。
```