---
name: nf-core-methylseq
description: "Methylation (Bisulfite-Sequencing) analysis pipeline using Bismark/bwa-meth + MethylDackel or"
homepage: https://github.com/nf-core/methylseq
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
---

# Nf Core Methylseq

<h1>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/images/nf-core-methylseq_logo_dark.png">
    <img alt="nf-core/methylseq" src="docs/images/nf-core-methylseq_logo_light.png">
  </picture>
</h1>

[![Open in GitHub Codespaces](https://img.shields.io/badge/Open_In_GitHub_Codespaces-black?labelColor=grey&logo=github)](https://github.com/codespaces/new/nf-core/methylseq)
[![GitHub Actions CI Status](https://github.com/nf-core/methylseq/actions/workflows/nf-test.yml/badge

## Usage

> [!NOTE]
> If you are new to Nextflow and nf-core, please refer to [this page](https://nf-co.re/docs/usage/installation) on how to set-up Nextflow. Make sure to [test your setup](https://nf-co.re/docs/usage/introduction#how-to-run-a-pipeline) with `-profile test` before running the workflow on actual data.

First, prepare a samplesheet with your input data that looks as follows:

`samplesheet.csv`:

```csv
sample,fastq_1,fastq_2,genome
SRR389222_sub1,https://github.com/nf-core/test-datasets/raw

```
