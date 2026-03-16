---
name: bridgecrewio-checkov
description: "Prevent cloud misconfigurations and find vulnerabilities during build-time in infrastructure as"
homepage: https://github.com/bridgecrewio/checkov
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["checkov", "docker", "jq", "pip", "python3"]
---

# Bridgecrewio Checkov

[![checkov](https://raw.githubusercontent.com/bridgecrewio/checkov/main/docs/web/images/checkov_blue_logo.png)](#)

[![Maintained by Prisma Cloud](https://img.shields.io/badge/maintained_by-Prisma_Cloud-blue)](https://prismacloud.io/?utm_source=github&utm_medium=organic_oss&utm_campaign=checkov)
[![build status](https://github.com/bridgecrewio/checkov/workflows/build/badge.svg)](https://github.com/bridgecrewio/checkov/actions?query=workflow%3Abuild)
[![security status](https://github.com/

## Installation

To install pip follow the official [docs](https://pip.pypa.io/en/stable/cli/pip_install/)

```sh
pip3 install checkov
```

Certain environments (e.g., Debian 12) may require you to install Checkov in a virtual environment

````sh



## Usage

Allow only the two specified checks to run:
```sh
checkov --directory . --check CKV_AWS_20,CKV_AWS_57
````

Run all checks except the one specified:

```sh
checkov -d . --skip-check CKV_AWS_20
```

Run all checks except checks with specified patterns:

```sh
checkov -d . --skip-check CKV_AWS*
```

Run all checks that are MEDIUM severity or higher (requires API key):

```sh
checkov -d . --check MEDIUM --bc-api-key ...
```

Run all checks that are MEDIUM severity or higher, as well as check CKV_123 (a
