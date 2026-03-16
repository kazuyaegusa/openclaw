---
name: open-mmlab-mmcv
description: "OpenMMLab Computer Vision Foundation"
homepage: https://github.com/open-mmlab/mmcv
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["go", "pip"]
---

# Open Mmlab Mmcv

<div align="center">
  <img src="https://raw.githubusercontent.com/open-mmlab/mmcv/main/docs/en/mmcv-logo.png" width="300"/>
  <div>&nbsp;</div>
  <div align="center">
    <b><font size="5">OpenMMLab website</font></b>
    <sup>
      <a href="https://openmmlab.com">
        <i><font size="4">HOT</font></i>
      </a>
    </sup>
    &nbsp;&nbsp;&nbsp;&nbsp;
    <b><font size="5">OpenMMLab platform</font></b>
    <sup>
      <a href="https://platform.openmmlab.com">
        <i><font size="4">TRY

## Installation

There are two versions of MMCV:

- **mmcv**: comprehensive, with full features and various CUDA ops out of the box. It takes longer time to build.
- **mmcv-lite**: lite, without CUDA ops but all other features, similar to mmcv\<1.0.0. It is useful when you do not need those CUDA ops.

**Note**: Do not install both versions in the same environment, otherwise you may encounter errors like `ModuleNotFound`. You need to uninstall one before installing the other. `Installing the full version is highl
