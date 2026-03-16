---
name: fastify-fastify-swagger
description: "Swagger documentation generator for Fastify"
homepage: https://github.com/fastify/fastify-swagger
metadata:
  openclaw:
    emoji: "📄"
    auto_generated: true
    requires:
      bins: ["curl", "npm"]
---

# Fastify Fastify Swagger

# @fastify/swagger

## Installation

```
npm i @fastify/swagger
```

## Usage

Add it with `register`, pass it options, call the `swagger` API, and you are done! Below is an example of configuring the OpenAPI v3 specification with Fastify Swagger:

```js
const fastify = require('fastify')()

await fastify.register(require('@fastify/swagger'), {
  openapi: {
    openapi: '3.0.0',
    info: {
      title: 'Test swagger',
      description: 'Testing the Fastify swagger API',
      version: '0.1.0'
    },
    servers: [
      {
        url: 'http://localhost:3000',
        des

```
