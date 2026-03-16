---
name: obie-claude-on-rails
description: "A development framework for Ruby on Rails developers using Claude Code, inspired by SuperClaude"
homepage: https://github.com/obie/claude-on-rails
metadata:
  openclaw:
    emoji: "🔧"
    auto_generated: true
---

# Obie Claude On Rails

# ClaudeOnRails

## Installation

Add to your Rails application's Gemfile:

```ruby
group :development do
  gem 'claude-on-rails'
end
```

Then run:

```bash
bundle install
rails generate claude_on_rails:swarm
```

During generation, you'll be offered to set up Rails MCP Server for enhanced documentation access. Simply press Y when prompted!

This will:

- Analyze your Rails project structure
- Optionally set up Rails MCP Server (recommended)
- Generate a customized swarm configuration
- Create agent-specific prompts
- Set up you

## Usage

See the [examples](./examples) directory for:

- E-commerce platform development
- API-only applications
- Real-time features with Turbo/Stimulus
- Performance optimization workflows
