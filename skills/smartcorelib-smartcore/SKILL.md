---
name: smartcorelib-smartcore
description: "A comprehensive library for machine learning and numerical computing. Apply Machine Learning with"
homepage: https://github.com/smartcorelib/smartcore
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["git"]
---

# Smartcorelib Smartcore

<p align="center">
  <a href="https://smartcorelib.org">
    <img src="smartcore.svg" width="450" alt="smartcore">    
  </a>  
</p>
<p align = "center">
    <strong>
        <a href="https://smartcorelib.org">User guide</a> | <a href="https://docs.rs/smartcore/">API</a> | <a href="https://github.com/smartcorelib/smartcore-jupyter">Notebooks</a>
    </strong>
</p>

---

<p align = "center">
<b>Machine Learning in Rust</b>
</p>

---

[![CI](https://github.com/smartcorelib/smartcore/actions/wor

## Installation

Add to Cargo.toml:

```toml
[dependencies]
smartcore = "^0.4.3"
```

For the latest development branch:

```toml
[dependencies]
smartcore = { git = "https://github.com/smartcorelib/smartcore", branch = "development" }
```

Optional features (examples):

- datasets
- serde
- ndarray-bindings (deprecated in favor of ndarray-only support per recent changes)

Check Cargo.toml for available features and compatibility notes.

## Usage

Here is a minimal example fitting a KNN classifier from native Rust vectors using DenseMatrix:

```rust
use smartcore::linalg::basic::matrix::DenseMatrix;
use smartcore::neighbors::knn_classifier::KNNClassifier;

// Turn vector slices into a matrix
let x = DenseMatrix::from_2d_array(&[
    &[1., 2.],
    &[3., 4.],
    &[5., 6.],
    &[7., 8.],
    &[9., 10.],
]).unwrap;

// Class labels
let y = vec![2, 2, 2, 3, 3];

// Train classifier
let knn = KNNClassifier::fit(&x, &y, Default::default()).un

```
