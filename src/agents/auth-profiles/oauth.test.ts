import { describe, expect, it } from "vitest";
import type { AuthProfileStore } from "./types.js";
import { resolveApiKeyForProfile } from "./oauth.js";

describe("resolveApiKeyForProfile", () => {
  it("プロファイルが存在しない場合 null を返す", async () => {
    const store: AuthProfileStore = { version: 1, profiles: {} };
    const result = await resolveApiKeyForProfile({ store, profileId: "nonexistent" });
    expect(result).toBeNull();
  });

  describe("api_key タイプ", () => {
    it("ログイン成功: 有効な API キーを返す", async () => {
      const store: AuthProfileStore = {
        version: 1,
        profiles: {
          "anthropic:default": { type: "api_key", provider: "anthropic", key: "sk-ant-test" },
        },
      };
      const result = await resolveApiKeyForProfile({ store, profileId: "anthropic:default" });
      expect(result?.apiKey).toBe("sk-ant-test");
      expect(result?.provider).toBe("anthropic");
    });

    it("ログイン失敗: キーが空文字の場合 null を返す", async () => {
      const store: AuthProfileStore = {
        version: 1,
        profiles: {
          "anthropic:default": { type: "api_key", provider: "anthropic", key: "" },
        },
      };
      const result = await resolveApiKeyForProfile({ store, profileId: "anthropic:default" });
      expect(result).toBeNull();
    });

    it("ログイン失敗: キーが未設定の場合 null を返す", async () => {
      const store: AuthProfileStore = {
        version: 1,
        profiles: {
          "anthropic:default": { type: "api_key", provider: "anthropic" },
        },
      };
      const result = await resolveApiKeyForProfile({ store, profileId: "anthropic:default" });
      expect(result).toBeNull();
    });

    it("email が含まれる場合も返却する", async () => {
      const store: AuthProfileStore = {
        version: 1,
        profiles: {
          "anthropic:default": {
            type: "api_key",
            provider: "anthropic",
            key: "sk-ant-test",
            email: "user@example.com",
          },
        },
      };
      const result = await resolveApiKeyForProfile({ store, profileId: "anthropic:default" });
      expect(result?.email).toBe("user@example.com");
    });
  });

  describe("token タイプ", () => {
    it("ログイン成功: 有効なトークン（期限なし）を返す", async () => {
      const store: AuthProfileStore = {
        version: 1,
        profiles: {
          "anthropic:default": { type: "token", provider: "anthropic", token: "claude-token" },
        },
      };
      const result = await resolveApiKeyForProfile({ store, profileId: "anthropic:default" });
      expect(result?.apiKey).toBe("claude-token");
      expect(result?.provider).toBe("anthropic");
    });

    it("ログイン成功: 期限が将来のトークンを返す", async () => {
      const store: AuthProfileStore = {
        version: 1,
        profiles: {
          "anthropic:default": {
            type: "token",
            provider: "anthropic",
            token: "valid-token",
            expires: Date.now() + 60_000,
          },
        },
      };
      const result = await resolveApiKeyForProfile({ store, profileId: "anthropic:default" });
      expect(result?.apiKey).toBe("valid-token");
    });

    it("トークン期限切れ: 期限が過去のトークンは null を返す", async () => {
      const store: AuthProfileStore = {
        version: 1,
        profiles: {
          "anthropic:default": {
            type: "token",
            provider: "anthropic",
            token: "expired-token",
            expires: Date.now() - 60_000,
          },
        },
      };
      const result = await resolveApiKeyForProfile({ store, profileId: "anthropic:default" });
      expect(result).toBeNull();
    });

    it("ログイン失敗: トークンが空白のみの場合 null を返す", async () => {
      const store: AuthProfileStore = {
        version: 1,
        profiles: {
          "anthropic:default": { type: "token", provider: "anthropic", token: "   " },
        },
      };
      const result = await resolveApiKeyForProfile({ store, profileId: "anthropic:default" });
      expect(result).toBeNull();
    });

    it("expires=0 はゼロ値として期限切れ扱いしない（条件分岐確認）", async () => {
      // expires > 0 の条件: expires=0 は期限切れチェックをスキップしてトークンを返す
      const store: AuthProfileStore = {
        version: 1,
        profiles: {
          "anthropic:default": {
            type: "token",
            provider: "anthropic",
            token: "zero-expires-token",
            expires: 0,
          },
        },
      };
      const result = await resolveApiKeyForProfile({ store, profileId: "anthropic:default" });
      expect(result?.apiKey).toBe("zero-expires-token");
    });
  });

  describe("oauth タイプ", () => {
    it("ログイン成功: 期限が将来の oauth トークンを直接返す", async () => {
      const store: AuthProfileStore = {
        version: 1,
        profiles: {
          "anthropic:default": {
            type: "oauth",
            provider: "anthropic",
            access: "fresh-access-token",
            refresh: "refresh-token",
            expires: Date.now() + 60_000,
          },
        },
      };
      const result = await resolveApiKeyForProfile({ store, profileId: "anthropic:default" });
      expect(result?.apiKey).toBe("fresh-access-token");
      expect(result?.provider).toBe("anthropic");
    });

    it("google-gemini-cli は JSON 形式の apiKey を返す", async () => {
      const store: AuthProfileStore = {
        version: 1,
        profiles: {
          "google-gemini-cli:default": {
            type: "oauth",
            provider: "google-gemini-cli",
            access: "ggl-token",
            refresh: "refresh-token",
            expires: Date.now() + 60_000,
            projectId: "my-project-123",
          },
        },
      };
      const result = await resolveApiKeyForProfile({
        store,
        profileId: "google-gemini-cli:default",
      });
      expect(result).not.toBeNull();
      const parsed = JSON.parse(result!.apiKey) as Record<string, unknown>;
      expect(parsed.token).toBe("ggl-token");
      expect(parsed.projectId).toBe("my-project-123");
    });
  });

  describe("config バリデーション", () => {
    it("ログイン失敗: config の provider がストアと不一致の場合 null を返す", async () => {
      const store: AuthProfileStore = {
        version: 1,
        profiles: {
          "anthropic:default": { type: "api_key", provider: "anthropic", key: "sk-test" },
        },
      };
      const result = await resolveApiKeyForProfile({
        store,
        profileId: "anthropic:default",
        cfg: {
          auth: {
            profiles: {
              "anthropic:default": { provider: "openai", mode: "api-key" },
            },
          },
        } as never,
      });
      expect(result).toBeNull();
    });

    it("ログイン失敗: config の mode がストアと不一致の場合 null を返す", async () => {
      const store: AuthProfileStore = {
        version: 1,
        profiles: {
          "anthropic:default": { type: "api_key", provider: "anthropic", key: "sk-test" },
        },
      };
      const result = await resolveApiKeyForProfile({
        store,
        profileId: "anthropic:default",
        cfg: {
          auth: {
            profiles: {
              "anthropic:default": { provider: "anthropic", mode: "oauth" },
            },
          },
        } as never,
      });
      expect(result).toBeNull();
    });

    it("ログイン成功: config mode=oauth でストア type=token は互換性あり", async () => {
      // oauth config は token ストアと互換: Claude CLIがこのパターンを使う
      const store: AuthProfileStore = {
        version: 1,
        profiles: {
          "anthropic:default": {
            type: "token",
            provider: "anthropic",
            token: "claude-cli-token",
          },
        },
      };
      const result = await resolveApiKeyForProfile({
        store,
        profileId: "anthropic:default",
        cfg: {
          auth: {
            profiles: {
              "anthropic:default": { provider: "anthropic", mode: "oauth" },
            },
          },
        } as never,
      });
      expect(result?.apiKey).toBe("claude-cli-token");
    });
  });
});
