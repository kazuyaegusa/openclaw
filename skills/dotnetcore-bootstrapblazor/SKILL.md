---
name: dotnetcore-bootstrapblazor
description: "Bootstrap Blazor is an enterprise-level UI component library based on Bootstrap and Blazor."
homepage: https://github.com/dotnetcore/BootstrapBlazor
metadata:
  openclaw:
    emoji: "🌐"
    auto_generated: true
---

# Dotnetcore Bootstrapblazor

<h1 align="center">Bootstrap Blazor Component</h1>

<div align="center">
<h2>Bootstrap Blazor is an enterprise-level UI component library based on Bootstrap and Blazor.</h2>

[![License](https://img.shields.io/github/license/dotnetcore/BootstrapBlazor.svg?logo=git&logoColor=red)](https://github.com/dotnetcore/BootstrapBlazor/blob/main/LICENSE)
[![Nuget](https://img.shields.io/nuget/v/BootstrapBlazor.svg?color=red&logo=nuget&logoColor=green)](https://www.nuget.org/packages/BootstrapBlazor/)
[![Nu

## Usage

```razor
<Display Value="@_text"></Display>
<Button Text="Button" OnClick="@ClickButton"></Button>

@code {
    private string? _text;
    private void ClickButton(MouseEventArgs e)
    {
        _text = DateTime.Now.ToString();
    }
}
```
