---
name: jgreenemi-parris
description: "Parris, the automated infrastructure setup tool for machine learning algorithms."
homepage: https://github.com/jgreenemi/Parris
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["git", "pip", "python3"]
---

# Jgreenemi Parris

# README

## Installation

You'll need an AWS account, AWS credentials loaded to your workstation (set up through `$ aws configure`), a machine learning algorithm to train, and of course a dataset that it can be trained on. You'll also likely want an S3 bucket or some other storage location for your algorithm's training results.

UNIX/Linux:

```bash
$ git clone https://github.com/jgreenemi/parris.git && cd parris
$ virtualenv -p python3 env
$ source env/bin/activate
(env) $ pip --version
pip 9.0.1 from .../env/lib/python3



## Usage

To use Parris, follow the [Getting Started guide](/docs/GETTING-STARTED.md) which will take you from setup all the way to launching your first ML training stack. While getting familiar with the tool you'll also want to [consult the Configuration guide](/docs/CONFIGURATION.md) to better understand what options are available to you. This will help a lot in conjunction with the Getting Started guide.

```
