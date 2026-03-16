---
name: lirantal-dockly
description: "Immersive terminal interface for managing docker containers and services"
homepage: https://github.com/lirantal/dockly
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["docker", "dockly", "npm"]
---

# Lirantal Dockly

<p align="center">
	<br>
  <img width="200" src="https://user-images.githubusercontent.com/316371/28937414-67ee5ffa-7893-11e7-95f9-5059cacf9170.png">
	<br>
 Immersive terminal interface for managing docker containers, services and images
</p>

[![Node Version](https://img.shields.io/badge/node-%3E=7.6.0-brightgreen.svg)]()
[![view on npm](http://img.shields.io/npm/v/dockly.svg)](https://www.npmjs.org/package/dockly)
[![view on npm](http://img.shields.io/npm/l/dockly.svg)](https://www.npmjs.org/

## Installation

Install the API module as a dependency in your project so you can easily use it to query Operations Orchestration REST API

```javascript
npm install -g dockly
```

## Usage

Just fire up dockly and it will automatically connect to your localhost docker daemon through the unix socket:

```
dockly
```
