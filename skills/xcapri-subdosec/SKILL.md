---
name: xcapri-subdosec
description: "Subdosec is a fast, accurate subdomain takeover scanner with no false positives. It also offers a"
homepage: https://github.com/xcapri/subdosec
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
    requires:
      bins: ["node"]
---

# Xcapri Subdosec

<p align="center">
<b>Subdosec</b>
</p>
<p align="center">
Subdomain takeover scanner & reconnaissance tool.
</p>

---

![Demo](img/final_demo.gif)

<p align="center">
  <a href="#installation">Install</a> •
  <a href="#running-subdosec">Usage</a> •
  <a href="#web-based">Web Based</a> •
  <a href="#contribution">Contribution</a> •
  <a href="#online-scan">Online scan</a> •
  <a href="#acknowledgments">Acknowledgments</a>
</p>

---

> Subdosec is a fast and accurate subdomain takeover scanner

## Installation

Install or upgrade subdosec

```
pipx install git+https://github.com/xcapri/subdosec.git
```

```
pipx upgrade subdosec
```

Then run this every time you start a new terminal session (until “server started successfully”).

```
$ subdosec -ins

Starting Node.js server...
Node.js server started successfully.
```

---
