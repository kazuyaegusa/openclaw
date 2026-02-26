"""SKILL.md を自動生成するモジュール。

カタログエントリと README から OpenClaw 形式の SKILL.md を生成する。
"""

from __future__ import annotations

import logging
import re
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

logger = logging.getLogger(__name__)

CATEGORY_EMOJI: dict[str, str] = {
    "claude-code": "\U0001f916",
    "mcp-servers": "\U0001f50c",
    "agent": "\U0001f575\ufe0f",
    "tools": "\U0001f527",
    "devops": "\u2699\ufe0f",
    "ml-ai": "\U0001f9e0",
    "web-frontend": "\U0001f310",
    "web-backend": "\U0001f5a5\ufe0f",
    "database": "\U0001f5c4\ufe0f",
    "security": "\U0001f512",
    "testing": "\U0001f9ea",
    "docs": "\U0001f4c4",
    "automation": "\u26a1",
}

# README から検出するインストールコマンドのパターン
_INSTALL_PATTERNS: list[tuple[str, int]] = [
    (r"npm\s+install\s+(?:-g\s+)?(\S+)", 1),
    (r"npx\s+(\S+)", 1),
    (r"pip\s+install\s+(\S+)", 1),
    (r"pip3\s+install\s+(\S+)", 1),
    (r"brew\s+install\s+(\S+)", 1),
    (r"cargo\s+install\s+(\S+)", 1),
    (r"go\s+install\s+(\S+)", 1),
]

_KNOWN_BINS: set[str] = {
    "node", "npm", "npx", "python3", "pip", "docker",
    "cargo", "go", "gh", "git", "curl", "jq",
}

# セクション見出しのエイリアス（小文字で照合）
_OVERVIEW_HEADINGS = {"description", "about", "overview"}
_INSTALL_HEADINGS = {"installation", "install", "setup", "getting started"}
_USAGE_HEADINGS = {"usage", "quick start", "how to use", "examples"}


def _split_sections(readme: str) -> list[tuple[int, str, str]]:
    """README を見出しで分割する。

    Returns:
        [(level, heading_text, body), ...] のリスト。
        見出し前のテキストは level=0, heading_text="" で格納。
    """
    heading_re = re.compile(r"^(#{1,6})\s+(.+?)[\s#]*$", re.MULTILINE)
    sections: list[tuple[int, str, str]] = []
    last_end = 0
    last_level = 0
    last_heading = ""

    for m in heading_re.finditer(readme):
        body = readme[last_end:m.start()].strip()
        sections.append((last_level, last_heading, body))
        last_level = len(m.group(1))
        last_heading = m.group(2).strip()
        last_end = m.end()

    # 最後のセクション
    body = readme[last_end:].strip()
    sections.append((last_level, last_heading, body))

    return sections


def extract_sections(readme: str) -> dict[str, str]:
    """README から overview / install / usage セクションを抽出する。"""
    sections = _split_sections(readme)
    result: dict[str, str] = {}

    for _level, heading, body in sections:
        if not body:
            continue
        heading_lower = heading.lower().strip()

        # overview: 見出しなし（冒頭）またはDescription/About/Overview
        if heading_lower == "" and "overview" not in result:
            result["overview"] = body[:500]
        elif heading_lower in _OVERVIEW_HEADINGS and "overview" not in result:
            result["overview"] = body[:500]

        # install
        if heading_lower in _INSTALL_HEADINGS and "install" not in result:
            result["install"] = body[:500]

        # usage
        if heading_lower in _USAGE_HEADINGS and "usage" not in result:
            result["usage"] = body[:500]

    # overview が取れなかった場合、最初の段落をフォールバック
    if "overview" not in result:
        paragraphs = re.split(r"\n\s*\n", readme.strip(), maxsplit=1)
        if paragraphs:
            result["overview"] = paragraphs[0].strip()[:500]

    return result


def extract_bins(readme: str) -> list[str]:
    """README から必要な CLI バイナリを推定する。"""
    bins: set[str] = set()

    for pattern, group_idx in _INSTALL_PATTERNS:
        for m in re.finditer(pattern, readme):
            pkg = m.group(group_idx)
            # パッケージ名からバイナリ名を推定（スコープやURLを除去）
            name = pkg.split("/")[-1].split("@")[0].strip()
            if name:
                bins.add(name)

    # 既知バイナリの直接参照も検出
    for b in _KNOWN_BINS:
        # コードブロック等で使われているか確認
        if re.search(rf"(?:^|\s|`){re.escape(b)}(?:\s|`|$)", readme, re.MULTILINE):
            bins.add(b)

    return sorted(bins)


