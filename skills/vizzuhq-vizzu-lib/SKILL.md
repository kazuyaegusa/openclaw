---
name: vizzuhq-vizzu-lib
description: "Library for animated data visualizations and data stories."
homepage: https://github.com/vizzuhq/vizzu-lib
metadata:
  openclaw:
    emoji: "📦"
    auto_generated: true
    requires:
      bins: ["npm", "vizzu"]
---

# Vizzuhq Vizzu Lib

<p align="center">
  <a href="https://lib.vizzuhq.com/latest/">
    <img src="https://lib.vizzuhq.com/latest/readme/infinite-60.gif" alt="Vizzu" />
  </a>
  <p align="center"><b>Vizzu</b> - Library for animated data visualizations and data stories.</p>
  <p align="center">
    <a href="https://lib.vizzuhq.com/latest/">Documentation</a>
    · <a href="https://lib.vizzuhq.com/latest/examples/">Examples</a>
    · <a href="https://lib.vizzuhq.com/latest/reference/">Code reference</a>
    ·

## Installation

Install via [npm](https://www.npmjs.com/package/vizzu):

```sh
npm install vizzu
```

Or use it from CDN:

```html
<html>
  <head>
    <script type="module">
      import Vizzu from "https://cdn.jsdelivr.net/npm/vizzu@latest/dist/vizzu.min.js";
    </script>
  </head>
</html>
```

## Usage

Create a placeholder element that will contain the rendered chart:

```html
<html>
  <body>
    <div id="myVizzu" style="width:800px; height:480px;"></div>
  </body>
</html>
```

Create a simple bar chart:

```javascript
import Vizzu from 'https://cdn.jsdelivr.net/npm/vizzu@latest/dist/vizzu.min.js';

let data = {
    series: [{
        name: 'Foo',
        values: ['Alice', 'Bob', 'Ted']
    }, {
        name: 'Bar',
        values: [15, 32, 12]
    }, {
        name: 'Ba

```
