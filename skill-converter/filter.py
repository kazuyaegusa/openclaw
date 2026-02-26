"""カタログエントリをフィルタリングするモジュール。"""

from __future__ import annotations

import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def filter_candidates(skills: list[dict], config: dict) -> list[dict]:
    """フィルタ条件に基づいてスキル候補を絞り込む。

    Args:
        skills: skills.json のエントリリスト
        config: config.yaml の filter セクションの辞書

    Returns:
        フィルタ済みのスキルリスト（quality_score 降順、上限適用済み）
    """
    categories = set(config.get("categories", []))
    min_quality = config.get("min_quality_score", 0.0)
    source_types = set(config.get("source_types", []))
    risk_exclude = set(config.get("security_risk_exclude", []))
    max_per_run = config.get("max_skills_per_run", 50)

    logger.info("フィルタ開始: 入力 %d 件", len(skills))

    # 各条件でフィルタ
    filtered = [
        s for s in skills
        if s.get("category") in categories
        and s.get("quality_score", 0.0) >= min_quality
        and s.get("source_type") in source_types
        and s.get("security_risk", "unknown") not in risk_exclude
    ]
    logger.info("条件フィルタ後: %d 件", len(filtered))

    # source_url で重複除去（先に出現したものを優先）
    seen_urls: set[str] = set()
    deduped: list[dict] = []
    for s in filtered:
        url = s.get("source_url", "")
        if url not in seen_urls:
            seen_urls.add(url)
            deduped.append(s)
    logger.info("重複除去後: %d 件", len(deduped))

    # quality_score 降順ソート
    deduped.sort(key=lambda s: s.get("quality_score", 0.0), reverse=True)

    # 上限適用
    result = deduped[:max_per_run]
    logger.info("上限適用後: %d 件 (max=%d)", len(result), max_per_run)

    return result


def exclude_existing(candidates: list[dict], output_dir: str | Path) -> list[dict]:
    """出力先に既に存在するスキルを候補から除外する。

    Args:
        candidates: フィルタ済みスキルリスト
        output_dir: 既存スキルが格納されているディレクトリ

    Returns:
        既存スキルを除外したリスト
    """
    out = Path(output_dir)
    if not out.exists():
        logger.info("出力先が存在しないため除外なし: %s", out)
        return candidates

    existing_slugs = {d.name for d in out.iterdir() if d.is_dir()}
    logger.info("既存スキル: %d 件", len(existing_slugs))

    result = [s for s in candidates if s.get("slug") not in existing_slugs]
    excluded = len(candidates) - len(result)
    if excluded:
        logger.info("既存スキル除外: %d 件除外 → 残り %d 件", excluded, len(result))

    return result


def filter_pipeline(
    skills: list[dict],
    config: dict,
    output_dir: str | Path,
) -> list[dict]:
    """filter_candidates → exclude_existing を順に適用するパイプライン。

    Args:
        skills: skills.json のエントリリスト
        config: config.yaml の filter セクションの辞書
        output_dir: 既存スキルが格納されているディレクトリ

    Returns:
        最終的な変換対象スキルリスト
    """
    candidates = filter_candidates(skills, config)
    result = exclude_existing(candidates, output_dir)
    logger.info("パイプライン完了: %d 件 → %d 件", len(skills), len(result))
    return result
