---
name: facebook-react
description: "The library for web and native user interfaces."
homepage: https://github.com/facebook/react
metadata:
  openclaw:
    emoji: "🌐"
    auto_generated: true
---

# Facebook React

# [React](https://react.dev/) &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/facebook/react/blob/main/LICENSE) [![npm version](https://img.shields.io/npm/v/react.svg?style=flat)](https://www.npmjs.com/package/react) [![(Runtime) Build and Test](https://github.com/facebook/react/actions/workflows/runtime_build_and_test.yml/badge.svg)](https://github.com/facebook/react/actions/workflows/runtime_build_and_test.yml) [![(Compiler) TypeScript](https:

## Installation

React has been designed for gradual adoption from the start, and **you can use as little or as much React as you need**:

- Use [Quick Start](https://react.dev/learn) to get a taste of React.
- [Add React to an Existing Project](https://react.dev/learn/add-react-to-an-existing-project) to use as little or as much React as you need.
- [Create a New React App](https://react.dev/learn/start-a-new-react-project) if you're looking for a powerful JavaScript toolchain.

## Usage

We have several examples [on the website](https://react.dev/). Here is the first one to get you started:

```jsx
import { createRoot } from "react-dom/client";

function HelloMessage({ name }) {
  return <div>Hello {name}</div>;
}

const root = createRoot(document.getElementById("container"));
root.render(<HelloMessage name="Taylor" />);
```

This example will render "Hello Taylor" into a container on the page.

You'll notice that we used an HTML-like syntax; [we call it JSX](https://react.dev/l
