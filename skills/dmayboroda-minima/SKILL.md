---
name: dmayboroda-minima
description: "On-premises conversational RAG with configurable containers"
homepage: https://github.com/dmayboroda/minima
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins: ["docker", "go", "npm"]
---

# Dmayboroda Minima

<p align="center">
  <a href="https://mnma.ai/" target="blank"><img src="assets/logo-full.svg" width="300" alt="MNMA Logo" /></a>
</p>

**Minima** is an open source RAG on-premises containers, with ability to integrate with ChatGPT and MCP.
Minima can also be used as a fully local RAG or with your own deployed LLM.

Minima currently supports four modes:

1. **Isolated installation (Ollama)** – Operate fully on-premises with containers, free from external dependencies such as ChatGPT or Claude. Al

## Usage

**Example of .env file for on-premises/local usage with Ollama:**

```
LOCAL_FILES_PATH=/Users/davidmayboroda/Downloads/PDFs/
EMBEDDING_MODEL_ID=sentence-transformers/all-mpnet-base-v2
EMBEDDING_SIZE=768
OLLAMA_MODEL=qwen2:0.5b # must be LLM model id from Ollama models page
RERANKER_MODEL=BAAI/bge-reranker-base # please, choose any BAAI reranker model
```

**Example of .env file for custom LLM deployment (OpenAI-compatible API):**

```
LOCAL_FILES_PATH=/Users/davidmayboroda/Downloads/PDFs/
EMBEDDI

```
