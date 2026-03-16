---
name: percona-pmm
description: "Percona Monitoring and Management: an open source database monitoring, observability and management"
homepage: https://github.com/percona/pmm
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
    requires:
      bins: ["docker", "node"]
---

# Percona Pmm

# Percona Monitoring and Management

## Installation

There are numbers of installation methods, please check our [About PMM installation](https://docs.percona.com/percona-monitoring-and-management/3/install-pmm/index.html) documentation page.

But in a nutshell:

1. Download PMM server Docker image:

```bash
$ docker pull percona/pmm-server:3
```

2. Create the data volume container:

```bash
$ docker volume create pmm-data
```

3. Run PMM Server container:

```bash
$ docker run --detach --restart always \
  --publish 443:8443 \
  --volume pmm-data:/sr



```
