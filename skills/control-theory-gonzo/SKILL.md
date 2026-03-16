---
name: control-theory-gonzo
description: "Gonzo! The Go based TUI log analysis tool"
homepage: https://github.com/control-theory/gonzo
metadata:
  openclaw:
    emoji: "📦"
    auto_generated: true
    requires:
      bins: ["curl", "docker", "git", "go", "gonzo"]
---

# Control Theory Gonzo

<p align="center">
<a href="https://controltheory.com"><img src="docs/sponsor-controltheory-dstl8.png" alt="Sponsored by ControlTheory: Dstl8"></a>
</p>

## Installation

Add this plugin to your `$XDG_CONFIG_HOME/k9s/plugins.yaml` file:

```yaml
plugins:
  gonzo:
    shortCut: Ctrl-L
    description: "Gonzo log analysis"
    scopes:
      - po
      - deploy
      - sts
      - ds
      - svc
      - job
      - cj
    command: sh
    background: false
    args:
      - -c
      - "kubectl logs -f --tail=0 $RESOURCE_NAME/$NAME -n $NAMESPACE --context $CONTEXT | gonzo"
```

> ⚠️ NOTE: on `macOS` although it is not required, defining `XDG_CONFIG_HOME=~/.config` is

## Usage

1. Launch k9s and navigate to pods
2. Select a pod and press `ctrl-l`
3. Gonzo opens with live log streaming and analysis
