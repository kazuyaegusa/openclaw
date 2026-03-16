---
name: concourse-concourse
description: "Concourse is a container-based automation system written in Go. It's mostly used for CI/CD."
homepage: https://github.com/concourse/concourse
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["git"]
---

# Concourse Concourse

# Concourse: the continuous thing-doer

## Installation

Concourse is distributed as a single `concourse` binary, available on the [Releases page](https://github.com/concourse/concourse/releases/latest).

If you want to just kick the tires, jump ahead to the [Quick Start](#quick-start).

In addition to the `concourse` binary, there are a few other supported formats.
Consult their GitHub repos for more information:

- [Docker image](https://github.com/concourse/concourse-docker)
- [Kubernetes Helm chart](https://github.com/concourse/concourse-chart)
-

## Usage

```sh
$ wget https://concourse-ci.org/docker-compose.yml
$ docker-compose up -d
Creating docs_concourse-db_1 ... done
Creating docs_concourse_1    ... done
```

Concourse will be running at [http://localhost:8080](http://localhost:8080).
You can log in with the username/password as `test`/`test`.

Next, install `fly` by downloading it from the web UI at
[http://localhost:8080/download-fly](http://localhost:8080/download-fly) and
target your local Concourse as the `test` user:

```sh
$ fly -t ci

```