def truncate_description(desc: str, max_len: int = 100) -> str:
    """説明文を max_len 以内に切り詰める。"""
    # angle brackets 除去、改行を空白に
    text = re.sub(r"<[^>]*>", "", desc)
    text = text.replace("\n", " ").strip()
    text = re.sub(r"\s+", " ", text)

    if len(text) <= max_len:
        return text

    # 文境界で切る
    truncated = text[:max_len]
    # 最後のピリオドか空白で切る
    last_period = truncated.rfind(".")
    last_space = truncated.rfind(" ")
    cut = max(last_period, last_space)
    if cut > max_len // 2:
        truncated = truncated[:cut + 1].rstrip()
    else:
        truncated = truncated.rstrip()

    return truncated


def adapt_existing_skill_md(skill_md: str, entry: dict) -> str:
    """既存の SKILL.md を OpenClaw 形式にアダプトする。"""
    frontmatter_re = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
    match = frontmatter_re.match(skill_md)

    meta = {
        "name": entry.get("slug", ""),
        "description": truncate_description(entry.get("description", "")),
        "homepage": entry.get("source_url", ""),
        "metadata": {
            "openclaw": {
                "auto_generated": True,
            },
        },
    }

    if match:
        # 既存 frontmatter をパースして上書き
        try:
            existing = yaml.safe_load(match.group(1)) or {}
        except yaml.YAMLError:
            existing = {}

        existing["name"] = meta["name"]
        existing["description"] = meta["description"]
        existing["homepage"] = meta["homepage"]

        # metadata.openclaw.auto_generated を設定
        if "metadata" not in existing or not isinstance(existing["metadata"], dict):
            existing["metadata"] = {}
        if "openclaw" not in existing["metadata"] or not isinstance(existing["metadata"]["openclaw"], dict):
            existing["metadata"]["openclaw"] = {}
        existing["metadata"]["openclaw"]["auto_generated"] = True

        body = skill_md[match.end():]
        new_fm = yaml.dump(existing, default_flow_style=False, allow_unicode=True, sort_keys=False).strip()
        return f"---\n{new_fm}\n---\n{body}"
    else:
        # frontmatter がない場合は先頭に追加
        new_fm = yaml.dump(meta, default_flow_style=False, allow_unicode=True, sort_keys=False).strip()
        return f"---\n{new_fm}\n---\n\n{skill_md}"


def generate_skill_md(
    entry: dict,
    readme: str | None,
    template_path: str | Path,
) -> str:
    """エントリと README から SKILL.md を生成する。"""
    tpl_path = Path(template_path)
    env = Environment(
        loader=FileSystemLoader(str(tpl_path.parent)),
        keep_trailing_newline=True,
    )
    template = env.get_template(tpl_path.name)

    name = validate_name(entry.get("slug", "unnamed"))
    description = truncate_description(entry.get("description", ""))
    homepage = entry.get("source_url", "")
    category = entry.get("category", "")
    emoji = CATEGORY_EMOJI.get(category, "\U0001f4e6")

    overview: str | None = None
    install_section: str | None = None
    usage_section: str | None = None
    bins: list[str] | None = None

    if readme:
        sections = extract_sections(readme)
        overview = sections.get("overview")
        install_section = sections.get("install")
        usage_section = sections.get("usage")
        extracted_bins = extract_bins(readme)
        bins = extracted_bins if extracted_bins else None

    rendered = template.render(
        name=name,
        description=description,
        homepage=homepage,
        emoji=emoji,
        bins=bins,
        install_section=install_section,
        usage_section=usage_section,
        overview=overview or description,
        auto_generated=True,
    )
    return rendered


def validate_name(slug: str) -> str:
    """OpenClaw の name 規則に適合するよう検証・修正する。

    - hyphen-case のみ（^[a-z0-9-]+$）
    - 先頭・末尾のハイフン禁止
    - 連続ハイフン禁止
    - 最大64文字
    """
    # 小文字化、アンダースコアやドットをハイフンに変換
    name = slug.lower()
    name = re.sub(r"[^a-z0-9-]", "-", name)
    # 連続ハイフンを1つに
    name = re.sub(r"-{2,}", "-", name)
    # 先頭・末尾のハイフン除去
    name = name.strip("-")
    # 最大64文字
    name = name[:64].rstrip("-")

    if not name:
        name = "unnamed"

    return name
