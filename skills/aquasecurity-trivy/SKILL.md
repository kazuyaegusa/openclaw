---
name: aquasecurity-trivy
description: "Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code"
homepage: https://github.com/aquasecurity/trivy
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["docker", "go", "trivy"]
---

# Aquasecurity Trivy

<div align="center">
<img src="docs/imgs/logo.png" width="200">

[![GitHub Release][release-img]][release]
[![Test][test-img]][test]
[![Go Report Card][go-report-img]][go-report]
[![License: Apache-2.0][license-img]][license]
[![GitHub Downloads][github-downloads-img]][release]
![Docker Pulls][docker-pulls]

[📖 Documentation][docs]

</div>

Trivy ([pronunciation][pronunciation]) is a comprehensive and versatile security scanner.
Trivy has _scanners_ that look for security issues, and _targets_ wh
