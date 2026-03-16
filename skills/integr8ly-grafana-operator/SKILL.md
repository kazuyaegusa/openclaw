---
name: integr8ly-grafana-operator
description: "An operator for Grafana that installs and manages Grafana instances, Dashboards and Datasources"
homepage: https://github.com/grafana/grafana-operator
metadata:
  openclaw:
    emoji: "📦"
    auto_generated: true
---

# Integr8ly Grafana Operator

<div align="center">

## Installation

**Option 1: Helm Chart**

Deploy the Grafana Operator easily in your cluster using Helm:

```bash
helm upgrade -i grafana-operator oci://ghcr.io/grafana/helm-charts/grafana-operator --version 5.22.0
```

**Option 2: Kustomize & More**

Prefer Kustomize, Openshift OLM, or Kubernetes directly? Find detailed instructions in our [Installation Guide](https://grafana.github.io/grafana-operator/docs/installation/kustomize/).

For even more detailed setups, see our [documentation](docs/README.md).
