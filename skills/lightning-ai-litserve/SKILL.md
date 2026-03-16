---
name: lightning-ai-litserve
description: "A minimal Python framework for building custom AI inference servers with full control over logic,"
homepage: https://github.com/Lightning-AI/LitServe
metadata:
  openclaw:
    emoji: "🖥️"
    auto_generated: true
    requires:
      bins: ["curl", "go", "litserve", "pip"]
---

# Lightning Ai Litserve

<div align='center'>

<h1>
  Build custom inference servers in pure Python
  <br/>
</h1> 
<h4>
  Define exactly how inference works for models, agents, RAG, or pipelines. 
  <br/>
  Control batching, routing, streaming, and orchestration without MLOps glue or config files.
</h4>

<img alt="Lightning" src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/ls_banner2.png" width="800px" style="max-width: 100%;">

&nbsp;

</div>

<div align='center'>
  
<pre>
✅ Custom inference logic  ✅

## Usage

Install LitServe via pip ([more options](https://lightning.ai/docs/litserve/home/install)):

```bash
pip install litserve
```

[Example 1](#inference-engine-example): Toy inference pipeline with multiple models.  
[Example 2](#agent-example): Minimal agent to fetch the news (with OpenAI API).  
([Advanced examples](#featured-examples)):
