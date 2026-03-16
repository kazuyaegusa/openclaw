---
name: cloudposse-terraform-datadog-platform
description: "Terraform module to configure and provision Datadog monitors, custom RBAC roles with permissions,"
homepage: https://github.com/cloudposse/terraform-datadog-platform
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
---

# Cloudposse Terraform Datadog Platform

<!-- markdownlint-disable -->

<a href="https://cpco.io/homepage"><img src="https://github.com/cloudposse/terraform-datadog-platform/blob/main/.github/banner.png?raw=true" alt="Project Banner"/></a><br/>

<p align="right"><a href="https://github.com/cloudposse/terraform-datadog-platform/releases/latest"><img src="https://img.shields.io/github/release/cloudposse/terraform-datadog-platform.svg?style=for-the-badge" alt="Latest Release"/></a><a href="https://github.com/cloudposse/terraform-datadog-p

## Usage

Provision Datadog monitors from the catalog of YAML definitions:

```hcl
module "monitor_configs" {
  source  = "cloudposse/config/yaml"
  version = "1.0.2"

  map_config_local_base_path = path.module
  map_config_paths           = var.monitor_paths

  context = module.this.context
}

module "datadog_monitors" {
  source = "cloudposse/platform/datadog//modules/monitors"
  # version = "x.x.x"

  datadog_monitors     = module.monitor_configs.map_configs
  alert_tags           = var.alert_tags
  al

```
