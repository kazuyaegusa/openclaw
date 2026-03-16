---
name: graphql-hive-graphql-modules
description: "Enterprise Grade Tooling For Your GraphQL Server"
homepage: https://github.com/graphql-hive/graphql-modules
metadata:
  openclaw:
    emoji: "🖥️"
    auto_generated: true
    requires:
      bins: ["graphql-modules", "npm"]
---

# Graphql Hive Graphql Modules

[![modules](https://user-images.githubusercontent.com/25294569/64067074-ed185b80-cc2a-11e9-8f4d-5f1e19feaa0a.gif)](https://graphql-modules.com/)

[![npm version](https://badge.fury.io/js/graphql-modules.svg)](https://www.npmjs.com/package/graphql-modules)
![CI](https://github.com/graphql-hive/graphql-modules/workflows/CI/badge.svg)
[![Discord Chat](https://img.shields.io/discord/625400653321076807)](https://the-guild.dev/discord)
[![GitHub license](https://img.shields.io/badge/license-MIT-lightg

## Installation

To install graphql-modules, use the following:

````sh
$ npm install graphql-modules



## Usage

More advanced usage at [graphql-modules.com](https://graphql-modules.com/docs)

```js
import { createModule, createApplication, gql } from 'graphql-modules'

const module = createModule({
  id: 'my-module',
  typeDefs: gql`
    type Post {
      id: ID
      title: String
      author: User
    }

    type Query {
      posts: [Post]
    }
  `,
  resolvers: blogResolvers
})

const application = createApplication({
  modules: [module]
})
````

Inside the `examples` directory you can find the follo
