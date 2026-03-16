---
name: awslabs-aws-data-wrangler
description: "pandas on AWS - Easy integration with Athena, Glue, Redshift, Timestream, Neptune, OpenSearch,"
homepage: https://github.com/aws/aws-sdk-pandas
metadata:
  openclaw:
    emoji: "📦"
    auto_generated: true
    requires:
      bins: ["awswrangler", "pip"]
---

# Awslabs Aws Data Wrangler

# AWS SDK for pandas (awswrangler)

## Usage

Installation command: `pip install awswrangler`

> ⚠️ **Starting version 3.0, optional modules must be installed explicitly:**<br>
> ➡️`pip install 'awswrangler[redshift]'`

```py3
import awswrangler as wr
import pandas as pd
from datetime import datetime

df = pd.DataFrame({"id": [1, 2], "value": ["foo", "boo"]})

```
