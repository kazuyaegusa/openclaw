---
name: seldonio-mlserver
description: "An inference server for your machine learning models, including support for multiple frameworks,"
homepage: https://github.com/SeldonIO/MLServer
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["mlserver", "mlserver-sklearn", "pip"]
---

# Seldonio Mlserver

MLServer aims to provide an easy way to start serving your machine learning
models through a REST and gRPC interface, fully compliant with [KFServing's V2
Dataplane](https://docs.seldon.io/projects/seldon-core/en/latest/reference/apis/v2-protocol.html)
spec. Watch a quick video introducing the project [here](https://www.youtube.com/watch?v=aZHe3z-8C_w).

- Multi-model serving, letting users run multiple models within the same
  process.
- Ability to run [inference in parallel for vertical
  scal

## Usage

You can install the `mlserver` package running:

```bash
pip install mlserver
```

Note that to use any of the optional [inference runtimes](#inference-runtimes),
you'll need to install the relevant package.
For example, to serve a `scikit-learn` model, you would need to install the
`mlserver-sklearn` package:

```bash
pip install mlserver-sklearn
```

For further information on how to use MLServer, you can check any of the
[available examples](#examples).
