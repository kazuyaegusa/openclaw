---
name: hugoduncan-criterium
description: "Benchmarking library for clojure"
homepage: https://github.com/hugoduncan/criterium
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["git"]
---

# Hugoduncan Criterium

# Criterium

## Usage

The top level interface is in `criterium.core`.

    (use 'criterium.core)

Use `bench` to run a benchmark in a simple manner.

```
(bench (Thread/sleep 1000))
 =>
                   Execution time mean : 1.000803 sec
          Execution time std-deviation : 328.501853 us
         Execution time lower quantile : 1.000068 sec ( 2.5%)
         Execution time upper quantile : 1.001186 sec (97.5%)
```

By default bench is quiet about its progress. Run `with-progress-reporting` to
get progress infor
