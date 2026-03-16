---
name: aklivity-zilla
description: "🦎 A multi-protocol edge & service proxy. Seamlessly interface web apps, IoT clients, &"
homepage: https://github.com/aklivity/zilla
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["curl", "docker", "git"]
---

# Aklivity Zilla

<div id="top"></div>
<div align="center">
  <img src="./assets/zilla-rings@2x.png" height="250">
</div>

</br>

<div align="center">

  <!--[![Build Status][build-status-image]][build-status]-->

[![Latest Release][release-latest-image]][release-latest]
[![Slack Community][community-image]][community-join]
[![Artifact HUB][artifact-hub-shield]][artifact-hub]

</div>

<h3 align="center">
  <a href="https://docs.aklivity.io/zilla/"><b>Docs</b></a> &bull;
  <a href="https://docs.aklivity.io

## Installation

Zilla has no external dependencies. Pick your preferred deployment method:

**Docker**

```bash
docker pull ghcr.io/aklivity/zilla
docker run ghcr.io/aklivity/zilla:latest start -v
```

**Helm (Kubernetes)**

```bash
helm install zilla oci://ghcr.io/aklivity/charts/zilla \
  --namespace zilla --create-namespace --wait \
  --values values.yaml \
  --set-file zilla\\.yaml=zilla.yaml
```

Both single-node and clustered deployments are supported.
