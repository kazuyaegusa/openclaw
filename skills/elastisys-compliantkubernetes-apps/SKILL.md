---
name: elastisys-compliantkubernetes-apps
description: "Elastisys Compliant Kubernetes is an open source, Certified Kubernetes distribution designed"
homepage: https://github.com/elastisys/compliantkubernetes-apps
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["git", "node"]
---

# Elastisys Compliantkubernetes Apps

This repository is part of the [Elastisys Welkin®][welkin] application platform.
The platform consists of the following repositories:

- [compliantkubernetes-kubespray][compliantkubernetes-kubespray] - Code for managing Kubernetes clusters and the infrastructure around them.
- [compliantkubernetes-apps][compliantkubernetes-apps] - Code, configuration and tools for running various services and applications on top of Kubernetes clusters.

The Elastisys Welkin® application platform runs two Kuberne

## Installation

The apps are installed using a combination of helm charts and manifests with the help of helmfile and some bash scripts.

## Usage

- Deploy apps to the workload cluster:

  ```bash
  ./bin/ck8s apply wc
  ```

- Run tests on the service cluster:

  ```bash
  ./bin/ck8s test sc
  ```

- Port-forward to a Service in the workload cluster:

  ```bash
  ./bin/ck8s ops kubectl wc port-forward svc/<service> --namespace <namespace> <port>
  ```

- Run `helmfile diff` on a helm release:

  ```bash
  ./bin/ck8s ops helmfile sc -l <label=selector> diff
  ```
