---
name: phpro-grumphp
description: "A PHP code-quality tool"
homepage: https://github.com/phpro/grumphp
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["git"]
---

# Phpro Grumphp

[![Github Actions](https://github.com/phpro/grumphp/workflows/GrumPHP/badge.svg?branch=master)](https://github.com/phpro/grumphp/actions/workflows/grumphp.yml)
[![AppVeyor](https://ci.appveyor.com/api/projects/status/ttlbau2sjg36ep01/branch/master?svg=true)](https://ci.appveyor.com/project/veewee/grumphp/branch/master)
[![Installs](https://img.shields.io/packagist/dt/phpro/grumphp.svg)](https://packagist.org/packages/phpro/grumphp/stats)
[![Packagist](https://img.shields.io/packagist/v/phpro/gru

## Installation

In order for this package to work, you have to make sure following tools are discoverable on the command-line:

- php
- composer
- git

This package is a composer plugin and should be installed to your project's dev dependency using composer:

Install GrumPHP as a phar without dependencies:

```sh
composer require --dev phpro/grumphp-shim
```

Install GrumPHP with dependencies:

```
composer require --dev phpro/grumphp
```

Install GrumPHP without dependencies and automated git hooks through phive
