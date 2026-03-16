---
name: graphieros-vue-data-ui
description: "An open source user-empowering data visualization Vue 3 components library for eloquent data"
homepage: https://github.com/graphieros/vue-data-ui
metadata:
  openclaw:
    emoji: "📦"
    auto_generated: true
    requires:
      bins: ["npm"]
---

# Graphieros Vue Data Ui

<p align="center">
    <a href="https://vue-data-ui.graphieros.com/"><img width="500" src="https://github.com/user-attachments/assets/19d4334d-679c-4c19-bc4f-6050810afa05"></a>
    <br>
    <a href="https://vue-data-ui.graphieros.com/"><img width="100%" src="https://github.com/user-attachments/assets/0474eb0e-0918-43e1-9756-30a5a8052d82"></a>

</p>

## Installation

```
npm i vue-data-ui
```

You can declare components globally in your main.js:

```js
import { createApp } from "vue";
import App from "./App.vue";
// Include the css;
import "vue-data-ui/style.css";

// You can declare Vue Data UI components globally
import { VueUiRadar } from "vue-data-ui";

const app = createApp(App);

app.component("VueUiRadar", VueUiRadar);
app.mount("#app");
```

Or you can import just what you need into your files:

```js
<script setup>import {(VueUiRadar, VueUiXy)} from



```
