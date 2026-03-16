---
name: jetstack-cert-manager
description: "Automatically provision and manage TLS certificates in Kubernetes"
homepage: https://github.com/cert-manager/cert-manager
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["go"]
---

# Jetstack Cert Manager

<p align="center">
  <img src="./logo/logo-small.png" height="256" width="256" alt="cert-manager project logo" />
</p>
<!-- note that the cert-manager logo in this repo is referred to in other README files in the cert-manager org
     as well as in Helm charts, etc.
     if you change its location or name, you'll need to update several other repos too! -->

<p align="center"><a href="https://prow.infra.cert-manager.io/?job=ci-cert-manager-master-make-test">
<!-- prow build badge, godoc, and go r

## Installation

[Installation](https://cert-manager.io/docs/installation/) is documented on the website, with a variety of supported methods.
