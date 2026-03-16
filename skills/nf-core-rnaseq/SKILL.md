---
name: nf-core-rnaseq
description: "RNA sequencing analysis pipeline using STAR, RSEM, HISAT2 or Salmon with gene/isoform counts and"
homepage: https://github.com/nf-core/rnaseq
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
---

# Nf Core Rnaseq

<h1>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/images/nf-core-rnaseq_logo_dark.png">
    <img alt="nf-core/rnaseq" src="docs/images/nf-core-rnaseq_logo_light.png">
  </picture>
</h1>

[![Open in GitHub Codespaces](https://img.shields.io/badge/Open_In_GitHub_Codespaces-black?labelColor=grey&logo=github)](https://github.com/codespaces/new/nf-core/rnaseq)
[![GitHub Actions CI Status](https://github.com/nf-core/rnaseq/actions/workflows/nf-test.yml/badge.svg)](https://

## Usage

> [!NOTE]
> If you are new to Nextflow and nf-core, please refer to [this page](https://nf-co.re/docs/usage/installation) on how to set-up Nextflow. Make sure to [test your setup](https://nf-co.re/docs/usage/introduction#how-to-run-a-pipeline) with `-profile test` before running the workflow on actual data.

First, prepare a samplesheet with your input data that looks as follows:

**samplesheet.csv**:

```csv
sample,fastq_1,fastq_2,strandedness,seq_platform
CONTROL_REP1,AEG588A1_S1_L002_R1_001.f

```
