---
name: cybersecsi-raudi
description: "A repo to automatically generate and keep updated a series of Docker images through GitHub Actions."
homepage: https://github.com/cybersecsi/RAUDI
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["docker", "git", "go", "pip", "pytest", "python3"]
---

# Cybersecsi Raudi

# 🐳 RAUDI: Regularly and Automatically Updated Docker Images

## Installation

This repo can also be executed locally. The requirements to be met are the following:

- Python 3.x
- Docker (with BuildX)

Here is the documentation for working with BuildX: https://docs.docker.com/buildx/working-with-buildx/

The setup phase is pretty straightforward, you just need the following commands:

```
git clone https://github.com/cybersecsi/RAUDI
cd RAUDI
pip install -r requirements.txt
```

You're ready to go!

## Usage

This section provides examples for the currently added Network Security Tools. As you can see the images do provide only the tool, so if you need to use a **wordlist** you need to mount it.
