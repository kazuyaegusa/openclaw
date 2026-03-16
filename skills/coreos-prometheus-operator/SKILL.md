---
name: coreos-prometheus-operator
description: "Prometheus Operator creates/configures/manages Prometheus clusters atop Kubernetes"
homepage: https://github.com/prometheus-operator/prometheus-operator
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["go", "node"]
---

# Coreos Prometheus Operator

The Prometheus Operator provides [Kubernetes](https://kubernetes.io/) native deployment and management of
[Prometheus](https://prometheus.io/) and related monitoring components. The purpose of this project is to
simplify and automate the configuration of a Prometheus based monitoring stack for Kubernetes clusters.

The Prometheus operator includes, but is not limited to, the following features:

- **Kubernetes Custom Resources**: Use Kubernetes custom resources to deploy and manage Prometheus, A
