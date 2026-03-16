---
name: awslabs-iam-policy-autopilot
description: "IAM Policy Autopilot is an open source static code analysis tool that helps you quickly create"
homepage: https://github.com/awslabs/iam-policy-autopilot
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins: ["cargo", "curl", "git", "iam-policy-autopilot", "pip"]
---

# Awslabs Iam Policy Autopilot

[![awslabs/iam-policy-autopilot License](https://img.shields.io/badge/license-Apache%202-blue)](https://github.com/awslabs/iam-policy-autopilot/blob/main/LICENSE)
[![GitHub CI Status](https://img.shields.io/github/actions/workflow/status/awslabs/iam-policy-autopilot/build_and_publish.yml?label=CI&logo=GitHub)](https://github.com/awslabs/iam-policy-autopilot/actions/workflows/build_and_publish.yml) [![PyPI - Version](https://img.shields.io/pypi/v/iam-policy-autopilot?logo=Python&logoColor=white)]

## Installation

Clone the repository with submodules:

```bash
git clone --recurse-submodules https://github.com/awslabs/iam-policy-autopilot.git
cd iam-policy-autopilot
```

Build the project:

```bash
cargo build --release
```

The compiled binary will be located at `target/release/iam-policy-autopilot`.
