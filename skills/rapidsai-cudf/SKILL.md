---
name: rapidsai-cudf
description: "cuDF - GPU DataFrame Library"
homepage: https://github.com/rapidsai/cudf
metadata:
  openclaw:
    emoji: "📦"
    auto_generated: true
    requires:
      bins:
        [
          "cudf-cu12",
          "cudf-cu13",
          "cudf-polars-cu12",
          "cudf-polars-cu13",
          "dask-cudf-cu12",
          "dask-cudf-cu13",
          "libcudf-cu12",
          "libcudf-cu13",
          "pip",
          "pylibcudf-cu12",
          "pylibcudf-cu13",
        ]
---

# Rapidsai Cudf

cuDF is composed of multiple libraries including:

- [libcudf](https://docs.rapids.ai/api/cudf/stable/libcudf_docs/): A CUDA C++ library with [Apache Arrow](https://arrow.apache.org/) compliant
  data structures and fundamental algorithms for tabular data.
- [pylibcudf](https://docs.rapids.ai/api/cudf/stable/pylibcudf/): A Python library providing [Cython](https://cython.org/) bindings for libcudf.
- [cudf](https://docs.rapids.ai/api/cudf/stable/user_guide/): A Python library providing
  - A Dat

## Usage

The following examples showcase reading a parquet file, dropping missing rows with a null value,
and performing a groupby aggregation on the data.
