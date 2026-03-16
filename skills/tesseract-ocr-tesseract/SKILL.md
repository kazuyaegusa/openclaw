---
name: tesseract-ocr-tesseract
description: "Tesseract Open Source OCR Engine (main repository)"
homepage: https://github.com/tesseract-ocr/tesseract
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
---

# Tesseract Ocr Tesseract

This package contains an **OCR engine** - `libtesseract` and a **command line program** - `tesseract`.

Tesseract 4 adds a new neural net (LSTM) based [OCR engine](https://en.wikipedia.org/wiki/Optical_character_recognition) which is focused on line recognition, but also still supports the legacy Tesseract OCR engine of Tesseract 3 which works by recognizing character patterns. Compatibility with Tesseract 3 is enabled by using the Legacy OCR Engine mode (--oem 0).
It also needs [traineddata](ht
