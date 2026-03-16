---
name: treeverse-lakefs
description: "lakeFS - Data version control for your data lake | Git for data"
homepage: https://github.com/treeverse/lakeFS
metadata:
  openclaw:
    emoji: "📦"
    auto_generated: true
    requires:
      bins: ["docker", "lakefs", "pip"]
---

# Treeverse Lakefs

<p align="center">
  <img src="docs/src/assets/img/logo_large.png"/>
</p>
<p align="center">
	<a href="https://raw.githubusercontent.com/treeverse/lakeFS/master/LICENSE" >
		<img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="Apache License" /></a>
	<a href="https://github.com/treeverse/lakeFS/actions/workflows/test.yaml?query=branch%3Amaster">
		<img src="https://github.com/treeverse/lakeFS/workflows/Test/badge.svg?branch=master" alt="Go tests status" /></a>
	<a href="htt

## Installation

You can spin up a standalone sandbox instance of lakeFS:

```bash
pip install lakefs
python -m lakefs.quickstart
```

Once you've got lakeFS running, open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.
