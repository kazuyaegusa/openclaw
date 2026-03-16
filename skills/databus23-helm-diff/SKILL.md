---
name: databus23-helm-diff
description: "A helm plugin that shows a diff explaining what a helm upgrade would change"
homepage: https://github.com/databus23/helm-diff
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["curl", "git", "go"]
---

# Databus23 Helm Diff

# Helm Diff Plugin

[![Go Report Card](https://goreportcard.com/badge/github.com/databus23/helm-diff)](https://goreportcard.com/report/github.com/databus23/helm-diff)
[![GoDoc](https://godoc.org/github.com/databus23/helm-diff?status.svg)](https://godoc.org/github.com/databus23/helm-diff)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/databus23/helm-diff/blob/master/LICENSE)
[![zread](https://img.shields.io/badge/Ask_Zread-_.svg?style=flat&color=00b0aa&

## Usage

```
The Helm Diff Plugin

* Shows a diff explaining what a helm upgrade would change:
    This fetches the currently deployed version of a release
  and compares it to a local chart plus values. This can be
  used to visualize what changes a helm upgrade will perform.

* Shows a diff explaining what had changed between two revisions:
    This fetches previously deployed versions of a release
  and compares them. This can be used to visualize what changes
  were made during revision change.

* Sh

```
