---
name: dedoc-scramble
description: "Modern Laravel OpenAPI (Swagger) documentation generator. No PHPDoc annotations required."
homepage: https://github.com/dedoc/scramble
metadata:
  openclaw:
    emoji: "📄"
    auto_generated: true
---

# Dedoc Scramble

<p>
  <a href="https://scramble.dedoc.co" target="_blank">
    <img src="./.github/gh-img.png?v=1" alt="Scramble – Laravel API documentation generator"/>
  </a>
</p>

## Installation

You can install the package via composer:

```shell
composer require dedoc/scramble
```

## Usage

After install you will have 2 routes added to your application:

- `/docs/api` - UI viewer for your documentation
- `/docs/api.json` - Open API document in JSON format describing your API.

By default, these routes are available only in `local` environment. You can change this behavior [by defining `viewApiDocs` gate](https://scramble.dedoc.co/usage/getting-started#docs-authorization).

---

<p>
  <a href="https://savelife.in.ua/en/donate-en/" target="_blank">
    <img src="./.github/gh-promo.sv
