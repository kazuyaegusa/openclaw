---
name: palantir-gradle-baseline
description: "A set of Gradle plugins that configure default code quality tools for developers."
homepage: https://github.com/palantir/gradle-baseline
metadata:
  openclaw:
    emoji: "🧪"
    auto_generated: true
---

# Palantir Gradle Baseline

<p align="right">
<a href="https://autorelease.general.dmz.palantir.tech/palantir/gradle-baseline"><img src="https://img.shields.io/badge/Perform%20an-Autorelease-success.svg" alt="Autorelease"></a>
</p>

## Usage

The baseline set of plugins requires at least Gradle 6.1.

It is recommended to add `apply plugin: 'com.palantir.baseline'` to your root project's build.gradle. Individual plugins will be automatically applied to appropriate subprojects.

```Gradle
buildscript {
    repositories {
        gradlePluginPortal()
        mavenCentral()
    }

    dependencies {
        classpath 'com.palantir.baseline:gradle-baseline-java:<version>'
        classpath 'gradle.plugin.org.inferred:gradle-processors:2.

```
