---
name: nf-core-sarek
description: "Analysis pipeline to detect germline or somatic variants (pre-processing, variant calling and"
homepage: https://github.com/nf-core/sarek
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
---

# Nf Core Sarek

<h1>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/images/nf-core-sarek_logo_dark.png">
    <img alt="nf-core/sarek" src="docs/images/nf-core-sarek_logo_light.png">
  </picture>
</h1>

[![Open in GitHub Codespaces](https://img.shields.io/badge/Open_In_GitHub_Codespaces-black?labelColor=grey&logo=github)](https://github.com/codespaces/new/nf-core/sarek)
[![GitHub Actions CI Status](https://github.com/nf-core/sarek/actions/workflows/nf-test.yml/badge.svg)](https://githu

## Usage

> [!NOTE]
> If you are new to Nextflow and nf-core, please refer to [this page](https://nf-co.re/docs/usage/installation) on how to set-up Nextflow. Make sure to [test your setup](https://nf-co.re/docs/usage/introduction#how-to-run-a-pipeline) with `-profile test` before running the workflow on actual data.

First, prepare a samplesheet with your input data that looks as follows:

`samplesheet.csv`:

```csv
patient,sample,lane,fastq_1,fastq_2
ID1,S1,L002,ID1_S1_L002_R1_001.fastq.gz,ID1_S1_L002_R

```
