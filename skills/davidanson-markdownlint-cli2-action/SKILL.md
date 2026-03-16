---
name: davidanson-markdownlint-cli2-action
description: "A GitHub Action to run the markdownlint-cli2 tool for linting Markdown/CommonMark files with the"
homepage: https://github.com/DavidAnson/markdownlint-cli2-action
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
---

# Davidanson Markdownlint Cli2 Action

# markdownlint-cli2-action

## Usage

To lint Markdown files in the base directory of a project:

```yaml
- uses: DavidAnson/markdownlint-cli2-action@v22
```

To lint all Markdown files in a project:

```yaml
- uses: DavidAnson/markdownlint-cli2-action@v22
  with:
    globs: "**/*.md"
```

To lint specific Markdown files in a project:

```yaml
- uses: DavidAnson/markdownlint-cli2-action@v22
  with:
    globs: |
      README.md
      CHANGELOG.md
      docs/*.md
```

To use a custom separator:

```yaml
- uses: DavidAnson/markdownlint
```
