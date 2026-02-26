"""メイン変換スクリプト。

カタログ → フィルタ → SKILL.md 生成の一連のパイプラインを実行する。
"""

from __future__ import annotations

import argparse
import logging
import sys
from datetime import datetime
from pathlib import Path

import yaml

from fetch_catalog import check_skill_md_exists, fetch_readme, fetch_skills_json
from filter import filter_pipeline
from generator import adapt_existing_skill_md, generate_skill_md, validate_name

logger = logging.getLogger("convert")


def setup_logging(log_dir: str | Path, verbose: bool = False) -> None:
    """ロガーを設定する。"""
    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)

    today = datetime.now().strftime("%Y%m%d")
    log_file = log_path / f"convert-{today}.log"

    fmt = "%(asctime)s %(levelname)s %(name)s: %(message)s"
    level = logging.DEBUG if verbose else logging.INFO

    # ルートロガーを設定
    root = logging.getLogger()
    root.setLevel(level)

    # FileHandler
    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setLevel(level)
    fh.setFormatter(logging.Formatter(fmt))
    root.addHandler(fh)

    # StreamHandler (stderr)
    sh = logging.StreamHandler(sys.stderr)
    sh.setLevel(level)
    sh.setFormatter(logging.Formatter(fmt))
    root.addHandler(sh)

    logger.info("ログ出力先: %s", log_file)


def load_config(config_path: str | Path) -> dict:
    """config.yaml を読み込む。"""
    path = Path(config_path)
    if not path.exists():
        logger.error("設定ファイルが見つかりません: %s", path)
        sys.exit(1)

    try:
        with open(path, encoding="utf-8") as f:
            config = yaml.safe_load(f)
        logger.info("設定読み込み完了: %s", path)
        return config
    except yaml.YAMLError as e:
        logger.error("設定ファイルのパースに失敗: %s", e)
        sys.exit(1)


def run(config: dict, dry_run: bool = False) -> None:
    """変換パイプラインを実行する。"""
    catalog_cfg = config["catalog"]
    filter_cfg = config["filter"]
    output_cfg = config["output"]

    output_dir = Path(output_cfg["dir"])
    template_path = output_cfg["template"]

    # カタログ取得
    try:
        skills = fetch_skills_json(
            repo=catalog_cfg["repo"],
            path=catalog_cfg["path"],
            cache_dir=catalog_cfg["cache_dir"],
            cache_ttl_hours=catalog_cfg.get("cache_ttl_hours", 24),
        )
    except Exception as e:
        logger.error("カタログ取得に失敗: %s", e)
        sys.exit(1)

    logger.info("カタログ取得: %d 件", len(skills))

    # フィルタリング
    candidates = filter_pipeline(skills, filter_cfg, output_dir)
    logger.info("変換候補: %d 件", len(candidates))

    if not candidates:
        logger.info("変換対象なし。終了します。")
        return

    # 各候補を変換
    success = 0
    skipped = 0
    errors = 0

    for entry in candidates:
        slug = entry.get("slug", "")
        source_url = entry.get("source_url", "")

        try:
            # スラッグ検証
            name = validate_name(slug)
            if name != slug:
                logger.info("スラッグ修正: %s → %s", slug, name)

            # 既存 SKILL.md の確認
            existing_skill_md = check_skill_md_exists(source_url)

            if existing_skill_md:
                logger.info("[%s] 既存 SKILL.md を検出、アダプト", name)
                content = adapt_existing_skill_md(existing_skill_md, entry)
            else:
                logger.info("[%s] README から SKILL.md を生成", name)
                readme = fetch_readme(source_url)
                content = generate_skill_md(entry, readme, template_path)

            # 書き出し
            if dry_run:
                logger.info("[DRY-RUN] %s/SKILL.md:\n%s", name, content[:200])
            else:
                skill_dir = output_dir / name
                skill_dir.mkdir(parents=True, exist_ok=True)
                skill_file = skill_dir / "SKILL.md"
                skill_file.write_text(content, encoding="utf-8")
                logger.info("[%s] 書き出し完了: %s", name, skill_file)

            success += 1

        except Exception as e:
            logger.error("[%s] 変換エラー: %s", slug, e, exc_info=True)
            errors += 1

    # サマリー
    total = success + skipped + errors
    logger.info(
        "変換完了: 合計 %d 件 (成功: %d, スキップ: %d, エラー: %d)",
        total, success, skipped, errors,
    )


def main() -> None:
    """エントリポイント。"""
    parser = argparse.ArgumentParser(
        description="カタログから OpenClaw SKILL.md を生成する",
    )
    parser.add_argument(
        "--config",
        default=str(Path(__file__).parent / "config.yaml"),
        help="config.yaml のパス (デフォルト: スクリプトと同じディレクトリの config.yaml)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="ファイル書き出しを行わず、変換結果をログに出力",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="DEBUG レベルのログ出力",
    )

    args = parser.parse_args()

    config = load_config(args.config)

    # ロギング設定（config 読み込み後）
    log_dir = config.get("output", {}).get(
        "log_dir",
        str(Path(__file__).parent / "logs"),
    )
    setup_logging(log_dir, verbose=args.verbose)

    run(config, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
