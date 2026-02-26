"""GitHub API 経由でカタログデータを取得するモジュール。"""

from __future__ import annotations

import base64
import json
import logging
import subprocess
import time
from pathlib import Path

logger = logging.getLogger(__name__)


def _run_gh(args: list[str], check: bool = True) -> str:
    """gh コマンドを実行して stdout を返す。"""
    cmd = ["gh"] + args
    logger.debug("実行: %s", " ".join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True, check=check)
    if result.returncode != 0 and not check:
        logger.warning("gh コマンド失敗 (rc=%d): %s", result.returncode, result.stderr.strip())
    return result.stdout.strip()


def _parse_owner_repo(repo_url: str) -> tuple[str, str]:
    """GitHub URL から owner/repo を抽出する。"""
    # https://github.com/owner/repo 形式を想定
    url = repo_url.rstrip("/")
    parts = url.split("/")
    return parts[-2], parts[-1]


def fetch_skills_json(
    repo: str,
    path: str,
    cache_dir: str | Path,
    cache_ttl_hours: int = 24,
) -> list[dict]:
    """skills.json をGitHub APIから取得する。キャッシュがあればそちらを返す。

    Args:
        repo: "owner/repo" 形式のリポジトリ指定
        path: リポジトリ内のファイルパス
        cache_dir: キャッシュ保存先ディレクトリ
        cache_ttl_hours: キャッシュの有効期間（時間）

    Returns:
        skills.json の内容（リスト）
    """
    cache_path = Path(cache_dir) / "skills.json"
    cache_path.parent.mkdir(parents=True, exist_ok=True)

    # キャッシュが有効期間内なら返す
    if cache_path.exists():
        age_hours = (time.time() - cache_path.stat().st_mtime) / 3600
        if age_hours < cache_ttl_hours:
            logger.info("キャッシュを使用 (経過: %.1f時間)", age_hours)
            return json.loads(cache_path.read_text(encoding="utf-8"))
        logger.info("キャッシュ期限切れ (経過: %.1f時間)", age_hours)

    # download_url を取得してダウンロード
    try:
        download_url = _run_gh([
            "api", f"repos/{repo}/contents/{path}",
            "--jq", ".download_url",
        ])
        if not download_url:
            raise ValueError("download_url が空です")

        logger.info("ダウンロード: %s", download_url)
        raw = subprocess.run(
            ["curl", "-sL", download_url],
            capture_output=True, text=True, check=True,
        ).stdout

        skills = json.loads(raw)
        # キャッシュに保存
        cache_path.write_text(json.dumps(skills, ensure_ascii=False, indent=2), encoding="utf-8")
        logger.info("取得完了: %d 件のスキル", len(skills))
        return skills

    except (subprocess.CalledProcessError, json.JSONDecodeError, ValueError) as e:
        logger.error("skills.json の取得に失敗: %s", e)
        # キャッシュが古くても存在すればフォールバック
        if cache_path.exists():
            logger.warning("古いキャッシュにフォールバック")
            return json.loads(cache_path.read_text(encoding="utf-8"))
        raise


def fetch_readme(repo_url: str) -> str | None:
    """GitHub リポジトリの README.md を取得する。

    Rate limit 対策として呼び出し前に2秒待機する。

    Args:
        repo_url: "https://github.com/owner/repo" 形式のURL

    Returns:
        README の内容。エラー時は None。
    """
    time.sleep(2)

    owner, repo = _parse_owner_repo(repo_url)
    try:
        content_b64 = _run_gh([
            "api", f"repos/{owner}/{repo}/readme",
            "--jq", ".content",
        ])
        if not content_b64:
            logger.warning("README が空: %s/%s", owner, repo)
            return None

        decoded = base64.b64decode(content_b64).decode("utf-8")
        logger.info("README 取得: %s/%s (%d 文字)", owner, repo, len(decoded))
        return decoded

    except subprocess.CalledProcessError as e:
        logger.warning("README 取得失敗 (%s/%s): %s", owner, repo, e)
        return None


def check_skill_md_exists(repo_url: str) -> str | None:
    """リポジトリに SKILL.md が存在するか確認し、あれば内容を返す。

    Args:
        repo_url: "https://github.com/owner/repo" 形式のURL

    Returns:
        SKILL.md の内容。存在しなければ None。
    """
    owner, repo = _parse_owner_repo(repo_url)
    try:
        content_b64 = _run_gh([
            "api", f"repos/{owner}/{repo}/contents/SKILL.md",
            "--jq", ".content",
        ])
        if not content_b64:
            return None

        decoded = base64.b64decode(content_b64).decode("utf-8")
        logger.info("SKILL.md 検出: %s/%s", owner, repo)
        return decoded

    except subprocess.CalledProcessError:
        logger.debug("SKILL.md なし: %s/%s", owner, repo)
        return None
