---
name: dani-garcia-vaultwarden
description: "Unofficial Bitwarden compatible server written in Rust, formerly known as bitwarden_rs"
homepage: https://github.com/dani-garcia/vaultwarden
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["docker"]
---

# Dani Garcia Vaultwarden

![Vaultwarden Logo](./resources/vaultwarden-logo-auto.svg)

An alternative server implementation of the Bitwarden Client API, written in Rust and compatible with [official Bitwarden clients](https://bitwarden.com/download/) [[disclaimer](#disclaimer)], perfect for self-hosted deployment where running the official resource-heavy service might not be ideal.

---

[![GitHub Release](https://img.shields.io/github/release/dani-garcia/vaultwarden.svg?style=for-the-badge&logo=vaultwarden&color=005AA4)]

## Usage

> [!IMPORTANT]
> The web-vault requires the use a secure context for the [Web Crypto API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API).
> That means it will only work via `http://localhost:8000` (using the port from the example below) or if you [enable HTTPS](https://github.com/dani-garcia/vaultwarden/wiki/Enabling-HTTPS).

The recommended way to install and use Vaultwarden is via our container images which are published to [ghcr.io](https://github.com/dani-garcia/vaultwarden
