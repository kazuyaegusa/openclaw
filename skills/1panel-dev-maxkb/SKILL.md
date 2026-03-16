---
name: 1panel-dev-maxkb
description: "🔥 MaxKB is an open-source platform for building enterprise-grade agents. 强大易用的开源企业级智能体平台。"
homepage: https://github.com/1Panel-dev/MaxKB
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins: ["docker"]
---

# 1panel Dev Maxkb

<p align="center"><img src= "https://github.com/1Panel-dev/maxkb/assets/52996290/c0694996-0eed-40d8-b369-322bf2a380bf" alt="MaxKB" width="300" /></p>
<h3 align="center">Open-source platform for building enterprise-grade agents</h3>
<h3 align="center">强大易用的企业级智能体平台</h3>
<p align="center"><a href="https://trendshift.io/repositories/9113" target="_blank"><img src="https://trendshift.io/api/badge/repositories/9113" alt="1Panel-dev%2FMaxKB | Trendshift" style="width: 250px; height: 55px;" width="250"

## Usage

Execute the script below to start a MaxKB container using Docker:

```bash
docker run -d --name=maxkb --restart=always -p 8080:8080 -v ~/.maxkb:/opt/maxkb 1panel/maxkb
```

Access MaxKB web interface at `http://your_server_ip:8080` with default admin credentials:

- username: admin
- password: MaxKB@123..

中国用户如遇到 Docker 镜像 Pull 失败问题，请参照该 [离线安装文档](https://maxkb.cn/docs/v2/installation/offline_installtion/) 进行安装。
