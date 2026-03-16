---
name: laa-software-engineering-golang-rest-api-template
description: "Template for REST API made with Golang using Gin framework, PostgreSQL database, JWT"
homepage: https://github.com/LAA-Software-Engineering/golang-rest-api-template
metadata:
  openclaw:
    emoji: "🖥️"
    auto_generated: true
    requires:
      bins: ["curl", "git", "pip"]
---

# Laa Software Engineering Golang Rest Api Template

This repository provides a template for building a RESTful API using Go with features like JWT Authentication, rate limiting, Swagger documentation, and database operations using GORM. The application uses the Gin Gonic web framework and is containerized using Docker.

## Installation

1. Clone the repository

```bash
git clone https://github.com/araujo88/golang-rest-api-template
```

2. Navigate to the directory

```bash
cd golang-rest-api-template
```

3. Build and run the Docker containers

```bash
make up
```

Please refer to the [Makefile](./Makefile) if you need to build in the local environment.
