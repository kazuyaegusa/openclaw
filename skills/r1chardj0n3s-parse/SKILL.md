---
name: r1chardj0n3s-parse
description: "Parse strings using a specification based on the Python format() syntax."
homepage: https://github.com/r1chardj0n3s/parse
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
    requires:
      bins: ["git", "parse", "pip"]
---

# R1chardj0n3s Parse

## Installation

.. code-block:: pycon

    pip install parse

## Usage

Parse strings using a specification based on the Python `format()`\_ syntax.

`parse()` is the opposite of `format()`

The module is set up to only export `parse()`, `search()`, `findall()`,
and `with_pattern()` when `import *` is used:

> > > from parse import \*

From there it's a simple thing to parse a string:

.. code-block:: pycon

    >>> parse("It's {}, I love it!", "It's spam, I love it!")
