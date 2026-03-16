---
name: blazemeter-taurus
description: "Automation-friendly framework for Continuous Testing by"
homepage: https://github.com/Blazemeter/taurus
metadata:
  openclaw:
    emoji: "🗄️"
    auto_generated: true
    requires:
      bins: ["bzt", "pip"]
---

# Blazemeter Taurus

# Taurus

## Installation

Create a file named `test.yml` with following contents:

```yaml
---
execution:
  - concurrency: 10
    ramp-up: 1m
    hold-for: 1m30s
    scenario: simple

scenarios:
  simple:
    think-time: 0.75
    requests:
      - http://blazedemo.com/
      - http://blazedemo.com/vacation.html
```

Then run `bzt test.yml`. After the tool finishes, observe resulting summary stats in console log (for more reporting options, see [Generating Test Reports](https://gettaurus.org/docs/Reporting.md)). All artifact files
