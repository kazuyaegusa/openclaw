---
name: casey-just
description: "🤖 Just a command runner"
homepage: https://github.com/casey/just
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["cargo", "cargo-watch", "curl", "git", "go", "just", "node", "npm", "python3"]
---

# Casey Just

<div align=right>Table of Contents↗️</div>

<h1 align=center><code>just</code></h1>

<div align=center>
  <a href=https://crates.io/crates/just>
    <img src=https://img.shields.io/crates/v/just.svg alt="crates.io version">
  </a>
  <a href=https://github.com/casey/just/actions/workflows/ci.yaml>
    <img src=https://github.com/casey/just/actions/workflows/ci.yaml/badge.svg alt="build status">
  </a>
  <a href=https://github.com/casey/just/releases>
    <img src=https://img.shields.io/github/dow

## Installation

`just` is written in Rust. Use
[rustup](https://www.rust-lang.org/tools/install) to install a Rust toolchain.

`just` is extensively tested. All new features must be covered by unit or
integration tests. Unit tests are under
[src](https://github.com/casey/just/blob/master/src), live alongside the code
being tested, and test code in isolation. Integration tests are in the [tests
directory](https://github.com/casey/just/blob/master/tests) and test the `just`
binary from the outside by invoking `ju
