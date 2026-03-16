---
name: bwmarrin-discordgo
description: "(Golang) Go bindings for Discord"
homepage: https://github.com/bwmarrin/discordgo
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
    requires:
      bins: ["go"]
---

# Bwmarrin Discordgo

# DiscordGo

## Usage

Import the package into your project.

```go
import "github.com/bwmarrin/discordgo"
```

Construct a new Discord client which can be used to access the variety of
Discord API functions and to set callback functions for Discord events.

```go
discord, err := discordgo.New("Bot " + "authentication token")
```

See Documentation and Examples below for more detailed information.
