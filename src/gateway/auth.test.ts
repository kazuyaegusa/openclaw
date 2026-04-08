import { describe, expect, it } from "vitest";
import {
  assertGatewayAuthConfigured,
  authorizeGatewayConnect,
  resolveGatewayAuth,
} from "./auth.js";

describe("gateway auth", () => {
  it("does not throw when req is missing socket", async () => {
    const res = await authorizeGatewayConnect({
      auth: { mode: "token", token: "secret", allowTailscale: false },
      connectAuth: { token: "secret" },
      // Regression: avoid crashing on req.socket.remoteAddress when callers pass a non-IncomingMessage.
      req: {} as never,
    });
    expect(res.ok).toBe(true);
  });

  it("reports missing and mismatched token reasons", async () => {
    const missing = await authorizeGatewayConnect({
      auth: { mode: "token", token: "secret", allowTailscale: false },
      connectAuth: null,
    });
    expect(missing.ok).toBe(false);
    expect(missing.reason).toBe("token_missing");

    const mismatch = await authorizeGatewayConnect({
      auth: { mode: "token", token: "secret", allowTailscale: false },
      connectAuth: { token: "wrong" },
    });
    expect(mismatch.ok).toBe(false);
    expect(mismatch.reason).toBe("token_mismatch");
  });

  it("reports missing token config reason", async () => {
    const res = await authorizeGatewayConnect({
      auth: { mode: "token", allowTailscale: false },
      connectAuth: { token: "anything" },
    });
    expect(res.ok).toBe(false);
    expect(res.reason).toBe("token_missing_config");
  });

  it("reports missing and mismatched password reasons", async () => {
    const missing = await authorizeGatewayConnect({
      auth: { mode: "password", password: "secret", allowTailscale: false },
      connectAuth: null,
    });
    expect(missing.ok).toBe(false);
    expect(missing.reason).toBe("password_missing");

    const mismatch = await authorizeGatewayConnect({
      auth: { mode: "password", password: "secret", allowTailscale: false },
      connectAuth: { password: "wrong" },
    });
    expect(mismatch.ok).toBe(false);
    expect(mismatch.reason).toBe("password_mismatch");
  });

  it("reports missing password config reason", async () => {
    const res = await authorizeGatewayConnect({
      auth: { mode: "password", allowTailscale: false },
      connectAuth: { password: "secret" },
    });
    expect(res.ok).toBe(false);
    expect(res.reason).toBe("password_missing_config");
  });

  it("treats local tailscale serve hostnames as direct", async () => {
    const res = await authorizeGatewayConnect({
      auth: { mode: "token", token: "secret", allowTailscale: true },
      connectAuth: { token: "secret" },
      req: {
        socket: { remoteAddress: "127.0.0.1" },
        headers: { host: "gateway.tailnet-1234.ts.net:443" },
      } as never,
    });

    expect(res.ok).toBe(true);
    expect(res.method).toBe("token");
  });

  it("allows tailscale identity to satisfy token mode auth", async () => {
    const res = await authorizeGatewayConnect({
      auth: { mode: "token", token: "secret", allowTailscale: true },
      connectAuth: null,
      tailscaleWhois: async () => ({ login: "peter", name: "Peter" }),
      req: {
        socket: { remoteAddress: "127.0.0.1" },
        headers: {
          host: "gateway.local",
          "x-forwarded-for": "100.64.0.1",
          "x-forwarded-proto": "https",
          "x-forwarded-host": "ai-hub.bone-egret.ts.net",
          "tailscale-user-login": "peter",
          "tailscale-user-name": "Peter",
        },
      } as never,
    });

    expect(res.ok).toBe(true);
    expect(res.method).toBe("tailscale");
    expect(res.user).toBe("peter");
  });
});

describe("resolveGatewayAuth", () => {
  it("reads token from OPENCLAW_GATEWAY_TOKEN env var", () => {
    const result = resolveGatewayAuth({ env: { OPENCLAW_GATEWAY_TOKEN: "env-token" } });
    expect(result.token).toBe("env-token");
    expect(result.mode).toBe("token");
    expect(result.allowTailscale).toBe(false);
  });

  it("reads token from legacy CLAWDBOT_GATEWAY_TOKEN env var", () => {
    const result = resolveGatewayAuth({ env: { CLAWDBOT_GATEWAY_TOKEN: "legacy-token" } });
    expect(result.token).toBe("legacy-token");
    expect(result.mode).toBe("token");
  });

  it("config token takes precedence over env var", () => {
    const result = resolveGatewayAuth({
      authConfig: { mode: "token", token: "config-token" },
      env: { OPENCLAW_GATEWAY_TOKEN: "env-token" },
    });
    expect(result.token).toBe("config-token");
  });

  it("reads password from OPENCLAW_GATEWAY_PASSWORD env var", () => {
    const result = resolveGatewayAuth({ env: { OPENCLAW_GATEWAY_PASSWORD: "my-password" } });
    expect(result.password).toBe("my-password");
    expect(result.mode).toBe("password");
  });

  it("読み取り成功: env変数なし時はtokenモードがデフォルト", () => {
    const result = resolveGatewayAuth({ env: {} });
    expect(result.mode).toBe("token");
    expect(result.token).toBeUndefined();
  });

  it("tailscaleMode=serve かつ tokenモードの場合 allowTailscale=true", () => {
    const result = resolveGatewayAuth({
      env: { OPENCLAW_GATEWAY_TOKEN: "token" },
      tailscaleMode: "serve",
    });
    expect(result.allowTailscale).toBe(true);
  });

  it("tailscaleMode=serve でも passwordモードの場合 allowTailscale=false", () => {
    const result = resolveGatewayAuth({
      env: { OPENCLAW_GATEWAY_PASSWORD: "password" },
      tailscaleMode: "serve",
    });
    expect(result.allowTailscale).toBe(false);
  });

  it("config の allowTailscale が env より優先される", () => {
    const result = resolveGatewayAuth({
      authConfig: { allowTailscale: true },
      env: {},
      tailscaleMode: "off",
    });
    expect(result.allowTailscale).toBe(true);
  });
});

describe("assertGatewayAuthConfigured", () => {
  it("ログイン失敗: tokenモードでtokenなし・tailscale無効時にthrow", () => {
    expect(() => assertGatewayAuthConfigured({ mode: "token", allowTailscale: false })).toThrow(
      /OPENCLAW_GATEWAY_TOKEN/,
    );
  });

  it("ログイン成功: tokenモードでtokenなしでもtailscale有効ならthrowしない", () => {
    expect(() =>
      assertGatewayAuthConfigured({ mode: "token", allowTailscale: true }),
    ).not.toThrow();
  });

  it("ログイン成功: tokenモードでtokenが設定済みならthrowしない", () => {
    expect(() =>
      assertGatewayAuthConfigured({ mode: "token", token: "secret", allowTailscale: false }),
    ).not.toThrow();
  });

  it("ログイン失敗: passwordモードでpasswordなし時にthrow", () => {
    expect(() => assertGatewayAuthConfigured({ mode: "password", allowTailscale: false })).toThrow(
      /password/i,
    );
  });

  it("ログイン成功: passwordモードでpasswordが設定済みならthrowしない", () => {
    expect(() =>
      assertGatewayAuthConfigured({ mode: "password", password: "secret", allowTailscale: false }),
    ).not.toThrow();
  });
});
