---
name: erikdarlingdata-performancemonitor
description: "Free, open-source SQL Server performance monitoring. Full Edition (server-installed, 30 collectors)"
homepage: https://github.com/erikdarlingdata/PerformanceMonitor
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
---

# Erikdarlingdata Performancemonitor

# SQL Server Performance Monitor

## Installation

Windows Authentication:

```
PerformanceMonitorInstaller.exe YourServerName
```

SQL Authentication:

```
PerformanceMonitorInstaller.exe YourServerName sa YourPassword
```

Entra ID (MFA) Authentication:

```
PerformanceMonitorInstaller.exe YourServerName --entra user@domain.com
```

Clean reinstall (drops existing database and all collected data):

```
PerformanceMonitorInstaller.exe YourServerName --reinstall
PerformanceMonitorInstaller.exe YourServerName sa YourPassword



```
