---
name: nolar-kopf
description: "A Python framework to write Kubernetes operators in just a few lines of code"
homepage: https://github.com/nolar/kopf
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["docker", "kopf", "pip"]
---

# Nolar Kopf

# Kubernetes Operator Pythonic Framework (Kopf)

## Usage

See [examples](https://github.com/nolar/kopf/tree/main/examples)
for examples of typical use cases.

A minimalistic operator can look like this:

```python
import kopf

@kopf.on.create('kopfexamples')
def create_fn(spec, name, meta, status, **kwargs):
    print(f"And here we are! Created {name} with spec: {spec}")
```

Numerous kwargs are available, such as `body`, `meta`, `spec`, `status`,
`name`, `namespace`, `retry`, `diff`, `old`, `new`, `logger`, etc:
see [Arguments](https://docs.kopf.dev/e
