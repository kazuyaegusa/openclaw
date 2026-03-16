---
name: hadolint-hadolint
description: "Dockerfile linter, validate inline bash, written in Haskell"
homepage: https://github.com/hadolint/hadolint
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["docker", "git", "go", "hadolint", "npm", "pip"]
---

# Hadolint Hadolint

# Haskell Dockerfile Linter

## Installation

You can download prebuilt binaries for OSX, Windows and Linux from the latest
[release page][]. However, if this does not work for you, please fall back to
container (Docker), `brew` or source installation.

On OSX, you can use [brew](https://brew.sh/) to install `hadolint`.

```bash
brew install hadolint
```

On Windows, you can use [scoop](https://github.com/lukesampson/scoop) to
install `hadolint`.

```batch
scoop install hadolint
```

On distributions that have `nix` installed, you can use t

## Usage

You can run `hadolint` locally to lint your Dockerfile.

```bash
hadolint <Dockerfile>
hadolint --ignore DL3003 --ignore DL3006 <Dockerfile> # exclude specific rules
hadolint --trusted-registry my-company.com:500 <Dockerfile> # Warn when using untrusted FROM images
```

Docker comes to the rescue, providing an easy way how to run `hadolint` on most
platforms.
Just pipe your `Dockerfile` to `docker run`:

```bash
docker run --rm -i hadolint/hadolint < Dockerfile

```
