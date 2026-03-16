---
name: radzenhq-radzen-blazor
description: "Radzen Blazor is the most sophisticated free UI component library for Blazor, featuring 100+ native"
homepage: https://github.com/radzenhq/radzen-blazor
metadata:
  openclaw:
    emoji: "🌐"
    auto_generated: true
---

# Radzenhq Radzen Blazor

![Radzen Blazor Components](https://raw.githubusercontent.com/radzenhq/radzen-blazor/master/RadzenBlazorDemos/wwwroot/images/radzen-blazor-components.png)

# Radzen Blazor Components

The most sophisticated free UI component library for Blazor, featuring **100+ native components**. MIT licensed, used by thousands of developers at companies like Microsoft, NASA, Porsche, Dell, Siemens, and DHL.

Supports .NET 10, Blazor Server, Blazor WebAssembly, and .NET MAUI Blazor Hybri

## Usage

Install the NuGet package:

```bash
dotnet add package Radzen.Blazor
```

Add to `_Imports.razor`:

```razor
@using Radzen
@using Radzen.Blazor
```

Add the theme and script to `App.razor`:

```html
<!-- inside <head> -->
<RadzenTheme Theme="material" />

<!-- after the last <script> -->
<script src="_content/Radzen.Blazor/Radzen.Blazor.js"></script>
```

Register services in `Program.cs`:

```csharp
builder.Services.AddRadzenComponents();
```

Use a component:

```razor
<RadzenButton Text="Hello Wor

```
