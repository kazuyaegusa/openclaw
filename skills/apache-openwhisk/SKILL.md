---
name: apache-openwhisk
description: "Apache OpenWhisk is an open source serverless cloud platform"
homepage: https://github.com/apache/openwhisk
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["git"]
---

# Apache Openwhisk

<!--




## Usage

The easiest way to start using OpenWhisk is to install the "Standalone" OpenWhisk stack.
This is a full-featured OpenWhisk stack running as a Java process for convenience.
Serverless functions run within Docker containers. You will need [Docker](https://docs.docker.com/install),
[Java](https://java.com/en/download/help/download_options.xml) and [Node.js](https://nodejs.org) available on your machine.

To get started:
```
git clone https://github.com/apache/openwhisk.git
cd openwhisk
./gradlew co
