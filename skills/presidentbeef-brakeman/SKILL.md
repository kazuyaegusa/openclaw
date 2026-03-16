---
name: presidentbeef-brakeman
description: "A static analysis security vulnerability scanner for Ruby on Rails applications"
homepage: https://github.com/presidentbeef/brakeman
metadata:
  openclaw:
    emoji: "🖥️"
    auto_generated: true
    requires:
      bins: ["docker", "git"]
---

# Presidentbeef Brakeman

[![Brakeman Logo](http://brakemanscanner.org/images/logo_medium.png)](http://brakemanscanner.org/)

[![Build Status](https://circleci.com/gh/presidentbeef/brakeman.svg?style=svg)](https://circleci.com/gh/presidentbeef/brakeman)
[![Code Coverage](https://qlty.sh/gh/presidentbeef/projects/brakeman/coverage.svg)](https://qlty.sh/gh/presidentbeef/projects/brakeman)

## Installation

Using RubyGems:

    gem install brakeman

Using Bundler:

```ruby
group :development do
  gem 'brakeman', require: false
end
```

Using Docker:

    docker pull presidentbeef/brakeman

Using Docker to build from source:

    git clone https://github.com/presidentbeef/brakeman.git
    cd brakeman
    docker build . -t brakeman
