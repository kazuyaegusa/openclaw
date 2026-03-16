---
name: anthropics-anthropic-sdk-go
description: "Access to Anthropic's safety-first language model APIs via Go"
homepage: https://github.com/anthropics/anthropic-sdk-go
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["go"]
---

# Anthropics Anthropic Sdk Go

# Anthropic Go API Library

## Installation

<!-- x-release-please-start-version -->

```go
import (
	"github.com/anthropics/anthropic-sdk-go" // imported as anthropic
)
```

<!-- x-release-please-end -->

Or to pin the version:

<!-- x-release-please-start-version -->

```sh
go get -u 'github.com/anthropics/anthropic-sdk-go@v1.26.0'
```

<!-- x-release-please-end -->

## Usage

The full API of this library can be found in [api.md](api.md).

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"), // defaults to os.LookupEnv("ANTHROPIC_API_KEY")
	)
	message, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
		MaxTokens: 1024,
		Messages: []anthropic.MessageParam{
			anthropic.

```
