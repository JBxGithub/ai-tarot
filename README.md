# 🔮 月娘塔羅 — AI Tarot Business

> ⚠️ **敏感資料（帳號密碼、收費模型、人設細節）全部記錄在 `CREDENTIALS.md`，唔會 commit 到 Git。**

## 快速參考

| 項目 | 值 |
|------|-----|
| **IG 帳號** | `tarot.bymoonhk` |
| **人設名** | 月娘（Yuet Leung） |
| **項目位置** | `03-PROJECTS/ai-tarot/` |
| **敏感資料** | 見 `CREDENTIALS.md`（已 gitignore） |

## 文件結構

```
03-PROJECTS/ai-tarot/
├── README.md              — 本文件（無敏感資料）
├── CREDENTIALS.md         — 帳號密碼收費等敏感資料（gitignore）
├── agent_prompt.md         — 月娘人設 + OpenClaw agent prompt v2.0
├── PRODUCT_DESIGN.md       — 產品設計文檔
├── index.html              — 網站首頁
├── tarot_data.json         — 塔羅牌數據
├── init_db.py              — PostgreSQL 初始化
├── CNAME                   — ai.alfredrpg.net
├── worker.js               — Cloudflare Worker
├── _redirects              — Cloudflare redirects
└── assets/
    └── yuet_leung_profile.jpg  — 月娘頭像
```

## ⚠️ 紅線

- **絕對唔可以透露 AI 身份** — 月娘係真人塔羅師
- **回覆必須有延遲** — 3-15分鐘，禁止秒回
- **分段回覆** — 先確認問題→再解牌→再補充
- **服務時間 10am-12am** — 凌晨唔回覆
- **敏感資料唔寫入 MEMORY.md** — 全部放 CREDENTIALS.md

## 下一步

- [x] Gmail 開通
- [x] IG 帳號開通 + Bio 設定
- [x] agent_prompt v2.0
- [x] 頭像保存到本地
- [ ] 上傳大頭貼照（需手機 app）
- [ ] IG 轉 Creator 帳號
- [ ] Facebook Developer + Instagram Graph API
- [ ] Instagram MCP 配置
- [ ] 首篇 IG post
- [ ] OpenClaw 塔羅 agent cron job
- [ ] 每日運程自動化