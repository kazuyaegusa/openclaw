---
name: realm-swiftlint
description: "A tool to enforce Swift style and conventions."
homepage: https://github.com/realm/SwiftLint
metadata:
  openclaw:
    emoji: "📦"
    auto_generated: true
    requires:
      bins: ["docker", "git", "go", "swiftlint"]
---

# Realm Swiftlint

SwiftLint is utterly maintained by volunteers contributing to its success
entirely in their free time. As such, SwiftLint isn't a commercial product
in any way.

Be kind to the people maintaining SwiftLint as a hobby and accept that their
time is limited. Support them by contributing to the project, reporting issues,
and helping others in the community.

Special thanks go to [MacStadium](https://www.macstadium.com) for providing
physical Mac mini machines to run our performance tests.

![MacStad

## Installation

> [!IMPORTANT]
> While it may seem intuitive to run SwiftLint before compiling Swift source
> files to exit a build early when there are lint violations, it is important
> to understand that SwiftLint is designed to analyze valid source code that
> is compilable. Non-compiling code can very easily lead to unexpected and
> confusing results, especially when executing with `--fix`/`--autocorrect`
> command line arguments.
