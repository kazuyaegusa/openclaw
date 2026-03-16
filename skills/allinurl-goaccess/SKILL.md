---
name: allinurl-goaccess
description: "GoAccess is a real-time web log analyzer and interactive viewer that runs in a terminal in *nix"
homepage: https://github.com/allinurl/goaccess
metadata:
  openclaw:
    emoji: "📦"
    auto_generated: true
    requires:
      bins: ["curl", "docker", "git", "goaccess"]
---

# Allinurl Goaccess

# GoAccess [![C build](https://github.com/allinurl/goaccess/actions/workflows/build-test.yml/badge.svg)](https://github.com/allinurl/goaccess/actions/workflows/build-test.yml) [![GoAccess](https://goaccess.io/badge)](https://goaccess.io)

## Installation

<a href="https://repology.org/project/goaccess/versions">
    <img src="https://repology.org/badge/vertical-allrepos/goaccess.svg" alt="Packaging status" align="right">
</a>

## Usage

// last month access log # goaccess access.log.1 --persist

then, load it with

    // append this month access log, and preserve new data
    # goaccess access.log --restore --persist

To read persisted data only (without parsing new data)

    # goaccess --restore
