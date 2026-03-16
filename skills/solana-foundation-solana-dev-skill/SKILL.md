---
name: solana-foundation-solana-dev-skill
description: "Claude Code skill for modern Solana development (Jan 2026 best practices)"
homepage: https://github.com/solana-foundation/solana-dev-skill
metadata:
  openclaw:
    emoji: "🤖"
    auto_generated: true
    requires:
      bins: ["git", "npx", "skills"]
---

# Solana Foundation Solana Dev Skill

This skill provides Claude Code with deep knowledge of the current Solana development ecosystem:

- **UI**: Solana Foundation framework-kit (`@solana/client` + `@solana/react-hooks`)
- **SDK**: `@solana/kit` (v5.x) for new client work
- **Legacy Interop**: `@solana/web3-compat` for bridging to web3.js dependencies
- **Programs**: Anchor (default), Pinocchio for high-performance needs
- **Testing**: LiteSVM/Mollusk for unit tests, Surfpool for integration
- **Codegen**: Codama-first IDL and clien

## Usage

Once installed, Claude Code will automatically use this skill when you ask about:

- Solana dApp UI work (React / Next.js)
- Wallet connection and signing flows
- Transaction building, sending, and confirmation UX
- On-chain program development (Anchor or Pinocchio)
- Client SDK generation (typed program clients)
- Local testing (LiteSVM, Mollusk, Surfpool)
- Security hardening and audit-style reviews
- Surfpool local network setup and cheatcodes
- **Toolchain issues** (version mismatches, GLIBC
