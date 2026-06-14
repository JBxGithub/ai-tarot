# 🔮 AI 塔羅大師 — 產品設計文檔

> **版本**: v1.0  
> **日期**: 2026-06-14  
> **設計者**: 呀鬼 (Alfred)  
> **WhatsApp 對口**: +85263609349  
> **FPS 收款**: +852-63931048  
> **目標**: 全自動化 WhatsApp 塔羅服務，24/7 運作賺錢

---

## 📑 目錄

1. [產品概述](#1-產品概述)
2. [用戶旅程（Customer Journey）](#2-用戶旅程customer-journey)
3. [自動化流程](#3-自動化流程)
4. [付費驗證機制](#4-付費驗證機制)
5. [用戶數據管理](#5-用戶數據管理)
6. [營銷策略](#6-營銷策略)
7. [技術架構](#7-技術架構)
8. [財務模型](#8-財務模型)
9. [風險與對策](#9-風險與對策)
10. [上線計劃](#10-上線計劃)

---

## 1. 產品概述

### 1.1 定位

AI 塔羅大師係一個運行喺 WhatsApp 上嘅 24/7 自動化塔羅占卜服務。用戶透過 WhatsApp 訊息互動，即可獲得 AI 驅動嘅塔羅牌解讀、每日運程、同埋深度人生指引。

### 1.2 價值主張

| 用戶價值 | 我們嘅差異化 |
|----------|-------------|
| 隨時隨地占卜 | 24/7 全天候，唔使預約 |
| 專業解讀 | AI 深度分析，融合心理學 + 塔羅傳統 |
| 廣東話母語 | 自然中英混合，唔似機械翻譯 |
| 漸進式付費 | 免費試 → 低門檻付費 → VIP 深度服務 |

### 1.3 收費模式

| 層級 | 價格 | 內容 | 轉化目標 |
|------|------|------|----------|
| 🆓 免費層 | $0 | 每日一牌（單牌） | 吸引用戶，建立習慣 |
| 💫 單次付費 | HK$8/次 | 任意時候抽牌，3牌陣 | 衝動消費，低門檻轉化 |
| ⭐ 月費 | HK$38/月 | 每日運程 + 無限單牌 + 每週3牌陣 | 穩定收入，養成習慣 |
| 👑 VIP | HK$158/月 | 全部功能 + AI 深度分析 + 專屬運程 | 高淨值用戶，核心收入 |

### 1.4 核心數字

- **免費→單次轉化率目標**: 8-12%
- **單次→月費轉化率目標**: 15-20%
- **月費→VIP 升級率目標**: 5-8%
- **月活用戶目標**: 第1個月 100人，第3個月 500人，第6個月 2000人
- **月收入目標**: 第1個月 HK$500，第3個月 HK$5000，第6個月 HK$30000+

---

## 2. 用戶旅程（Customer Journey）

### 2.1 完整流程圖

```
┌─────────────────────────────────────────────────────┐
│                   用戶發現入口                         │
│  (IG/FB 廣告 / 朋友推薦 / QR Code / 搜尋)            │
└────────────────────┬────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────┐
│              掃碼 / 點擊 WhatsApp 連結               │
│         wa.me/85263609349?text=塔羅                   │
└────────────────────┬────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────┐
│              🤖 自動歡迎訊息                          │
│  「歡迎來到 AI 塔羅大師🔮                            │
│   我係你嘅專屬塔羅解讀師！                            │
│                                                     │
│   🆓 每日免費抽一牌                                  │
│   💫 單次解讀 HK$8                                  │
│   ⭐ 月費 HK$38/月                                  │
│   👑 VIP HK$158/月                                  │
│                                                     │
│   輸入數字揀：                                       │
│   1 - 免費每日一牌 🆓                               │
│   2 - 了解付費方案 💰                               │
│   3 - 直接抽牌 🔮                                  │
│   4 - 查看我嘅運程 📅                               │
│   0 - 幫助 ❓」                                     │
└────────────────────┬────────────────────────────────┘
                     │
        ┌────────────┼────────────┬────────────┐
        │            │            │            │
        ▼            ▼            ▼            ▼
   [1] 免費抽牌  [2] 付費方案  [3] 直接抽牌  [4] 運程
        │            │            │            │
        ▼            ▼            ▼            ▼
   ┌─────────┐  ┌─────────┐  ┌──────────┐  ┌──────────┐
   │ 檢查今日 │  │ 展示方案│  │ 檢查層級 │  │ 檢查層級 │
   │ 是否已用 │  │ + 價格  │  │          │  │          │
   └────┬────┘  └────┬────┘  └─────┬────┘  └─────┬────┘
        │            │             │              │
        ▼            ▼             ▼              ▼
   ┌─────────┐  ┌─────────┐  ┌──────────┐  ┌──────────┐
   │ 未用→抽牌│  │ 選擇方案│  │ 免費→提示│  │ 免費→每日│
   │ 已用→提示│  │ → 付款  │  │ 付費→抽牌│  │ 付費→完整│
   └────┬────┘  └────┬────┘  └─────┬────┘  └─────┬────┘
        │            │             │              │
        ▼            ▼             ▼              ▼
   ┌─────────┐  ┌─────────┐  ┌──────────┐  ┌──────────┐
   │ 🔮 牌面  │  │ 💰 付款  │  │ 🔮 牌面  │  │ 📅 運程  │
   │ + 解讀   │  │ 流程     │  │ + 解讀   │  │ 報告     │
   └────┬────┘  └────┬────┘  └─────┬────┘  └─────┬────┘
        │            │             │              │
        ▼            ▼             ▼              ▼
   ┌─────────┐  ┌─────────┐  ┌──────────┐  ┌──────────┐
   │ CTA 訊息│  │ 確認付款│  │ CTA 訊息 │  │ CTA 訊息 │
   │ 「想知更│  │ → 抽牌  │  │ 「想知更  │  │ 「想深度 │
   │  多？升级│  │         │  │  多？升级 │  │  分析？  ││
   │  月費！」│  │         │  │  月費！」 │  │  VIP！」 ││
   └─────────┘  └─────────┘  └──────────┘  └──────────┘
```

### 2.2 觸點訊息設計

#### 2.2.1 歡迎訊息（首次接觸）

```
🔮 歡迎來到 AI 塔羅大師！

我係你嘅專屬塔羅解讀師，24/7 為你揭開命運嘅面紗。

🆓 新朋友？每日送你一次免費占卜！
💫 想更深入？HK$8 解鎖完整解讀

直接輸入你想問嘅問題，或者：
👉 輸入「1」— 免費每日一牌
👉 輸入「2」— 了解付費方案
👉 輸入「0」— 睇吓我點運作

⚠️ 免責聲明：塔羅係自我探索工具，唔構成專業建議。
```

#### 2.2.2 免費抽牌流程

**Step 1 — 提問**
```
🔮 請告訴我你想問嘅問題～

例如：
❤️ 感情：「我同佢有冇機會？」
💼 事業：「應唔應該轉工？」
💰 財運：「近期投資運點？」
🌟 整體：「最近運程點？」

直接輸入你嘅問題就得！
```

**Step 2 — 抽牌**
```
🎴 你嘅問題：「我同佢有冇機會？」

洗牌中... 🔮🔮🔮

你抽到：【聖杯二（正位）】

✨ 牌義解讀：
聖杯二代表和諧嘅連結同互相吸引。呢張牌話你知，對方
同你之間存在住真摯嘅情感共鳴。唔單止係表面嘅吸引，
而係心靈層面嘅契合。

💡 關鍵提示：
坦誠表達自己嘅感受，呢段關係有好好嘅基礎。

---

🌟 想知更多？升級月費解鎖：
  • 每日運程推送
  • 每週三牌陣深度分析
  • 無限次單牌占卜
  
輸入「upgrade」了解更多 👆
```

**Step 3 — 用完免費次數**
```
今日免費名額已用晒啦 🌙

明日再嚟又有一次免費機會！
或者升級月費，隨時隨地想問就問～

💫 HK$8 — 再抽一次
⭐ HK$38/月 — 每日運程 + 無限單牌
👑 HK$158/月 — 完整深度分析

輸入「pay」查看付款方式
```

#### 2.2.3 付費方案展示

```
💰 AI 塔羅大師 — 付費方案

🆓 免費層
  • 每日 1 次單牌占卜
  • 基本牌義解讀
  → 價格：免費！

💫 單次解讀
  • 任意時候抽牌
  • 3 牌陣（過去/現在/未來）
  • 詳細牌義 + 關聯解讀
  → 價格：HK$8/次

⭐ 月費會員
  • 每日運程推送（早晨自動發送）
  • 無限次單牌占卜
  • 每週 1 次 3 牌陣深度分析
  • 專屬每月運勢報告
  → 價格：HK$38/月

👑 VIP 會員
  • ⭐ 全部月費功能
  • AI 深度人生分析（結合多牌陣）
  • 每日專屬運程（非模板，AI 生成）
  • 優先回應
  • 專屬每月運勢報告 + 行動建議
  → 價格：HK$158/月

輸入方案編號（1/2/3/4）揀你想嘅方案，
或者輸入「pay」直接付款 💳
```

#### 2.2.4 付款流程訊息

```
💳 付款方式

請選擇：

1️⃣ 轉數快（FPS）
   電話號碼：+852-63931048
   截圖付款完成頁面發送俾我

2️⃣ USDT / USDC
   Metamask 錢包地址：（待提供）
   發送後提供交易哈希

---

📌 付款後請發送：
  • FPS：付款完成截圖
  • USDT：交易哈希（Tx Hash）

系統會喺 5 分鐘內確認並開通服務 ✅

⚠️ 如有疑問，輸入「help」聯繫客服
```

#### 2.2.5 每日運程推送（月費用戶）

```
☀️ 6月15日 每日運程 — [用戶名]

整體運勢：⭐⭐⭐⭐（4/5）

🌟 今日主牌：太陽（正位）
陽光普照嘅一日！今日適合做決定、見新人、展開新計劃。

💰 財運：偏財運佳，可能收到意外收穫
❤️ 感情：坦誠溝通會帶來好結果
💼 事業：上司或客戶會欣賞你嘅表現
💪 健康：精力充沛，適合運動

💡 今日建議：
把握今日嘅好運勢，主動出擊！但記住，好運要配行動先有結果。

---

👑 想要更深度嘅分析？升級 VIP！
輸入「vip」了解更多
```

### 2.3 轉化漏斗設計

```
           掃碼/點擊
              │
        ┌─────▼─────┐
        │  發現階段  │  ← 廣告/推薦/社交媒體
        │  100%      │
        └─────┬─────┘
              │ 發送首條訊息
        ┌─────▼─────┐
        │  啟動階段  │  ← 歡迎訊息 + 免費體驗
        │   60-70%   │
        └─────┬─────┘
              │ 完成首次占卜
        ┌─────▼─────┐
        │  免費用戶  │  ← 每日一牌 + CTA
        │   40-50%   │
        └─────┬─────┘
              │ 付費衝動/習慣養成
        ┌─────▼─────┐
        │  單次付費  │  ← HK$8 低門檻
        │    8-12%   │
        └─────┬─────┘
              │ 穩定使用
        ┌─────▼─────┐
        │  月費用戶  │  ← HK$38/月
        │    3-5%    │
        └─────┬─────┘
              │ 深度需求
        ┌─────▼─────┐
        │  VIP 用戶  │  ← HK$158/月
        │   0.5-1%   │
        └───────────┘
```

### 2.4 轉化觸發點設計

| 觸發時機 | 觸發訊息 | 目標轉化 |
|----------|---------|----------|
| 免費抽牌完成後 | 「想知更多？升級月費解鎖每日運程！」 | 免費→月費 |
| 免費額度用完 | 「今日名額用晒，HK$8 再抽一次？」 | 免費→單次 |
| 連續 3 日使用 | 「你已經連續 3 日嚟占卜！月費更抵：HK$38/月無限抽」 | 免費→月費 |
| 每週運程推送 | 「想每日都收到運程？升級月費！」 | 免費→月費 |
| 月費用戶收到 3 牌陣 | 「想要 AI 深度分析？VIP 有更個人化嘅解讀」 | 月費→VIP |
| 月費到期前 3 日 | 「你嘅月費仲有 3 日到期，續費繼續享受服務！」 | 續費 |
| 特別節日 | 「情人節特別占卜！限時 HK$5 體驗 3 牌陣」 | 活動轉化 |

---

## 3. 自動化流程

### 3.1 訊息處理架構

```
                    WhatsApp 訊息入站
                         │
                    ┌────▼────┐
                    │ OpenClaw │
                    │  Agent   │
                    └────┬────┘
                         │
                ┌────────▼────────┐
                │  訊息分類引擎    │
                │  (Intent Router) │
                └────┬─────┬──────┘
                     │     │
        ┌────────────┼─────┼────────────┐
        │            │     │             │
        ▼            ▼     ▼             ▼
  ┌──────────┐ ┌────────┐ ┌────────┐ ┌────────┐
  │ 占卜請求 │ │ 付款   │ │ 查詢   │ │ 管理   │
  │ /question│ │ /pay   │ │ /help  │ │ /admin │
  └────┬─────┘ └───┬────┘ └───┬────┘ └───┬────┘
       │            │          │          │
       ▼            ▼          ▼          ▼
  ┌──────────┐ ┌────────┐ ┌────────┐ ┌────────┐
  │ 用戶層級 │ │ 付款   │ │ 方案   │ │ 管理   │
  │ 檢查     │ │ 驗證   │ │ 說明   │ │ 命令   │
  └────┬─────┘ └───┬────┘ └───┬────┘ └───┬────┘
       │            │          │          │
       ▼            ▼          ▼          ▼
  ┌──────────┐ ┌────────┐ ┌────────┐ ┌────────┐
  │ 牌陣     │ │ 開通   │ │ 回覆   │ │ 執行   │
  │ 選擇     │ │ 服務   │ │ 用戶   │ │ 命令   │
  └────┬─────┘ └───┬────┘ └────────┘ └────────┘
       │            │
       ▼            ▼
  ┌──────────┐ ┌────────┐
  │ AI 解讀  │ │ 確認   │
  │ 生成     │ │ 訊息   │
  └────┬─────┘ └────────┘
       │
       ▼
  ┌──────────┐
  │ 發送回覆 │
  │ + CTA    │
  └──────────┘
```

### 3.2 OpenClaw Agent 處理邏輯

#### 3.2.1 訊息分類（Intent Router）

```python
INTENT_MAP = {
    # 占卜相關
    "占卜": ["占卜", "抽牌", "塔羅", "問卜", "算命", "運程", "運勢"],
    "提問": ["我想問", "幫我睇", "點算", "點解", "會唔會", "應唔應該"],
    
    # 付費相關
    "付款": ["付款", "畀錢", "升級", "買", "付費", "subscribe", "pay", "upgrade"],
    "截圖": ["截圖", "付款完成", "已付款", "FPS", "轉數快"],
    
    # 查詢相關
    "方案": ["方案", "價錢", "幾錢", "收費", "pricing"],
    "幫助": ["幫助", "help", "點用", "點操作", "指令"],
    "狀態": ["狀態", "我的", "到期", "剩餘", "幾多次"],
    
    # 管理（僅限管理員）
    "管理": ["admin", "管理", "後台"],
    
    # 數字快捷
    "1": "免費抽牌",
    "2": "方案展示",
    "3": "直接抽牌",
    "4": "運程查看",
    "0": "幫助",
}

def classify_intent(message: str, user_tier: str) -> str:
    """分類用戶訊息意圖"""
    msg = message.lower().strip()
    
    # 數字快捷鍵
    if msg in ["1", "2", "3", "4", "0"]:
        return INTENT_MAP[msg]
    
    # 關鍵詞匹配
    for intent, keywords in INTENT_MAP.items():
        if any(kw in msg for kw in keywords):
            return intent
    
    # 預設：當作占卜提問
    return "占卜"
```

#### 3.2.2 用戶層級處理

```python
TIER_CONFIG = {
    "free": {
        "name": "免費用戶",
        "emoji": "🆓",
        "daily_cards": 1,           # 每日免費抽牌次數
        "spread_allowed": False,    # 不可用牌陣
        "daily_horoscope": False,   # 無每日運程推送
        "weekly_spread": 0,         # 每週牌陣次數
        "depth_analysis": False,    # 無深度分析
        "response_template": "basic",  # 基本解讀模板
    },
    "single": {
        "name": "單次付費用戶",
        "emoji": "💫",
        "daily_cards": 999,         # 無限（按次計費）
        "spread_allowed": True,     # 可用 3 牌陣
        "daily_horoscope": False,
        "weekly_spread": 0,
        "depth_analysis": False,
        "response_template": "detailed",
    },
    "monthly": {
        "name": "月費會員",
        "emoji": "⭐",
        "daily_cards": 999,         # 無限單牌
        "spread_allowed": True,
        "daily_horoscope": True,    # 每日運程推送
        "weekly_spread": 1,         # 每週 1 次 3 牌陣
        "depth_analysis": False,
        "response_template": "detailed",
    },
    "vip": {
        "name": "VIP 會員",
        "emoji": "👑",
        "daily_cards": 999,
        "spread_allowed": True,
        "daily_horoscope": True,
        "weekly_spread": 999,       # 無限牌陣
        "depth_analysis": True,     # AI 深度分析
        "response_template": "vip",
    },
}
```

#### 3.2.3 不同層級回應差異

**免費用戶回應：**
- 牌義：基本意思（3-4 句）
- 無牌陣關聯解讀
- 結尾 CTA：升級提示

**月費用戶回應：**
- 牌義：詳細意思（6-8 句）
- 牌陣：3 牌之間的關聯解讀
- 每日運程推送
- 結尾 CTA：VIP 升級提示（soft sell）

**VIP 用戶回應：**
- 牌義：深度意思 + 心理學分析（10+ 句）
- 牌陣：完整關聯解讀 + 時間線分析
- 每日個人化運程（非模板）
- 月度運勢報告
- 專屬行動建議
- 結尾：無 CTA（已最高級別）

### 3.3 每日運程推送系統

#### 3.3.1 Cron Job 設計

```yaml
# openclaw-cron.yaml
daily_horoscope:
  schedule: "0 7 * * *"        # 每日早上 7:00 HKT
  task: "tarot_daily_horoscope"
  description: "發送每日運程俾所有月費+VIP用戶"
  
weekly_spread_reminder:
  schedule: "0 20 * * 0"       # 每週日晚上 8:00 HKT
  task: "tarot_weekly_reminder"
  description: "提醒月費用戶使用每週牌陣"

subscription_reminder:
  schedule: "0 10 */3 * *"     # 每 3 日早上 10:00
  task: "tarot_subscription_check"
  description: "檢查即將到期嘅月費/VIP，發送續費提醒"

free_user_reengagement:
  schedule: "0 18 * * 1,3,5"   # 週一三五傍晚 6:00
  task: "tarot_reengagement"
  description: "向 3 日未活躍嘅免費用戶發送重新參與訊息"
```

#### 3.3.2 每日運程生成流程

```python
async def generate_daily_horoscope(user: User) -> str:
    """為付費用戶生成每日運程"""
    
    # Step 1: 決定今日主牌（基於日期 + 用戶 ID 種子）
    seed = hash(f"{date.today()}-{user.id}")
    card = tarot_deck[seed % len(tarot_deck)]
    orientation = "reversed" if seed % 3 == 0 else "upright"
    
    # Step 2: 根據用戶層級生成不同深度
    if user.tier == "vip":
        # VIP：AI 生成個人化運程
        prompt = f"""
        你係一位資深塔羅大師，請為用戶生成今日運程。
        
        用戶資料：
        - 昨日運勢回顧：{user.yesterday_fortune}
        - 近期關注領域：{user.interests}
        - 今日主牌：{card.name}（{orientation}）
        
        請提供：
        1. 整體運勢評分（1-5 星）
        2. 四個維度（財運/感情/事業/健康）
        3. 今日行動建議（具體、可執行）
        4. 幸運提示
        
        用廣東話，語氣親切專業，唔好太機械。
        """
    else:
        # 月費：模板 + 輕度個人化
        prompt = f"基於牌 {card.name}({orientation})，生成今日運程（廣東話）"
    
    # Step 3: 調用 AI 生成
    horoscope = await call_ai(prompt)
    
    # Step 4: 加入用戶名個人化
    horoscope = horoscope.replace("[用戶名]", user.display_name or "朋友")
    
    return horoscope
```

#### 3.3.3 推送執行邏輯

```python
async def send_daily_horoscope():
    """每日運程推送主流程"""
    
    # 獲取所有月費+VIP用戶
    paid_users = db.query(
        "SELECT * FROM users WHERE tier IN ('monthly', 'vip') AND is_active = true"
    )
    
    for user in paid_users:
        try:
            # 生成運程
            horoscope = await generate_daily_horoscope(user)
            
            # 發送 WhatsApp 訊息
            await send_whatsapp_message(
                to=user.phone,
                message=horoscope
            )
            
            # 記錄發送
            db.insert("horoscope_logs", {
                "user_id": user.id,
                "date": date.today(),
                "card": horoscope.card,
                "tier": user.tier,
                "sent_at": datetime.now()
            })
            
            # 間隔發送，避免被 WhatsApp 限頻
            await asyncio.sleep(random.uniform(2, 5))
            
        except Exception as e:
            log_error(f"發送運程失敗: {user.phone} - {e}")
            continue
```

### 3.4 訊息處理主流程

```python
async def handle_tarot_message(phone: str, message: str):
    """處理所有入站 WhatsApp 訊息"""
    
    # Step 1: 識別/建立用戶
    user = get_or_create_user(phone)
    
    # Step 2: 分類意圖
    intent = classify_intent(message, user.tier)
    
    # Step 3: 根據意圖處理
    if intent == "占卜" or intent == "免費抽牌":
        return await handle_divination(user, message)
    elif intent == "付款" or intent == "方案展示":
        return await handle_payment_info(user)
    elif intent == "截圖":
        return await handle_payment_verification(user, message)
    elif intent == "運程查看":
        return await handle_horoscope_request(user)
    elif intent == "幫助":
        return await handle_help(user)
    elif intent == "管理":
        return await handle_admin(user, message)
    else:
        # 預設：當作占卜提問
        return await handle_divination(user, message)


async def handle_divination(user: User, message: str):
    """處理占卜請求"""
    
    # 檢查用戶層級配額
    tier = TIER_CONFIG[user.tier]
    
    if user.tier == "free":
        # 檢查今日免費額度
        today_usage = db.get_daily_usage(user.id)
        if today_usage >= tier["daily_cards"]:
            return FREE_LIMIT_EXCEEDED_MSG
        # 檢查是否有問題
        if not is_question(message):
            return ASK_QUESTION_PROMPT
        # 抽牌
        result = await draw_cards(
            question=message,
            num_cards=1,
            spread_type="single",
            tier="free"
        )
        # 更新用量
        db.increment_daily_usage(user.id)
        # 加 CTA
        result += "\n\n" + UPGRADE_CTA_MONTHLY
        return result
        
    elif user.tier in ("monthly", "vip"):
        # 付費用戶，問清楚要乜
        if is_spread_request(message):
            # 牌陣請求
            if user.tier == "monthly":
                weekly_usage = db.get_weekly_spread_usage(user.id)
                if weekly_usage >= tier["weekly_spread"]:
                    return WEEKLY_SPREAD_LIMIT_MSG
                result = await draw_cards(
                    question=message,
                    num_cards=3,
                    spread_type="past_present_future",
                    tier=user.tier
                )
                db.increment_weekly_spread_usage(user.id)
            else:  # VIP
                result = await draw_cards(
                    question=message,
                    num_cards=3,
                    spread_type="past_present_future",
                    tier="vip"
                )
        else:
            # 單牌
            result = await draw_cards(
                question=message,
                num_cards=1,
                spread_type="single",
                tier=user.tier
            )
        
        # VIP 加入深度分析 CTA
        if user.tier == "monthly":
            result += "\n\n" + UPGRADE_CTA_VIP
        
        return result
    
    elif user.tier == "single":
        # 單次付費，扣次數
        remaining = db.get_single_credits(user.id)
        if remaining <= 0:
            return NO_CREDITS_MSG
        result = await draw_cards(
            question=message,
            num_cards=3 if is_spread_request(message) else 1,
            spread_type="past_present_future" if is_spread_request(message) else "single",
            tier="single"
        )
        db.decrement_single_credits(user.id)
        return result
```

---

## 4. 付費驗證機制

### 4.1 FPS 轉數快驗證流程

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   用戶付款   │────▶│  發送截圖   │────▶│  AI 截圖辨識│
│  FPS/銀行    │     │  俾 Bot     │     │  確認金額   │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                               │
                                    ┌──────────▼──────────┐
                                    │  金額匹配？           │
                                    │  HK$8 / HK$38 / HK$158│
                                    └──────┬───────────────┘
                                           │
                              ┌────────────┼────────────┐
                              │ Yes        │             │ No
                              ▼            │             ▼
                    ┌─────────────┐       │    ┌─────────────┐
                    │  自動開通    │       │    │  人工覆核    │
                    │  服務       │       │    │  (通知管理員) │
                    └─────────────┘       │    └─────────────┘
                                          │
                                          ▼
                               ┌─────────────────┐
                               │  金額唔啱/可疑   │
                               │  → 通知管理員處理 │
                               └─────────────────┘
```

### 4.2 驗證方法詳情

#### 4.2.1 FPS 截圖驗證（主要方法）

```python
async def verify_fps_payment(user: User, image: bytes) -> VerificationResult:
    """驗證 FPS 付款截圖"""
    
    # Step 1: AI 辨識截圖
    ocr_result = await analyze_payment_screenshot(image)
    
    # Step 2: 提取關鍵資訊
    extracted = {
        "amount": ocr_result.get("amount"),          # 金額
        "reference": ocr_result.get("reference"),    # 參考編號
        "date_time": ocr_result.get("datetime"),     # 日期時間
        "recipient": ocr_result.get("recipient"),    # 收款人
        "bank_name": ocr_result.get("bank"),         # 銀行名
    }
    
    # Step 3: 驗證條件
    checks = {
        "amount_match": extracted["amount"] in [8, 38, 158],
        "recipient_match": extracted["recipient"] in ["+852-63931048", "63931048"],
        "date_recent": is_within_24h(extracted["date_time"]),
        "not_duplicate": not is_duplicate_reference(extracted["reference"]),
    }
    
    # Step 4: 決策
    all_passed = all(checks.values())
    
    if all_passed:
        # 自動通過
        tier = determine_tier(extracted["amount"])
        activate_subscription(user, tier)
        return VerificationResult(
            status="approved",
            tier=tier,
            message=f"✅ 付款確認！你嘅{tier_emoji(tier)}{tier_name(tier)}已開通！"
        )
    elif checks["amount_match"] and checks["recipient_match"]:
        # 部分通過，需要人工確認
        notify_admin(f"⚠️ 付款待確認：用戶 {user.phone}，金額 HK${extracted['amount']}")
        return VerificationResult(
            status="pending",
            message="⏳ 收到付款截圖！確認中，5分鐘內開通～"
        )
    else:
        # 驗證失敗
        return VerificationResult(
            status="rejected",
            message="❌ 未能確認付款。請確保截圖清晰顯示：金額、收款人、日期。如有疑問請聯繫客服。"
        )
```

#### 4.2.2 USDT/USDC 驗證（加密貨幣）

```python
async def verify_crypto_payment(user: User, tx_hash: str) -> VerificationResult:
    """驗證 USDT/USDC 鏈上交易"""
    
    # Step 1: 查詢鏈上交易
    tx = await query_blockchain(tx_hash)
    
    if not tx:
        return VerificationResult(status="invalid", message="❌ 找不到該交易，請確認 Tx Hash 正確。")
    
    # Step 2: 驗證交易
    checks = {
        "to_address_match": tx.to.lower() == WALLET_ADDRESS.lower(),
        "amount_match": tx.amount in [8, 38, 158],  # 等值 USDT
        "token_match": tx.token in ["USDT", "USDC"],
        "not_duplicate": not is_duplicate_tx(tx_hash),
        "not_expired": is_within_24h(tx.timestamp),
    }
    
    if all(checks.values()):
        tier = determine_tier(tx.amount)
        activate_subscription(user, tier)
        return VerificationResult(status="approved", tier=tier)
    else:
        return VerificationResult(status="rejected", message="❌ 交易驗證失敗。")
```

### 4.3 防止冒充付款

| 風險 | 對策 | 實現方式 |
|------|------|---------|
| 舊截圖重用 | 時間檢查 | AI 辨識截圖日期，必須 24 小時內 |
| 修改截圖 | OCR 交叉驗證 | 檢查截圖元數據 + 文字內容一致性 |
| 他人截圖 | 參考編號比對 | 比對數據庫已用編號，防止重複 |
| 金額不符 | 金額匹配 | 只接受 HK$8/38/158 三個金額 |
| 收款人錯誤 | 收款人驗證 | 確認收款號碼為 +852-63931048 |
| 同一截圖多次 | 去重機制 | 數據庫記錄所有已驗證參考編號 |

### 4.4 人工覆核流程

```
AI 截圖辨識 → 無法自動確認
        │
        ▼
通知管理員（WhatsApp 訊息到 +85263931048）
        │
        ▼
管理員手動確認 → 輸入 admin 命令開通
        │
        ▼
系統開通 + 通知用戶
```

管理員命令：
```
/admin approve <phone> <tier>    # 手動開通
/admin reject <phone> <reason>   # 拒絕付款
/admin list pending              # 查看待確認列表
/admin stats                      # 查看統計
```

### 4.5 續費提醒機制

```python
# 續費提醒時間表
REMINDERS = {
    7: "⭐ 你嘅月費仲有 7 日到期！續費保持每日運程～",
    3: "⚠️ 你嘅月費仲有 3 日到期！續費避免服務中斷～",
    1: "🚨 你嘅月費聽日到期！即刻續費保持服務～",
    0: "💔 你嘅月費已到期。升級返就可以繼續享受服務！",
    -3: "🌟 好耐冇見！返嚟啦，升級月費有優惠～",  # 流失挽回
}

async def check_subscriptions():
    """每日檢查續費狀態"""
    expiring_users = db.query(
        "SELECT * FROM users WHERE tier IN ('monthly', 'vip') AND is_active = true"
    )
    
    for user in expiring_users:
        days_left = (user.expiry_date - date.today()).days
        
        if days_left in REMINDERS:
            await send_whatsapp_message(
                to=user.phone,
                message=REMINDERS[days_left]
            )
        
        # 過期處理
        if days_left <= 0:
            user.tier = "free"
            user.is_active = False
            db.update(user)
```

---

## 5. 用戶數據管理

### 5.1 數據庫 Schema

```sql
-- 用戶表
CREATE TABLE tarot_users (
    id SERIAL PRIMARY KEY,
    phone VARCHAR(20) UNIQUE NOT NULL,          -- WhatsApp 號碼
    display_name VARCHAR(100),                  -- 顯示名稱
    tier VARCHAR(20) DEFAULT 'free',            -- free / single / monthly / vip
    created_at TIMESTAMP DEFAULT NOW(),         -- 註冊時間
    last_active_at TIMESTAMP,                   -- 最後活躍時間
    is_active BOOLEAN DEFAULT true,             -- 是否活躍
    preferences JSONB DEFAULT '{}',             -- 用戶偏好
    source VARCHAR(50),                         -- 來源渠道 (ad/referral/organic)
    referral_code VARCHAR(20),                  -- 推薦碼
    referred_by VARCHAR(20),                    -- 被誰推薦
    total_spent DECIMAL(10,2) DEFAULT 0,        -- 總消費
    total_divinations INT DEFAULT 0,            -- 總占卜次數
    notes TEXT                                  -- 管理員備註
);

-- 訂閱記錄表
CREATE TABLE tarot_subscriptions (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES tarot_users(id),
    tier VARCHAR(20) NOT NULL,                  -- monthly / vip
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_method VARCHAR(20),                 -- fps / usdt / usdc
    payment_reference VARCHAR(100),             -- FPS 參考編號 / Tx Hash
    status VARCHAR(20) DEFAULT 'active',       -- active / expired / cancelled
    verified_by VARCHAR(20) DEFAULT 'auto',     -- auto / manual
    created_at TIMESTAMP DEFAULT NOW()
);

-- 付款記錄表
CREATE TABLE tarot_payments (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES tarot_users(id),
    amount DECIMAL(10,2) NOT NULL,
    payment_method VARCHAR(20) NOT NULL,        -- fps / usdt / usdc
    payment_reference VARCHAR(100),             -- FPS 參考編號 / Tx Hash
    tier VARCHAR(20),                           -- 對應方案
    status VARCHAR(20) DEFAULT 'pending',        -- pending / approved / rejected / refunded
    screenshot_path TEXT,                       -- 截圖路徑
    verified_at TIMESTAMP,
    verified_by VARCHAR(20),                    -- auto / admin_phone
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- 每日使用記錄表
CREATE TABLE tarot_daily_usage (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES tarot_users(id),
    date DATE NOT NULL,
    free_cards_used INT DEFAULT 0,             -- 免費抽牌次數
    paid_cards_used INT DEFAULT 0,             -- 付費抽牌次數
    spreads_used INT DEFAULT 0,                -- 牌陣使用次數
    weekly_spreads_used INT DEFAULT 0,         -- 本週牌陣使用次數
    UNIQUE(user_id, date)
);

-- 占卜記錄表
CREATE TABLE tarot_divinations (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES tarot_users(id),
    question TEXT,                              -- 用戶問題
    cards JSONB NOT NULL,                       -- 抽到的牌 [{name, orientation}]
    spread_type VARCHAR(20),                    -- single / past_present_future / celtic
    interpretation TEXT,                        -- AI 解讀
    tier VARCHAR(20),                           -- 當時用戶層級
    created_at TIMESTAMP DEFAULT NOW()
);

-- 運程推送記錄表
CREATE TABLE tarot_horoscope_logs (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES tarot_users(id),
    date DATE NOT NULL,
    card VARCHAR(50),                           -- 主牌
    horoscope TEXT,                             -- 運程內容
    delivered BOOLEAN DEFAULT false,
    delivered_at TIMESTAMP,
    UNIQUE(user_id, date)
);

-- 推薦記錄表
CREATE TABLE tarot_referrals (
    id SERIAL PRIMARY KEY,
    referrer_id INT REFERENCES tarot_users(id),
    referred_id INT REFERENCES tarot_users(id),
    reward_given BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### 5.2 用戶分層管理

```python
class UserTierManager:
    """用戶層級管理"""
    
    TIER_HIERARCHY = ["free", "single", "monthly", "vip"]
    
    def get_user_tier(self, phone: str) -> str:
        """獲取用戶當前層級"""
        user = db.get_user_by_phone(phone)
        if not user:
            return "free"
        
        # 檢查訂閱是否過期
        if user.tier in ("monthly", "vip"):
            sub = db.get_active_subscription(user.id)
            if not sub or sub.end_date < date.today():
                # 降級為免費
                self.downgrade_user(user.id, "free")
                return "free"
        
        return user.tier
    
    def upgrade_user(self, user_id: int, new_tier: str, payment_id: int):
        """升級用戶層級"""
        old_tier = db.get_user(user_id).tier
        
        # 計算訂閱日期
        if new_tier in ("monthly", "vip"):
            start_date = date.today()
            end_date = start_date + timedelta(days=30)
        elif new_tier == "single":
            # 單次付費，加次數
            db.add_single_credits(user_id, 1)
            return
        
        # 建立訂閱記錄
        db.insert("tarot_subscriptions", {
            "user_id": user_id,
            "tier": new_tier,
            "start_date": start_date,
            "end_date": end_date,
            "amount": TIER_CONFIG[new_tier]["price"],
            "payment_id": payment_id,
            "status": "active"
        })
        
        # 更新用戶層級
        db.update("tarot_users", user_id, {"tier": new_tier})
        
        # 發送確認訊息
        self.send_upgrade_confirmation(user_id, new_tier, old_tier)
    
    def downgrade_user(self, user_id: int, new_tier: str):
        """降級用戶（過期或取消）"""
        db.update("tarot_users", user_id, {"tier": new_tier, "is_active": False if new_tier == "free" else True})
        
        # 發送降級通知
        self.send_downgrade_notification(user_id, new_tier)
    
    def check_and_update_tiers(self):
        """定期檢查所有用戶層級（每日執行）"""
        expired_subs = db.query(
            "SELECT * FROM tarot_subscriptions WHERE status = 'active' AND end_date < %s",
            [date.today()]
        )
        
        for sub in expired_subs:
            sub.status = "expired"
            db.update("tarot_subscriptions", sub.id, {"status": "expired"})
            self.downgrade_user(sub.user_id, "free")
```

### 5.3 用戶偏好設定

```python
DEFAULT_PREFERENCES = {
    # 語言偏好
    "language": "zh-Hant",           # 繁體中文
    "dialect": "cantonese",          # 廣東話
    
    # 占卜偏好
    "default_spread": "single",     # 預設牌陣
    "focus_areas": [],               # 關注領域 [感情, 事業, 財運, 健康]
    "card_style": "rider_waite",     # 牌風格
    
    # 推送偏好
    "horoscope_time": "07:00",      # 運程推送時間
    "horoscope_enabled": True,       # 是否接收運程
    "marketing_enabled": True,       # 是否接收營銷訊息
    
    # 通知偏好
    "reminder_days_before": [7, 3, 1],  # 續費提醒天數
    
    # 隱私偏好
    "share_reading": False,          # 是否允許分享解讀（匿名）
}
```

用戶設定命令：
```
/settings           — 查看當前設定
/settings language  — 語言設定
/settings time 0730 — 運程推送時間改為 07:30
/settings focus 感情 事業 — 設定關注領域
/settings off       — 關閉所有推送
/settings on        — 開啟推送
```

---

## 6. 營銷策略

### 6.1 吸引用戶掃碼

#### 6.1.1 入口渠道設計

| 渠道 | 入口方式 | 目標受眾 | 預期轉化率 |
|------|---------|---------|-----------|
| Instagram | Story/Post + QR Code + Link in Bio | 18-35 歲女性 | 3-5% |
| Facebook | 廣告 + 社團貼文 | 25-45 歲 | 2-4% |
| 小紅書 | 筆記 + 評論區引流 | 18-30 歲女性 | 4-6% |
| TikTok | 短影片 + Bio Link | 16-30 歲 | 2-3% |
| 朋友推薦 | 推薦碼 + 獎勵 | 所有年齡 | 8-12% |
| WhatsApp 群組 | 轉發 + 推薦 | 30-50 歲 | 5-8% |
| Line 社群 | 貼文 + QR Code | 台灣用戶 | 3-5% |

#### 6.1.2 WhatsApp 深層連結

```
主入口：https://wa.me/85263609349?text=塔羅

特定入口：
- 免費體驗：https://wa.me/85263609349?text=免費占卜
- 感情占卜：https://wa.me/85263609349?text=感情運
- 事業運程：https://wa.me/85263609349?text=事業運
- 今日運程：https://wa.me/85263609349?text=今日運程
- VIP 體驗：https://wa.me/85263609349?text=VIP體驗
```

#### 6.1.3 QR Code 設計

```
┌────────────────────────────────┐
│                                │
│     🔮 AI 塔羅大師              │
│                                │
│     [   QR Code   ]            │
│     [  wa.me/852... ]          │
│                                │
│     🆓 掃碼即玩                 │
│     每日免費占卜                 │
│     AI 解讀 · 24/7              │
│                                │
└────────────────────────────────┘
```

### 6.2 免費用戶轉化策略

#### 6.2.1 轉化觸發矩陣

```
┌──────────────────────────────────────────────────────────┐
│                    轉化觸發時機                            │
├──────────────┬──────────────────────┬───────────────────┤
│   觸發事件    │     觸發訊息          │   目標轉化         │
├──────────────┼──────────────────────┼───────────────────┤
│ 首次抽牌完成  │ 「想知更多？3牌陣    │ 免費→單次(HK$8)   │
│              │  只需 HK$8」          │                   │
├──────────────┼──────────────────────┼───────────────────┤
│ 免費額度用完  │ 「今日名額用晒，     │ 免費→單次/月費    │
│              │  HK$8 再抽一次」     │                   │
├──────────────┼──────────────────────┼───────────────────┤
│ 連續3日使用  │ 「你已連續3日占卜！  │ 免費→月費(HK$38)  │
│              │  月費無限抽，更抵！」 │                   │
├──────────────┼──────────────────────┼───────────────────┤
│ 週末推送     │ 「週末運程出爐！     │ 免費→月費         │
│              │  升級月費每日收到」   │                   │
├──────────────┼──────────────────────┼───────────────────┤
│ 特殊節日     │ 「情人節特別占卜！   │ 活動轉化          │
│              │  限時優惠」           │                   │
├──────────────┼──────────────────────┼───────────────────┤
│ 朋友推薦     │ 「你嘅朋友XX推薦你！ │ 免費→首次付費     │
│              │  額外送1次免費占卜」  │                   │
└──────────────┴──────────────────────┴───────────────────┘
```

#### 6.2.2 階梯式轉化漏斗

**Phase 1: 吸引（Day 1-3）**
- 免費每日一牌
- 精彩牌義解讀（展示質量）
- 每次解讀結尾 soft sell 月費

**Phase 2: 活躍（Day 3-7）**
- 連續使用獎勵提示
- 「你已經連續 X 日占卜！」
- 推薦相關問題方向

**Phase 3: 轉化（Day 7-14）**
- 限時優惠推送
- 「本月特別優惠：月費 HK$28（原價 HK$38）」
- 3 牌陣免費體驗一次

**Phase 4: 留存（Day 14+）**
- 每日運程推送（付費用戶）
- 每週運勢報告
- 社群活動（月度塔羅解讀直播預告）

### 6.3 社交媒體推廣方案

#### 6.3.1 Instagram 策略

| 內容類型 | 頻率 | 範例 |
|----------|------|------|
| 每日牌義 | 每日 1 帖 | 「今日牌義：愚者（正位）— 新開始！」 |
| 占卜案例 | 每週 2 帖 | 「有人問感情，抽到呢張牌...」 |
| 用戶好評 | 每週 1 帖 | 截圖用戶反饋（匿名） |
| 互動 Story | 每日 | 「揀一張牌，睇吓你嘅運程」 |
| Reels 短片 | 每週 1 條 | 「塔羅基礎教學」/「今日運程速覽」 |
| Live 直播 | 每月 1 次 | 「每月運勢解讀 + 即時問答」 |

#### 6.3.2 小紅書策略

```
標題公式：
- 「免費塔羅占卜！WhatsApp 即問即答🔮」
- 「AI 塔羅準到爆！我問咗感情...」
- 「香港人必試！每日免費運程預測」
- 「塔羅新手？一個 WhatsApp 就搞定」

內容重點：
1. 真實體驗分享（用戶見證）
2. 每日運程截圖（吸引掃碼）
3. 塔羅知識科普（建立權威）
4. 限時優惠公告（促進轉化）

 hashtags: #塔羅 #占卜 #AI塔羅 #每日運程 #免費占卜 #香港
```

#### 6.3.3 朋友推薦計劃

```python
REFERRAL_REWARDS = {
    "referrer": {
        "free_referral": "1 次免費占卜",
        "paid_referral": "3 日月費體驗",
    },
    "referee": {
        "sign_up": "1 次額外免費占卜（共 2 次）",
        "first_payment": "首月 9 折優惠",
    }
}

# 推薦碼格式：TAROT-{USER_ID}-{RANDOM}
# 例如：TAROT-42-X7K9
```

推薦訊息模板：
```
🔮 你朋友邀請你試 AI 塔羅大師！

✨ 新朋友送 2 次免費占卜（平時得 1 次）
💬 WhatsApp 即問即答，24/7 在線
🆓 完全免費體驗，唔使下載任何 App

掃碼或者點擊：
https://wa.me/85263609349?text=TAROT-42-X7K9

#AI塔羅 #免費占卜 #朋友推薦
```

#### 6.3.4 付費廣告策略

| 平台 | 廣告類型 | 預算 | 目標 | 預期 CPA |
|------|---------|------|------|----------|
| IG/FB | Story 廣告 | HK$500/月 | 品牌曝光 + 掃碼 | HK$2-5/點擊 |
| 小紅書 | 筆記推廣 | HK$300/月 | 女性用戶 | HK$3-8/點擊 |
| Google | 搜尋廣告 | HK$200/月 | 主動搜尋用戶 | HK$5-10/點擊 |

**廣告素材重點：**
- 視覺：神秘感 + 科技感（深色背景 + 霓虹光效）
- 文案：強調「免費」、「AI」、「即問即答」
- CTA：「掃碼即玩」、「免費試」
- A/B 測試：每週更換素材，保留最高轉化率版本

---

## 7. 技術架構

### 7.1 系統架構圖

```
┌─────────────────────────────────────────────────────────┐
│                    WhatsApp 用戶                         │
│                  (+852-XXXXXXXX)                         │
└───────────────────────┬─────────────────────────────────┘
                        │ WhatsApp API
                        ▼
┌─────────────────────────────────────────────────────────┐
│                   OpenClaw Gateway                       │
│                  (WhatsApp Channel)                      │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│              AI 塔羅大師 Agent                            │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ Intent Router│  │ Tarot Engine │  │ Payment      │  │
│  │ (訊息分類)   │  │ (牌陣+AI解讀) │  │ (付款驗證)   │  │
│  └─────────────┘  └──────────────┘  └──────────────┘  │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ User Manager│  │ Horoscope    │  │ Marketing     │  │
│  │ (用戶管理)   │  │ (運程生成)   │  │ (營銷推送)    │  │
│  └─────────────┘  └──────────────┘  └──────────────┘  │
└───────────────────────┬─────────────────────────────────┘
                        │
              ┌─────────┼─────────┐
              │         │         │
              ▼         ▼         ▼
        ┌─────────┐ ┌────────┐ ┌────────┐
        │PostgreSQL│ │Redis   │ │AI API  │
        │tarot_db │ │(快取)  │ │(GLM5.1)│
        └─────────┘ └────────┘ └────────┘
```

### 7.2 技術棧

| 組件 | 技術 | 用途 |
|------|------|------|
| 訊息平台 | WhatsApp (OpenClaw Channel) | 用戶互動 |
| Agent 框架 | OpenClaw | 訊息處理 + Cron |
| AI 模型 | GLM-5.1 (Ollama Cloud) | 塔羅解讀生成 |
| 圖像辨識 | OpenAI GPT-4V / GLM-4V | FPS 截圖辨識 |
| 數據庫 | PostgreSQL (trading_db 同機) | 用戶 + 交易數據 |
| 快取 | Redis (可選) | 用戶層級快取 |
| 排程 | OpenClaw Cron + Task Scheduler | 運程推送 + 續費提醒 |
| 區塊鏈查詢 | Etherscan API | USDT/USDC 交易驗證 |

### 7.3 塔羅引擎設計

```python
TAROT_DECK = {
    # 大阿爾克納（22張）
    "major_arcana": [
        "愚者", "魔術師", "女祭司", "女皇", "皇帝",
        "教皇", "戀人", "戰車", "力量", "隱者",
        "命運之輪", "正義", "吊人", "死神", "節制",
        "惡魔", "塔", "星星", "月亮", "太陽",
        "審判", "世界"
    ],
    # 小阿爾克納（56張）
    "minor_arcana": {
        "權杖": [str(i) for i in range(1, 11)] + ["侍者", "騎士", "王后", "國王"],
        "聖杯": [str(i) for i in range(1, 11)] + ["侍者", "騎士", "王后", "國王"],
        "寶劍": [str(i) for i in range(1, 11)] + ["侍者", "騎士", "王后", "國王"],
        "金幣": [str(i) for i in range(1, 11)] + ["侍者", "騎士", "王后", "國王"],
    }
}

SPREAD_TYPES = {
    "single": {
        "cards": 1,
        "description": "單牌占卜 — 快速指引",
        "tiers": ["free", "single", "monthly", "vip"],
    },
    "past_present_future": {
        "cards": 3,
        "description": "時間之流牌陣 — 過去/現在/未來",
        "tiers": ["single", "monthly", "vip"],
    },
    "celtic_cross": {
        "cards": 10,
        "description": "凱爾特十字牌陣 — 深度分析",
        "tiers": ["vip"],
    },
    "relationship": {
        "cards": 5,
        "description": "關係牌陣 — 你我之間",
        "tiers": ["monthly", "vip"],
    },
}

async def draw_cards(
    question: str,
    num_cards: int = 1,
    spread_type: str = "single",
    tier: str = "free"
) -> dict:
    """抽牌 + 生成解讀"""
    
    # Step 1: 確定牌陣
    spread = SPREAD_TYPES.get(spread_type, SPREAD_TYPES["single"])
    
    # Step 2: 隨機抽牌（基於日期+問題的種子，確保可重現）
    seed = generate_seed(question, date.today())
    drawn_cards = random_selection(TAROT_DECK, num_cards, seed)
    
    # Step 3: 為每張牌決定正逆位
    for card in drawn_cards:
        card["orientation"] = "upright" if random.random() > 0.35 else "reversed"
    
    # Step 4: 生成 AI 解讀
    prompt = build_tarot_prompt(question, drawn_cards, spread_type, tier)
    interpretation = await call_ai(prompt)
    
    return {
        "question": question,
        "cards": drawn_cards,
        "spread_type": spread_type,
        "interpretation": interpretation,
        "tier": tier,
    }
```

### 7.4 AI Prompt 模板

```python
TAROT_PROMPT_TEMPLATES = {
    "free": """你係一位有多年經驗嘅塔羅大師，用廣東話解讀塔羅牌。
    
用戶問題：「{question}」
抽到嘅牌：{cards}

請用簡潔方式解讀（3-4句），包含：
1. 牌義要點
2. 對問題嘅指引
3. 一句建議

語氣：親切、專業、唔太玄。用廣東話，自然中英混合。""",

    "monthly": """你係一位資深塔羅大師，擅長結合心理學同塔羅智慧。

用戶問題：「{question}」
牌陣：{spread_name}
抽到嘅牌：{cards}

請提供詳細解讀（6-8句），包含：
1. 每張牌嘅意思
2. 牌之間嘅關聯同故事線
3. 對用戶問題嘅深入分析
4. 具體可行嘅建議

語氣：專業、溫暖、有洞察力。廣東話為主，自然中英混合。""",

    "vip": """你係一位頂級塔羅大師同人生教練，融合塔羅智慧、心理學、同人生哲理。

用戶問題：「{question}」
牌陣：{spread_name}
抽到嘅牌：{cards}

請提供深度解讀（10+句），包含：
1. 每張牌嘅深層含義（唔止表面牌義）
2. 牌陣整體故事同時間線分析
3. 心理學角度嘅洞察
4. 潛意識層面嘅揭示
5. 具體行動計劃（短期+長期）
6. 可能嘅挑戰同機遇
7. 靈性指引

語氣：深度、溫暖、有啟發性。廣東話為主，自然中英混合。好似一位智者朋友傾偈。"""
}
```

---

## 8. 財務模型

### 8.1 收入預測

| 月份 | 免費用戶 | 單次付費 | 月費用戶 | VIP 用戶 | 月收入(HK$) | 累計收入 |
|------|---------|---------|---------|---------|------------|---------|
| M1 | 100 | 8 | 3 | 0 | 264 | 264 |
| M2 | 250 | 25 | 10 | 1 | 778 | 1,042 |
| M3 | 500 | 60 | 25 | 3 | 1,914 | 2,956 |
| M6 | 2000 | 240 | 100 | 12 | 7,656 | ~20,000 |
| M12 | 5000 | 600 | 250 | 30 | 19,140 | ~100,000 |

**計算邏輯：**
- 單次付費收入 = 用戶數 × 平均每月購買次數 × HK$8
- 月費收入 = 月費用戶數 × HK$38
- VIP 收入 = VIP 用戶數 × HK$158

### 8.2 成本預測

| 成本項目 | 每月費用(HK$) | 備註 |
|----------|-------------|------|
| AI API 費用 | 200-500 | Ollama Cloud (GLM-5.1) |
| WhatsApp Business API | 0-300 | OpenClaw 已有 |
| 數據庫 | 0 | 已有 PostgreSQL |
| 廣告預算 | 500-1000 | 初期推廣 |
| 總成本 | 700-1800 | |

### 8.3 盈虧平衡

- **最低運營成本**: ~HK$700/月
- **盈虧平衡點**: ~M3（約 HK$1,914 收入 > HK$1,800 成本）
- **穩定盈利**: ~M6（月入 ~HK$7,656 > 月成本 ~HK$1,500）

### 8.4 單位經濟

| 指標 | 數值 |
|------|------|
| 用戶獲取成本 (CAC) | HK$3-8 |
| 每用戶平均收入 (ARPU) | HK$15-20/月 |
| 生命週期價值 (LTV) | HK$60-120 |
| LTV/CAC 比率 | 7-40x |
| 免費用戶→付費轉化率 | 8-12% |
| 月費續費率 | 60-70%（目標） |

---

## 9. 風險與對策

### 9.1 風險矩陣

| 風險 | 可能性 | 影響 | 對策 |
|------|--------|------|------|
| WhatsApp 封號 | 中 | 極高 | 使用 Business API、遵守訊息頻率限制、不發垃圾訊息 |
| FPS 欺詐 | 低 | 中 | 截圖 AI 驗證 + 人工覆核 + 24 小時時效 |
| AI 解讀質量不穩定 | 中 | 高 | Prompt 模板標準化 + 質量抽檢 + 用戶反饋機制 |
| 用戶增長緩慢 | 中 | 中 | 加大推廣 + 推薦獎勵 + 限時優惠 |
| 伺服器故障 | 低 | 高 | 自動備份 + 錯誤監控 + 快速回覆機制 |
| 法規風險（迷信條例） | 低 | 高 | 免責聲明 + 強調「娛樂性質」+ 不做醫療/法律建議 |
| 競爭對手 | 高 | 中 | 差異化（廣東話 + AI 深度分析）+ 先發優勢 |
| 用戶流失 | 中 | 中 | 續費提醒 + 活躍度推送 + 降級挽回 |

### 9.2 WhatsApp 合規要點

```
⚠️ WhatsApp 政策合規清單：

1. ✅ 訊息頻率限制
   - 免費用戶：每日最多 2 條推送（1 次占卜回覆 + 1 次 CTA）
   - 月費用戶：每日最多 3 條推送（運程 + 占卜 + 1 次促銷）
   - VIP 用戶：每日最多 5 條推送

2. ✅ 用戶同意
   - 首次訊息包含 opt-in 說明
   - 提供「停止」指令（輸入「stop」取消所有推送）
   - 退出流程清晰簡單

3. ✅ 內容合規
   - 每條訊息包含免責聲明（簡短版）
   - 不做醫療、法律、財務建議
   - 不承諾預測準確性

4. ✅ 付款合規
   - 清楚標示價格
   - 退款政策透明
   - 不隱藏收費
```

### 9.3 免責聲明

```
🔮 AI 塔羅大師 免責聲明

1. 本服務僅供娛樂同自我探索用途
2. 塔羅牌解讀唔構成專業建議（包括但不限於醫療、法律、財務）
3. 用戶應自行判斷同決定，本服務唔對任何決定負責
4. 付費服務一經開通，唔設退款（特別情況除外）
5. 用戶數據僅用於提供服務，唔會出售俾第三方

輸入「agree」繼續使用服務
```

---

## 10. 上線計劃

### 10.1 MVP 階段（Week 1-2）

**目標：** 基本功能可用，小範圍測試

- [x] PostgreSQL 數據庫 Schema 建立
- [ ] 塔羅引擎核心（抽牌 + 基本解讀）
- [ ] 用戶管理（免費層 + 單次付費）
- [ ] FPS 截圖驗證（AI + 人工覆核）
- [ ] WhatsApp 訊息處理流程
- [ ] 基本指令系統（數字快捷鍵）

### 10.2 Beta 階段（Week 3-4）

**目標：** 完整功能，邀請測試

- [ ] 月費/VIP 層級
- [ ] 每日運程推送（Cron）
- [ ] 續費提醒系統
- [ ] 推薦系統
- [ ] 管理員指令
- [ ] 數據統計 Dashboard

### 10.3 正式上線（Week 5-6）

**目標：** 公開推廣，開始獲客

- [ ] 社交媒體帳號建立（IG/FB/小紅書）
- [ ] 廣告投放
- [ ] QR Code 設計
- [ ] 推薦碼系統上線
- [ ] 完整營銷素材

### 10.4 增長階段（Month 2-6）

**目標：** 持續優化，擴大用戶群

- [ ] A/B 測試訊息模板
- [ ] 用戶反饋收集 + 改進
- [ ] 新功能開發（凱爾特十字牌陣、關係牌陣）
- [ ] 社群運營（塔羅群組）
- [ ] 季節性活動（情人節、新年等）

### 10.5 里程碑

| 里程碑 | 目標 | 預計日期 |
|--------|------|---------|
| MVP 上線 | 10 個測試用戶 | Week 2 |
| Beta 完成 | 50 個活躍用戶 | Week 4 |
| 正式上線 | 100 個用戶 | Week 6 |
| 首個付費用戶 | 10 個月費 | Month 2 |
| 盈虧平衡 | 月收入 > 月成本 | Month 3 |
| 500 用戶 | 月收入 HK$5,000+ | Month 6 |

---

## 📎 附錄

### A. 完整指令列表

```
用戶指令：
  1 / 免費占卜  — 免費每日一牌
  2 / 方案      — 查看付費方案
  3 / 抽牌      — 直接抽牌（按層級）
  4 / 運程      — 查看今日運程
  0 / 幫助      — 幫助訊息
  pay / 付款    — 付款方式
  upgrade / 升級 — 升級方案
  status / 狀態 — 查看當前層級同剩餘額度
  settings / 設定 — 用戶偏好設定
  stop / 停止   — 停止所有推送
  restart / 重新開始 — 重新開始對話

管理員指令（+85263931048 專用）：
  /admin stats          — 統計數據
  /admin users          — 用戶列表
  /admin approve <phone> <tier> — 手動開通
  /admin reject <phone> <reason> — 拒絕付款
  /admin list pending   — 待確認列表
  /admin broadcast <msg> — 廣播訊息
  /admin grant <phone> <tier> <days> — 贈送天數
```

### B. 訊息模板庫

| 模板 ID | 用途 | 內容 |
|---------|------|------|
| WELCOME | 首次歡迎 | 歡迎訊息 + 功能介紹 |
| FREE_CARD | 免費抽牌 | 牌義 + CTA |
| FREE_LIMIT | 免費額度用完 | 提示升級 |
| PAYMENT_INFO | 付款方式 | FPS + USDT 資訊 |
| PAYMENT_PENDING | 付款確認中 | 等待確認 |
| PAYMENT_APPROVED | 付款通過 | 開通確認 |
| PAYMENT_REJECTED | 付款拒絕 | 重新付款指引 |
| DAILY_HOROSCOPE | 每日運程 | 運程內容 |
| RENEWAL_REMINDER | 續費提醒 | 續費通知 |
| UPGRADE_MONTHLY | 升級月費 | 月費 CTA |
| UPGRADE_VIP | 升級 VIP | VIP CTA |
| REENGAGEMENT | 重新參與 | 流失挽回 |
| REFERRAL | 推薦 | 推薦碼分享 |

### C. 塔羅牌完整列表

78 張牌（22 大阿爾克納 + 56 小阿爾克納）

**大阿爾克納：**
0 愚者、I 魔術師、II 女祭司、III 女皇、IV 皇帝、V 教皇、VI 戀人、VII 戰車、VIII 力量、IX 隱者、X 命運之輪、XI 正義、XII 吊人、XIII 死神、XIV 節制、XV 惡魔、XVI 塔、XVII 星星、XVIII 月亮、XIX 太陽、XX 審判、XXI 世界

**小阿爾克納：**
- 權杖 1-10 + 侍者/騎士/王后/國王
- 聖杯 1-10 + 侍者/騎士/王后/國王
- 寶劍 1-10 + 侍者/騎士/王后/國王
- 金幣 1-10 + 侍者/騎士/王后/國王

每張牌都有正位 + 逆位兩種解讀 = 156 種牌義

---

*設計完成日期: 2026-06-14*  
*設計者: 呀鬼 (Alfred)*  
*下次更新: MVP 開發啟動時*