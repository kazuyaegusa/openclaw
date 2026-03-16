---
name: agenticgokit-agenticgokit
description: "Open-source Agentic AI framework in Go for building, orchestrating, and deploying intelligent"
homepage: https://github.com/AgenticGoKit/AgenticGoKit
metadata:
  openclaw:
    emoji: "📦"
    auto_generated: true
    requires:
      bins: ["agk", "go"]
---

# Agenticgokit Agenticgokit

# AgenticGoKit

## Usage

**Start building immediately with the modern v1beta API:**

```go
package main

import (
    "context"
    "fmt"
    "log"
    "time"

    "github.com/agenticgokit/agenticgokit/v1beta"
)

func main() {
    // Create a chat agent with Ollama
    agent, err := v1beta.NewBuilder("ChatAgent").
        WithConfig(&v1beta.Config{
            Name:         "ChatAgent",
            SystemPrompt: "You are a helpful assistant",
            LLM: v1beta.LLMConfig{
                Provider: "ollama",


```
