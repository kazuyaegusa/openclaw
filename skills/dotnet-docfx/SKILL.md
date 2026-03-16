---
name: dotnet-docfx
description: "Static site generator for .NET API documentation."
homepage: https://github.com/dotnet/docfx
metadata:
  openclaw:
    emoji: "📄"
    auto_generated: true
    requires:
      bins: ["git", "npm"]
---

# Dotnet Docfx

# Build your docs with docfx

## Installation

1. Install docfx as a global tool:

   ```bash
   dotnet tool install -g docfx
   ```

2. Create and start a website locally:

   ```
   docfx init -y
   docfx build docfx_project\docfx.json --serve
   ```

3. Go to https://localhost:8080 to see the sample site.

For more information, refer to [Getting Started](http://dotnet.github.io/docfx/tutorial/docfx_getting_started.html).

> [!TIP]
> Docfx publishes nightly builds to [GitHub Packages](https://github.com/orgs/dotnet/packages), this allow
