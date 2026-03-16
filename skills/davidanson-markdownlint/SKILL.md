---
name: davidanson-markdownlint
description: "A Node.js style checker and lint tool for Markdown/CommonMark files."
homepage: https://github.com/DavidAnson/markdownlint
metadata:
  openclaw:
    emoji: "📄"
    auto_generated: true
    requires:
      bins: ["markdownlint", "npm"]
---

# Davidanson Markdownlint

The [Markdown][markdown] markup language is designed to be easy to read, write,
and understand. It succeeds - and its flexibility is both a benefit and a
drawback. Many styles are possible, so formatting can be inconsistent; some
constructs don't work well in all parsers and should be avoided.

`markdownlint` is a [static analysis][static-analysis] tool for
[Node.js][nodejs] with a library of rules to enforce standards and consistency
for Markdown files. It was inspired by - and heavily influenc

## Installation

```bash
npm install markdownlint --save-dev
```

## Usage

Invoke `lint` as an asynchronous call:

```javascript
import { lint as lintAsync } from "markdownlint/async";

const options = {
  files: ["good.md", "bad.md"],
  strings: {
    "good.string": "# good.string\n\nThis string passes all rules.",
    "bad.string": "#bad.string\n\n#This string fails\tsome rules.",
  },
};

lintAsync(options, function callback(error, results) {
  if (!error && results) {
    console.dir(results, { colors: true, depth: null });
  }
});
```

Or as a synchronous
