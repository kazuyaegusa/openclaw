---
name: gorse-io-gorse
description: "AI powered open source recommender system engine supports classical/LLM rankers and multimodal"
homepage: https://github.com/gorse-io/gorse
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["curl", "docker", "node"]
---

# Gorse Io Gorse

# Gorse Open-source Recommender System Engine

## Usage

The playground mode has been prepared for beginners. Just set up a recommender system for GitHub repositories by the following commands.

```bash
docker run -p 8088:8088 zhenghaoz/gorse-in-one --playground
```

The playground mode will download data from [GitRec](https://gitrec.gorse.io/) and import it into Gorse. The dashboard is available at `http://localhost:8088`.

![](https://github.com/gorse-io/docs/blob/main/src/img/dashboard/overview.png?raw=true)

After the "Generate item-to-item recomm
