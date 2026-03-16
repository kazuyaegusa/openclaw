---
name: inspec-inspec
description: "InSpec: Auditing and Testing Framework"
homepage: https://github.com/inspec/inspec
metadata:
  openclaw:
    emoji: "⚙️"
    auto_generated: true
    requires:
      bins: ["curl", "docker"]
---

# Inspec Inspec

# Chef InSpec: Inspect Your Infrastructure

## Installation

Chef InSpec requires Ruby ( >= 3.1.0 ).

All currently supported versions of Chef InSpec (5.0 and later) require accepting the EULA to use. Please visit the [license acceptance page](https://docs.chef.io/licensing/accept/) on the Chef docs site for more information.

## Usage

- Only accept requests on secure ports - This test ensures that a web server is only listening on well-secured ports.

```ruby
describe port(80) do
  it { should_not be_listening }
end

describe port(443) do
  it { should be_listening }
  its('protocols') {should include 'tcp'}
end
```

- Test your `kitchen.yml` file to verify that only Vagrant is configured as the driver. The %w() formatting will
  pass rubocop linting and allow you to access nested mappings.

```ruby
describe yaml('.kitchen.yml

```
