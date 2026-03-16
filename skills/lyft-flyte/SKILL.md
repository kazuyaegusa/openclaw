---
name: lyft-flyte
description: "Scalable and flexible workflow orchestration platform that seamlessly unifies data, ML and"
homepage: https://github.com/flyteorg/flyte
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["flytekit", "pip"]
---

# Lyft Flyte

> [!IMPORTANT]
>
> ## Looking for Flyte 2?
>
> - **Use Flyte locally?** Head to **[flyte-sdk](https://github.com/flyteorg/flyte-sdk)** — the new Python SDK for Flyte 2.
> - **Want to contribute to the distributed backend?** See the **[`v2` branch](https://github.com/flyteorg/flyte/tree/v2)** of this repo.
>
> **The README below is for Flyte 1.x.**

---

<p align="center">
  <img src="https://raw.githubusercontent.com/flyteorg/static-resources/main/flyte/readme/flyte_and_lf.png" alt="Flyte and LF A

## Usage

1. Install Flyte's Python SDK

```bash
pip install flytekit
```

2. Create a workflow (see [example](https://github.com/flyteorg/flytesnacks/blob/master/examples/basics/basics/hello_world.py))
3. Run it locally with:

```bash
pyflyte run hello_world.py hello_world_wf
```

**Ready to try a Flyte cluster?**

1. Create a new sandbox cluster, running as a Docker container:

```bash
flytectl demo start
```

2. Now execute your workflows on the cluster:

```bash
pyflyte run --remote hello_world.py hello_worl

```
