---
name: softeria-ms-365-mcp-server
description: "A Model Context Protocol (MCP) server for interacting with Microsoft 365 and Office services"
homepage: https://github.com/Softeria/ms-365-mcp-server
metadata:
  openclaw:
    emoji: "🔌"
    auto_generated: true
    requires:
      bins: ["docker", "go", "ms-365-mcp-server", "npm", "npx", "tsx"]
---

# Softeria Ms 365 Mcp Server

# ms-365-mcp-server

## Installation

1. **Create a Key Vault** (if you don't have one):

   ```bash
   az keyvault create --name your-keyvault-name --resource-group your-rg --location eastus
   ```

2. **Add secrets to Key Vault**:

   ```bash
   az keyvault secret set --vault-name your-keyvault-name --name ms365-mcp-client-id --value "your-client-id"
   az keyvault secret set --vault-name your-keyvault-name --name ms365-mcp-tenant-id --value "your-tenant-id"
   # Optional: if using confidential client flow
   az keyvault secret se
   ```

## Usage

![Image](https://github.com/user-attachments/assets/ed275100-72e8-4924-bcf2-cd8e1b4c6f3a)
