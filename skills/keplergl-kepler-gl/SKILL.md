---
name: keplergl-kepler-gl
description: "Kepler.gl is a powerful open source geospatial analysis tool for large-scale data sets."
homepage: https://github.com/keplergl/kepler.gl
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["node", "npm"]
---

# Keplergl Kepler Gl

<p align="right">
  <a href="https://npmjs.org/package/kepler.gl">
    <img src="https://img.shields.io/npm/v/kepler.gl.svg?style=flat" alt="version" />
  </a>
  <a href="https://travis-ci.com/keplergl/kepler.gl">
    <img src="https://api.travis-ci.com/keplergl/kepler.gl.svg?branch=master" alt="build" />
  </a>
  <a href="https://github.com/keplergl/kepler.gl">
    <img src="https://img.shields.io/github/stars/keplergl/kepler.gl.svg?style=flat" alt="stars" />
  </a>
  <a href='https://opensourc

## Usage

```javascript
// app.js
import {addDataToMap} from '@kepler.gl/actions';

const sampleTripData = {
  fields: [
    {name: 'tpep_pickup_datetime', format: 'YYYY-M-D H:m:s', type: 'timestamp'},
    {name: 'pickup_longitude', format: '', type: 'real'},
    {name: 'pickup_latitude', format: '', type: 'real'}
  ],
  rows: [
    ['2015-01-15 19:05:39 +00:00', -73.99389648, 40.75011063],
    ['2015-01-15 19:05:39 +00:00', -73.97642517, 40.73981094],
    ['2015-01-15 19:05:40 +00:00', -73.96870422, 40.7

```
