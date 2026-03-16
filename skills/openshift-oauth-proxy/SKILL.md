---
name: openshift-oauth-proxy
description: "A reverse proxy that provides authentication with OpenShift via OAuth and Kubernetes service"
homepage: https://github.com/openshift/oauth-proxy
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["docker", "go"]
---

# Openshift Oauth Proxy

# OpenShift oauth-proxy

A reverse proxy and static file server that provides authentication and authorization to an OpenShift OAuth
server or Kubernetes master supporting the 1.6+ remote authorization endpoints to validate access to content.
It is intended for use within OpenShift clusters to make it easy to run both end-user and infrastructure
services that don't provide their own authentication.

Features:

- Performs zero-configuration OAuth when run as a pod in OpenShift
