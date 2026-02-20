# Polymarket Developer Documentation

> Fetched on 2026-02-04 17:34:30
> Source: https://docs.polymarket.com

---

## Table of Contents

1. [Developer Quickstart](#developer-quickstart)
2. [Fetching Market Data](#fetching-market-data)
3. [Placing Your First Order](#placing-your-first-order)
4. [API Rate Limits](#api-rate-limits)
5. [Endpoints](#endpoints)
6. [Glossary](#glossary)
7. [WSS Quickstart](#wss-quickstart)
8. [CLOB Introduction](#clob-introduction)
9. [CLOB Quickstart](#clob-quickstart)
10. [Authentication](#authentication)
11. [Geographic Restrictions](#geographic-restrictions)
12. [CLOB Status](#clob-status)
13. [Historical Timeseries Data](#historical-timeseries-data)
14. [Methods Overview](#methods-overview)
15. [Public Methods](#public-methods)
16. [L1 Methods](#l1-methods)
17. [L2 Methods](#l2-methods)
18. [Builder Methods](#builder-methods)
19. [Orders Overview](#orders-overview)
20. [Place Single Order](#place-single-order)
21. [Place Multiple Orders (Batching)](#place-multiple-orders-batching)
22. [Cancel Orders](#cancel-orders)
23. [Get Order](#get-order)
24. [Get Active Orders](#get-active-orders)
25. [Check Order Reward Scoring](#check-order-reward-scoring)
26. [Onchain Order Info](#onchain-order-info)
27. [Trades Overview](#trades-overview)
28. [Get Trades](#get-trades)
29. [WSS Overview](#wss-overview)
30. [WSS Authentication](#wss-authentication)
31. [Market Channel](#market-channel)
32. [User Channel](#user-channel)
33. [CTF Overview](#ctf-overview)
34. [Splitting USDC](#splitting-usdc)
35. [Merging Tokens](#merging-tokens)
36. [Redeeming Tokens](#redeeming-tokens)
37. [Deployment Resources](#deployment-resources)
38. [Gamma API Overview](#gamma-api-overview)
39. [Gamma Structure](#gamma-structure)
40. [How to Fetch Markets](#how-to-fetch-markets)
41. [Market Maker Introduction](#market-maker-introduction)
42. [MM Setup](#mm-setup)
43. [MM Trading](#mm-trading)
44. [Data Feeds](#data-feeds)
45. [Inventory Management](#inventory-management)
46. [Liquidity Rewards](#liquidity-rewards)
47. [Maker Rebates Program](#maker-rebates-program)
48. [Builder Program Introduction](#builder-program-introduction)
49. [Builder Profile & Keys](#builder-profile-keys)
50. [Builder Tiers](#builder-tiers)
51. [Order Attribution](#order-attribution)
52. [Relayer Client](#relayer-client)
53. [Builder Examples](#builder-examples)
54. [Blockchain Data Resources](#blockchain-data-resources)
55. [RTDS Overview](#rtds-overview)
56. [RTDS Comments](#rtds-comments)
57. [RTDS Crypto Prices](#rtds-crypto-prices)
58. [Sports WS Overview](#sports-ws-overview)
59. [Sports WS Quickstart](#sports-ws-quickstart)
60. [Sports WS Message Format](#sports-ws-message-format)
61. [Subgraph Overview](#subgraph-overview)
62. [Bridge Overview](#bridge-overview)
63. [Neg Risk Overview](#neg-risk-overview)
64. [Proxy Wallet](#proxy-wallet)
65. [UMA Resolution](#uma-resolution)
66. [API: Create Deposit Addresses](#api-create-deposit-addresses)
67. [API: Create Withdrawal Addresses](#api-create-withdrawal-addresses)
68. [API: Get a Quote](#api-get-a-quote)
69. [API: Get Supported Assets](#api-get-supported-assets)
70. [API: Get Transaction Status](#api-get-transaction-status)
71. [API: Get Aggregated Builder Leaderboard](#api-get-aggregated-builder-leaderboard)
72. [API: Get Daily Builder Volume Time-series](#api-get-daily-builder-volume-time-series)
73. [API: Get Comments by Comment ID](#api-get-comments-by-comment-id)
74. [API: Get Comments by User Address](#api-get-comments-by-user-address)
75. [API: List Comments](#api-list-comments)
76. [API: Get Closed Positions](#api-get-closed-positions)
77. [API: Get Current Positions](#api-get-current-positions)
78. [API: Get Top Holders](#api-get-top-holders)
79. [API: Get Total Position Value](#api-get-total-position-value)
80. [API: Get Trader Leaderboard](#api-get-trader-leaderboard)
81. [API: Get Trades](#api-get-trades)
82. [API: Get User Activity](#api-get-user-activity)
83. [API: Data API Health Check](#api-data-api-health-check)
84. [API: Get Event by ID](#api-get-event-by-id)
85. [API: Get Event by Slug](#api-get-event-by-slug)
86. [API: Get Event Tags](#api-get-event-tags)
87. [API: List Events](#api-list-events)
88. [API: Gamma Health Check](#api-gamma-health-check)
89. [API: Get Market by ID](#api-get-market-by-id)
90. [API: Get Market by Slug](#api-get-market-by-slug)
91. [API: Get Market Tags](#api-get-market-tags)
92. [API: List Markets](#api-list-markets)
93. [API: Download Accounting Snapshot](#api-download-accounting-snapshot)
94. [API: Get Live Volume](#api-get-live-volume)
95. [API: Get Open Interest](#api-get-open-interest)
96. [API: Get Total Markets Traded](#api-get-total-markets-traded)
97. [API: Get Multiple Orderbook Summaries](#api-get-multiple-orderbook-summaries)
98. [API: Get Orderbook Summary](#api-get-orderbook-summary)
99. [API: Get Market Price](#api-get-market-price)
100. [API: Get Midpoint Price](#api-get-midpoint-price)
101. [API: Get Multiple Market Prices](#api-get-multiple-market-prices)
102. [API: Get Multiple Market Prices by Request](#api-get-multiple-market-prices-by-request)
103. [API: Get Price History](#api-get-price-history)
104. [API: Get Public Profile](#api-get-public-profile)
105. [API: Search](#api-search)
106. [API: Get Series by ID](#api-get-series-by-id)
107. [API: List Series](#api-list-series)
108. [API: Get Sports Metadata](#api-get-sports-metadata)
109. [API: Get Sports Market Types](#api-get-sports-market-types)
110. [API: List Teams](#api-list-teams)
111. [API: Get Bid-Ask Spreads](#api-get-bid-ask-spreads)
112. [API: Get Related Tags by ID](#api-get-related-tags-by-id)
113. [API: Get Related Tags by Slug](#api-get-related-tags-by-slug)
114. [API: Get Tag by ID](#api-get-tag-by-id)
115. [API: Get Tag by Slug](#api-get-tag-by-slug)
116. [API: Get Tags Related to Tag ID](#api-get-tags-related-to-tag-id)
117. [API: Get Tags Related to Tag Slug](#api-get-tags-related-to-tag-slug)
118. [API: List Tags](#api-list-tags)
119. [Changelog](#changelog)
120. [FAQ: Does Polymarket have an API?](#faq-does-polymarket-have-an-api)
121. [FAQ: How To Use Embeds](#faq-how-to-use-embeds)
122. [FAQ: Geographic Restrictions](#faq-geographic-restrictions)
123. [FAQ: How Do I Export My Key?](#faq-how-do-i-export-my-key)
124. [FAQ: Is My Money Safe?](#faq-is-my-money-safe)
125. [FAQ: Is Polymarket The House?](#faq-is-polymarket-the-house)
126. [FAQ: Polymarket vs. Polling](#faq-polymarket-vs-polling)
127. [FAQ: Recover Missing Deposit](#faq-recover-missing-deposit)
128. [FAQ: Can I Sell Early?](#faq-can-i-sell-early)
129. [FAQ: How Do I Contact Support?](#faq-how-do-i-contact-support)
130. [FAQ: Does Polymarket Have a Token?](#faq-does-polymarket-have-a-token)
131. [FAQ: What is a Prediction Market?](#faq-what-is-a-prediction-market)
132. [FAQ: Why Crypto?](#faq-why-crypto)
133. [Deposit with Coinbase](#deposit-with-coinbase)
134. [How to Withdraw](#how-to-withdraw)
135. [Large Cross Chain Deposits](#large-cross-chain-deposits)
136. [Deposit Using Your Card](#deposit-using-your-card)
137. [Deposit by Transferring Crypto](#deposit-by-transferring-crypto)
138. [Deposit USDC on Ethereum](#deposit-usdc-on-ethereum)
139. [How to Deposit](#how-to-deposit)
140. [How to Sign-Up](#how-to-sign-up)
141. [Making Your First Trade](#making-your-first-trade)
142. [What is Polymarket?](#what-is-polymarket)
143. [How Are Markets Disputed?](#how-are-markets-disputed)
144. [How Are Markets Clarified?](#how-are-markets-clarified)
145. [How Are Markets Created?](#how-are-markets-created)
146. [How Are Markets Resolved?](#how-are-markets-resolved)
147. [Trading Fees](#trading-fees)
148. [Holding Rewards](#holding-rewards)
149. [How Are Prices Calculated?](#how-are-prices-calculated)
150. [Limit Orders](#limit-orders)
151. [Liquidity Rewards (Learn)](#liquidity-rewards-learn)
152. [Maker Rebates Program (Learn)](#maker-rebates-program-learn)
153. [Market Orders](#market-orders)
154. [Does Polymarket Have Trading Limits?](#does-polymarket-have-trading-limits)
155. [Using the Order Book](#using-the-order-book)

---


## Developer Quickstart

> Source: https://docs.polymarket.com/quickstart/overview

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Developer Quickstart

Developer Quickstart

Polymarket provides a suite of APIs and SDKs for building prediction market applications. This guide will help you understand what’s available and where to find it.

---

## [​](#what-can-you-build) What Can You Build?

| If you want to… | Start here |
| --- | --- |
| Fetch markets & prices | [Fetching Market Data](/quickstart/fetching-data) |
| Place orders for yourself | [Placing Your First Order](/quickstart/first-order) |
| Build a trading app for users | [Builders Program Introduction](/developers/builders/builder-intro) |
| Provide liquidity | [Market Makers](/developers/market-makers/introduction) |

---

## [​](#apis-at-a-glance) APIs at a Glance

### [​](#markets-&-data) Markets & Data

[## Gamma API

**Market discovery & metadata**Fetch events, markets, categories, and resolution data. This is where you discover what’s tradeable.`https://gamma-api.polymarket.com`](/developers/gamma-markets-api/overview)[## CLOB API

**Prices, orderbooks & trading**Get real-time prices, orderbook depth, and place orders. The core trading API.`https://clob.polymarket.com`](/developers/CLOB/introduction)[## Data API

**Positions, activity & history**Query user positions, trade history, and portfolio data.`https://data-api.polymarket.com`](/developers/misc-endpoints/data-api-get-positions)[## WebSocket

**Real-time updates**Subscribe to orderbook changes, price updates, and order status.`wss://ws-subscriptions-clob.polymarket.com`](/developers/CLOB/websocket/wss-overview)

### [​](#additional-data-sources) Additional Data Sources

[## RTDS

**Low-latency data stream**Real-time crypto prices and comments. Optimized for market makers.](/developers/RTDS/RTDS-overview)[## Subgraph

**Onchain queries**Query blockchain state directly via GraphQL.](/developers/subgraph/overview)

### [​](#trading-infrastructure) Trading Infrastructure

[## CTF Operations

**Token split/merge/redeem**Convert between USDC and outcome tokens. Essential for inventory management.](/developers/CTF/overview)[## Relayer Client

**Gasless transactions**Builders can offer gasfree transactions via Polymarket’s relayer.](/developers/builders/relayer-client)

---

## [​](#sdks-&-libraries) SDKs & Libraries

[## CLOB Client (TypeScript)

`npm install @polymarket/clob-client`](https://github.com/Polymarket/clob-client)

[## CLOB Client (Python)

`pip install py-clob-client`](https://github.com/Polymarket/py-clob-client)[## CLOB Client (Rust)

`cargo add polymarket-client-sdk`](https://github.com/Polymarket/rs-clob-client)

For builders routing orders for users:

[## Relayer Client

Gasless wallet operations](https://github.com/Polymarket/builder-relayer-client)[## Signing SDK

Builder authentication headers](https://github.com/Polymarket/builder-signing-sdk)

[Fetching Market Data](/quickstart/fetching-data)

⌘I

---


## Fetching Market Data

> Source: https://docs.polymarket.com/quickstart/fetching-data

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Developer Quickstart

Fetching Market Data

Get market data with zero setup. No API key, no authentication, no wallet required.

---

## [​](#understanding-the-data-model) Understanding the Data Model

Before fetching data, understand how Polymarket structures its markets:

1

Event

The top-level object representing a question like “Will X happen?”

2

Market

Each event contains one or more markets. Each market is a specific tradable binary outcome.

3

Outcomes & Prices

Markets have `outcomes` and `outcomePrices` arrays that map 1:1. These prices represent implied probabilities.

Copy

```shiki
{
  "outcomes": "[\"Yes\", \"No\"]",
  "outcomePrices": "[\"0.20\", \"0.80\"]"
}
// Index 0: "Yes" → 0.20 (20% probability)
// Index 1: "No" → 0.80 (80% probability)
```

---

## [​](#fetch-active-events) Fetch Active Events

List all currently active events on Polymarket:

Copy

```shiki
curl "https://gamma-api.polymarket.com/events?active=true&closed=false&limit=5"
```

Example Response

Copy

```shiki
[
  {
    "id": "123456",
    "slug": "will-bitcoin-reach-100k-by-2025",
    "title": "Will Bitcoin reach $100k by 2025?",
    "active": true,
    "closed": false,
    "tags": [
      { "id": "21", "label": "Crypto", "slug": "crypto" }
    ],
    "markets": [
      {
        "id": "789",
        "question": "Will Bitcoin reach $100k by 2025?",
        "clobTokenIds": ["TOKEN_YES_ID", "TOKEN_NO_ID"],
        "outcomes": "[\"Yes\", \"No\"]",
        "outcomePrices": "[\"0.65\", \"0.35\"]"
      }
    ]
  }
]
```

Always use `active=true&closed=false` to filter for live, tradable events.

---

## [​](#market-discovery-best-practices) Market Discovery Best Practices

### [​](#for-sports-events) For Sports Events

Use the `/sports` endpoint to discover leagues, then query by `series_id`:

Copy

```shiki
# Get all supported sports leagues
curl "https://gamma-api.polymarket.com/sports"

# Get events for a specific league (e.g., NBA series_id=10345)
curl "https://gamma-api.polymarket.com/events?series_id=10345&active=true&closed=false"

# Filter to just game bets (not futures) using tag_id=100639
curl "https://gamma-api.polymarket.com/events?series_id=10345&tag_id=100639&active=true&closed=false&order=startTime&ascending=true"
```

`/sports` only returns automated leagues. For others (UFC, Boxing, F1, Golf, Chess), use tag IDs via `/events?tag_id=<tag_id>`.

### [​](#for-non-sports-topics) For Non-Sports Topics

Use `/tags` to discover all available categories, then filter events:

Copy

```shiki
# Get all available tags
curl "https://gamma-api.polymarket.com/tags?limit=100"

# Query events by topic
curl "https://gamma-api.polymarket.com/events?tag_id=2&active=true&closed=false"
```

Each event response includes a `tags` array, useful for discovering categories from live data and building your own tag mapping.

---

## [​](#get-market-details) Get Market Details

Once you have an event, get details for a specific market using its ID or slug:

Copy

```shiki
curl "https://gamma-api.polymarket.com/markets?slug=will-bitcoin-reach-100k-by-2025"
```

The response includes `clobTokenIds`, you’ll need these to fetch prices and place orders.

---

## [​](#get-current-price) Get Current Price

Query the CLOB for the current price of any token:

Copy

```shiki
curl "https://clob.polymarket.com/price?token_id=YOUR_TOKEN_ID&side=buy"
```

Example Response

Copy

```shiki
{
  "price": "0.65"
}
```

---

## [​](#get-orderbook-depth) Get Orderbook Depth

See all bids and asks for a market:

Copy

```shiki
curl "https://clob.polymarket.com/book?token_id=YOUR_TOKEN_ID"
```

Example Response

Copy

```shiki
{
  "market": "0x...",
  "asset_id": "YOUR_TOKEN_ID",
  "bids": [
    { "price": "0.64", "size": "500" },
    { "price": "0.63", "size": "1200" }
  ],
  "asks": [
    { "price": "0.66", "size": "300" },
    { "price": "0.67", "size": "800" }
  ]
}
```

---

## [​](#more-data-apis) More Data APIs

[## Gamma API

Deep dive into market discovery](/developers/gamma-markets-api/overview)[## Data API

Positions, activity, and holders data](/developers/misc-endpoints/data-api-get-positions)[## WebSocket

Real-time orderbook updates](/developers/CLOB/websocket/wss-overview)[## RTDS

Real-time data streaming service](/developers/RTDS/RTDS-overview)

[Developer Quickstart](/quickstart/overview)[Placing Your First Order](/quickstart/first-order)

⌘I

---


## Placing Your First Order

> Source: https://docs.polymarket.com/quickstart/first-order

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Developer Quickstart

Placing Your First Order

This guide walks you through placing an order on Polymarket using your own wallet.

---

## [​](#installation) Installation

TypeScript

Python

Rust

Copy

```shiki
npm install @polymarket/clob-client ethers@5
```

---

## [​](#step-1-initialize-client-with-private-key) Step 1: Initialize Client with Private Key

TypeScript

Python

Copy

```shiki
import { ClobClient } from "@polymarket/clob-client";
import { Wallet } from "ethers"; // v5.8.0

const HOST = "https://clob.polymarket.com";
const CHAIN_ID = 137; // Polygon mainnet
const signer = new Wallet(process.env.PRIVATE_KEY);

const client = new ClobClient(HOST, CHAIN_ID, signer);
```

---

## [​](#step-2-derive-user-api-credentials) Step 2: Derive User API Credentials

Your private key is used once to derive API credentials. These credentials authenticate all subsequent requests.

TypeScript

Python

Copy

```shiki
// Get existing API key, or create one if none exists
const userApiCreds = await client.createOrDeriveApiKey();

console.log("API Key:", userApiCreds.apiKey);
console.log("Secret:", userApiCreds.secret);
console.log("Passphrase:", userApiCreds.passphrase);
```

---

## [​](#step-3-configure-signature-type-and-funder) Step 3: Configure Signature Type and Funder

Before reinitializing the client, determine your **signature type** and **funder address**:

| How do you want to trade? | Type | Value | Funder Address |
| --- | --- | --- | --- |
| I want to use an EOA wallet. It holds USDCe and position tokens, and I’ll pay my own gas. | EOA | `0` | Your EOA wallet address |
| I want to trade through my Polymarket.com account (Magic Link email/Google login). | POLY\_PROXY | `1` | Your proxy wallet address |
| I want to trade through my Polymarket.com account (browser wallet connection). | GNOSIS\_SAFE | `2` | Your proxy wallet address |

If you have a Polymarket.com account, your funds are in a proxy wallet (visible in the profile dropdown). Use type 1 or 2. Type 0 is for standalone EOA wallets only.

---

## [​](#step-4-reinitialize-with-full-authentication) Step 4: Reinitialize with Full Authentication

TypeScript

Python

Copy

```shiki
// Choose based on your wallet type (see table above)
const SIGNATURE_TYPE = 0; // EOA example
const FUNDER_ADDRESS = signer.address; // For EOA, funder is your wallet

const client = new ClobClient(
  HOST,
  CHAIN_ID,
  signer,
  userApiCreds,
  SIGNATURE_TYPE,
  FUNDER_ADDRESS
);
```

**Do not use Builder API credentials in place of User API credentials!** Builder credentials are for order attribution, not user authentication. See [Builder Order Attribution](/developers/builders/order-attribution).

---

## [​](#step-5-place-an-order) Step 5: Place an Order

Now you’re ready to trade! First, get a token ID from the [Gamma API](/developers/gamma-markets-api/get-markets).

TypeScript

Python

Copy

```shiki
import { Side, OrderType } from "@polymarket/clob-client";

// Get market info first
const market = await client.getMarket("TOKEN_ID");

const response = await client.createAndPostOrder(
  {
    tokenID: "TOKEN_ID",
    price: 0.50,        // Price per share ($0.50)
    size: 10,           // Number of shares
    side: Side.BUY,     // BUY or SELL
  },
  {
    tickSize: market.tickSize,
    negRisk: market.negRisk,    // true for multi-outcome events
  },
  OrderType.GTC  // Good-Til-Cancelled
);

console.log("Order ID:", response.orderID);
console.log("Status:", response.status);
```

---

## [​](#step-6-check-your-orders) Step 6: Check Your Orders

TypeScript

Python

Copy

```shiki
// View all open orders
const openOrders = await client.getOpenOrders();
console.log(`You have ${openOrders.length} open orders`);

// View your trade history
const trades = await client.getTrades();
console.log(`You've made ${trades.length} trades`);

// Cancel an order
await client.cancelOrder(response.orderID);
```

---

## [​](#troubleshooting) Troubleshooting

Invalid Signature / L2 Auth Not Available

Wrong private key, signature type, or funder address for the derived User API credentials.Double check the following values when creating User API credentials via `createOrDeriveApiKey()`:

* Do not use Builder API credentials in place of User API credentials
* Check `signatureType` matches your account type (0, 1, or 2)
* Ensure `funder` is correct for your wallet type

Unauthorized / Invalid API Key

Wrong API key, secret, or passphrase.Re-derive credentials with `createOrDeriveApiKey()` and update your config.

Not Enough Balance / Allowance

Either not enough USDCe / position tokens in your funder address, or you lack approvals to spend your tokens.

* Deposit USDCe to your funder address.
* Ensure you have more USDCe than what’s committed in open orders.
* Check that you’ve set all necessary token approvals.

Blocked by Cloudflare / Geoblock

You’re trying to place a trade from a restricted region.See [Geographic Restrictions](/developers/CLOB/geoblock) for details.

---

## [​](#adding-builder-api-credentials) Adding Builder API Credentials

If you’re building an app that routes orders for your users, you can add builder credentials to get attribution on the [Builder Leaderboard](https://builders.polymarket.com/):

TypeScript

Copy

```shiki
import { BuilderConfig, BuilderApiKeyCreds } from "@polymarket/builder-signing-sdk";

const builderCreds: BuilderApiKeyCreds = {
  key: process.env.POLY_BUILDER_API_KEY!,
  secret: process.env.POLY_BUILDER_SECRET!,
  passphrase: process.env.POLY_BUILDER_PASSPHRASE!,
};

const builderConfig = new BuilderConfig({ localBuilderCreds: builderCreds });

// Add builderConfig as the last parameter
const client = new ClobClient(
  HOST, 
  CHAIN_ID, 
  signer, 
  userApiCreds, 
  signatureType, 
  funderAddress,
  undefined, 
  false, 
  builderConfig
);
```

Builder credentials are **separate** from user credentials. You use your builder
credentials to tag orders, but each user still needs their own L2 credentials to trade.

[## Full Builder Guide

Complete documentation for order attribution and gasless transactions](/developers/builders/order-attribution)

[Fetching Market Data](/quickstart/fetching-data)[Glossary](/quickstart/reference/glossary)

⌘I

---


## API Rate Limits

> Source: https://docs.polymarket.com/quickstart/introduction/rate-limits

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Developer Quickstart

API Rate Limits

## [​](#how-rate-limiting-works) How Rate Limiting Works

All rate limits are enforced using Cloudflare’s throttling system. When you exceed the maximum configured rate for any endpoint, requests are throttled rather than immediately rejected. This means:

* **Throttling**: Requests over the limit are delayed/queued rather than dropped
* **Burst Allowances**: Some endpoints allow short bursts above the sustained rate
* **Time Windows**: Limits reset based on sliding time windows (e.g., per 10 seconds, per minute)

## [​](#general-rate-limits) General Rate Limits

| Endpoint | Limit | Notes |
| --- | --- | --- |
| General Rate Limiting | 15000 requests / 10s | Throttle requests over the maximum configured rate |
| ”OK” Endpoint | 100 requests / 10s | Throttle requests over the maximum configured rate |

## [​](#data-api-rate-limits) Data API Rate Limits

| Endpoint | Limit | Notes |
| --- | --- | --- |
| Data API (General) | 1000 requests / 10s | Throttle requests over the maximum configured rate |
| Data API `/trades` | 200 requests / 10s | Throttle requests over the maximum configured rate |
| Data API `/positions` | 150 requests / 10s | Throttle requests over the maximum configured rate |
| Data API `/closed-positions` | 150 requests / 10s | Throttle requests over the maximum configured rate |
| Data API “OK” Endpoint | 100 requests / 10s | Throttle requests over the maximum configured rate |

## [​](#gamma-api-rate-limits) GAMMA API Rate Limits

| Endpoint | Limit | Notes |
| --- | --- | --- |
| GAMMA (General) | 4000 requests / 10s | Throttle requests over the maximum configured rate |
| GAMMA Get Comments | 200 requests / 10s | Throttle requests over the maximum configured rate |
| GAMMA `/events` | 500 requests / 10s | Throttle requests over the maximum configured rate |
| GAMMA `/markets` | 300 requests / 10s | Throttle requests over the maximum configured rate |
| GAMMA `/markets` /events listing | 900 requests / 10s | Throttle requests over the maximum configured rate |
| GAMMA Tags | 200 requests / 10s | Throttle requests over the maximum configured rate |
| GAMMA Search | 350 requests / 10s | Throttle requests over the maximum configured rate |

## [​](#clob-api-rate-limits) CLOB API Rate Limits

### [​](#general-clob-endpoints) General CLOB Endpoints

| Endpoint | Limit | Notes |
| --- | --- | --- |
| CLOB (General) | 9000 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB GET Balance Allowance | 200 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB UPDATE Balance Allowance | 50 requests / 10s | Throttle requests over the maximum configured rate |

### [​](#clob-market-data) CLOB Market Data

| Endpoint | Limit | Notes |
| --- | --- | --- |
| CLOB `/book` | 1500 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB `/books` | 500 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB `/price` | 1500 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB `/prices` | 500 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB `/midprice` | 1500 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB `/midprices` | 500 requests / 10s | Throttle requests over the maximum configured rate |

### [​](#clob-ledger-endpoints) CLOB Ledger Endpoints

| Endpoint | Limit | Notes |
| --- | --- | --- |
| CLOB Ledger (`/trades` `/orders` `/notifications` `/order`) | 900 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB Ledger `/data/orders` | 500 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB Ledger `/data/trades` | 500 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB `/notifications` | 125 requests / 10s | Throttle requests over the maximum configured rate |

### [​](#clob-markets-&-pricing) CLOB Markets & Pricing

| Endpoint | Limit | Notes |
| --- | --- | --- |
| CLOB Price History | 1000 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB Market Tick Size | 200 requests / 10s | Throttle requests over the maximum configured rate |

### [​](#clob-authentication) CLOB Authentication

| Endpoint | Limit | Notes |
| --- | --- | --- |
| CLOB API Keys | 100 requests / 10s | Throttle requests over the maximum configured rate |

### [​](#clob-trading-endpoints) CLOB Trading Endpoints

| Endpoint | Limit | Notes |
| --- | --- | --- |
| CLOB POST `/order` | 3500 requests / 10s (500/s) | BURST - Throttle requests over the maximum configured rate |
| CLOB POST `/order` | 36000 requests / 10 minutes (60/s) | Throttle requests over the maximum configured rate |
| CLOB DELETE `/order` | 3000 requests / 10s (300/s) | BURST - Throttle requests over the maximum configured rate |
| CLOB DELETE `/order` | 30000 requests / 10 minutes (50/s) | Throttle requests over the maximum configured rate |
| CLOB POST `/orders` | 1000 requests / 10s (100/s) | BURST - Throttle requests over the maximum configured rate |
| CLOB POST `/orders` | 15000 requests / 10 minutes (25/s) | Throttle requests over the maximum configured rate |
| CLOB DELETE `/orders` | 1000 requests / 10s (100/s) | BURST - Throttle requests over the maximum configured rate |
| CLOB DELETE `/orders` | 15000 requests / 10 minutes (25/s) | Throttle requests over the maximum configured rate |
| CLOB DELETE `/cancel-all` | 250 requests / 10s (25/s) | BURST - Throttle requests over the maximum configured rate |
| CLOB DELETE `/cancel-all` | 6000 requests / 10 minutes (10/s) | Throttle requests over the maximum configured rate |
| CLOB DELETE `/cancel-market-orders` | 1000 requests / 10s (100/s) | BURST - Throttle requests over the maximum configured rate |
| CLOB DELETE `/cancel-market-orders` | 1500 requests / 10 minutes (25/s) | Throttle requests over the maximum configured rate |

## [​](#other-api-rate-limits) Other API Rate Limits

| Endpoint | Limit | Notes |
| --- | --- | --- |
| RELAYER `/submit` | 25 requests / 1 minute | Throttle requests over the maximum configured rate |
| User PNL API | 200 requests / 10s | Throttle requests over the maximum configured rate |

[Glossary](/quickstart/reference/glossary)[Endpoints](/quickstart/reference/endpoints)

⌘I

---


## Endpoints

> Source: https://docs.polymarket.com/quickstart/reference/endpoints

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Developer Quickstart

Endpoints

All base URLs for Polymarket APIs. See individual API documentation for available routes and parameters.

---

## [​](#rest-apis) REST APIs

| API | Base URL | Description |
| --- | --- | --- |
| **CLOB API** | `https://clob.polymarket.com` | Order management, prices, orderbooks |
| **Gamma API** | `https://gamma-api.polymarket.com` | Market discovery, metadata, events |
| **Data API** | `https://data-api.polymarket.com` | User positions, activity, history |

---

## [​](#websocket-endpoints) WebSocket Endpoints

| Service | URL | Description |
| --- | --- | --- |
| **CLOB WebSocket** | `wss://ws-subscriptions-clob.polymarket.com/ws/` | Orderbook updates, order status |
| **RTDS** | `wss://ws-live-data.polymarket.com` | Low-latency crypto prices, comments |

---

## [​](#quick-reference) Quick Reference

### [​](#clob-api) CLOB API

Copy

```shiki
https://clob.polymarket.com
```

Common endpoints:

* `GET /price` — Get current price for a token
* `GET /book` — Get orderbook for a token
* `GET /midpoint` — Get midpoint price
* `POST /order` — Place an order (auth required)
* `DELETE /order` — Cancel an order (auth required)

[Full CLOB documentation →](/developers/CLOB/introduction)

### [​](#gamma-api) Gamma API

Copy

```shiki
https://gamma-api.polymarket.com
```

Common endpoints:

* `GET /events` — List events
* `GET /markets` — List markets
* `GET /events/{id}` — Get event details

[Full Gamma documentation →](/developers/gamma-markets-api/overview)

### [​](#data-api) Data API

Copy

```shiki
https://data-api.polymarket.com
```

Common endpoints:

* `GET /positions` — Get user positions
* `GET /activity` — Get user activity
* `GET /trades` — Get trade history

[Full Data API documentation →](/developers/misc-endpoints/data-api-get-positions)

### [​](#clob-websocket) CLOB WebSocket

Copy

```shiki
wss://ws-subscriptions-clob.polymarket.com/ws/
```

Channels:

* `market` — Orderbook and price updates (public)
* `user` — Order status updates (authenticated)

[Full WebSocket documentation →](/developers/CLOB/websocket/wss-overview)

### [​](#rtds-real-time-data-stream) RTDS (Real-Time Data Stream)

Copy

```shiki
wss://ws-live-data.polymarket.com
```

Channels:

* Crypto price feeds
* Comment streams

[Full RTDS documentation →](/developers/RTDS/RTDS-overview)

[API Rate Limits](/quickstart/introduction/rate-limits)[Market Maker Introduction](/developers/market-makers/introduction)

⌘I

---


## Glossary

> Source: https://docs.polymarket.com/quickstart/reference/glossary

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Developer Quickstart

Glossary

## [​](#markets-&-events) Markets & Events

| Term | Definition |
| --- | --- |
| **Event** | A collection of related markets grouped under a common topic. Example: “2024 US Presidential Election” contains markets for each candidate. |
| **Market** | A single tradeable outcome within an event. Each market has a Yes and No side. Corresponds to a condition ID, question ID, and pair of token IDs. |
| **Token** | Represents a position in a specific outcome (Yes or No). Prices range from 0.00 to 1.00. Winning tokens redeem for $1 USDCe. Also called *outcome token* or referenced by *token ID*. |
| **Token ID** | The unique identifier for a specific outcome token. Required when placing orders or querying prices. |
| **Condition ID** | Onchain identifier for a market’s resolution condition. Used in CTF operations. |
| **Question ID** | Identifier linking a market to its resolution oracle (UMA). |
| **Slug** | Human-readable URL identifier for a market or event. Found in Polymarket URLs: `polymarket.com/event/[slug]` |

---

## [​](#trading) Trading

| Term | Definition |
| --- | --- |
| **CLOB** | Central Limit Order Book. Polymarket’s off-chain order matching system. Orders are matched here before onchain settlement. |
| **Tick Size** | The minimum price increment for a market. Usually `0.01` (1 cent) or `0.001` (0.1 cent). |
| **Fill** | When an order is matched and executed. Orders can be partially or fully filled. |

---

## [​](#order-types) Order Types

| Term | Definition |
| --- | --- |
| **GTC** | Good-Til-Cancelled. An order that remains open until filled or manually cancelled. |
| **GTD** | Good-Til-Date. An order that expires at a specified time if not filled. |
| **FOK** | Fill-Or-Kill. An order that must be filled entirely and immediately, or it’s cancelled. No partial fills. |
| **FAK** | Fill-And-Kill. An order that fills as much as possible immediately, then cancels any remaining unfilled portion. |

---

## [​](#market-types) Market Types

| Term | Definition |
| --- | --- |
| **Binary Market** | A market with exactly two outcomes: Yes and No. The prices always sum to approximately $1. |
| **Negative Risk (NegRisk)** | A multi-outcome event where only one outcome can resolve Yes. Requires `negRisk: true` in order parameters. [Details](/developers/neg-risk/overview) |

---

## [​](#wallets) Wallets

| Term | Definition |
| --- | --- |
| **EOA** | Externally Owned Account. A standard Ethereum wallet controlled by a private key. |
| **Funder Address** | The wallet address that holds funds and tokens for trading. |
| **Signature Type** | Identifies wallet type when trading. `0` = EOA, `1` = Magic Link proxy, `2` = Gnosis Safe proxy. |

---

## [​](#token-operations-ctf) Token Operations (CTF)

| Term | Definition |
| --- | --- |
| **CTF** | Conditional Token Framework. The onchain smart contracts that manage outcome tokens. |
| **Split** | Convert USDCe into a complete set of outcome tokens (one Yes + one No). |
| **Merge** | Convert a complete set of outcome tokens back into USDCe. |
| **Redeem** | After resolution, exchange winning tokens for $1 USDCe each. |

---

## [​](#infrastructure) Infrastructure

| Term | Definition |
| --- | --- |
| **Polygon** | The blockchain network where Polymarket operates. Chain ID: `137`. |
| **USDCe** | The stablecoin used as collateral on Polymarket. Bridged USDC on Polygon. |

[Placing Your First Order](/quickstart/first-order)[API Rate Limits](/quickstart/introduction/rate-limits)

⌘I

---


## WSS Quickstart

> Source: https://docs.polymarket.com/quickstart/websocket/WSS-Quickstart

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Websocket

WSS Quickstart

The following code samples and explanation will show you how to subscribe to the Marker and User channels of the Websocket.
You’ll need your API keys to do this so we’ll start with that.

## [​](#getting-your-api-keys) Getting your API Keys

DeriveAPIKeys-Python

DeriveAPIKeys-TS

Copy

```shiki
from py_clob_client.client import ClobClient

host: str = "https://clob.polymarket.com"
key: str = "" #This is your Private Key. If using email login export from https://reveal.magic.link/polymarket otherwise export from your Web3 Application
chain_id: int = 137 #No need to adjust this
POLYMARKET_PROXY_ADDRESS: str = '' #This is the address you deposit/send USDC to to FUND your Polymarket account.

#Select from the following 3 initialization options to matches your login method, and remove any unused lines so only one client is initialized.

### Initialization of a client using a Polymarket Proxy associated with an Email/Magic account. If you login with your email use this example.
client = ClobClient(host, key=key, chain_id=chain_id, signature_type=1, funder=POLYMARKET_PROXY_ADDRESS)

### Initialization of a client using a Polymarket Proxy associated with a Browser Wallet(Metamask, Coinbase Wallet, etc)
client = ClobClient(host, key=key, chain_id=chain_id, signature_type=2, funder=POLYMARKET_PROXY_ADDRESS)

### Initialization of a client that trades directly from an EOA. 
client = ClobClient(host, key=key, chain_id=chain_id)

print( client.derive_api_key() )
```

See all 20 lines

## [​](#using-those-keys-to-connect-to-the-market-or-user-websocket) Using those keys to connect to the Market or User Websocket

WSS-Connection

Copy

```shiki
from websocket import WebSocketApp
import json
import time
import threading

MARKET_CHANNEL = "market"
USER_CHANNEL = "user"

class WebSocketOrderBook:
    def __init__(self, channel_type, url, data, auth, message_callback, verbose):
        self.channel_type = channel_type
        self.url = url
        self.data = data
        self.auth = auth
        self.message_callback = message_callback
        self.verbose = verbose
        furl = url + "/ws/" + channel_type
        self.ws = WebSocketApp(
            furl,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open,
        )
        self.orderbooks = {}

    def on_message(self, ws, message):
        print(message)
        pass

    def on_error(self, ws, error):
        print("Error: ", error)
        exit(1)

    def on_close(self, ws, close_status_code, close_msg):
        print("closing")
        exit(0)

    def on_open(self, ws):
        if self.channel_type == MARKET_CHANNEL:
            ws.send(json.dumps({"assets_ids": self.data, "type": MARKET_CHANNEL}))
        elif self.channel_type == USER_CHANNEL and self.auth:
            ws.send(
                json.dumps(
                    {"markets": self.data, "type": USER_CHANNEL, "auth": self.auth}
                )
            )
        else:
            exit(1)

        thr = threading.Thread(target=self.ping, args=(ws,))
        thr.start()

    def subscribe_to_tokens_ids(self, assets_ids):
        if self.channel_type == MARKET_CHANNEL:
            self.ws.send(json.dumps({"assets_ids": assets_ids, "operation": "subscribe"}))

    def unsubscribe_to_tokens_ids(self, assets_ids):
        if self.channel_type == MARKET_CHANNEL:
            self.ws.send(json.dumps({"assets_ids": assets_ids, "operation": "unsubscribe"}))

    def ping(self, ws):
        while True:
            ws.send("PING")
            time.sleep(10)

    def run(self):
        self.ws.run_forever()

if __name__ == "__main__":
    url = "wss://ws-subscriptions-clob.polymarket.com"
    #Complete these by exporting them from your initialized client. 
    api_key = ""
    api_secret = ""
    api_passphrase = ""

    asset_ids = [
        "109681959945973300464568698402968596289258214226684818748321941747028805721376",
    ]
    condition_ids = [] # no really need to filter by this one

    auth = {"apiKey": api_key, "secret": api_secret, "passphrase": api_passphrase}

    market_connection = WebSocketOrderBook(
        MARKET_CHANNEL, url, asset_ids, auth, None, True
    )
    user_connection = WebSocketOrderBook(
        USER_CHANNEL, url, condition_ids, auth, None, True
    )

    market_connection.subscribe_to_tokens_ids(["123"])
    # market_connection.unsubscribe_to_tokens_ids(["123"])

    market_connection.run()
    # user_connection.run()
```

See all 99 lines

[WSS Overview](/developers/CLOB/websocket/wss-overview)[WSS Authentication](/developers/CLOB/websocket/wss-auth)

⌘I

---


## CLOB Introduction

> Source: https://docs.polymarket.com/developers/CLOB/introduction

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Central Limit Order Book

CLOB Introduction

Welcome to the Polymarket Order Book API! This documentation provides overviews, explanations, examples, and annotations to simplify interaction with the order book. The following sections detail the Polymarket Order Book and the API usage.

## [​](#system) System

Polymarket’s Order Book, or CLOB (Central Limit Order Book), is hybrid-decentralized. It includes an operator for off-chain matching/ordering, with settlement executed on-chain, non-custodially, via signed order messages.
The exchange uses a custom Exchange contract facilitating atomic swaps between binary Outcome Tokens (CTF ERC1155 assets and ERC20 PToken assets) and collateral assets (ERC20), following signed limit orders. Designed for binary markets, the contract enables complementary tokens to match across a unified order book.
Orders are EIP712-signed structured data. Matched orders have one maker and one or more takers, with price improvements benefiting the taker. The operator handles off-chain order management and submits matched trades to the blockchain for on-chain execution.

## [​](#api) API

The Polymarket Order Book API enables market makers and traders to programmatically manage market orders. Orders of any amount can be created, listed, fetched, or read from the market order books. Data includes all available markets, market prices, and order history via REST and WebSocket endpoints.

## [​](#security) Security

Polymarket’s Exchange contract has been audited by Chainsecurity ([View Audit](https://github.com/Polymarket/ctf-exchange/blob/main/audit/ChainSecurity_Polymarket_Exchange_audit.pdf)).
The operator’s privileges are limited to order matching, non-censorship, and ensuring correct ordering. Operators can’t set prices or execute unauthorized trades. Users can cancel orders on-chain independently if trust issues arise.

## [​](#fees) Fees

### [​](#schedule) Schedule

> Subject to change

| Volume Level | Maker Fee Base Rate (bps) | Taker Fee Base Rate (bps) |
| --- | --- | --- |
| >0 USDC | 0 | 0 |

### [​](#overview) Overview

Fees apply symmetrically in output assets (proceeds). This symmetry ensures fairness and market integrity. Fees are calculated differently depending on whether you are buying or selling:

* **Selling outcome tokens (base) for collateral (quote):**

feeQuote=baseRate×min⁡(price,1−price)×sizefeeQuote = baseRate \times \min(price, 1 - price) \times sizefeeQuote=baseRate×min(price,1−price)×size

* **Buying outcome tokens (base) with collateral (quote):**

feeBase=baseRate×min⁡(price,1−price)×sizepricefeeBase = baseRate \times \min(price, 1 - price) \times \frac{size}{price}feeBase=baseRate×min(price,1−price)×pricesize​

## [​](#additional-resources) Additional Resources

* [Exchange contract source code](https://github.com/Polymarket/ctf-exchange/tree/main/src)
* [Exchange contract documentation](https://github.com/Polymarket/ctf-exchange/blob/main/docs/Overview.md)

[Blockchain Data Resources](/developers/builders/blockchain-data-resources)[Status](/developers/CLOB/status)

⌘I

---


## CLOB Quickstart

> Source: https://docs.polymarket.com/developers/CLOB/quickstart

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Central Limit Order Book

Quickstart

## [​](#installation) Installation

TypeScript

Python

Rust

Copy

```shiki
npm install @polymarket/clob-client ethers
```

---

## [​](#quick-start) Quick Start

### [​](#1-setup-client) 1. Setup Client

TypeScript

Python

Copy

```shiki
import { ClobClient } from "@polymarket/clob-client";
import { Wallet } from "ethers"; // v5.8.0

const HOST = "https://clob.polymarket.com";
const CHAIN_ID = 137; // Polygon mainnet
const signer = new Wallet(process.env.PRIVATE_KEY);

// Create or derive user API credentials
const tempClient = new ClobClient(HOST, CHAIN_ID, signer);
const apiCreds = await tempClient.createOrDeriveApiKey();

// See 'Signature Types' note below
const signatureType = 0;

// Initialize trading client
const client = new ClobClient(
  HOST, 
  CHAIN_ID, 
  signer, 
  apiCreds, 
  signatureType
);
```

This quick start sets your EOA as the trading account. You’ll need to fund this
wallet to trade and pay for gas on transactions. Gas-less transactions are only
available by deploying a proxy wallet and using Polymarket’s Polygon relayer
infrastructure.

Signature Types

| Wallet Type | ID | When to Use |
| --- | --- | --- |
| EOA | `0` | Standard Ethereum wallet (MetaMask) |
| Custom Proxy | `1` | Specific to Magic Link users from Polymarket only |
| Gnosis Safe | `2` | Injected providers (Metamask, Rabby, embedded wallets) |

---

### [​](#2-place-an-order) 2. Place an Order

TypeScript

Python

Copy

```shiki
import { Side } from "@polymarket/clob-client";

// Place a limit order in one step
const response = await client.createAndPostOrder({
  tokenID: "YOUR_TOKEN_ID", // Get from Gamma API
  price: 0.65, // Price per share
  size: 10, // Number of shares
  side: Side.BUY, // or SELL
});

console.log(`Order placed! ID: ${response.orderID}`);
```

---

### [​](#3-check-your-orders) 3. Check Your Orders

TypeScript

Python

Copy

```shiki
// View all open orders
const openOrders = await client.getOpenOrders();
console.log(`You have ${openOrders.length} open orders`);

// View your trade history
const trades = await client.getTrades();
console.log(`You've made ${trades.length} trades`);
```

---

## [​](#complete-example) Complete Example

TypeScript

Python

Copy

```shiki
import { ClobClient, Side } from "@polymarket/clob-client";
import { Wallet } from "ethers";

async function trade() {
  const HOST = "https://clob.polymarket.com";
  const CHAIN_ID = 137; // Polygon mainnet
  const signer = new Wallet(process.env.PRIVATE_KEY);

  const tempClient = new ClobClient(HOST, CHAIN_ID, signer);
  const apiCreds = await tempClient.createOrDeriveApiKey();

  const signatureType = 0;

  const client = new ClobClient(
    HOST,
    CHAIN_ID,
    signer,
    apiCreds,
    signatureType
  );

  const response = await client.createAndPostOrder({
    tokenID: "YOUR_TOKEN_ID",
    price: 0.65,
    size: 10,
    side: Side.BUY,
  });

  console.log(`Order placed! ID: ${response.orderID}`);
}

trade();
```

---

## [​](#troubleshooting) Troubleshooting

Error: L2\_AUTH\_NOT\_AVAILABLE

You forgot to call `createOrDeriveApiKey()`. Make sure you initialize the client with API credentials:

Copy

```shiki
const creds = await clobClient.createOrDeriveApiKey();
const client = new ClobClient(host, chainId, wallet, creds);
```

Order rejected: insufficient balance

Ensure you have:

* **USDC** in your funder address for BUY orders
* **Outcome tokens** in your funder address for SELL orders

Check your balance at [polymarket.com/portfolio](https://polymarket.com/portfolio).

Order rejected: insufficient allowance

You need to approve the Exchange contract to spend your tokens. This is typically done through the Polymarket UI on your first trade. Or use the CTF contract’s `setApprovalForAll()` method.

What's my funder address?

Your funder address is the Polymarket proxy wallet where you deposit funds. Find it:

1. Go to [polymarket.com/settings](https://polymarket.com/settings)
2. Look for “Wallet Address” or “Profile Address”
3. This is your `FUNDER_ADDRESS`

---

## [​](#next-steps) Next Steps

[## Full Example Implementations

Complete Next.js examples demonstrating integration of embedded wallets
(Privy, Magic, Turnkey, wagmi) and the CLOB and Builder Relay clients](/developers/builders/examples)

[## Understand CLOB Authentication

Deep dive into L1 and L2 authentication](/developers/CLOB/authentication)[## Browse Client Methods

Explore the complete client reference](/developers/CLOB/clients/methods-overview)[## Find Markets to Trade

Use Gamma API to discover markets](/developers/gamma-markets-api/get-markets)[## Monitor with WebSocket

Get real-time order updates](/developers/CLOB/websocket/wss-overview)

[Status](/developers/CLOB/status)[Authentication](/developers/CLOB/authentication)

⌘I

---


## Authentication

> Source: https://docs.polymarket.com/developers/CLOB/authentication

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Central Limit Order Book

Authentication

The CLOB uses two levels of authentication: **L1 (Private Key)** and **L2 (API Key)**.
Either can be accomplished using the CLOB client or REST API. Authentication is not
required to access client public methods and public endpoints.

## [​](#authentication-levels) Authentication Levels

[## L1 Authentication

Use the private key of the user’s account to sign messages](#l1-authentication)[## L2 Authentication

Use API credentials (key, secret, passphrase) to authenticate requests to the CLOB](#l2-authentication)

---

## [​](#l1-authentication) L1 Authentication

### [​](#what-is-l1) What is L1?

L1 authentication uses the wallet’s private key to sign an EIP-712 message used in the
request header. It proves ownership and control over the private key. The private key
stays in control of the user and all trading activity remains non-custodial.

### [​](#what-this-enables) What This Enables

Access to L1 methods that create or derive L2 authentication headers.

* Create user API credentials
* Derive existing user API credentials
* Sign/create user’s orders locally

### [​](#clob-client) CLOB Client

* TypeScript
* Python

Copy

```shiki
import { ClobClient } from "@polymarket/clob-client";
import { Wallet } from "ethers"; // v5.8.0

const HOST = "https://clob.polymarket.com";
const CHAIN_ID = 137; // Polygon mainnet
const signer = new Wallet(process.env.PRIVATE_KEY);

const client = new ClobClient(
  HOST,
  CHAIN_ID,
  signer // Signer enables L1 methods
);

// Gets API key, or else creates
const apiCreds = await client.createOrDeriveApiKey();

/*
apiCreds = {
  "apiKey": "550e8400-e29b-41d4-a716-446655440000",
  "secret": "base64EncodedSecretString",
  "passphrase": "randomPassphraseString"
}
*/
```

Copy

```shiki
from py_clob_client.client import ClobClient
import os

host = "https://clob.polymarket.com"
chain_id = 137 # Polygon mainnet
private_key = os.getenv("PRIVATE_KEY")

client = ClobClient(
    host=host,
    chain_id=chaind_id,
    key=private_key  # Signer enables L1 methods
)

# Gets API key, or else creates
api_creds = await client.create_or_derive_api_key()

# api_creds = {
#     "apiKey": "550e8400-e29b-41d4-a716-446655440000",
#     "secret": "base64EncodedSecretString",
#     "passphrase": "randomPassphraseString"
# }
```

**Never commit private keys to version control.** Always use environment
variables or secure key management systems.

---

### [​](#rest-api) REST API

While we highly recommend using our provided clients to handle signing
and authentication, the following is for developers who choose NOT to
use our [Python](https://github.com/Polymarket/py-clob-client) or
[TypeScript](https://github.com/Polymarket/clob-client) clients.
When making direct REST API calls with L1 authentication, include these headers:

| Header | Required? | Description |
| --- | --- | --- |
| `POLY_ADDRESS` | yes | Polygon signer address |
| `POLY_SIGNATURE` | yes | CLOB EIP 712 signature |
| `POLY_TIMESTAMP` | yes | Current UNIX timestamp |
| `POLY_NONCE` | yes | Nonce. Default 0 |

The `POLY_SIGNATURE` is generated by signing the following EIP-712 struct.

EIP-712 Signing Example

Typescript

Python

Copy

```shiki
const domain = {
  name: "ClobAuthDomain",
  version: "1",
  chainId: chainId, // Polygon Chain ID 137
};

const types = {
  ClobAuth: [
    { name: "address", type: "address" },
    { name: "timestamp", type: "string" },
    { name: "nonce", type: "uint256" },
    { name: "message", type: "string" },
  ],
};

const value = {
  address: signingAddress, // The Signing address
  timestamp: ts,            // The CLOB API server timestamp
  nonce: nonce,             // The nonce used
  message: "This message attests that I control the given wallet",
};

const sig = await signer._signTypedData(domain, types, value);
```

Reference implementations:

* [TypeScript](https://github.com/Polymarket/clob-client/blob/main/src/signing/eip712.ts)
* [Python](https://github.com/Polymarket/py-clob-client/blob/main/py_clob_client/signing/eip712.py)

---

**Create API Credentials**
Create new API credentials for user.

Copy

```shiki
POST {clob-endpoint}/auth/api-key
```

**Derive API Credentials**
Derive API credentials for user.

Copy

```shiki
GET {clob-endpoint}/auth/derive-api-key
```

**Response**

Copy

```shiki
{
  "apiKey": "550e8400-e29b-41d4-a716-446655440000",
  "secret": "base64EncodedSecretString",
  "passphrase": "randomPassphraseString"
}
```

**You’ll need all three values for L2 authentication.**

---

## [​](#l2-authentication) L2 Authentication

### [​](#what-is-l2) What is L2?

The next level of authentication is called L2, and it consists of the
user’s API credentials (apiKey, secret, passphrase) generated from L1
authentication. These are used solely to authenticate requests made to
the CLOB API. Requests are signed using HMAC-SHA256.

### [​](#what-this-enables-2) What This Enables

Access to L2 methods such as posting signed/created orders, viewing open
orders, cancelling open orders, getting trades

* Cancel or get user’s open orders
* Check user’s balances and allowances
* Post user’s signed orders

### [​](#clob-client-2) CLOB Client

* TypeScript
* Python

Copy

```shiki
import { ClobClient } from "@polymarket/clob-client";
import { Wallet } from "ethers"; // v5.8.0

const HOST = "https://clob.polymarket.com";
const CHAIN_ID = 137; // Polygon mainnet
const signer = new Wallet(process.env.PRIVATE_KEY);

const client = new ClobClient(
  HOST,
  CHAIN_ID,
  signer,
  apiCreds, // Generated from L1 auth, API credentials enable L2 methods
  1, // signatureType explained below
  FUNDER // funder explained below
);

// Now you can trade!*
const order = await client.createAndPostOrder(
  { tokenID: "123456", price: 0.65, size: 100, side: "BUY" },
  { tickSize: "0.01", negRisk: false }
);
```

Copy

```shiki
from py_clob_client.client import ClobClient
import os

host = "https://clob.polymarket.com"
chain_id = 137 # Polygon mainnet
private_key = os.getenv("PRIVATE_KEY")

client = ClobClient(
    host="https://clob.polymarket.com",
    chain_id=137,
    key=os.getenv("PRIVATE_KEY"),
    creds=api_creds,  # Generated from L1 auth, API credentials enable L2 methods
    signature_type=1,  # signatureType explained below
    funder=os.getenv("FUNDER_ADDRESS") # funder explained below
)

# Now you can trade!*
order = await client.create_and_post_order(
    {"token_id": "123456", "price": 0.65, "size": 100, "side": "BUY"},
    {"tick_size": "0.01", "neg_risk": False}
)
```

Even with L2 authentication headers, methods that create user orders still require the user to sign the order payload.

---

### [​](#rest-api-2) REST API

While we highly recommend using our provided clients to handle signing
and authentication, the following is for developers who choose NOT to
use our [Python](https://github.com/Polymarket/py-clob-client) or
[TypeScript](https://github.com/Polymarket/clob-client) clients.
When making direct REST API calls with L2 authentication, include these headers:

| Header | Required? | Description |
| --- | --- | --- |
| `POLY_ADDRESS` | yes | Polygon signer address |
| `POLY_SIGNATURE` | yes | HMAC signature for request |
| `POLY_TIMESTAMP` | yes | Current UNIX timestamp |
| `POLY_API_KEY` | yes | User’s API `apiKey` value |
| `POLY_PASSPHRASE` | yes | User’s API `passphrase` value |

The `POLY_SIGNATURE` for L2 is an HMAC-SHA256 signature created using the user’s API credentials `secret` value.
Reference implementations can be found in the [Typescript](https://github.com/Polymarket/clob-client/blob/main/src/signing/hmac.ts)
and [Python](https://github.com/Polymarket/py-clob-client/blob/main/py_clob_client/signing/hmac.py) clients.

---

## [​](#signature-types-and-funder) Signature Types and Funder

When initializing the L2 client, you must specify your wallet **signatureType** and the **funder** address which holds the funds:

| Signature Type | Value | Description |
| --- | --- | --- |
| EOA | 0 | Standard Ethereum wallet (MetaMask). Funder is the EOA address and will need POL to pay gas on transactions. |
| POLY\_PROXY | 1 | A custom proxy wallet only used with users who logged in via Magic Link email/Google. Using this requires the user to have exported their PK from Polymarket.com and imported into your app. |
| GNOSIS\_SAFE | 2 | Gnosis Safe multisig proxy wallet (most common). Use this for any new or returning user who does not fit the other 2 types. |

The wallet addresses displayed to the user on Polymarket.com is the proxy wallet and should be used as the funder.
These can be deterministically derived or you can deploy them on behalf of the user.
These proxy wallets are automatically deployed for the user on their first login to Polymarket.com.

---

## [​](#troubleshooting) Troubleshooting

Error: INVALID\_SIGNATURE

Your wallet’s private key is incorrect or improperly formatted.**Solution:**

* Verify your private key is a valid hex string (starts with “0x”)
* Ensure you’re using the correct key for the intended address
* Check that the key has proper permissions

Error: NONCE\_ALREADY\_USED

The nonce you provided has already been used to create an API key.**Solution:**

* Use `deriveApiKey()` with the same nonce to retrieve existing credentials
* Or use a different nonce with `createApiKey()`

Error: Invalid Funder Address

Your funder address is incorrect or doesn’t match your wallet.**Solution:** Check your Polymarket profile address at [polymarket.com/settings](https://polymarket.com/settings).If it does not exist or user has never logged into Polymarket.com, deploy it first before creating L2 authentication.

Lost API credentials but have nonce

Copy

```shiki
// Use deriveApiKey with the original nonce
const recovered = await client.deriveApiKey(originalNonce);
```

Lost both credentials and nonce

Unfortunately, there’s no way to recover lost API credentials without the nonce. You’ll need to create new credentials:

Copy

```shiki
// Create fresh credentials with a new nonce
const newCreds = await client.createApiKey();
// Save the nonce this time!
```

---

## [​](#see-client-methods) See Client Methods

[## Public Methods

Access market data, orderbooks, and prices.](/developers/CLOB/clients/methods-public)[## L1 Methods

Private key authentication to create or derive API keys (L2 headers).](/developers/CLOB/clients/methods-l1)[## L2 Methods

Manage and close orders. Creating orders requires signer.](/developers/CLOB/clients/methods-l2)[## Builder Program Methods

Builder-specific operations for those in the Builders Program.](/developers/CLOB/clients/methods-builder)

[Quickstart](/developers/CLOB/quickstart)[Geographic Restrictions](/developers/CLOB/geoblock)

⌘I

---


## Geographic Restrictions

> Source: https://docs.polymarket.com/developers/CLOB/geoblock

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Central Limit Order Book

Geographic Restrictions

## [​](#overview) Overview

Polymarket restricts order placement from certain geographic locations due to regulatory requirements and compliance with international sanctions.
Before placing orders, builders should verify the location.

Orders submitted from blocked regions will be rejected. Implement geoblock checks
in your application to provide users with appropriate feedback before they attempt to trade.

---

## [​](#server-infrastructure) Server Infrastructure

* **Primary Servers**: eu-west-2
* **Closest Non-Georestricted Region**: eu-west-1

---

## [​](#geoblock-endpoint) Geoblock Endpoint

Check the geographic eligibility of the requesting IP address:

Copy

```shiki
GET https://polymarket.com/api/geoblock
```

### [​](#response) Response

Copy

```shiki
{
  "blocked": boolean;
  "ip": string;
  "country": string;
  "region": string;
}
```

| Field | Type | Description |
| --- | --- | --- |
| `blocked` | boolean | Whether the user is blocked from placing orders |
| `ip` | string | Detected IP address |
| `country` | string | ISO 3166-1 alpha-2 country code |
| `region` | string | Region/state code |

---

## [​](#blocked-countries) Blocked Countries

The following **33 countries** are completely restricted from placing orders on Polymarket:

| Country Code | Country Name |
| --- | --- |
| AU | Australia |
| BE | Belgium |
| BY | Belarus |
| BI | Burundi |
| CF | Central African Republic |
| CD | Congo (Kinshasa) |
| CU | Cuba |
| DE | Germany |
| ET | Ethiopia |
| FR | France |
| GB | United Kingdom |
| IR | Iran |
| IQ | Iraq |
| IT | Italy |
| KP | North Korea |
| LB | Lebanon |
| LY | Libya |
| MM | Myanmar |
| NI | Nicaragua |
| PL | Poland |
| RU | Russia |
| SG | Singapore |
| SO | Somalia |
| SS | South Sudan |
| SD | Sudan |
| SY | Syria |
| TH | Thailand |
| TW | Taiwan |
| UM | United States Minor Outlying Islands |
| US | United States |
| VE | Venezuela |
| YE | Yemen |
| ZW | Zimbabwe |

---

## [​](#blocked-regions) Blocked Regions

In addition to fully blocked countries, the following specific regions within otherwise accessible countries are also restricted:

| Country | Region | Region Code |
| --- | --- | --- |
| Canada (CA) | Ontario | ON |
| Ukraine (UA) | Crimea | 43 |
| Ukraine (UA) | Donetsk | 14 |
| Ukraine (UA) | Luhansk | 09 |

---

## [​](#usage-examples) Usage Examples

* TypeScript
* Python

Copy

```shiki
interface GeoblockResponse {
  blocked: boolean;
  ip: string;
  country: string;
  region: string;
}

async function checkGeoblock(): Promise<GeoblockResponse> {
  const response = await fetch("https://polymarket.com/api/geoblock");
  return response.json();
}

// Usage
const geo = await checkGeoblock();

if (geo.blocked) {
  console.log(`Trading not available in ${geo.country}`);
} else {
  console.log("Trading available");
}
```

Copy

```shiki
import requests

def check_geoblock() -> dict:
    response = requests.get("https://polymarket.com/api/geoblock")
    return response.json()

# Usage
geo = check_geoblock()

if geo["blocked"]:
    print(f"Trading not available in {geo['country']}")
else:
    print("Trading available")
```

[Authentication](/developers/CLOB/authentication)[Methods Overview](/developers/CLOB/clients/methods-overview)

⌘I

---


## CLOB Status

> Source: https://docs.polymarket.com/developers/CLOB/status

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Check the status of the Polymarket Order Book:
[Status Page](https://status-clob.polymarket.com/)

[CLOB Introduction](/developers/CLOB/introduction)[Quickstart](/developers/CLOB/quickstart)

⌘I

---


## Historical Timeseries Data

> Source: https://docs.polymarket.com/developers/CLOB/timeseries

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Historical Timeseries Data

Historical Timeseries Data

GET

/

prices-history

Try it

Get price history for a traded token

cURL

Copy

```shiki
curl --request GET \
  --url https://clob.polymarket.com/prices-history
```

200

400

404

500

Copy

```shiki
{
  "history": [
    {
      "t": 1697875200,
      "p": 1800.75
    }
  ]
}
```

The CLOB provides detailed price history for each traded token.
**HTTP REQUEST**
`GET /<clob-endpoint>/prices-history`

We also have a Interactive Notebook to visualize the data from this endpoint available [here](https://colab.research.google.com/drive/1s4TCOR4K7fRP7EwAH1YmOactMakx24Cs?usp=sharing#scrollTo=mYCJBcfB9Zu4).

#### Query Parameters

[​](#parameter-market)

market

string

required

The CLOB token ID for which to fetch price history

[​](#parameter-start-ts)

startTs

number

The start time, a Unix timestamp in UTC

[​](#parameter-end-ts)

endTs

number

The end time, a Unix timestamp in UTC

[​](#parameter-interval)

interval

enum<string>

A string representing a duration ending at the current time. Mutually exclusive with startTs and endTs

Available options:

`1m`,

`1w`,

`1d`,

`6h`,

`1h`,

`max`

[​](#parameter-fidelity)

fidelity

number

The resolution of the data, in minutes

#### Response

200

application/json

A list of timestamp/price pairs

[​](#response-history)

history

object[]

required

Show child attributes

[Get bid-ask spreads](/api-reference/spreads/get-bid-ask-spreads)[Orders Overview](/developers/CLOB/orders/orders)

⌘I

---


## Methods Overview

> Source: https://docs.polymarket.com/developers/CLOB/clients/methods-overview

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Client

Methods Overview

[## Public Methods

Access market data, orderbooks, and prices.](/developers/CLOB/clients/methods-public)[## L1 Methods

Private key authentication to create or derive API keys (L2 headers).](/developers/CLOB/clients/methods-l1)[## L2 Methods

Manage and close orders. Creating orders requires signer.](/developers/CLOB/clients/methods-l2)[## Builder Program Methods

Builder-specific operations for those in the Builders Program.](/developers/CLOB/clients/methods-builder)

---

## [​](#client-initialization-by-use-case) Client Initialization by Use Case

* Get Market Data
* Generate User API Credentials
* Create and Post Order
* Get Builders Orders

TypeScript

Python

Copy

```shiki
// No signer or credentials needed
const client = new ClobClient(
  "https://clob.polymarket.com", 
  137
);

// All public methods available
const markets = await client.getMarkets();
const book = await client.getOrderBook(tokenId);
const price = await client.getPrice(tokenId, "BUY");
```

TypeScript

Python

Copy

```shiki
// Create client with signer
const client = new ClobClient(
  "https://clob.polymarket.com", 
  137, 
  signer
);

// All public and L1 methods available
const newCreds = createApiKey();
const derivedCreds = deriveApiKey();
const creds = createOrDeriveApiKey();
```

TypeScript

Python

Copy

```shiki
// Create client with signer and creds
const client = new ClobClient(
  "https://clob.polymarket.com", 
  137, 
  signer,
  creds,
  2, // Indicates Gnosis Safe proxy
  funder // Safe wallet address holding funds
);

// All public, L1, and L2 methods available
const order = await client.createOrder({ /* ... */ });
const result = await client.postOrder(order);
const trades = await client.getTrades();
```

TypeScript

Python

Copy

```shiki
// Create client with builder's authentication headers
import { BuilderConfig, BuilderApiKeyCreds } from "@polymarket/builder-signing-sdk";

const builderCreds: BuilderApiKeyCreds = {
  key: process.env.POLY_BUILDER_API_KEY!,
  secret: process.env.POLY_BUILDER_SECRET!,
  passphrase: process.env.POLY_BUILDER_PASSPHRASE!
};

const builderConfig: BuilderConfig = {
  localBuilderCreds: builderCreds
};

const client = new ClobClient(
  "https://clob.polymarket.com", 
  137, 
  signer,
  creds, // User's API credentials
  2,
  funder,
  undefined,
  false,
  builderConfig // Builder's API credentials
);

// You can call all methods including builder methods
const builderTrades = await client.getBuilderTrades();
```

Learn more about the Builders Program and Relay Client here

---

## [​](#resources) Resources

[## TypeScript Client

Open source TypeScript client on GitHub](https://github.com/Polymarket/clob-client)[## Python Client

Open source Python client for GitHub](https://github.com/Polymarket/py-clob-client)[## Rust Client

Open source Rust client on GitHub](https://github.com/Polymarket/rs-clob-client)[## TypeScript Examples

TypeScript client method examples](https://github.com/Polymarket/clob-client/tree/main/examples)[## Python Examples

Python client method examples](https://github.com/Polymarket/py-clob-client/tree/main/examples)[## Rust Examples

Rust client method examples](https://github.com/Polymarket/rs-clob-client/tree/main/examples)[## CLOB Rest API Reference

Complete REST endpoint documentation](/api-reference/orderbook/get-order-book-summary)[## Web Socket API

Real-time market data streaming](/developers/CLOB/websocket/wss-overview)

[Geographic Restrictions](/developers/CLOB/geoblock)[Public Methods](/developers/CLOB/clients/methods-public)

⌘I

---


## Public Methods

> Source: https://docs.polymarket.com/developers/CLOB/clients/methods-public

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Client

Public Methods

## [​](#client-initialization) Client Initialization

Public methods require the client to initialize with the host URL and Polygon chain ID.

* TypeScript
* Python

Copy

```shiki
import { ClobClient } from "@polymarket/clob-client";

const client = new ClobClient(
  "https://clob.polymarket.com",
  137
);

// Ready to call public methods
const markets = await client.getMarkets();
```

Copy

```shiki
from py_clob_client.client import ClobClient

client = ClobClient(
    host="https://clob.polymarket.com",
    chain_id=137
)

# Ready to call public methods
markets = await client.get_markets()
```

---

## [​](#health-check) Health Check

---

### [​](#getok) getOk()

Health check endpoint to verify the CLOB service is operational.

Signature

Copy

```shiki
async getOk(): Promise<any>
```

---

## [​](#markets) Markets

---

### [​](#getmarket) getMarket()

Get details for a single market by condition ID.

Signature

Copy

```shiki
async getMarket(conditionId: string): Promise<Market>
```

Response

Copy

```shiki
interface MarketToken {
  outcome: string;
  price: number;
  token_id: string;
  winner: boolean;
}

interface Market {
  accepting_order_timestamp: string | null;
  accepting_orders: boolean;
  active: boolean;
  archived: boolean;
  closed: boolean;
  condition_id: string;
  description: string;
  enable_order_book: boolean;
  end_date_iso: string;
  fpmm: string;
  game_start_time: string;
  icon: string;
  image: string;
  is_50_50_outcome: boolean;
  maker_base_fee: number;
  market_slug: string;
  minimum_order_size: number;
  minimum_tick_size: number;
  neg_risk: boolean;
  neg_risk_market_id: string;
  neg_risk_request_id: string;
  notifications_enabled: boolean;
  question: string;
  question_id: string;
  rewards: {
    max_spread: number;
    min_size: number;
    rates: any | null;
  };
  seconds_delay: number;
  tags: string[];
  taker_base_fee: number;
  tokens: MarketToken[];
}
```

---

### [​](#getmarkets) getMarkets()

Get details for multiple markets paginated.

Signature

Copy

```shiki
async getMarkets(): Promise<PaginationPayload>
```

Response

Copy

```shiki
interface PaginationPayload {
  limit: number;
  count: number;
  data: Market[];
}

interface Market {
  accepting_order_timestamp: string | null;
  accepting_orders: boolean;
  active: boolean;
  archived: boolean;
  closed: boolean;
  condition_id: string;
  description: string;
  enable_order_book: boolean;
  end_date_iso: string;
  fpmm: string;
  game_start_time: string;
  icon: string;
  image: string;
  is_50_50_outcome: boolean;
  maker_base_fee: number;
  market_slug: string;
  minimum_order_size: number;
  minimum_tick_size: number;
  neg_risk: boolean;
  neg_risk_market_id: string;
  neg_risk_request_id: string;
  notifications_enabled: boolean;
  question: string;
  question_id: string;
  rewards: {
    max_spread: number;
    min_size: number;
    rates: any | null;
  };
  seconds_delay: number;
  tags: string[];
  taker_base_fee: number;
  tokens: MarketToken[];
}

interface MarketToken {
  outcome: string;
  price: number;
  token_id: string;
  winner: boolean;
}
```

---

### [​](#getsimplifiedmarkets) getSimplifiedMarkets()

Get simplified market data paginated for faster loading.

Signature

Copy

```shiki
async getSimplifiedMarkets(): Promise<PaginationPayload>
```

Response

Copy

```shiki
interface PaginationPayload {
  limit: number;
  count: number;
  data: SimplifiedMarket[];
}

interface SimplifiedMarket {
  accepting_orders: boolean;
  active: boolean;
  archived: boolean;
  closed: boolean;
  condition_id: string;
  rewards: {
    rates: any | null;
    min_size: number;
    max_spread: number;
  };
    tokens: SimplifiedToken[];
}

interface SimplifiedToken {
  outcome: string;
  price: number;
  token_id: string;
}
```

---

### [​](#getsamplingmarkets) getSamplingMarkets()

Signature

Copy

```shiki
async getSamplingMarkets(): Promise<PaginationPayload>
```

Response

Copy

```shiki
interface PaginationPayload {
  limit: number;
  count: number;
  data: Market[];
}

interface Market {
  accepting_order_timestamp: string | null;
  accepting_orders: boolean;
  active: boolean;
  archived: boolean;
  closed: boolean;
  condition_id: string;
  description: string;
  enable_order_book: boolean;
  end_date_iso: string;
  fpmm: string;
  game_start_time: string;
  icon: string;
  image: string;
  is_50_50_outcome: boolean;
  maker_base_fee: number;
  market_slug: string;
  minimum_order_size: number;
  minimum_tick_size: number;
  neg_risk: boolean;
  neg_risk_market_id: string;
  neg_risk_request_id: string;
  notifications_enabled: boolean;
  question: string;
  question_id: string;
  rewards: {
    max_spread: number;
    min_size: number;
    rates: any | null;
  };
  seconds_delay: number;
  tags: string[];
  taker_base_fee: number;
  tokens: MarketToken[];
}

interface MarketToken {
  outcome: string;
  price: number;
  token_id: string;
  winner: boolean;
}
```

---

### [​](#getsamplingsimplifiedmarkets) getSamplingSimplifiedMarkets()

Signature

Copy

```shiki
async getSamplingSimplifiedMarkets(): Promise<PaginationPayload>
```

Response

Copy

```shiki
interface PaginationPayload {
  limit: number;
  count: number;
  data: SimplifiedMarket[];
}

interface SimplifiedMarket {
  accepting_orders: boolean;
  active: boolean;
  archived: boolean;
  closed: boolean;
  condition_id: string;
  rewards: {
    rates: any | null;
    min_size: number;
    max_spread: number;
  };
    tokens: SimplifiedToken[];
}

interface SimplifiedToken {
  outcome: string;
  price: number;
  token_id: string;
}
```

---

## [​](#order-books-and-prices) Order Books and Prices

---

### [​](#calculatemarketprice) calculateMarketPrice()

Signature

Copy

```shiki
async calculateMarketPrice(
  tokenID: string,
  side: Side,
  amount: number,
  orderType: OrderType = OrderType.FOK
): Promise<number>
```

Params

Copy

```shiki
enum OrderType {
  GTC = "GTC",  // Good Till Cancelled
  FOK = "FOK",  // Fill or Kill
  GTD = "GTD",  // Good Till Date
  FAK = "FAK",  // Fill and Kill
}

enum Side {
  BUY = "BUY",
  SELL = "SELL",
}
```

Response

Copy

```shiki
number // calculated market price
```

---

### [​](#getorderbook) getOrderBook()

Get the order book for a specific token ID.

Signature

Copy

```shiki
async getOrderBook(tokenID: string): Promise<OrderBookSummary>
```

Response

Copy

```shiki
interface OrderBookSummary {
  market: string;
  asset_id: string;
  timestamp: string;
  bids: OrderSummary[];
  asks: OrderSummary[];
  min_order_size: string;
  tick_size: string;
  neg_risk: boolean;
  hash: string;
}

interface OrderSummary {
  price: string;
  size: string;
}
```

---

### [​](#getorderbooks) getOrderBooks()

Get order books for multiple token IDs.

Signature

Copy

```shiki
async getOrderBooks(params: BookParams[]): Promise<OrderBookSummary[]>
```

Params

Copy

```shiki
interface BookParams {
  token_id: string;
  side: Side;  // Side.BUY or Side.SELL
}
```

Response

Copy

```shiki
OrderBookSummary[]
```

---

### [​](#getprice) getPrice()

Get the current best price for buying or selling a token ID.

Signature

Copy

```shiki
async getPrice(
  tokenID: string,
  side: "BUY" | "SELL"
): Promise<any>
```

Response

Copy

```shiki
{
  price: string;
}
```

---

### [​](#getprices) getPrices()

Get the current best prices for multiple token IDs.

Signature

Copy

```shiki
async getPrices(params: BookParams[]): Promise<PricesResponse>
```

Params

Copy

```shiki
interface BookParams {
  token_id: string;
  side: Side;  // Side.BUY or Side.SELL
}
```

Response

Copy

```shiki
interface TokenPrices {
  BUY?: string;
  SELL?: string;
}

type PricesResponse = {
  [tokenId: string]: TokenPrices;
}
```

---

### [​](#getmidpoint) getMidpoint()

Get the midpoint price (average of best bid and best ask) for a token ID.

Signature

Copy

```shiki
async getMidpoint(tokenID: string): Promise<any>
```

Response

Copy

```shiki
{
  mid: string;
}
```

---

### [​](#getmidpoints) getMidpoints()

Get the midpoint prices (average of best bid and best ask) for multiple token IDs.

Signature

Copy

```shiki
async getMidpoints(params: BookParams[]): Promise<any>
```

Params

Copy

```shiki
interface BookParams {
  token_id: string;
  side: Side;  // Side is ignored
}
```

Response

Copy

```shiki
{
  [tokenId: string]: string;
}
```

---

### [​](#getspread) getSpread()

Get the spread (difference between best ask and best bid) for a token ID.

Signature

Copy

```shiki
async getSpread(tokenID: string): Promise<SpreadResponse>
```

Response

Copy

```shiki
interface SpreadResponse {
  spread: string;
}
```

---

### [​](#getspreads) getSpreads()

Get the spreads (difference between best ask and best bid) for multiple token IDs.

Signature

Copy

```shiki
async getSpreads(params: BookParams[]): Promise<SpreadsResponse>
```

Params

Copy

```shiki
interface BookParams {
  token_id: string;
  side: Side;
}
```

Response

Copy

```shiki
type SpreadsResponse = {
  [tokenId: string]: string;
}
```

---

### [​](#getpriceshistory) getPricesHistory()

Get historical price data for a token.

Signature

Copy

```shiki
async getPricesHistory(params: PriceHistoryFilterParams): Promise<MarketPrice[]>
```

Params

Copy

```shiki
interface PriceHistoryFilterParams {
  market: string; // tokenID
  startTs?: number;
  endTs?: number;
  fidelity?: number;
  interval: PriceHistoryInterval;
}

enum PriceHistoryInterval {
  MAX = "max",
  ONE_WEEK = "1w",
  ONE_DAY = "1d",
  SIX_HOURS = "6h",
  ONE_HOUR = "1h",
}
```

Response

Copy

```shiki
interface MarketPrice {
  t: number;  // timestamp
  p: number;  // price
}
```

---

## [​](#trades) Trades

---

### [​](#getlasttradeprice) getLastTradePrice()

Get the price of the most recent trade for a token.

Signature

Copy

```shiki
async getLastTradePrice(tokenID: string): Promise<LastTradePrice>
```

Response

Copy

```shiki
interface LastTradePrice {
  price: string;
  side: string;
}
```

---

### [​](#getlasttradesprices) getLastTradesPrices()

Get the price of the most recent trade for a token.

Signature

Copy

```shiki
async getLastTradesPrices(params: BookParams[]): Promise<LastTradePriceWithToken[]>
```

Params

Copy

```shiki
interface BookParams {
  token_id: string;
  side: Side;
}
```

Response

Copy

```shiki
interface LastTradePriceWithToken {
  price: string;
  side: string;
  token_id: string;
}
```

---

### [​](#getmarkettradesevents) getMarketTradesEvents

Signature

Copy

```shiki
async getMarketTradesEvents(conditionID: string): Promise<MarketTradeEvent[]>
```

Response

Copy

```shiki
interface MarketTradeEvent {
  event_type: string;
  market: {
    condition_id: string;
    asset_id: string;
    question: string;
    icon: string;
    slug: string;
  };
  user: {
    address: string;
    username: string;
    profile_picture: string;
    optimized_profile_picture: string;
    pseudonym: string;
  };
  side: Side;
  size: string;
  fee_rate_bps: string;
  price: string;
  outcome: string;
  outcome_index: number;
  transaction_hash: string;
  timestamp: string;
}
```

## [​](#market-parameters) Market Parameters

---

### [​](#getfeeratebps) getFeeRateBps()

Get the fee rate in basis points for a token.

Signature

Copy

```shiki
async getFeeRateBps(tokenID: string): Promise<number>
```

Response

Copy

```shiki
number
```

---

### [​](#getticksize) getTickSize()

Get the tick size (minimum price increment) for a market.

Signature

Copy

```shiki
async getTickSize(tokenID: string): Promise<TickSize>
```

Response

Copy

```shiki
type TickSize = "0.1" | "0.01" | "0.001" | "0.0001";
```

---

### [​](#getnegrisk) getNegRisk()

Check if a market uses negative risk (binary complementary tokens).

Signature

Copy

```shiki
async getNegRisk(tokenID: string): Promise<boolean>
```

Response

Copy

```shiki
boolean
```

---

## [​](#time-&-server-info) Time & Server Info

### [​](#getservertime) getServerTime()

Get the current server timestamp.

Signature

Copy

```shiki
async getServerTime(): Promise<number>
```

Response

Copy

```shiki
number // Unix timestamp in seconds
```

---

## [​](#see-also) See Also

[## L1 Methods

Private key authentication to create or derive API keys (L2 headers).](/developers/CLOB/clients/methods-l1)[## L2 Methods

Manage and close orders. Creating orders requires signer.](/developers/CLOB/clients/methods-l2)[## CLOB Rest API Reference

Complete REST endpoint documentation](/api-reference/orderbook/get-order-book-summary)[## Web Socket API

Real-time market data streaming](/developers/CLOB/websocket/wss-overview)

[Methods Overview](/developers/CLOB/clients/methods-overview)[L1 Methods](/developers/CLOB/clients/methods-l1)

⌘I

---


## L1 Methods

> Source: https://docs.polymarket.com/developers/CLOB/clients/methods-l1

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Client

L1 Methods

## [​](#client-initialization) Client Initialization

L1 methods require the client to initialize with a signer.

* TypeScript
* Python

Copy

```shiki
import { ClobClient } from "@polymarket/clob-client";
import { Wallet } from "ethers";

const signer = new Wallet(process.env.PRIVATE_KEY);

const client = new ClobClient(
  "https://clob.polymarket.com",
  137,
  signer // Signer required for L1 methods
);

// Ready to create user API credentials
const apiKey = await client.createApiKey();
```

Copy

```shiki
from py_clob_client.client import ClobClient
import os

private_key = os.getenv("PRIVATE_KEY")

client = ClobClient(
    host="https://clob.polymarket.com",
    chain_id=137,
    key=private_key  # Signer required for L1 methods
)

# Ready to create user API credentials
api_key = await client.create_api_key()
```

**Security:** Never commit private keys to version control. Always use environment variables or secure key management systems.

---

## [​](#api-key-management) API Key Management

---

### [​](#createapikey) createApiKey()

Creates a new API key (L2 credentials) for the wallet signer. This generates a new set of credentials that can be used for L2 authenticated requests.
Each wallet can only have one active API key at a time. Creating a new key invalidates the previous one.

Signature

Copy

```shiki
async createApiKey(nonce?: number): Promise<ApiKeyCreds>
```

Params

Copy

```shiki
`nonce` (optional): Custom nonce for deterministic key generation. If not provided, a default derivation is used.
```

Response

Copy

```shiki
interface ApiKeyCreds {
  apiKey: string;
  secret: string;
  passphrase: string;
}
```

---

### [​](#deriveapikey) deriveApiKey()

Derives an existing API key (L2 credentials) using a specific nonce. If you’ve already created API credentials with a particular nonce, this method will return the same credentials again.

Signature

Copy

```shiki
async deriveApiKey(nonce?: number): Promise<ApiKeyCreds>
```

Params

Copy

```shiki
`nonce` (optional): Custom nonce for deterministic key generation. If not provided, a default derivation is used.
```

Response

Copy

```shiki
interface ApiKeyCreds {
  apiKey: string;
  secret: string;
  passphrase: string;
}
```

---

### [​](#createorderiveapikey) createOrDeriveApiKey()

Convenience method that attempts to derive an API key with the default nonce, or creates a new one if it doesn’t exist. This is the recommended method for initial setup if you’re unsure if credentials already exist.

Signature

Copy

```shiki
async createOrDeriveApiKey(nonce?: number): Promise<ApiKeyCreds>
```

Params

Copy

```shiki
`nonce` (optional): Custom nonce for deterministic key generation. If not provided, a default derivation is used.
```

Response

Copy

```shiki
interface ApiKeyCreds {
  apiKey: string;
  secret: string;
  passphrase: string;
}
```

---

## [​](#order-signing) Order Signing

### [​](#createorder) createOrder()

Create and sign a limit order locally without posting it to the CLOB.
Use this when you want to sign orders in advance or implement custom order submission logic.
Place order via L2 methods postOrder or postOrders.

Signature

Copy

```shiki
async createOrder(
  userOrder: UserOrder,
  options?: Partial<CreateOrderOptions>
): Promise<SignedOrder>
```

Params

Copy

```shiki
interface UserOrder {
  tokenID: string;
  price: number;
  size: number;
  side: Side;
  feeRateBps?: number;
  nonce?: number;
  expiration?: number;
  taker?: string;
}

interface CreateOrderOptions {
  tickSize: TickSize;
  negRisk?: boolean;
}
```

Response

Copy

```shiki
interface SignedOrder {
  salt: string;
  maker: string;
  signer: string;
  taker: string;
  tokenId: string;
  makerAmount: string;
  takerAmount: string;
  side: number;  // 0 = BUY, 1 = SELL
  expiration: string;
  nonce: string;
  feeRateBps: string;
  signatureType: number;
  signature: string;
}
```

---

### [​](#createmarketorder) createMarketOrder()

Create and sign a market order locally without posting it to the CLOB.
Use this when you want to sign orders in advance or implement custom order submission logic.
Place orders via L2 methods postOrder or postOrders.

Signature

Copy

```shiki
async createMarketOrder(
  userMarketOrder: UserMarketOrder,
  options?: Partial<CreateOrderOptions>
): Promise<SignedOrder>
```

Params

Copy

```shiki
interface UserMarketOrder {
  tokenID: string;
  amount: number;  // BUY: dollar amount, SELL: number of shares
  side: Side;
  price?: number;  // Optional price limit
  feeRateBps?: number;
  nonce?: number;
  taker?: string;
  orderType?: OrderType.FOK | OrderType.FAK;
}
```

Response

Copy

```shiki
interface SignedOrder {
  salt: string;
  maker: string;
  signer: string;
  taker: string;
  tokenId: string;
  makerAmount: string;
  takerAmount: string;
  side: number;  // 0 = BUY, 1 = SELL
  expiration: string;
  nonce: string;
  feeRateBps: string;
  signatureType: number;
  signature: string;
}
```

---

## [​](#troubleshooting) Troubleshooting

Error: INVALID\_SIGNATURE

Your wallet’s private key is incorrect or improperly formatted.**Solution:**

* Verify your private key is a valid hex string (starts with “0x”)
* Ensure you’re using the correct key for the intended address
* Check that the key has proper permissions

Error: NONCE\_ALREADY\_USED

The nonce you provided has already been used to create an API key.**Solution:**

* Use `deriveApiKey()` with the same nonce to retrieve existing credentials
* Or use a different nonce with `createApiKey()`

Error: Invalid Funder Address

Your funder address is incorrect or doesn’t match your wallet.**Solution:** Check your Polymarket profile address at [polymarket.com/settings](https://polymarket.com/settings).If it does not exist or user has never logged into Polymarket.com, deploy it first before creating L2 authentication.

Lost API credentials but have nonce

Copy

```shiki
// Use deriveApiKey with the original nonce
const recovered = await client.deriveApiKey(originalNonce);
```

Lost both credentials and nonce

Unfortunately, there’s no way to recover lost API credentials without the nonce. You’ll need to create new credentials:

Copy

```shiki
// Create fresh credentials with a new nonce
const newCreds = await client.createApiKey();
// Save the nonce this time!
```

---

## [​](#see-also) See Also

[## Understand CLOB Authentication

Deep dive into L1 and L2 authentication](/developers/CLOB/authentication)[## CLOB Quickstart Guide

Initialize the CLOB quickly and place your first order.](/developers/CLOB/quickstart)[## Public Methods

Access market data, orderbooks, and prices.](/developers/CLOB/clients/methods-l2)[## L2 Methods

Manage and close orders. Creating orders requires signer.](/developers/CLOB/clients/methods-l2)

[Public Methods](/developers/CLOB/clients/methods-public)[L2 Methods](/developers/CLOB/clients/methods-l2)

⌘I

---


## L2 Methods

> Source: https://docs.polymarket.com/developers/CLOB/clients/methods-l2

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Client

L2 Methods

---

## [​](#client-initialization) Client Initialization

L2 methods require the client to initialize with the signer, signatureType, user API credentials, and funder.

* TypeScript
* Python

Copy

```shiki
import { ClobClient } from "@polymarket/clob-client";
import { Wallet } from "ethers";

const signer = new Wallet(process.env.PRIVATE_KEY)

const apiCreds = {
  apiKey: process.env.API_KEY,
  secret: process.env.SECRET,
  passphrase: process.env.PASSPHRASE,
};

const client = new ClobClient(
  "https://clob.polymarket.com",
  137,
  signer,
  apiCreds,
  2, // Deployed Safe proxy wallet
  process.env.FUNDER_ADDRESS // Address of deployed Safe proxy wallet
);

// Ready to send authenticated requests to the CLOB API!
const order = await client.postOrder(signedOrder);
```

Copy

```shiki
from py_clob_client.client import ClobClient
from py_clob_client.clob_types import ApiCreds
import os

api_creds = ApiCreds(
    api_key=os.getenv("API_KEY"),
    api_secret=os.getenv("SECRET"),
    api_passphrase=os.getenv("PASSPHRASE")
)

client = ClobClient(
    host="https://clob.polymarket.com",
    chain_id=137,
    key=os.getenv("PRIVATE_KEY"),
    creds=api_creds,
    signature_type=2, # Deployed Safe proxy wallet
    funder=os.getenv("FUNDER_ADDRESS") # Address of deployed Safe proxy wallet
)

# Ready to send authenticated requests to the CLOB API!
order = await client.post_order(signed_order)
```

---

## [​](#order-creation-and-management) Order Creation and Management

---

### [​](#createandpostorder) createAndPostOrder()

A convenience method that creates, prompts signature, and posts an order in a single call.
Use when you want to buy/sell at a specific price and can wait.

Signature

Copy

```shiki
async createAndPostOrder(
  userOrder: UserOrder,
  options?: Partial<CreateOrderOptions>,
  orderType?: OrderType.GTC | OrderType.GTD, // Defaults to GTC
): Promise<OrderResponse>
```

Params

Copy

```shiki
interface UserOrder {
  tokenID: string;
  price: number;
  size: number;
  side: Side;
  feeRateBps?: number;
  nonce?: number;
  expiration?: number;
  taker?: string;
}

type CreateOrderOptions = {
  tickSize: TickSize;
  negRisk?: boolean;
}

type TickSize = "0.1" | "0.01" | "0.001" | "0.0001";
```

Response

Copy

```shiki
interface OrderResponse {
  success: boolean;
  errorMsg: string;
  orderID: string;
  transactionsHashes: string[];
  status: string;
  takingAmount: string;
  makingAmount: string;
}
```

---

### [​](#createandpostmarketorder) createAndPostMarketOrder()

A convenience method that creates, prompts signature, and posts an order in a single call.
Use when you want to buy/sell right now at whatever the market price is.

Signature

Copy

```shiki
async createAndPostMarketOrder(
  userMarketOrder: UserMarketOrder,
  options?: Partial<CreateOrderOptions>,
  orderType?: OrderType.FOK | OrderType.FAK, // Defaults to FOK
): Promise<OrderResponse>
```

Params

Copy

```shiki
interface UserMarketOrder {
  tokenID: string;
  amount: number;
  side: Side;
  price?: number;
  feeRateBps?: number;
  nonce?: number;
  taker?: string;
  orderType?: OrderType.FOK | OrderType.FAK;
}

type CreateOrderOptions = {
  tickSize: TickSize;
  negRisk?: boolean;
}

type TickSize = "0.1" | "0.01" | "0.001" | "0.0001";
```

Response

Copy

```shiki
interface OrderResponse {
  success: boolean;
  errorMsg: string;
  orderID: string;
  transactionsHashes: string[];
  status: string;
  takingAmount: string;
  makingAmount: string;
}
```

---

### [​](#postorder) postOrder()

Posts a pre-signed and created order to the CLOB.

Signature

Copy

```shiki
async postOrder(
  order: SignedOrder,
  orderType?: OrderType, // Defaults to GTC
  postOnly?: boolean, // Defaults to false
): Promise<OrderResponse>
```

Params

Copy

```shiki
order: SignedOrder  // Pre-signed order from createOrder() or createMarketOrder()
orderType?: OrderType  // Optional, defaults to GTC
postOnly?: boolean  // Optional, defaults to false
```

Response

Copy

```shiki
interface OrderResponse {
  success: boolean;
  errorMsg: string;
  orderID: string;
  transactionsHashes: string[];
  status: string;
  takingAmount: string;
  makingAmount: string;
}
```

---

### [​](#postorders) postOrders()

Posts up to 15 pre-signed and created orders in a single batch.

Copy

```shiki
async postOrders(
  args: PostOrdersArgs[],
): Promise<OrderResponse[]>
```

Params

Copy

```shiki
interface PostOrdersArgs {
  order: SignedOrder;
  orderType: OrderType;
  postOnly?: boolean; // Defaults to false
}
```

Response

Copy

```shiki
OrderResponse[]  // Array of OrderResponse objects

interface OrderResponse {
  success: boolean;
  errorMsg: string;
  orderID: string;
  transactionsHashes: string[];
  status: string;
  takingAmount: string;
  makingAmount: string;
}
```

---

### [​](#cancelorder) cancelOrder()

Cancels a single open order.

Signature

Copy

```shiki
async cancelOrder(orderID: string): Promise<CancelOrdersResponse>
```

Response

Copy

```shiki
interface CancelOrdersResponse {
  canceled: string[];
  not_canceled: Record<string, any>;
}
```

---

### [​](#cancelorders) cancelOrders()

Cancels multiple orders in a single batch.

Signature

Copy

```shiki
async cancelOrders(orderIDs: string[]): Promise<CancelOrdersResponse>
```

Params

Copy

```shiki
orderIDs: string[];
```

Response

Copy

```shiki
interface CancelOrdersResponse {
  canceled: string[];
  not_canceled: Record<string, any>;
}
```

---

### [​](#cancelall) cancelAll()

Cancels all open orders.

Signature

Copy

```shiki
async cancelAll(): Promise<CancelResponse>
```

Response

Copy

```shiki
interface CancelOrdersResponse {
  canceled: string[];
  not_canceled: Record<string, any>;
}
```

---

### [​](#cancelmarketorders) cancelMarketOrders()

Cancels all open orders for a specific market.

Signature

Copy

```shiki
async cancelMarketOrders(
  payload: OrderMarketCancelParams
): Promise<CancelOrdersResponse>
```

Parameters

Copy

```shiki
interface OrderMarketCancelParams {
  market?: string;
  asset_id?: string;
}
```

Response

Copy

```shiki
interface CancelOrdersResponse {
  canceled: string[];
  not_canceled: Record<string, any>;
}
```

---

## [​](#order-and-trade-queries) Order and Trade Queries

---

### [​](#getorder) getOrder()

Get details for a specific order.

Signature

Copy

```shiki
async getOrder(orderID: string): Promise<OpenOrder>
```

Response

Copy

```shiki
interface OpenOrder {
  id: string;
  status: string;
  owner: string;
  maker_address: string;
  market: string;
  asset_id: string;
  side: string;
  original_size: string;
  size_matched: string;
  price: string;
  associate_trades: string[];
  outcome: string;
  created_at: number;
  expiration: string;
  order_type: string;
}
```

---

### [​](#getopenorders) getOpenOrders()

Get all your open orders.

Signature

Copy

```shiki
async getOpenOrders(
  params?: OpenOrderParams,
  only_first_page?: boolean,
): Promise<OpenOrdersResponse>
```

Params

Copy

```shiki
interface OpenOrderParams {
  id?: string; // Order ID
  market?: string; // Market condition ID
  asset_id?: string; // Token ID
}

only_first_page?: boolean  // Defaults to false
```

Response

Copy

```shiki
type OpenOrdersResponse = OpenOrder[];

interface OpenOrder {
  id: string;
  status: string;
  owner: string;
  maker_address: string;
  market: string;
  asset_id: string;
  side: string;
  original_size: string;
  size_matched: string;
  price: string;
  associate_trades: string[];
  outcome: string;
  created_at: number;
  expiration: string;
  order_type: string;
}
```

---

### [​](#gettrades) getTrades()

Get your trade history (filled orders).

Signature

Copy

```shiki
async getTrades(
  params?: TradeParams,
  only_first_page?: boolean,
): Promise<Trade[]>
```

Params

Copy

```shiki
interface TradeParams {
  id?: string;
  maker_address?: string;
  market?: string;
  asset_id?: string;
  before?: string;
  after?: string;
}

only_first_page?: boolean  // Defaults to false
```

Response

Copy

```shiki
interface Trade {
  id: string;
  taker_order_id: string;
  market: string;
  asset_id: string;
  side: Side;
  size: string;
  fee_rate_bps: string;
  price: string;
  status: string;
  match_time: string;
  last_update: string;
  outcome: string;
  bucket_index: number;
  owner: string;
  maker_address: string;
  maker_orders: MakerOrder[];
  transaction_hash: string;
  trader_side: "TAKER" | "MAKER";
}

interface MakerOrder {
  order_id: string;
  owner: string;
  maker_address: string;
  matched_amount: string;
  price: string;
  fee_rate_bps: string;
  asset_id: string;
  outcome: string;
  side: Side;
}
```

---

### [​](#gettradespaginated) getTradesPaginated()

Get trade history with pagination for large result sets.

Signature

Copy

```shiki
async getTradesPaginated(
  params?: TradeParams,
): Promise<TradesPaginatedResponse>
```

Params

Copy

```shiki
interface TradeParams {
  id?: string;
  maker_address?: string;
  market?: string;
  asset_id?: string;
  before?: string;
  after?: string;
}
```

Response

Copy

```shiki
interface TradesPaginatedResponse {
  trades: Trade[];
  limit: number;
  count: number;
}
```

---

## [​](#balance-and-allowances) Balance and Allowances

---

### [​](#getbalanceallowance) getBalanceAllowance()

Get your balance and allowance for specific tokens.

Signature

Copy

```shiki
async getBalanceAllowance(
  params?: BalanceAllowanceParams
): Promise<BalanceAllowanceResponse>
```

Params

Copy

```shiki
interface BalanceAllowanceParams {
  asset_type: AssetType;
  token_id?: string;
}

enum AssetType {
  COLLATERAL = "COLLATERAL",
  CONDITIONAL = "CONDITIONAL",
}
```

Response

Copy

```shiki
interface BalanceAllowanceResponse {
  balance: string;
  allowance: string;
}
```

---

### [​](#updatebalanceallowance) updateBalanceAllowance()

Updates the cached balance and allowance for specific tokens.

Signature

Copy

```shiki
async updateBalanceAllowance(
  params?: BalanceAllowanceParams
): Promise<void>
```

Params

Copy

```shiki
interface BalanceAllowanceParams {
  asset_type: AssetType;
  token_id?: string;
}

enum AssetType {
  COLLATERAL = "COLLATERAL",
  CONDITIONAL = "CONDITIONAL",
}
```

---

## [​](#api-key-management-l2) API Key Management (L2)

### [​](#getapikeys) getApiKeys()

Get all API keys associated with your account.

Signature

Copy

```shiki
async getApiKeys(): Promise<ApiKeysResponse>
```

Response

Copy

```shiki
interface ApiKeysResponse {
  apiKeys: ApiKeyCreds[];
}

interface ApiKeyCreds {
  key: string;
  secret: string;
  passphrase: string;
}
```

---

### [​](#deleteapikey) deleteApiKey()

Deletes (revokes) the currently authenticated API key.
**TypeScript Signature:**

Copy

```shiki
async deleteApiKey(): Promise<any>
```

---

## [​](#notifications) Notifications

---

### [​](#getnotifications) getNotifications()

Retrieves all event notifications for the L2 authenticated user.
Records are removed automatically after 48 hours or if manually removed via dropNotifications().

Signature

Copy

```shiki
public async getNotifications(): Promise<Notification[]>
```

Response

Copy

```shiki
interface Notification {
    id: number;           // Unique notification ID
    owner: string;        // User's L2 credential apiKey or empty string for global notifications
    payload: any;         // Type-specific payload data
    timestamp?: number;   // Unix timestamp
    type: number;         // Notification type (see type mapping below)
}
```

**Notification Type Mapping**

| Name | Value | Description |
| --- | --- | --- |
| Order Cancellation | 1 | User’s order was canceled |
| Order Fill | 2 | User’s order was filled (maker or taker) |
| Market Resolved | 4 | Market was resolved |

---

### [​](#dropnotifications) dropNotifications()

Mark notifications as read/dismissed.

Signature

Copy

```shiki
public async dropNotifications(params?: DropNotificationParams): Promise<void>
```

Params

Copy

```shiki
interface DropNotificationParams {
    ids: string[];  // Array of notification IDs to mark as read
}
```

---

## [​](#see-also) See Also

[## Understand CLOB Authentication

Deep dive into L1 and L2 authentication](/developers/CLOB/authentication)[## Public Methods

Access market data, orderbooks, and prices.](/developers/CLOB/clients/methods-l2)[## L1 Methods

Private key authentication to create or derive API keys (L2 headers)](/developers/CLOB/clients/methods-l2)[## Web Socket API

Real-time market data streaming](/developers/CLOB/websocket/wss-overview)

[L1 Methods](/developers/CLOB/clients/methods-l1)[Builder Methods](/developers/CLOB/clients/methods-builder)

⌘I

---


## Builder Methods

> Source: https://docs.polymarket.com/developers/CLOB/clients/methods-builder

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Client

Builder Methods

## [​](#client-initialization) Client Initialization

Builder methods require the client to initialize with a separate authentication setup using
builder configs acquired from [Polymarket.com](https://polymarket.com/settings?tab=builder)
and the `@polymarket/builder-signing-sdk` package.

* Local Builder Credentials
* Remote Builder Signing

TypeScript

Python

Copy

```shiki
import { ClobClient } from "@polymarket/clob-client";
import { BuilderConfig, BuilderApiKeyCreds } from "@polymarket/builder-signing-sdk";

const builderConfig = new BuilderConfig({
  localBuilderCreds: new BuilderApiKeyCreds({
    key: process.env.BUILDER_API_KEY,
    secret: process.env.BUILDER_SECRET,
    passphrase: process.env.BUILDER_PASS_PHRASE,
  }),
});

const clobClient = new ClobClient(
  "https://clob.polymarket.com",
  137,
  signer,
  apiCreds, // The user's API credentials generated from L1 authentication
  signatureType,
  funderAddress,
  undefined,
  false,
  builderConfig
);
```

TypeScript

Python

Copy

```shiki
import { ClobClient } from "@polymarket/clob-client";
import { BuilderConfig } from "@polymarket/builder-signing-sdk";

const builderConfig = new BuilderConfig({
    remoteBuilderConfig: {url: "http://localhost:3000/sign"}
});

const clobClient = new ClobClient(
  "https://clob.polymarket.com",
  137,
  signer,
  apiCreds, // The user's API credentials generated from L1 authentication
  signatureType,
  funder,
  undefined,
  false,
  builderConfig
);
```

[More information on builder signing](/developers/builders/order-attribution)

---

## [​](#methods) Methods

---

### [​](#getbuildertrades) getBuilderTrades()

Retrieves all trades attributed to your builder account.
This method allows builders to track which trades were routed through your platform.

Signature

Copy

```shiki
async getBuilderTrades(
  params?: TradeParams,
): Promise<BuilderTradesPaginatedResponse>
```

Params

Copy

```shiki
interface TradeParams {
  id?: string;
  maker_address?: string;
  market?: string;
  asset_id?: string;
  before?: string;
  after?: string;
}
```

Response

Copy

```shiki
interface BuilderTradesPaginatedResponse {
  trades: BuilderTrade[];
  next_cursor: string;
  limit: number;
  count: number;
}

interface BuilderTrade {
  id: string;
  tradeType: string;
  takerOrderHash: string;
  builder: string;
  market: string;
  assetId: string;
  side: string;
  size: string;
  sizeUsdc: string;
  price: string;
  status: string;
  outcome: string;
  outcomeIndex: number;
  owner: string;
  maker: string;
  transactionHash: string;
  matchTime: string;
  bucketIndex: number;
  fee: string;
  feeUsdc: string;
  err_msg?: string | null;
  createdAt: string | null;
  updatedAt: string | null;
}
```

---

### [​](#revokebuilderapikey) revokeBuilderApiKey()

Revokes the builder API key used to authenticate the current request.
After revocation, the key can no longer be used to make builder-authenticated requests.

Signature

Copy

```shiki
async revokeBuilderApiKey(): Promise<any>
```

---

## [​](#see-also) See Also

[## Builders Program Introduction

Learn the benefits, how to implement, and more.](/developers/builders/builder-intro)[## Implement Builders Signing

Attribute orders to you, and pre-requisite to using the Relayer Client.](/developers/builders/order-attribution)[## Relayer Client

The relayer executes other gasless transactions for your users, on your app.](/developers/builders/relayer-client)[## Full Example Implementations

Complete Next.js examples integrated with embedded wallets (Privy, Magic, Turnkey, wagmi)](/developers/builders/examples)

[L2 Methods](/developers/CLOB/clients/methods-l2)[Get order book summary](/api-reference/orderbook/get-order-book-summary)

⌘I

---


## Orders Overview

> Source: https://docs.polymarket.com/developers/CLOB/orders/orders

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Order Management

Orders Overview

All orders are expressed as limit orders (can be marketable). The underlying order primitive must be in the form expected and executable by the on-chain binary limit order protocol contract. Preparing such an order is quite involved (structuring, hashing, signing), thus Polymarket suggests using the open source typescript, python and golang libraries.

## [​](#allowances) Allowances

To place an order, allowances must be set by the funder address for the specified `maker` asset for the Exchange contract. When buying, this means the funder must have set a USDC allowance greater than or equal to the spending amount. When selling, the funder must have set an allowance for the conditional token that is greater than or equal to the selling amount. This allows the Exchange contract to execute settlement according to the signed order instructions created by a user and matched by the operator.

## [​](#signature-types) Signature Types

Polymarket’s CLOB supports 3 signature types. Orders must identify what signature type they use. The available typescript and python clients abstract the complexity of signing and preparing orders with the following signature types by allowing a funder address and signer type to be specified on initialization. The supported signature types are:

| Type | ID | Description |
| --- | --- | --- |
| EOA | 0 | EIP712 signature signed by an EOA |
| POLY\_PROXY | 1 | EIP712 signatures signed by a signer associated with funding Polymarket proxy wallet |
| POLY\_GNOSIS\_SAFE | 2 | EIP712 signatures signed by a signer associated with funding Polymarket gnosis safe wallet |

## [​](#validity-checks) Validity Checks

Orders are continually monitored to make sure they remain valid. Specifically, this includes continually tracking underlying balances, allowances and on-chain order cancellations. Any maker that is caught intentionally abusing these checks (which are essentially real time) will be blacklisted.
Additionally, there are rails on order placement in a market. Specifically, you can only place orders that sum to less than or equal to your available balance for each market. For example if you have 500 USDC in your funding wallet, you can place one order to buy 1000 YES in marketA @ $.50, then any additional buy orders to that market will be rejected since your entire balance is reserved for the first (and only) buy order. More explicitly the max size you can place for an order is:
maxOrderSize=underlyingAssetBalance−∑(orderSize−orderFillAmount)\text{maxOrderSize} = \text{underlyingAssetBalance} - \sum(\text{orderSize} - \text{orderFillAmount})maxOrderSize=underlyingAssetBalance−∑(orderSize−orderFillAmount)

[Historical Timeseries Data](/developers/CLOB/timeseries)[Place Single Order](/developers/CLOB/orders/create-order)

⌘I

---


## Place Single Order

> Source: https://docs.polymarket.com/developers/CLOB/orders/create-order

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Order Management

Place Single Order

# [​](#create-and-place-an-order) Create and Place an Order

This endpoint requires a L2 Header

Create and place an order using the Polymarket CLOB API clients. All orders are represented as “limit” orders, but “market” orders are also supported. To place a market order, simply ensure your price is marketable against current resting limit orders, which are executed on input at the best price.
**HTTP REQUEST**
`POST /<clob-endpoint>/order`

### [​](#request-payload-parameters) Request Payload Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| order | yes | Order | signed object |
| owner | yes | string | api key of order owner |
| orderType | yes | string | order type (“FOK”, “GTC”, “GTD”) |
| postOnly | no | boolean | if `true`, the order will only rest on the book and not match immediately (default: `false`) |

### [​](#post-only-orders) Post-only orders

* postOnly submits a limit order that will not match resting liquidity upon entry.
* If a postOnly order would cross the spread (i.e., it is marketable), it will be rejected rather than executed.
* postOnly cannot be combined with market order types (e.g., FOK or FAK). If `postOnly = true` is sent with a market order type, the order will be rejected.

An `order` object is the form:

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| salt | yes | integer | random salt used to create unique order |
| maker | yes | string | maker address (funder) |
| signer | yes | string | signing address |
| taker | yes | string | taker address (operator) |
| tokenId | yes | string | ERC1155 token ID of conditional token being traded |
| makerAmount | yes | string | maximum amount maker is willing to spend |
| takerAmount | yes | string | minimum amount taker will pay the maker in return |
| expiration | yes | string | unix expiration timestamp |
| nonce | yes | string | maker’s exchange nonce of the order is associated |
| feeRateBps | yes | string | fee rate basis points as required by the operator |
| side | yes | string | buy or sell enum index |
| signatureType | yes | integer | signature type enum index |
| signature | yes | string | hex encoded signature |

### [​](#order-types) Order types

* **FOK**: A Fill-Or-Kill order is an market order to buy (in dollars) or sell (in shares) shares that must be executed immediately in its entirety; otherwise, the entire order will be cancelled.
* **FAK**: A Fill-And-Kill order is a market order to buy (in dollars) or sell (in shares) that will be executed immediately for as many shares as are available; any portion not filled at once is cancelled.
* **GTC**: A Good-Til-Cancelled order is a limit order that is active until it is fulfilled or cancelled.
* **GTD**: A Good-Til-Date order is a type of order that is active until its specified date (UTC seconds timestamp), unless it has already been fulfilled or cancelled. There is a security threshold of one minute. If the order needs to expire in 90 seconds the correct expiration value is: now + 1 minute + 30 seconds

### [​](#response-format) Response Format

| Name | Type | Description |
| --- | --- | --- |
| success | boolean | boolean indicating if server-side err (`success = false`) -> server-side error |
| errorMsg | string | error message in case of unsuccessful placement (in case `success = false`, e.g. `client-side error`, the reason is in `errorMsg`) |
| orderId | string | id of order |
| orderHashes | string[] | hash of settlement transaction order was marketable and triggered a match |

### [​](#insert-error-messages) Insert Error Messages

If the `errorMsg` field of the response object from placement is not an empty string, the order was not able to be immediately placed. This might be because of a delay or because of a failure. If the `success` is not `true`, then there was an issue placing the order. The following `errorMessages` are possible:

#### [​](#error) Error

| Error | Success | Message | Description |
| --- | --- | --- | --- |
| INVALID\_ORDER\_MIN\_TICK\_SIZE | yes | order is invalid. Price breaks minimum tick size rules | order price isn’t accurate to correct tick sizing |
| INVALID\_ORDER\_MIN\_SIZE | yes | order is invalid. Size lower than the minimum | order size must meet min size threshold requirement |
| INVALID\_ORDER\_DUPLICATED | yes | order is invalid. Duplicated. Same order has already been placed, can’t be placed again |  |
| INVALID\_ORDER\_NOT\_ENOUGH\_BALANCE | yes | not enough balance / allowance | funder address doesn’t have sufficient balance or allowance for order |
| INVALID\_ORDER\_EXPIRATION | yes | invalid expiration | expiration field expresses a time before now |
| INVALID\_ORDER\_ERROR | yes | could not insert order | system error while inserting order |
| INVALID\_POST\_ONLY\_ORDER\_TYPE | yes | invalid post-only order: only GTC and GTD order types are allowed | post only flag attached to a market order |
| INVALID\_POST\_ONLY\_ORDER | yes | invalid post-only order: order crosses book | post only order would match |
| EXECUTION\_ERROR | yes | could not run the execution | system error while attempting to execute trade |
| ORDER\_DELAYED | no | order match delayed due to market conditions | order placement delayed |
| DELAYING\_ORDER\_ERROR | yes | error delaying the order | system error while delaying order |
| FOK\_ORDER\_NOT\_FILLED\_ERROR | yes | order couldn’t be fully filled, FOK orders are fully filled/killed | FOK order not fully filled so can’t be placed |
| MARKET\_NOT\_READY | no | the market is not yet ready to process new orders | system not accepting orders for market yet |

### [​](#insert-statuses) Insert Statuses

When placing an order, a status field is included. The status field provides additional information regarding the order’s state as a result of the placement. Possible values include:

#### [​](#status) Status

| Status | Description |
| --- | --- |
| matched | order placed and matched with an existing resting order |
| live | order placed and resting on the book |
| delayed | order marketable, but subject to matching delay |
| unmatched | order marketable, but failure delaying, placement successful |

Python

typescript

Copy

```shiki
from py_clob_client.client import ClobClient
from py_clob_client.clob_types import OrderArgs, OrderType
from py_clob_client.order_builder.constants import BUY

host: str = "https://clob.polymarket.com"
key: str = "" #This is your Private Key. Export from reveal.polymarket.com or from your Web3 Application
chain_id: int = 137 #No need to adjust this
POLYMARKET_PROXY_ADDRESS: str = '' #This is the address you deposit/send USDC to to FUND your Polymarket account.

#Select from the following 3 initialization options to matches your login method, and remove any unused lines so only one client is initialized.

### Initialization of a client using a Polymarket Proxy associated with an Email/Magic account. If you login with your email use this example.
client = ClobClient(host, key=key, chain_id=chain_id, signature_type=1, funder=POLYMARKET_PROXY_ADDRESS)

### Initialization of a client using a Polymarket Proxy associated with a Browser Wallet(Metamask, Coinbase Wallet, etc)
client = ClobClient(host, key=key, chain_id=chain_id, signature_type=2, funder=POLYMARKET_PROXY_ADDRESS)

### Initialization of a client that trades directly from an EOA. 
client = ClobClient(host, key=key, chain_id=chain_id)

## Create and sign a limit order buying 100 YES tokens for 0.50c each
#Refer to the Markets API documentation to locate a tokenID: https://docs.polymarket.com/developers/gamma-markets-api/get-markets

client.set_api_creds(client.create_or_derive_api_creds()) 

order_args = OrderArgs(
    price=0.01,
    size=5.0,
    side=BUY,
    token_id="", #Token ID you want to purchase goes here. 
)
signed_order = client.create_order(order_args)

## GTC(Good-Till-Cancelled) Order
resp = client.post_order(signed_order, OrderType.GTC)
print(resp)
```

[Orders Overview](/developers/CLOB/orders/orders)[Place Multiple Orders (Batching)](/developers/CLOB/orders/create-order-batch)

⌘I

---


## Place Multiple Orders (Batching)

> Source: https://docs.polymarket.com/developers/CLOB/orders/create-order-batch

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Order Management

Place Multiple Orders (Batching)

This endpoint requires a L2 Header

Polymarket’s CLOB supports batch orders, allowing you to place up to `15` orders in a single request. Before using this feature, make sure you’re comfortable placing a single order first. You can find the documentation for that [here.](/developers/CLOB/orders/create-order)
**HTTP REQUEST**
`POST /<clob-endpoint>/orders`

### [​](#request-payload-parameters) Request Payload Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PostOrder | yes | PostOrders[] | list of signed order objects (Signed Order + Order Type + Owner) |

A `PostOrder` object is the form:

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| order | yes | order | See below table for details on crafting this object |
| orderType | yes | string | order type (“FOK”, “GTC”, “GTD”, “FAK”) |
| owner | yes | string | api key of order owner |
| postOnly | no | boolean | if `true`, the order will only rest on the book and not match immediately (default: `false`) |

An `order` object is the form:

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| salt | yes | integer | random salt used to create unique order |
| maker | yes | string | maker address (funder) |
| signer | yes | string | signing address |
| taker | yes | string | taker address (operator) |
| tokenId | yes | string | ERC1155 token ID of conditional token being traded |
| makerAmount | yes | string | maximum amount maker is willing to spend |
| takerAmount | yes | string | minimum amount taker will pay the maker in return |
| expiration | yes | string | unix expiration timestamp |
| nonce | yes | string | maker’s exchange nonce of the order is associated |
| feeRateBps | yes | string | fee rate basis points as required by the operator |
| side | yes | string | buy or sell enum index |
| signatureType | yes | integer | signature type enum index |
| signature | yes | string | hex encoded signature |

### [​](#order-types) Order types

* **FOK**: A Fill-Or-Kill order is an market order to buy (in dollars) or sell (in shares) shares that must be executed immediately in its entirety; otherwise, the entire order will be cancelled.
* **FAK**: A Fill-And-Kill order is a market order to buy (in dollars) or sell (in shares) that will be executed immediately for as many shares as are available; any portion not filled at once is cancelled.
* **GTC**: A Good-Til-Cancelled order is a limit order that is active until it is fulfilled or cancelled.
* **GTD**: A Good-Til-Date order is a type of order that is active until its specified date (UTC seconds timestamp), unless it has already been fulfilled or cancelled. There is a security threshold of one minute. If the order needs to expire in 90 seconds the correct expiration value is: now + 1 minute + 30 seconds

### [​](#response-format) Response Format

| Name | Type | Description |
| --- | --- | --- |
| success | boolean | boolean indicating if server-side err (`success = false`) -> server-side error |
| errorMsg | string | error message in case of unsuccessful placement (in case `success = false`, e.g. `client-side error`, the reason is in `errorMsg`) |
| orderId | string | id of order |
| orderHashes | string[] | hash of settlement transaction order was marketable and triggered a match |

### [​](#insert-error-messages) Insert Error Messages

If the `errorMsg` field of the response object from placement is not an empty string, the order was not able to be immediately placed. This might be because of a delay or because of a failure. If the `success` is not `true`, then there was an issue placing the order. The following `errorMessages` are possible:

#### [​](#error) Error

| Error | Success | Message | Description |
| --- | --- | --- | --- |
| INVALID\_ORDER\_MIN\_TICK\_SIZE | yes | order is invalid. Price breaks minimum tick size rules | order price isn’t accurate to correct tick sizing |
| INVALID\_ORDER\_MIN\_SIZE | yes | order is invalid. Size lower than the minimum | order size must meet min size threshold requirement |
| INVALID\_ORDER\_DUPLICATED | yes | order is invalid. Duplicated. Same order has already been placed, can’t be placed again |  |
| INVALID\_ORDER\_NOT\_ENOUGH\_BALANCE | yes | not enough balance / allowance | funder address doesn’t have sufficient balance or allowance for order |
| INVALID\_ORDER\_EXPIRATION | yes | invalid expiration | expiration field expresses a time before now |
| INVALID\_ORDER\_ERROR | yes | could not insert order | system error while inserting order |
| INVALID\_POST\_ONLY\_ORDER\_TYPE | yes | invalid post-only order: only GTC and GTD order types are allowed | post only flag attached to a market order |
| INVALID\_POST\_ONLY\_ORDER | yes | invalid post-only order: order crosses book | post only order would match |
| EXECUTION\_ERROR | yes | could not run the execution | system error while attempting to execute trade |
| ORDER\_DELAYED | no | order match delayed due to market conditions | order placement delayed |
| DELAYING\_ORDER\_ERROR | yes | error delaying the order | system error while delaying order |
| FOK\_ORDER\_NOT\_FILLED\_ERROR | yes | order couldn’t be fully filled, FOK orders are fully filled/killed | FOK order not fully filled so can’t be placed |
| MARKET\_NOT\_READY | no | the market is not yet ready to process new orders | system not accepting orders for market yet |

### [​](#insert-statuses) Insert Statuses

When placing an order, a status field is included. The status field provides additional information regarding the order’s state as a result of the placement. Possible values include:

#### [​](#status) Status

| Status | Description |
| --- | --- |
| matched | order placed and matched with an existing resting order |
| live | order placed and resting on the book |
| delayed | order marketable, but subject to matching delay |
| unmatched | order marketable, but failure delaying, placement successful |

Python

typescript

Example Payload

Copy

```shiki
from py_clob_client.client import ClobClient
from py_clob_client.clob_types import OrderArgs, OrderType, PostOrdersArgs
from py_clob_client.order_builder.constants import BUY

host: str = "https://clob.polymarket.com"
key: str = "" ##This is your Private Key. Export from https://reveal.magic.link/polymarket or from your Web3 Application
chain_id: int = 137 #No need to adjust this
POLYMARKET_PROXY_ADDRESS: str = '' #This is the address listed below your profile picture when using the Polymarket site.

#Select from the following 3 initialization options to matches your login method, and remove any unused lines so only one client is initialized.

### Initialization of a client using a Polymarket Proxy associated with an Email/Magic account. If you login with your email use this example.
client = ClobClient(host, key=key, chain_id=chain_id, signature_type=1, funder=POLYMARKET_PROXY_ADDRESS)

### Initialization of a client using a Polymarket Proxy associated with a Browser Wallet(Metamask, Coinbase Wallet, etc)
client = ClobClient(host, key=key, chain_id=chain_id, signature_type=2, funder=POLYMARKET_PROXY_ADDRESS)

### Initialization of a client that trades directly from an EOA. 
client = ClobClient(host, key=key, chain_id=chain_id)

## Create and sign a limit order buying 100 YES tokens for 0.50c each
#Refer to the Markets API documentation to locate a tokenID: https://docs.polymarket.com/developers/gamma-markets-api/get-markets

client.set_api_creds(client.create_or_derive_api_creds()) 

resp = client.post_orders([
    PostOrdersArgs(
        # Create and sign a limit order buying 100 YES tokens for 0.50 each
        order=client.create_order(OrderArgs(
            price=0.01,
            size=5,
            side=BUY,
            token_id="88613172803544318200496156596909968959424174365708473463931555296257475886634",
        )),
        orderType=OrderType.GTC,  # Good 'Til Cancelled
    ),
    PostOrdersArgs(
        # Create and sign a limit order selling 200 NO tokens for 0.25 each
        order=client.create_order(OrderArgs(
            price=0.01,
            size=5,
            side=BUY,
            token_id="93025177978745967226369398316375153283719303181694312089956059680730874301533",
        )),
        orderType=OrderType.GTC,  # Good 'Til Cancelled
    )
])
print(resp)
print("Done!")
```

[Place Single Order](/developers/CLOB/orders/create-order)[Get Order](/developers/CLOB/orders/get-order)

⌘I

---


## Cancel Orders

> Source: https://docs.polymarket.com/developers/CLOB/orders/cancel-orders

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Order Management

Cancel Orders(s)

# [​](#cancel-an-single-order) Cancel an single Order

This endpoint requires a L2 Header.

Cancel an order.
**HTTP REQUEST**
`DELETE /<clob-endpoint>/order`

### [​](#request-payload-parameters) Request Payload Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| orderID | yes | string | ID of order to cancel |

### [​](#response-format) Response Format

| Name | Type | Description |
| --- | --- | --- |
| canceled | string[] | list of canceled orders |
| not\_canceled | a order id -> reason map that explains why that order couldn’t be canceled |  |

Python

Typescript

Copy

```shiki
resp = client.cancel(order_id="0x38a73eed1e6d177545e9ab027abddfb7e08dbe975fa777123b1752d203d6ac88")
print(resp)
```

# [​](#cancel-multiple-orders) Cancel Multiple Orders

This endpoint requires a L2 Header.

**HTTP REQUEST**
`DELETE /<clob-endpoint>/orders`

### [​](#request-payload-parameters-2) Request Payload Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| null | yes | string[] | IDs of the orders to cancel |

### [​](#response-format-2) Response Format

| Name | Type | Description |
| --- | --- | --- |
| canceled | string[] | list of canceled orders |
| not\_canceled | a order id -> reason map that explains why that order couldn’t be canceled |  |

Python

Typescript

Copy

```shiki
resp = client.cancel_orders(["0x38a73eed1e6d177545e9ab027abddfb7e08dbe975fa777123b1752d203d6ac88", "0xaaaa..."])
print(resp)
```

# [​](#cancel-all-orders) Cancel ALL Orders

This endpoint requires a L2 Header.

Cancel all open orders posted by a user.
**HTTP REQUEST**
`DELETE /<clob-endpoint>/cancel-all`

### [​](#response-format-3) Response Format

| Name | Type | Description |
| --- | --- | --- |
| canceled | string[] | list of canceled orders |
| not\_canceled | a order id -> reason map that explains why that order couldn’t be canceled |  |

Python

Typescript

Copy

```shiki
resp = client.cancel_all()
print(resp)
print("Done!")
```

# [​](#cancel-orders-from-market) Cancel orders from market

This endpoint requires a L2 Header.

Cancel orders from market.
**HTTP REQUEST**
`DELETE /<clob-endpoint>/cancel-market-orders`

### [​](#request-payload-parameters-3) Request Payload Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| market | no | string | condition id of the market |
| asset\_id | no | string | id of the asset/token |

### [​](#response-format-4) Response Format

| Name | Type | Description |
| --- | --- | --- |
| canceled | string[] | list of canceled orders |
| not\_canceled | a order id -> reason map that explains why that order couldn’t be canceled |  |

Python

Typescript

Copy

```shiki
resp = client.cancel_market_orders(market="0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af", asset_id="52114319501245915516055106046884209969926127482827954674443846427813813222426")
print(resp)
```

[Check Order Reward Scoring](/developers/CLOB/orders/check-scoring)[Onchain Order Info](/developers/CLOB/orders/onchain-order-info)

⌘I

---


## Get Order

> Source: https://docs.polymarket.com/developers/CLOB/orders/get-order

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Order Management

Get Order

This endpoint requires a L2 Header.

Get single order by id.
**HTTP REQUEST**
`GET /<clob-endpoint>/data/order/<order_hash>`

### [​](#request-parameters) Request Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| id | no | string | id of order to get information about |

### [​](#response-format) Response Format

| Name | Type | Description |
| --- | --- | --- |
| order | OpenOrder | order if it exists |

An `OpenOrder` object is of the form:

| Name | Type | Description |
| --- | --- | --- |
| associate\_trades | string[] | any Trade id the order has been partially included in |
| id | string | order id |
| status | string | order current status |
| market | string | market id (condition id) |
| original\_size | string | original order size at placement |
| outcome | string | human readable outcome the order is for |
| maker\_address | string | maker address (funder) |
| owner | string | api key |
| price | string | price |
| side | string | buy or sell |
| size\_matched | string | size of order that has been matched/filled |
| asset\_id | string | token id |
| expiration | string | unix timestamp when the order expired, 0 if it does not expire |
| type | string | order type (GTC, FOK, GTD) |
| created\_at | string | unix timestamp when the order was created |

Python

Typescript

Copy

```shiki
order = clob_client.get_order("0xb816482a5187a3d3db49cbaf6fe3ddf24f53e6c712b5a4bf5e01d0ec7b11dabc")
print(order)
```

[Place Multiple Orders (Batching)](/developers/CLOB/orders/create-order-batch)[Get Active Orders](/developers/CLOB/orders/get-active-order)

⌘I

---


## Get Active Orders

> Source: https://docs.polymarket.com/developers/CLOB/orders/get-active-order

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Order Management

Get Active Orders

This endpoint requires a L2 Header.

Get active order(s) for a specific market.
**HTTP REQUEST**
`GET /<clob-endpoint>/data/orders`

### [​](#request-parameters) Request Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| id | no | string | id of order to get information about |
| market | no | string | condition id of market |
| asset\_id | no | string | id of the asset/token |

### [​](#response-format) Response Format

| Name | Type | Description |
| --- | --- | --- |
| null | OpenOrder[] | list of open orders filtered by the query parameters |

Python

Typescript

Copy

```shiki
from py_clob_client.clob_types import OpenOrderParams

resp = client.get_orders(
    OpenOrderParams(
        market="0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
    )
)
print(resp)
print("Done!")
```

[Get Order](/developers/CLOB/orders/get-order)[Check Order Reward Scoring](/developers/CLOB/orders/check-scoring)

⌘I

---


## Check Order Reward Scoring

> Source: https://docs.polymarket.com/developers/CLOB/orders/check-scoring

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Order Management

Check Order Reward Scoring

This endpoint requires a L2 Header.

Returns a boolean value where it is indicated if an order is scoring or not.
**HTTP REQUEST**
`GET /<clob-endpoint>/order-scoring?order_id={...}`

### [​](#request-parameters) Request Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| orderId | yes | string | id of order to get information about |

### [​](#response-format) Response Format

| Name | Type | Description |
| --- | --- | --- |
| null | OrdersScoring | order scoring data |

An `OrdersScoring` object is of the form:

| Name | Type | Description |
| --- | --- | --- |
| scoring | boolean | indicates if the order is scoring or not |

# [​](#check-if-some-orders-are-scoring) Check if some orders are scoring

> This endpoint requires a L2 Header.

Returns to a dictionary with boolean value where it is indicated if an order is scoring or not.
**HTTP REQUEST**
`POST /<clob-endpoint>/orders-scoring`

### [​](#request-parameters-2) Request Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| orderIds | yes | string[] | ids of the orders to get information about |

### [​](#response-format-2) Response Format

| Name | Type | Description |
| --- | --- | --- |
| null | OrdersScoring | orders scoring data |

An `OrdersScoring` object is a dictionary that indicates the order by if it score.

Python

Typescript

Copy

```shiki
scoring = client.is_order_scoring(
    OrderScoringParams(
        orderId="0x..."
    )
)
print(scoring)

scoring = client.are_orders_scoring(
    OrdersScoringParams(
        orderIds=["0x..."]
    )
)
print(scoring)
```

[Get Active Orders](/developers/CLOB/orders/get-active-order)[Cancel Orders(s)](/developers/CLOB/orders/cancel-orders)

⌘I

---


## Onchain Order Info

> Source: https://docs.polymarket.com/developers/CLOB/orders/onchain-order-info

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Order Management

Onchain Order Info

## [​](#how-do-i-interpret-the-orderfilled-onchain-event) How do I interpret the OrderFilled onchain event?

Given an OrderFilled event:

* `orderHash`: a unique hash for the Order being filled
* `maker`: the user generating the order and the source of funds for the order
* `taker`: the user filling the order OR the Exchange contract if the order fills multiple limit orders
* `makerAssetId`: id of the asset that is given out. If 0, indicates that the Order is a BUY, giving USDC in exchange for Outcome tokens. Else, indicates that the Order is a SELL, giving Outcome tokens in exchange for USDC.
* `takerAssetId`: id of the asset that is received. If 0, indicates that the Order is a SELL, receiving USDC in exchange for Outcome tokens. Else, indicates that the Order is a BUY, receiving Outcome tokens in exchange for USDC.
* `makerAmountFilled`: the amount of the asset that is given out.
* `takerAmountFilled`: the amount of the asset that is received.
* `fee`: the fees paid by the order maker

[Cancel Orders(s)](/developers/CLOB/orders/cancel-orders)[Trades Overview](/developers/CLOB/trades/trades-overview)

⌘I

---


## Trades Overview

> Source: https://docs.polymarket.com/developers/CLOB/trades/trades-overview

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Trades

Trades Overview

## [​](#overview) Overview

All historical trades can be fetched via the Polymarket CLOB REST API. A trade is initiated by a “taker” who creates a marketable limit order. This limit order can be matched against one or more resting limit orders on the associated book. A trade can be in various states as described below. Note: in some cases (due to gas limitations) the execution of a “trade” must be broken into multiple transactions which case separate trade entities will be returned. To associate trade entities, there is a bucket\_index field and a match\_time field. Trades that have been broken into multiple trade objects can be reconciled by combining trade objects with the same market\_order\_id, match\_time and incrementing bucket\_index’s into a top level “trade” client side.

## [​](#statuses) Statuses

| Status | Terminal? | Description |
| --- | --- | --- |
| MATCHED | no | trade has been matched and sent to the executor service by the operator, the executor service submits the trade as a transaction to the Exchange contract |
| MINED | no | trade is observed to be mined into the chain, no finality threshold established |
| CONFIRMED | yes | trade has achieved strong probabilistic finality and was successful |
| RETRYING | no | trade transaction has failed (revert or reorg) and is being retried/resubmitted by the operator |
| FAILED | yes | trade has failed and is not being retried |

[Onchain Order Info](/developers/CLOB/orders/onchain-order-info)[Get Trades](/developers/CLOB/trades/trades)

⌘I

---


## Get Trades

> Source: https://docs.polymarket.com/developers/CLOB/trades/trades

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Trades

Get Trades

This endpoint requires a L2 Header.

Get trades for the authenticated user based on the provided filters.
**HTTP REQUEST**
`GET /<clob-endpoint>/data/trades`

### [​](#request-parameters) Request Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| id | no | string | id of trade to fetch |
| taker | no | string | address to get trades for where it is included as a taker |
| maker | no | string | address to get trades for where it is included as a maker |
| market | no | string | market for which to get the trades (condition ID) |
| before | no | string | unix timestamp representing the cutoff up to which trades that happened before then can be included |
| after | no | string | unix timestamp representing the cutoff for which trades that happened after can be included |

### [​](#response-format) Response Format

| Name | Type | Description |
| --- | --- | --- |
| null | Trade[] | list of trades filtered by query parameters |

A `Trade` object is of the form:

| Name | Type | Description |
| --- | --- | --- |
| id | string | trade id |
| taker\_order\_id | string | hash of taker order (market order) that catalyzed the trade |
| market | string | market id (condition id) |
| asset\_id | string | asset id (token id) of taker order (market order) |
| side | string | buy or sell |
| size | string | size |
| fee\_rate\_bps | string | the fees paid for the taker order expressed in basic points |
| price | string | limit price of taker order |
| status | string | trade status (see above) |
| match\_time | string | time at which the trade was matched |
| last\_update | string | timestamp of last status update |
| outcome | string | human readable outcome of the trade |
| maker\_address | string | funder address of the taker of the trade |
| owner | string | api key of taker of the trade |
| transaction\_hash | string | hash of the transaction where the trade was executed |
| bucket\_index | integer | index of bucket for trade in case trade is executed in multiple transactions |
| maker\_orders | MakerOrder[] | list of the maker trades the taker trade was filled against |
| type | string | side of the trade: TAKER or MAKER |

A `MakerOrder` object is of the form:

| Name | Type | Description |
| --- | --- | --- |
| order\_id | string | id of maker order |
| maker\_address | string | maker address of the order |
| owner | string | api key of the owner of the order |
| matched\_amount | string | size of maker order consumed with this trade |
| fee\_rate\_bps | string | the fees paid for the taker order expressed in basic points |
| price | string | price of maker order |
| asset\_id | string | token/asset id |
| outcome | string | human readable outcome of the maker order |
| side | string | the side of the maker order. Can be `buy` or `sell` |

Python

Typescript

Copy

```shiki
from py_clob_client.clob_types import TradeParams

resp = client.get_trades(
    TradeParams(
        maker_address=client.get_address(),
        market="0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
    ),
)
print(resp)
print("Done!")
```

[Trades Overview](/developers/CLOB/trades/trades-overview)[WSS Overview](/developers/CLOB/websocket/wss-overview)

⌘I

---


## WSS Overview

> Source: https://docs.polymarket.com/developers/CLOB/websocket/wss-overview

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Websocket

WSS Overview

## [​](#overview) Overview

The Polymarket CLOB API provides websocket (wss) channels through which clients can get pushed updates. These endpoints allow clients to maintain almost real-time views of their orders, their trades and markets in general. There are two available channels `user` and `market`.

## [​](#subscription) Subscription

To subscribe send a message including the following authentication and intent information upon opening the connection.

| Field | Type | Description |
| --- | --- | --- |
| auth | Auth | see next page for auth information |
| markets | string[] | array of markets (condition IDs) to receive events for (for `user` channel) |
| assets\_ids | string[] | array of asset ids (token IDs) to receive events for (for `market` channel) |
| type | string | id of channel to subscribe to (USER or MARKET) |
| custom\_feature\_enabled | bool | enabling / disabling custom features |

Where the `auth` field is of type `Auth` which has the form described in the WSS Authentication section below.

### [​](#subscribe-to-more-assets) Subscribe to more assets

Once connected, the client can subscribe and unsubscribe to `asset_ids` by sending the following message:

| Field | Type | Description |
| --- | --- | --- |
| assets\_ids | string[] | array of asset ids (token IDs) to receive events for (for `market` channel) |
| markets | string[] | array of market ids (condition IDs) to receive events for (for `user` channel) |
| operation | string | ”subscribe” or “unsubscribe” |
| custom\_feature\_enabled | bool | enabling / disabling custom features |

[Get Trades](/developers/CLOB/trades/trades)[WSS Quickstart](/quickstart/websocket/WSS-Quickstart)

⌘I

---


## WSS Authentication

> Source: https://docs.polymarket.com/developers/CLOB/websocket/wss-auth

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Websocket

WSS Authentication

Only connections to `user` channel require authentication.

| Field | Optional | Description |
| --- | --- | --- |
| apikey | yes | Polygon account’s CLOB api key |
| secret | yes | Polygon account’s CLOB api secret |
| passphrase | yes | Polygon account’s CLOB api passphrase |

[WSS Quickstart](/quickstart/websocket/WSS-Quickstart)[User Channel](/developers/CLOB/websocket/user-channel)

⌘I

---


## Market Channel

> Source: https://docs.polymarket.com/developers/CLOB/websocket/market-channel

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Websocket

Market Channel

Public channel for updates related to market updates (level 2 price data).
**SUBSCRIBE**
`<wss-channel> market`

## [​](#book-message) book Message

Emitted When:

* First subscribed to a market
* When there is a trade that affects the book

### [​](#structure) Structure

| Name | Type | Description |
| --- | --- | --- |
| event\_type | string | ”book” |
| asset\_id | string | asset ID (token ID) |
| market | string | condition ID of market |
| timestamp | string | unix timestamp the current book generation in milliseconds (1/1,000 second) |
| hash | string | hash summary of the orderbook content |
| buys | OrderSummary[] | list of type (size, price) aggregate book levels for buys |
| sells | OrderSummary[] | list of type (size, price) aggregate book levels for sells |

Where a `OrderSummary` object is of the form:

| Name | Type | Description |
| --- | --- | --- |
| price | string | price of the orderbook level |
| size | string | size available at that price level |

Response

Copy

```shiki
{
  "event_type": "book",
  "asset_id": "65818619657568813474341868652308942079804919287380422192892211131408793125422",
  "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
  "bids": [
    { "price": ".48", "size": "30" },
    { "price": ".49", "size": "20" },
    { "price": ".50", "size": "15" }
  ],
  "asks": [
    { "price": ".52", "size": "25" },
    { "price": ".53", "size": "60" },
    { "price": ".54", "size": "10" }
  ],
  "timestamp": "123456789000",
  "hash": "0x0...."
}
```

## [​](#price_change-message) price\_change Message

**⚠️ Breaking Change Notice:** The price\_change message schema will be updated on September 15, 2025 at 11 PM UTC. Please see the [migration guide](/developers/CLOB/websocket/market-channel-migration-guide) for details.

Emitted When:

* A new order is placed
* An order is cancelled

### [​](#structure-2) Structure

| Name | Type | Description |
| --- | --- | --- |
| event\_type | string | ”price\_change” |
| market | string | condition ID of market |
| price\_changes | PriceChange[] | array of price change objects |
| timestamp | string | unix timestamp in milliseconds |

Where a `PriceChange` object is of the form:

| Name | Type | Description |
| --- | --- | --- |
| asset\_id | string | asset ID (token ID) |
| price | string | price level affected |
| size | string | new aggregate size for price level |
| side | string | ”BUY” or “SELL” |
| hash | string | hash of the order |
| best\_bid | string | current best bid price |
| best\_ask | string | current best ask price |

Response

Copy

```shiki
{
    "market": "0x5f65177b394277fd294cd75650044e32ba009a95022d88a0c1d565897d72f8f1",
    "price_changes": [
        {
            "asset_id": "71321045679252212594626385532706912750332728571942532289631379312455583992563",
            "price": "0.5",
            "size": "200",
            "side": "BUY",
            "hash": "56621a121a47ed9333273e21c83b660cff37ae50",
            "best_bid": "0.5",
            "best_ask": "1"
        },
        {
            "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
            "price": "0.5",
            "size": "200",
            "side": "SELL",
            "hash": "1895759e4df7a796bf4f1c5a5950b748306923e2",
            "best_bid": "0",
            "best_ask": "0.5"
        }
    ],
    "timestamp": "1757908892351",
    "event_type": "price_change"
}
```

## [​](#tick_size_change-message) tick\_size\_change Message

Emitted When:

* The minimum tick size of the market changes. This happens when the book’s price reaches the limits: price > 0.96 or price < 0.04

### [​](#structure-3) Structure

| Name | Type | Description |
| --- | --- | --- |
| event\_type | string | ”price\_change” |
| asset\_id | string | asset ID (token ID) |
| market | string | condition ID of market |
| old\_tick\_size | string | previous minimum tick size |
| new\_tick\_size | string | current minimum tick size |
| side | string | buy/sell |
| timestamp | string | time of event |

Response

Copy

```shiki
{
"event_type": "tick_size_change",
"asset_id": "65818619657568813474341868652308942079804919287380422192892211131408793125422",\
"market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
"old_tick_size": "0.01",
"new_tick_size": "0.001",
"timestamp": "100000000"
}
```

## [​](#last_trade_price-message) last\_trade\_price Message

Emitted When:

* When a maker and taker order is matched creating a trade event.

Response

Copy

```shiki
{
"asset_id":"114122071509644379678018727908709560226618148003371446110114509806601493071694",
"event_type":"last_trade_price",
"fee_rate_bps":"0",
"market":"0x6a67b9d828d53862160e470329ffea5246f338ecfffdf2cab45211ec578b0347",
"price":"0.456",
"side":"BUY",
"size":"219.217767",
"timestamp":"1750428146322"
}
```

## [​](#best_bid_ask-message) best\_bid\_ask Message

Emitted When:

* The best bid and ask prices for a market change.

(This message is behind the `custom_feature_enabled` flag)

### [​](#structure-4) Structure

| Name | Type | Description |
| --- | --- | --- |
| event\_type | string | ”best\_bid\_ask” |
| market | string | condition ID of market |
| asset\_id | string | asset ID (token ID) |
| best\_bid | string | current best bid price |
| best\_ask | string | current best ask price |
| spread | string | spread between best bid and ask |
| timestamp | string | unix timestamp in milliseconds |

### [​](#example) Example

Response

Copy

```shiki
{
  "event_type": "best_bid_ask",
  "market": "0x0005c0d312de0be897668695bae9f32b624b4a1ae8b140c49f08447fcc74f442",
  "asset_id": "85354956062430465315924116860125388538595433819574542752031640332592237464430",
  "best_bid": "0.73",
  "best_ask": "0.77",
  "spread": "0.04",
  "timestamp": "1766789469958"
}
```

## [​](#new_market-message) new\_market Message

Emitted When:

* A new market is created.

(This message is behind the `custom_feature_enabled` flag)

### [​](#structure-5) Structure

| Name | Type | Description |
| --- | --- | --- |
| id | string | market ID |
| question | string | market question |
| market | string | condition ID of market |
| slug | string | market slug |
| description | string | market description |
| assets\_ids | string[] | list of asset IDs |
| outcomes | string[] | list of outcomes |
| event\_message | object | event message object |
| timestamp | string | unix timestamp in milliseconds |
| event\_type | string | ”new\_market” |

Where a `EventMessage` object is of the form:

| Name | Type | Description |
| --- | --- | --- |
| id | string | event message ID |
| ticker | string | event message ticker |
| slug | string | event message slug |
| title | string | event message title |
| description | string | event message description |

### [​](#example-2) Example

Response

Copy

```shiki
{
    "id": "1031769",
    "question": "Will NVIDIA (NVDA) close above $240 end of January?",
    "market": "0x311d0c4b6671ab54af4970c06fcf58662516f5168997bdda209ec3db5aa6b0c1",
    "slug": "nvda-above-240-on-january-30-2026",
    "description": "This market will resolve to \"Yes\" if the official closing price for NVIDIA (NVDA) on the final trading day of January 2026 is higher than the listed price. Otherwise, this market will resolve to \"No\".\n\nIf the final trading day of the month is shortened (for example, due to a market-holiday schedule), the official closing price published for that shortened session will still be used for resolution.\n\nIf no official closing price is published for that session (for example, due to a trading halt into the close, system issue, or other disruption), the market will use the last valid on-exchange trade price of the regular session as the effective closing price.\n\nThe resolution source for this market is Yahoo Finance — specifically, the NVIDIA (NVDA) \"Close\" prices available at https://finance.yahoo.com/quote/NVDA/history, published under \"Historical Prices.\"\n\nIn the event of a stock split, reverse stock split, or similar corporate action affecting the listed company during the listed time frame, this market will resolve based on split-adjusted prices as displayed on Yahoo Finance.",
    "assets_ids": [
        "76043073756653678226373981964075571318267289248134717369284518995922789326425",
        "31690934263385727664202099278545688007799199447969475608906331829650099442770"
    ],
    "outcomes": [
        "Yes",
        "No"
    ],
    "event_message": {
        "id": "125819",
        "ticker": "nvda-above-in-january-2026",
        "slug": "nvda-above-in-january-2026",
        "title": "Will NVIDIA (NVDA) close above ___ end of January?",
        "description": "This market will resolve to \"Yes\" if the official closing price for NVIDIA (NVDA) on the final trading day of January 2026 is higher than the listed price. Otherwise, this market will resolve to \"No\".\n\nIf the final trading day of the month is shortened (for example, due to a market-holiday schedule), the official closing price published for that shortened session will still be used for resolution.\n\nIf no official closing price is published for that session (for example, due to a trading halt into the close, system issue, or other disruption), the market will use the last valid on-exchange trade price of the regular session as the effective closing price.\n\nThe resolution source for this market is Yahoo Finance — specifically, the NVIDIA (NVDA) \"Close\" prices available at https://finance.yahoo.com/quote/NVDA/history, published under \"Historical Prices.\"\n\nIn the event of a stock split, reverse stock split, or similar corporate action affecting the listed company during the listed time frame, this market will resolve based on split-adjusted prices as displayed on Yahoo Finance."
    },
    "timestamp": "1766790415550",
    "event_type": "new_market"
}
```

## [​](#market_resolved-message) market\_resolved Message

Emitted When:

* A market is resolved.

(This message is behind the `custom_feature_enabled` flag)

### [​](#structure-6) Structure

| Name | Type | Description |
| --- | --- | --- |
| id | string | market ID |
| question | string | market question |
| market | string | condition ID of market |
| slug | string | market slug |
| description | string | market description |
| assets\_ids | string[] | list of asset IDs |
| outcomes | string[] | list of outcomes |
| winning\_asset\_id | string | winning asset ID |
| winning\_outcome | string | winning outcome |
| event\_message | object | event message object |
| timestamp | string | unix timestamp in milliseconds |
| event\_type | string | ”market\_resolved” |

Where a `EventMessage` object is of the form:

| Name | Type | Description |
| --- | --- | --- |
| id | string | event message ID |
| ticker | string | event message ticker |
| slug | string | event message slug |
| title | string | event message title |
| description | string | event message description |

### [​](#example-3) Example

Response

Copy

```shiki
{
    "id": "1031769",
    "question": "Will NVIDIA (NVDA) close above $240 end of January?",
    "market": "0x311d0c4b6671ab54af4970c06fcf58662516f5168997bdda209ec3db5aa6b0c1",
    "slug": "nvda-above-240-on-january-30-2026",
    "description": "This market will resolve to \"Yes\" if the official closing price for NVIDIA (NVDA) on the final trading day of January 2026 is higher than the listed price. Otherwise, this market will resolve to \"No\".\n\nIf the final trading day of the month is shortened (for example, due to a market-holiday schedule), the official closing price published for that shortened session will still be used for resolution.\n\nIf no official closing price is published for that session (for example, due to a trading halt into the close, system issue, or other disruption), the market will use the last valid on-exchange trade price of the regular session as the effective closing price.\n\nThe resolution source for this market is Yahoo Finance — specifically, the NVIDIA (NVDA) \"Close\" prices available at https://finance.yahoo.com/quote/NVDA/history, published under \"Historical Prices.\"\n\nIn the event of a stock split, reverse stock split, or similar corporate action affecting the listed company during the listed time frame, this market will resolve based on split-adjusted prices as displayed on Yahoo Finance.",
    "assets_ids": [
        "76043073756653678226373981964075571318267289248134717369284518995922789326425",
        "31690934263385727664202099278545688007799199447969475608906331829650099442770"
    ],
    "winning_asset_id": "76043073756653678226373981964075571318267289248134717369284518995922789326425",
    "winning_outcome": "Yes",
    "event_message": {
        "id": "125819",
        "ticker": "nvda-above-in-january-2026",
        "slug": "nvda-above-in-january-2026",
        "title": "Will NVIDIA (NVDA) close above ___ end of January?",
        "description": "This market will resolve to \"Yes\" if the official closing price for NVIDIA (NVDA) on the final trading day of January 2026 is higher than the listed price. Otherwise, this market will resolve to \"No\".\n\nIf the final trading day of the month is shortened (for example, due to a market-holiday schedule), the official closing price published for that shortened session will still be used for resolution.\n\nIf no official closing price is published for that session (for example, due to a trading halt into the close, system issue, or other disruption), the market will use the last valid on-exchange trade price of the regular session as the effective closing price.\n\nThe resolution source for this market is Yahoo Finance — specifically, the NVIDIA (NVDA) \"Close\" prices available at https://finance.yahoo.com/quote/NVDA/history, published under \"Historical Prices.\"\n\nIn the event of a stock split, reverse stock split, or similar corporate action affecting the listed company during the listed time frame, this market will resolve based on split-adjusted prices as displayed on Yahoo Finance."
    },
    "timestamp": "1766790415550",
    "event_type": "new_market"
}
```

[User Channel](/developers/CLOB/websocket/user-channel)[Overview](/developers/sports-websocket/overview)

⌘I

---


## User Channel

> Source: https://docs.polymarket.com/developers/CLOB/websocket/user-channel

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Websocket

User Channel

Authenticated channel for updates related to user activities (orders, trades), filtered for authenticated user by apikey.
**SUBSCRIBE**
`<wss-channel> user`

## [​](#trade-message) Trade Message

Emitted when:

* when a market order is matched (“MATCHED”)
* when a limit order for the user is included in a trade (“MATCHED”)
* subsequent status changes for trade (“MINED”, “CONFIRMED”, “RETRYING”, “FAILED”)

### [​](#structure) Structure

| Name | Type | Description |
| --- | --- | --- |
| asset\_id | string | asset id (token ID) of order (market order) |
| event\_type | string | ”trade” |
| id | string | trade id |
| last\_update | string | time of last update to trade |
| maker\_orders | MakerOrder[] | array of maker order details |
| market | string | market identifier (condition ID) |
| matchtime | string | time trade was matched |
| outcome | string | outcome |
| owner | string | api key of event owner |
| price | string | price |
| side | string | BUY/SELL |
| size | string | size |
| status | string | trade status |
| taker\_order\_id | string | id of taker order |
| timestamp | string | time of event |
| trade\_owner | string | api key of trade owner |
| type | string | ”TRADE” |

Where a `MakerOrder` object is of the form:

| Name | Type | Description |
| --- | --- | --- |
| asset\_id | string | asset of the maker order |
| matched\_amount | string | amount of maker order matched in trade |
| order\_id | string | maker order ID |
| outcome | string | outcome |
| owner | string | owner of maker order |
| price | string | price of maker order |

Response

Copy

```shiki
{
  "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
  "event_type": "trade",
  "id": "28c4d2eb-bbea-40e7-a9f0-b2fdb56b2c2e",
  "last_update": "1672290701",
  "maker_orders": [
    {
      "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
      "matched_amount": "10",
      "order_id": "0xff354cd7ca7539dfa9c28d90943ab5779a4eac34b9b37a757d7b32bdfb11790b",
      "outcome": "YES",
      "owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
      "price": "0.57"
    }
  ],
  "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
  "matchtime": "1672290701",
  "outcome": "YES",
  "owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
  "price": "0.57",
  "side": "BUY",
  "size": "10",
  "status": "MATCHED",
  "taker_order_id": "0x06bc63e346ed4ceddce9efd6b3af37c8f8f440c92fe7da6b2d0f9e4ccbc50c42",
  "timestamp": "1672290701",
  "trade_owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
  "type": "TRADE"
}
```

## [​](#order-message) Order Message

Emitted when:

* When an order is placed (PLACEMENT)
* When an order is updated (some of it is matched) (UPDATE)
* When an order is canceled (CANCELLATION)

### [​](#structure-2) Structure

| Name | Type | Description |
| --- | --- | --- |
| asset\_id | string | asset ID (token ID) of order |
| associate\_trades | string[] | array of ids referencing trades that the order has been included in |
| event\_type | string | ”order” |
| id | string | order id |
| market | string | condition ID of market |
| order\_owner | string | owner of order |
| original\_size | string | original order size |
| outcome | string | outcome |
| owner | string | owner of orders |
| price | string | price of order |
| side | string | BUY/SELL |
| size\_matched | string | size of order that has been matched |
| timestamp | string | time of event |
| type | string | PLACEMENT/UPDATE/CANCELLATION |

Response

Copy

```shiki
{
  "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
  "associate_trades": null,
  "event_type": "order",
  "id": "0xff354cd7ca7539dfa9c28d90943ab5779a4eac34b9b37a757d7b32bdfb11790b",
  "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
  "order_owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
  "original_size": "10",
  "outcome": "YES",
  "owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
  "price": "0.57",
  "side": "SELL",
  "size_matched": "0",
  "timestamp": "1672290687",
  "type": "PLACEMENT"
}
```

[WSS Authentication](/developers/CLOB/websocket/wss-auth)[Market Channel](/developers/CLOB/websocket/market-channel)

⌘I

---


## CTF Overview

> Source: https://docs.polymarket.com/developers/CTF/overview

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Conditional Token Frameworks

Overview

All outcomes on Polymarket are tokenized on the Polygon network. Specifically, Polymarket outcomes shares are binary outcomes (ie “YES” and “NO”) using Gnosis’ Conditional Token Framework (CTF). They are distinct ERC1155 tokens related to a parent condition and backed by the same collateral. More technically, the binary outcome tokens are referred to as “positionIds” in Gnosis’s documentation. “PositionIds” are derived from a collateral token and distinct “collectionIds”. “CollectionIds” are derived from a “parentCollectionId”, (always bytes32(0) in our case) a “conditionId”, and a unique “indexSet”.
The “indexSet” is a 256 bit array denoting which outcome slots are in an outcome collection; it MUST be a nonempty proper subset of a condition’s outcome slots. In the binary case, which we are interested in, there are two “indexSets”, one for the first outcome and one for the second. The first outcome’s “indexSet” is 0b01 = 1 and the second’s is 0b10 = 2. The parent “conditionId” (shared by both “collectionIds” and therefore “positionIds”) is derived from a “questionId” (a hash of the UMA ancillary data), an “oracle” (the UMA adapter V2), and an “outcomeSlotCount” (always 2 in the binary case). The steps for calculating the ERC1155 token ids (positionIds) is as follows:

1. Get the conditionId
   1. Function:
      1. `getConditionId(oracle, questionId, outcomeSlotCount)`
   2. Inputs:
      1. `oracle`: address - UMA adapter V2
      2. `questionId`: bytes32 - hash of the UMA ancillary data
      3. `outcomeSlotCount`: uint - 2 for binary markets
2. Get the two collectionIds
   1. Function:
      1. `getCollectionId(parentCollectionId, conditionId, indexSet)`
   2. Inputs:
      1. `parentCollectionId`: bytes32 - bytes32(0)
      2. `conditionId`: bytes32 - the conditionId derived from (1)
      3. `indexSet`: uint - 1 (0b01) for the first and 2 (0b10) for the second.
3. Get the two positionIds
   1. Function:
      1. `getPositionId(collateralToken, collectionId)`
   2. Inputs:
      1. `collateralToken`: IERC20 - address of ERC20 token collateral (USDC)
      2. `collectionId`: bytes32 - the two collectionIds derived from (3)

Leveraging the relations above, specifically “conditionIds” -> “positionIds” the Gnosis CTF contract allows for “splitting” and “merging” full outcome sets. We explore these actions and provide code examples below.

[Resolution](/developers/resolution/UMA)[Splitting USDC](/developers/CTF/split)

⌘I

---


## Splitting USDC

> Source: https://docs.polymarket.com/developers/CTF/split

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Conditional Token Frameworks

Splitting USDC

At any time, after a condition has been prepared on the CTF contract (via `prepareCondition`), it is possible to “split” collateral into a full (position) set. In other words, one unit USDC can be split into 1 YES unit and 1 NO unit. If splitting from the collateral, the CTF contract will attempt to transfer `amount` collateral from the message sender to itself. If successful, `amount` stake will be minted in the split target positions. If any of the transfers, mints, or burns fail, the transaction will revert. The transaction will also revert if the given partition is trivial, invalid, or refers to more slots than the condition is prepared with. This operation happens via the `splitPosition()` function on the CTF contract with the following parameters:

* `collateralToken`: IERC20 - The address of the positions’ backing collateral token.
* `parentCollectionId`: bytes32 - The ID of the outcome collections common to the position being split and the split target positions. Null in Polymarket case.
* `conditionId`: bytes32 - The ID of the condition to split on.
* `partition`: uint[] - An array of disjoint index sets representing a nontrivial partition of the outcome slots of the given condition. E.G. A|B and C but not A|B and B|C (is not disjoint). Each element’s a number which, together with the condition, represents the outcome collection. E.G. 0b110 is A|B, 0b010 is B, etc. In the Polymarket case 1|2.
* `amount` - The amount of collateral or stake to split. Also the number of full sets to receive.

[Overview](/developers/CTF/overview)[Merging Tokens](/developers/CTF/merge)

⌘I

---


## Merging Tokens

> Source: https://docs.polymarket.com/developers/CTF/merge

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Conditional Token Frameworks

Merging Tokens

In addition to splitting collateral for a full set, the inverse can also happen; a full set can be “merged” for collateral. This operation can again happen at any time after a condition has been prepared on the CTF contract. One unit of each position in a full set is burned in return for 1 collateral unit. This operation happens via the `mergePositions()` function on the CTF contract with the following parameters:

* `collateralToken`: IERC20 - The address of the positions’ backing collateral token.
* `parentCollectionId`: bytes32 - The ID of the outcome collections common to the position being merged and the merge target positions. Null in Polymarket case.
* `conditionId`: bytes32 - The ID of the condition to merge on.
* `partition`: uint[] - An array of disjoint index sets representing a nontrivial partition of the outcome slots of the given condition. E.G. A|B and C but not A|B and B|C (is not disjoint). Each element’s a number which, together with the condition, represents the outcome collection. E.G. 0b110 is A|B, 0b010 is B, etc. In the Polymarket case 1|2.
* `amount` - The number of full sets to merge. Also the amount of collateral to receive.

[Splitting USDC](/developers/CTF/split)[Reedeeming Tokens](/developers/CTF/redeem)

⌘I

---


## Redeeming Tokens

> Source: https://docs.polymarket.com/developers/CTF/redeem

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Conditional Token Frameworks

Reedeeming Tokens

Once a condition has had it’s payouts reported (ie by the UMACTFAdapter calling `reportPayouts` on the CTF contract), users with shares in the winning outcome can redeem them for the underlying collateral. Specifically, users can call the `redeemPositions` function on the CTF contract which will burn all valuable conditional tokens in return for collateral according to the reported payout vector. This function has the following parameters:

* `collateralToken`: IERC20 - The address of the positions’ backing collateral token.
* `parentCollectionId`: bytes32 - The ID of the outcome collections common to the position being redeemed. Null in Polymarket case.
* `indexSets`: uint[] - The ID of the condition to redeem.
* `indexSets`: uint[] - An array of disjoint index sets representing a nontrivial partition of the outcome slots of the given condition. E.G. A|B and C but not A|B and B|C (is not disjoint). Each element’s a number which, together with the condition, represents the outcome collection. E.G. 0b110 is A|B, 0b010 is B, etc. In the Polymarket case 1|2.

[Merging Tokens](/developers/CTF/merge)[Deployment and Additional Information](/developers/CTF/deployment-resources)

⌘I

---


## Deployment Resources

> Source: https://docs.polymarket.com/developers/CTF/deployment-resources

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Conditional Token Frameworks

Deployment and Additional Information

## [​](#deployment) Deployment

The CTF contract is deployed (and verified) at the following addresses:

| Network | Deployed Address |
| --- | --- |
| Polygon Mainnet | [0x4D97DCd97eC945f40cF65F87097ACe5EA0476045](https://polygonscan.com/address/0x4D97DCd97eC945f40cF65F87097ACe5EA0476045) |
| Polygon Mainnet | [0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E](https://polygonscan.com/address/0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E) |

Polymarket provides code samples in both Python and TypeScript for interacting
with our smart chain contracts. You will need an RPC endpoint to access the
blockchain, and you’ll be responsible for paying gas fees when executing these
RPC/function calls. Please ensure you’re using the correct example for your wallet
type (Safe Wallet vs Proxy Wallet) when implementing.

## [​](#resources) Resources

* [On-Chain Code Samples](https://github.com/Polymarket/examples/tree/main/examples)
* [Polygon RPC List](https://chainlist.org/chain/137)
* [CTF Source Code](https://github.com/gnosis/conditional-tokens-contracts)
* [Audits](https://github.com/gnosis/conditional-tokens-contracts/tree/master/docs/audit)
* [Gist For positionId Calculation](https://gist.github.com/L-Kov/950bce141a9d1aa1ed3b1cfce6d30217)

[Reedeeming Tokens](/developers/CTF/redeem)[Proxy wallet](/developers/proxy-wallet)

⌘I

---


## Gamma API Overview

> Source: https://docs.polymarket.com/developers/gamma-markets-api/overview

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

All market data necessary for market resolution is available on-chain (ie ancillaryData in UMA 00 request), but Polymarket also provides a hosted service, Gamma, that indexes this data and provides additional market metadata (ie categorization, indexed volume, etc). This service is made available through a REST API. For public users, this resource read only and can be used to fetch useful information about markets for things like non-profit research projects, alternative trading interfaces, automated trading systems etc.

# [​](#endpoint) Endpoint

<https://gamma-api.polymarket.com>

[RTDS Comments](/developers/RTDS/RTDS-comments)[Gamma Structure](/developers/gamma-markets-api/gamma-structure)

⌘I

---


## Gamma Structure

> Source: https://docs.polymarket.com/developers/gamma-markets-api/gamma-structure

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Gamma Structure

Gamma Structure

Gamma provides some organizational models. These include events, and markets. The most fundamental element is always markets and the other models simply provide additional organization.

# [​](#detail) Detail

1. **Market**
   1. Contains data related to a market that is traded on. Maps onto a pair of clob token ids, a market address, a question id and a condition id
2. **Event**
   1. Contains a set of markets
   2. Variants:
      1. Event with 1 market (i.e., resulting in an SMP)
      2. Event with 2 or more markets (i.e., resulting in an GMP)

# [​](#example) Example

* **[Event]** Where will Barron Trump attend College?
  + **[Market]** Will Barron attend Georgetown?
  + **[Market]** Will Barron attend NYU?
  + **[Market]** Will Barron attend UPenn?
  + **[Market]** Will Barron attend Harvard?
  + **[Market]** Will Barron attend another college?

[Overview](/developers/gamma-markets-api/overview)[Fetching Markets](/developers/gamma-markets-api/fetch-markets-guide)

⌘I

---


## How to Fetch Markets

> Source: https://docs.polymarket.com/developers/gamma-markets-api/fetch-markets-guide

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Gamma Structure

How to Fetch Markets

Both the getEvents and getMarkets are paginated. See [pagination section](#pagination) for details.

This guide covers the three recommended approaches for fetching market data from the Gamma API, each optimized for different use cases.

## [​](#overview) Overview

There are three main strategies for retrieving market data:

1. **By Slug** - Best for fetching specific individual markets or events
2. **By Tags** - Ideal for filtering markets by category or sport
3. **Via Events Endpoint** - Most efficient for retrieving all active markets

---

## [​](#1-fetch-by-slug) 1. Fetch by Slug

**Use Case:** When you need to retrieve a specific market or event that you already know about.
Individual markets and events are best fetched using their unique slug identifier. The slug can be found directly in the Polymarket frontend URL.

### [​](#how-to-extract-the-slug) How to Extract the Slug

From any Polymarket URL, the slug is the path segment after `/event/` or `/market/`:

Copy

```shiki
https://polymarket.com/event/fed-decision-in-october?tid=1758818660485
                            ↑
                  Slug: fed-decision-in-october
```

### [​](#api-endpoints) API Endpoints

**For Events:** [GET /events/slug/](/api-reference/events/list-events)
**For Markets:** [GET /markets/slug/](/api-reference/markets/list-markets)

### [​](#examples) Examples

Copy

```shiki
curl "https://gamma-api.polymarket.com/events/slug/fed-decision-in-october"
```

---

## [​](#2-fetch-by-tags) 2. Fetch by Tags

**Use Case:** When you want to filter markets by category, sport, or topic.
Tags provide a powerful way to categorize and filter markets. You can discover available tags and then use them to filter your market requests.

### [​](#discover-available-tags) Discover Available Tags

**General Tags:** [GET /tags](/api-reference/tags/list-tags)
**Sports Tags & Metadata:** [GET /sports](/api-reference/sports/get-sports-metadata-information)
The `/sports` endpoint returns comprehensive metadata for sports including tag IDs, images, resolution sources, and series information.

### [​](#using-tags-in-market-requests) Using Tags in Market Requests

Once you have tag IDs, you can use them with the `tag_id` parameter in both markets and events endpoints.
**Markets with Tags:** [GET /markets](/api-reference/markets/list-markets)
**Events with Tags:** [GET /events](/api-reference/events/list-events)

Copy

```shiki
curl "https://gamma-api.polymarket.com/events?tag_id=100381&limit=1&closed=false"
```

### [​](#additional-tag-filtering) Additional Tag Filtering

You can also:

* Use `related_tags=true` to include related tag markets
* Exclude specific tags with `exclude_tag_id`

---

## [​](#3-fetch-all-active-markets) 3. Fetch All Active Markets

**Use Case:** When you need to retrieve all available active markets, typically for broader analysis or market discovery.
The most efficient approach is to use the `/events` endpoint and work backwards, as events contain their associated markets.
**Events Endpoint:** [GET /events](/api-reference/events/list-events)
**Markets Endpoint:** [GET /markets](/api-reference/markets/list-markets)

### [​](#key-parameters) Key Parameters

* `order=id` - Order by event ID
* `ascending=false` - Get newest events first
* `closed=false` - Only active markets
* `limit` - Control response size
* `offset` - For pagination

### [​](#examples-2) Examples

Copy

```shiki
curl "https://gamma-api.polymarket.com/events?order=id&ascending=false&closed=false&limit=100"
```

This approach gives you all active markets ordered from newest to oldest, allowing you to systematically process all available trading opportunities.

### [​](#pagination) Pagination

For large datasets, use pagination with `limit` and `offset` parameters:

* `limit=50` - Return 50 results per page
* `offset=0` - Start from the beginning (increment by limit for subsequent pages)

**Pagination Examples:**

Copy

```shiki
# Page 1: First 50 results (offset=0)
curl "https://gamma-api.polymarket.com/events?order=id&ascending=false&closed=false&limit=50&offset=0"
```

Copy

```shiki
# Page 2: Next 50 results (offset=50)
curl "https://gamma-api.polymarket.com/events?order=id&ascending=false&closed=false&limit=50&offset=50"
```

Copy

```shiki
# Page 3: Next 50 results (offset=100)
curl "https://gamma-api.polymarket.com/events?order=id&ascending=false&closed=false&limit=50&offset=100"
```

Copy

```shiki
# Paginating through markets with tag filtering
curl "https://gamma-api.polymarket.com/markets?tag_id=100381&closed=false&limit=25&offset=0"
```

Copy

```shiki
# Next page of markets with tag filtering
curl "https://gamma-api.polymarket.com/markets?tag_id=100381&closed=false&limit=25&offset=25"
```

---

## [​](#best-practices) Best Practices

1. **For Individual Markets:** Always use the slug method for best performance
2. **For Category Browsing:** Use tag filtering to reduce API calls
3. **For Complete Market Discovery:** Use the events endpoint with pagination
4. **Always Include `closed=false`:** Unless you specifically need historical data
5. **Implement Rate Limiting:** Respect API limits for production applications

## [​](#related-endpoints) Related Endpoints

* [Get Markets](/developers/gamma-markets-api/get-markets) - Full markets endpoint documentation
* [Get Events](/developers/gamma-markets-api/get-events) - Full events endpoint documentation
* [Search Markets](/developers/gamma-markets-api/get-public-search) - Search functionality

[Gamma Structure](/developers/gamma-markets-api/gamma-structure)[Gamma API Health check](/api-reference/gamma-status/gamma-api-health-check)

⌘I

---


## Market Maker Introduction

> Source: https://docs.polymarket.com/developers/market-makers/introduction

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Market Makers

Market Maker Introduction

## [​](#what-is-a-market-maker) What is a Market Maker?

A Market Maker (MM) on Polymarket is a sophisticated trader who provides liquidity to prediction markets by continuously posting bid and ask orders. By “laying the spread,” market makers enable other users to trade efficiently while earning the spread as compensation for the risk they take.
Market makers are essential to Polymarket’s ecosystem:

* **Provide liquidity** across all markets
* **Tighten spreads** for better user experience
* **Enable price discovery** through continuous quoting
* **Absorb trading flow** from retail and institutional users

**Not a Market Maker?** If you’re building an application that routes orders for your
users, see the [Builders Program](/developers/builders/builder-intro) instead. Builders
get access to gasless transactions via the Relayer Client and can earn grants through order attribution.

## [​](#getting-started) Getting Started

To become a market maker on Polymarket:

1. **Complete setup** - Deploy wallets, fund with USDCe, set token approvals
2. **Connect to data feeds** - WebSocket for orderbook, RTDS for low-latency data
3. **Start quoting** - Post orders via CLOB REST API

## [​](#available-tools) Available Tools

### [​](#by-action-type) By Action Type

[## Setup

Deposits, token approvals, wallet deployment, API keys](/developers/market-makers/setup)[## Trading

CLOB order entry, order types, quoting best practices](/developers/market-makers/trading)[## Data Feeds

WebSocket, RTDS, Gamma API, on-chain data](/developers/market-makers/data-feeds)[## Inventory Management

Split, merge, and redeem outcome tokens](/developers/market-makers/inventory)[## Liquidity Rewards

Earn rewards for providing liquidity](/developers/market-makers/liquidity-rewards)[## Maker Rebates Program

Earn rebates for providing liquidity](/developers/market-makers/maker-rebates-program)

## [​](#quick-reference) Quick Reference

| Action | Tool | Documentation |
| --- | --- | --- |
| Deposit USDCe | Bridge API | [Bridge Overview](/developers/misc-endpoints/bridge-overview) |
| Approve tokens | Relayer Client | [Setup Guide](/developers/market-makers/setup) |
| Post limit orders | CLOB REST API | [CLOB Client](/developers/CLOB/clients/methods-l2) |
| Monitor orderbook | WebSocket | [WebSocket Overview](/developers/CLOB/websocket/wss-overview) |
| Low-latency data | RTDS | [Data Feeds](/developers/market-makers/data-feeds) |
| Split USDCe to tokens | CTF / Relayer | [Inventory](/developers/market-makers/inventory) |
| Merge tokens to USDCe | CTF / Relayer | [Inventory](/developers/market-makers/inventory) |

## [​](#support) Support

For market maker onboarding and support, contact [[email protected]](/cdn-cgi/l/email-protection#43303633332c313703332c2f3a2e22312826376d202c2e).

[Endpoints](/quickstart/reference/endpoints)[Setup](/developers/market-makers/setup)

⌘I

---


## MM Setup

> Source: https://docs.polymarket.com/developers/market-makers/setup

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Market Makers

Setup

## [​](#overview) Overview

Before you can start market making on Polymarket, you need to complete these one-time setup steps:

1. Deposit bridged USDCe to Polygon
2. Deploy a wallet (EOA or Safe)
3. Approve tokens for trading
4. Generate API credentials

## [​](#deposit-usdce) Deposit USDCe

Market makers need USDCe on Polygon to fund their trading operations.

### [​](#options) Options

| Method | Best For | Documentation |
| --- | --- | --- |
| Bridge API | Automated deposits from other chains | [Bridge Overview](/developers/misc-endpoints/bridge-overview) |
| Direct Polygon transfer | Already have USDCe on Polygon | N/A |
| Cross-chain bridge | Large deposits from Ethereum | [Large Deposits](/polymarket-learn/deposits/large-cross-chain-deposits) |

### [​](#using-the-bridge-api) Using the Bridge API

Copy

```shiki
// Deposit USDCe from Ethereum to Polygon
const deposit = await fetch("https://clob.polymarket.com/deposit", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    chainId: "1",
    fromChain: "ethereum",
    toChain: "polygon",
    asset: "USDCe",
    amount: "100000000000" // $100,000 in USDCe (6 decimals)
  })
});
```

See [Bridge Deposit](/api-reference/bridge/create-deposit-addresses) for full API details.

## [​](#wallet-options) Wallet Options

### [​](#eoa-externally-owned-account) EOA (Externally Owned Account)

Standard Ethereum wallet. You pay for all onchain transactions (approvals, splits, merges, trade exedcution).

### [​](#safe-wallet-recommended) Safe Wallet (Recommended)

Gnosis Safe-based wallet deployed via Polymarket’s relayer. Benefits:

* **Gasless transactions** - Polymarket pays gas fees for onchain operations
* **Contract wallet** - Enables advanced features like batched transactions.

Deploy a Safe wallet using the [Relayer Client](/developers/builders/relayer-client):

Copy

```shiki
import { RelayClient, RelayerTxType } from "@polymarket/builder-relayer-client";

const client = new RelayClient(
  "https://relayer-v2.polymarket.com/",
  137, // Polygon mainnet
  signer,
  builderConfig,
  RelayerTxType.SAFE
);

// Deploy the Safe wallet
const response = await client.deploy();
const result = await response.wait();
console.log("Safe Address:", result?.proxyAddress);
```

## [​](#token-approvals) Token Approvals

Before trading, you must approve the exchange contracts to spend your tokens.

### [​](#required-approvals) Required Approvals

| Token | Spender | Purpose |
| --- | --- | --- |
| USDCe | CTF Contract | Split USDCe into outcome tokens |
| CTF (outcome tokens) | CTF Exchange | Trade outcome tokens |
| CTF (outcome tokens) | Neg Risk CTF Exchange | Trade neg-risk market tokens |

### [​](#contract-addresses-polygon-mainnet) Contract Addresses (Polygon Mainnet)

Copy

```shiki
const ADDRESSES = {
  USDCe: "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
  CTF: "0x4d97dcd97ec945f40cf65f87097ace5ea0476045",
  CTF_EXCHANGE: "0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E",
  NEG_RISK_CTF_EXCHANGE: "0xC5d563A36AE78145C45a50134d48A1215220f80a",
  NEG_RISK_ADAPTER: "0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296"
};
```

### [​](#approve-via-relayer-client) Approve via Relayer Client

Copy

```shiki
import { ethers } from "ethers";
import { Interface } from "ethers/lib/utils";

const erc20Interface = new Interface([
  "function approve(address spender, uint256 amount) returns (bool)"
]);

// Approve USDCe for CTF contract
const approveTx = {
  to: ADDRESSES.USDCe,
  data: erc20Interface.encodeFunctionData("approve", [
    ADDRESSES.CTF,
    ethers.constants.MaxUint256
  ]),
  value: "0"
};

const response = await client.execute([approveTx], "Approve USDCe for CTF");
await response.wait();
```

See [Relayer Client](/developers/builders/relayer-client) for complete examples.

## [​](#api-key-generation) API Key Generation

To place orders and access authenticated endpoints, you need L2 API credentials.

### [​](#generate-api-key) Generate API Key

Copy

```shiki
import { ClobClient } from "@polymarket/clob-client";

const client = new ClobClient(
  "https://clob.polymarket.com",
  137,
  signer
);

// Derive API credentials from your wallet
const credentials = await client.deriveApiKey();
console.log("API Key:", credentials.key);
console.log("Secret:", credentials.secret);
console.log("Passphrase:", credentials.passphrase);
```

### [​](#using-credentials) Using Credentials

Once you have credentials, initialize the client for authenticated operations:

Copy

```shiki
const client = new ClobClient(
  "https://clob.polymarket.com",
  137,
  wallet,
  credentials
);
```

See [CLOB Authentication](/developers/CLOB/authentication) for full details.

## [​](#next-steps) Next Steps

Once setup is complete:

[## Start Trading

Post limit orders and manage quotes](/developers/market-makers/trading)

[Market Maker Introduction](/developers/market-makers/introduction)[Trading](/developers/market-makers/trading)

⌘I

---


## MM Trading

> Source: https://docs.polymarket.com/developers/market-makers/trading

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Market Makers

Trading

## [​](#overview) Overview

Market makers primarily interact with Polymarket through the CLOB (Central Limit Order Book) API to post and manage limit orders.

## [​](#order-entry) Order Entry

### [​](#posting-limit-orders) Posting Limit Orders

Use the CLOB client to create and post limit orders:

Copy

```shiki
import { ClobClient, Side, OrderType } from "@polymarket/clob-client";

const client = new ClobClient(
  "https://clob.polymarket.com",
  137,
  wallet,
  credentials,
  signatureType,
  funder
);

// Post a bid (buy order)
const bidOrder = await client.createAndPostOrder({
  tokenID: "34097058504275310827233323421517291090691602969494795225921954353603704046623",
  side: Side.BUY,
  price: 0.48,
  size: 1000,
  orderType: OrderType.GTC
});

// Post an ask (sell order)
const askOrder = await client.createAndPostOrder({
  tokenID: "34097058504275310827233323421517291090691602969494795225921954353603704046623",
  side: Side.SELL,
  price: 0.52,
  size: 1000,
  orderType: OrderType.GTC
});
```

See [Create Order](/developers/CLOB/clients/methods-l1#createandpostorder) for full documentation.

### [​](#batch-orders) Batch Orders

For efficiency, post multiple orders in a single request:

Copy

```shiki
const orders = await Promise.all([
  client.createOrder({ tokenID, side: Side.BUY, price: 0.48, size: 500 }),
  client.createOrder({ tokenID, side: Side.BUY, price: 0.47, size: 500 }),
  client.createOrder({ tokenID, side: Side.SELL, price: 0.52, size: 500 }),
  client.createOrder({ tokenID, side: Side.SELL, price: 0.53, size: 500 })
]);

const response = await client.postOrders(
  orders.map(order => ({ order, orderType: OrderType.GTC }))
);
```

See [Post Orders Batch](/developers/CLOB/clients/methods-l2#postorders) for details.

## [​](#order-types) Order Types

| Type | Behavior | MM Use Case |
| --- | --- | --- |
| **GTC** (Good Till Cancelled) | Rests on book until filled or cancelled | Default for passive quoting |
| **GTD** (Good Till Date) | Auto-expires at specified time | Auto-expire before events |
| **FOK** (Fill or Kill) | Fill entirely immediately or cancel | Aggressive rebalancing (all or nothing) |
| **FAK** (Fill and Kill) | Fill available immediately, cancel rest | Partial rebalancing acceptable |

### [​](#when-to-use-each) When to Use Each

**For passive market making (maker orders):**

* **GTC** - Standard quotes that sit on the book
* **GTD** - Time-limited quotes (e.g., expire before market close)

**For rebalancing (taker orders):**

* **FOK** - When you need exact size or nothing
* **FAK** - When partial fills are acceptable

Copy

```shiki
// GTD example: expire in 1 hour
const expiringOrder = await client.createOrder({
  tokenID,
  side: Side.BUY,
  price: 0.50,
  size: 1000,
  orderType: OrderType.GTD,
  expiration: Math.floor(Date.now() / 1000) + 3600 // 1 hour from now
});
```

## [​](#order-management) Order Management

### [​](#cancel-orders) Cancel Orders

Cancel individual orders or all orders:

Copy

```shiki
// Cancel single order
await client.cancelOrder(orderId);

// Cancel multiple orders in a single calls
await client.cancelOrders(orderIds: string[]);

// Cancel all orders for a market
await client.cancelMarketOrders(conditionId);

// Cancel all orders
await client.cancelAll();
```

See [Cancel Orders](/developers/CLOB/clients/methods-l2#cancelorder) for full documentation.

### [​](#get-active-orders) Get Active Orders

Monitor your open orders:

Copy

```shiki
// Get active order
const order = await client.getOrder(orderId);

// Get active orders optionally filtered
const orders = await client.getOpenOrders({
  id?: string; // Order ID (hash)
  market?: string; // Market condition ID
  asset_id?: string; // Token ID
});
```

See [Get Active Orders](/developers/CLOB/clients/methods-l2#getorder) for details.

## [​](#best-practices) Best Practices

### [​](#quote-management) Quote Management

1. **Two-sided quoting** - Post both bids and asks to earn maximum [liquidity rewards](/developers/market-makers/liquidity-rewards)
2. **Monitor inventory** - Skew quotes based on your position
3. **Cancel stale quotes** - Remove orders when market conditions change
4. **Use GTD for events** - Auto-expire quotes before known events

### [​](#latency-optimization) Latency Optimization

1. **Batch orders** - Use `postOrders()` instead of multiple `createAndPostOrder()` calls
2. **WebSocket for data** - Use WebSocket feeds instead of polling REST endpoints

### [​](#risk-management) Risk Management

1. **Size limits** - Check token balances before quoting; don’t exceed inventory
2. **Price guards** - Validate against book midpoint; reject outlier prices
3. **Kill switch** - Use `cancelAll()` on error or position breach
4. **Monitor fills** - Subscribe to WebSocket user channel for real-time fill updates

## [​](#tick-sizes) Tick Sizes

Markets have different minimum price increments:

Copy

```shiki
const tickSize = await client.getTickSize(tokenID);
// Returns: "0.1" | "0.01" | "0.001" | "0.0001"
```

Ensure your prices conform to the market’s tick size.

## [​](#fee-structure) Fee Structure

| Role | Fee |
| --- | --- |
| Maker | 0 bps |
| Taker | 0 bps |

Current fees are 0% for both makers and takers. See [CLOB Introduction](/developers/CLOB/introduction) for fee calculation details.

## [​](#related-documentation) Related Documentation

[## CLOB Client Overview

Complete client method reference](/developers/CLOB/clients/methods-overview)[## L2 Methods

Authenticated order management methods](/developers/CLOB/clients/methods-l2)[## WebSocket Feeds

Real-time order and market data](/developers/CLOB/websocket/wss-overview)[## Liquidity Rewards

Earn rewards for providing liquidity](/developers/market-makers/liquidity-rewards)

[Setup](/developers/market-makers/setup)[Liquidity Rewards](/developers/market-makers/liquidity-rewards)

⌘I

---


## Data Feeds

> Source: https://docs.polymarket.com/developers/market-makers/data-feeds

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Market Makers

Data Feeds

## [​](#overview) Overview

Market makers need fast, reliable data to price markets and manage inventory. Polymarket provides several data feeds at different latency and detail levels.

| Feed | Latency | Use Case | Access |
| --- | --- | --- | --- |
| WebSocket | ~100ms | Standard MM operations | Public |
| Gamma API | ~1s | Market metadata, indexing | Public |
| Onchain | Block time | Settlement, resolution | Public |

## [​](#websocket-feeds) WebSocket Feeds

The WebSocket API provides real-time market data with low latency. This is sufficient for most market making strategies.

### [​](#connecting) Connecting

Copy

```shiki
const ws = new WebSocket("wss://ws-subscriptions-clob.polymarket.com/ws/market");

ws.onopen = () => {
  // Subscribe to orderbook updates
  ws.send(JSON.stringify({
    type: "market",
    assets_ids: [tokenId]
  }));
};

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  // Handle orderbook update
};
```

### [​](#available-channels) Available Channels

| Channel | Message Types | Documentation |
| --- | --- | --- |
| `market` | `book`, `price_change`, `last_trade_price` | [Market Channel](/developers/CLOB/websocket/market-channel) |
| `user` | Order fills, cancellations | [User Channel](/developers/CLOB/websocket/user-channel) |

### [​](#user-channel-authenticated) User Channel (Authenticated)

Monitor your order activity in real-time:

Copy

```shiki
// Requires authentication
const userWs = new WebSocket("wss://ws-subscriptions-clob.polymarket.com/ws/user");

userWs.onopen = () => {
  userWs.send(JSON.stringify({
    type: "user",
    auth: {
      apiKey: "your-api-key",
      secret: "your-secret",
      passphrase: "your-passphrase"
    },
    markets: [conditionId] // Optional: filter to specific markets
  }));
};

userWs.onmessage = (event) => {
  const data = JSON.parse(event.data);
  // Handle order fills, cancellations, etc.
};
```

See [WebSocket Authentication](/developers/CLOB/websocket/wss-auth) for auth details.

### [​](#best-practices) Best Practices

1. **Reconnection logic** - Implement automatic reconnection with exponential backoff
2. **Heartbeats** - Respond to ping messages to maintain connection
3. **Local orderbook** - Maintain a local copy and apply incremental updates
4. **Sequence numbers** - Track sequence to detect missed messages

See [WebSocket Overview](/developers/CLOB/websocket/wss-overview) for complete documentation.

## [​](#gamma-api) Gamma API

The Gamma API provides market metadata and indexing. Use it for:

* Market titles, slugs, categories
* Event/condition mapping
* Volume and liquidity data
* Outcome token metadata

### [​](#get-markets) Get Markets

Copy

```shiki
const response = await fetch(
  "https://gamma-api.polymarket.com/markets?active=true"
);
const markets = await response.json();
```

### [​](#get-events) Get Events

Copy

```shiki
const response = await fetch(
  "https://gamma-api.polymarket.com/events?slug=us-presidential-election"
);
const event = await response.json();
```

### [​](#key-fields-for-mms) Key Fields for MMs

| Field | Description |
| --- | --- |
| `conditionId` | Unique market identifier |
| `clobTokenIds` | Outcome token IDs |
| `outcomes` | Outcome names |
| `outcomePrices` | Current outcome prices |
| `volume` | Trading volume |
| `liquidity` | Current liquidity |

See [Gamma API Overview](/developers/gamma-markets-api/overview) for complete documentation.

## [​](#onchain-data) Onchain Data

For settlement, resolution, and position tracking, market makers may query onchain data directly.

### [​](#data-sources) Data Sources

| Data | Source | Use Case |
| --- | --- | --- |
| Token balances | ERC1155 `balanceOf` | Position tracking |
| Resolution | UMA Oracle events | Pre-resolution risk modeling |
| Condition resolution | CTF contract | Post-resolution redemption |

### [​](#rpc-providers) RPC Providers

Common providers for Polygon:

* Alchemy
* QuickNode
* Infura

### [​](#uma-oracle) UMA Oracle

Markets are resolved via UMA’s Optimistic Oracle. Monitor resolution events for risk management.
See [Resolution](/developers/resolution/UMA) for details on the resolution process.

## [​](#related-documentation) Related Documentation

[## WebSocket Overview

Complete WebSocket documentation](/developers/CLOB/websocket/wss-overview)[## Gamma API

Market metadata and indexing](/developers/gamma-markets-api/overview)[## Resolution

UMA Oracle resolution process](/developers/resolution/UMA)

[Maker Rebates Program](/developers/market-makers/maker-rebates-program)[Inventory Management](/developers/market-makers/inventory)

⌘I

---


## Inventory Management

> Source: https://docs.polymarket.com/developers/market-makers/inventory

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Market Makers

Inventory Management

## [​](#overview) Overview

Market makers need to manage their inventory of outcome tokens. This involves:

1. **Splitting** USDCe into YES/NO tokens to have inventory to quote
2. **Merging** tokens back to USDCe to reduce exposure
3. **Redeeming** winning tokens after market resolution

All these operations use the Conditional Token Framework (CTF) contract, typically via the Relayer Client for gasless execution.

These examples assume you have initialized a RelayClient. See [Setup](/developers/market-makers/setup) for client initialization.

## [​](#splitting-usdce-into-tokens) Splitting USDCe into Tokens

Split 1 USDCe into 1 YES + 1 NO token. This creates inventory for quoting both sides.

### [​](#via-relayer-client-recommended) Via Relayer Client (Recommended)

Copy

```shiki
import { ethers } from "ethers";
import { Interface } from "ethers/lib/utils";
import { RelayClient, Transaction } from "@polymarket/builder-relayer-client";

const CTF_ADDRESS = "0x4d97dcd97ec945f40cf65f87097ace5ea0476045";
const USDCe_ADDRESS = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174";

const ctfInterface = new Interface([
  "function splitPosition(address collateralToken, bytes32 parentCollectionId, bytes32 conditionId, uint[] partition, uint amount)"
]);

// Split $1000 USDCe into YES/NO tokens
const amount = ethers.utils.parseUnits("1000", 6); // USDCe has 6 decimals

const splitTx: Transaction = {
  to: CTF_ADDRESS,
  data: ctfInterface.encodeFunctionData("splitPosition", [
    USDCe_ADDRESS,                                    // collateralToken
    ethers.constants.HashZero,                       // parentCollectionId (null for Polymarket)
    conditionId,                                     // conditionId from market
    [1, 2],                                          // partition: [YES, NO]
    amount
  ]),
  value: "0"
};

const response = await client.execute([splitTx], "Split USDCe into tokens");
const result = await response.wait();
console.log("Split completed:", result?.transactionHash);
```

### [​](#result) Result

After splitting 1000 USDCe:

* Receive 1000 YES tokens
* Receive 1000 NO tokens
* USDCe balance decreases by 1000

## [​](#merging-tokens-to-usdce) Merging Tokens to USDCe

Merge equal amounts of YES + NO tokens back into USDCe. Useful for:

* Reducing inventory
* Exiting a market
* Converting profits to USDCe

### [​](#via-relayer-client) Via Relayer Client

Copy

```shiki
const ctfInterface = new Interface([
  "function mergePositions(address collateralToken, bytes32 parentCollectionId, bytes32 conditionId, uint[] partition, uint amount)"
]);

// Merge 500 YES + 500 NO back to 500 USDCe
const amount = ethers.utils.parseUnits("500", 6);

const mergeTx: Transaction = {
  to: CTF_ADDRESS,
  data: ctfInterface.encodeFunctionData("mergePositions", [
    USDCe_ADDRESS,
    ethers.constants.HashZero,
    conditionId,
    [1, 2],
    amount
  ]),
  value: "0"
};

const response = await client.execute([mergeTx], "Merge tokens to USDCe");
await response.wait();
```

### [​](#result-2) Result

After merging 500 of each:

* YES tokens decrease by 500
* NO tokens decrease by 500
* USDCe balance increases by 500

## [​](#redeeming-after-resolution) Redeeming After Resolution

After a market resolves, redeem winning tokens for USDCe.

### [​](#check-resolution-status) Check Resolution Status

Copy

```shiki
// Via CLOB API
const market = await clobClient.getMarket(conditionId);
if (market.closed) {
  // Market is resolved
  const winningToken = market.tokens.find(t => t.winner);
  console.log("Winning outcome:", winningToken?.outcome);
}
```

### [​](#redeem-winning-tokens) Redeem Winning Tokens

Copy

```shiki
const ctfInterface = new Interface([
  "function redeemPositions(address collateralToken, bytes32 parentCollectionId, bytes32 conditionId, uint[] indexSets)"
]);

const redeemTx: Transaction = {
  to: CTF_ADDRESS,
  data: ctfInterface.encodeFunctionData("redeemPositions", [
    USDCe_ADDRESS,
    ethers.constants.HashZero,
    conditionId,
    [1, 2]  // Redeem both YES and NO (only winners pay out)
  ]),
  value: "0"
};

const response = await client.execute([redeemTx], "Redeem winning tokens");
await response.wait();
```

### [​](#payout) Payout

* If YES wins: Each YES token redeems for $1 USDCe
* If NO wins: Each NO token redeems for $1 USDCe
* Losing tokens are worthless (redeem for $0)

## [​](#negative-risk-markets) Negative Risk Markets

Multi-outcome markets use the Negative Risk CTF Exchange. The split/merge process is similar but uses different contract addresses.

Copy

```shiki
const NEG_RISK_ADAPTER = "0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296";
const NEG_RISK_CTF_EXCHANGE = "0xC5d563A36AE78145C45a50134d48A1215220f80a";
```

See [Negative Risk Overview](/developers/neg-risk/overview) for details.

## [​](#inventory-strategies) Inventory Strategies

### [​](#pre-market-preparation) Pre-market Preparation

Before quoting a market:

1. Check market metadata via Gamma API
2. Split sufficient USDCe to cover expected quoting size
3. Set token approvals if not already done

### [​](#during-trading) During Trading

Monitor inventory and adjust:

* Skew quotes when inventory is imbalanced
* Merge excess tokens to free up capital
* Split more when inventory runs low

### [​](#post-resolution) Post-Resolution

After market closes:

1. Cancel all open orders
2. Wait for resolution
3. Redeem winning tokens
4. Merge any remaining pairs

## [​](#batch-operations) Batch Operations

For efficiency, batch multiple operations:

Copy

```shiki
const transactions: Transaction[] = [
  // Split on Market A
  {
    to: CTF_ADDRESS,
    data: ctfInterface.encodeFunctionData("splitPosition", [
      USDCe_ADDRESS,
      ethers.constants.HashZero,
      conditionIdA,
      [1, 2],
      ethers.utils.parseUnits("1000", 6)
    ]),
    value: "0"
  },
  // Split on Market B
  {
    to: CTF_ADDRESS,
    data: ctfInterface.encodeFunctionData("splitPosition", [
      USDCe_ADDRESS,
      ethers.constants.HashZero,
      conditionIdB,
      [1, 2],
      ethers.utils.parseUnits("1000", 6)
    ]),
    value: "0"
  }
];

const response = await client.execute(transactions, "Batch inventory setup");
await response.wait();
```

## [​](#related-documentation) Related Documentation

[## CTF Overview

Conditional Token Framework basics](/developers/CTF/overview)[## Split Positions

Detailed split documentation](/developers/CTF/split)[## Merge Positions

Detailed merge documentation](/developers/CTF/merge)[## Relayer Client

Gasless transaction execution](/developers/builders/relayer-client)

[Data Feeds](/developers/market-makers/data-feeds)[Builder Program Introduction](/developers/builders/builder-intro)

⌘I

---


## Liquidity Rewards

> Source: https://docs.polymarket.com/developers/market-makers/liquidity-rewards

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Market Makers

Liquidity Rewards

## [​](#overview) Overview

By posting resting limit orders, liquidity providers (makers) are automatically eligible for Polymarket’s incentive program. The overall goal of this program is to catalyze a healthy, liquid marketplace. We can further define this as creating incentives that:

* Catalyze liquidity across all markets
* Encourage liquidity throughout a market’s entire lifecycle
* Motivate passive, balanced quoting tight to a market’s mid-point
* Encourages trading activity
* Discourages blatantly exploitative behaviors

This program is heavily inspired by dYdX’s liquidity provider rewards which you can read more about [here](https://www.dydx.foundation/blog/liquidity-provider-rewards). In fact, the incentive methodology is essentially a copy of dYdX’s successful methodology but with some adjustments including specific adaptations for binary contract markets with distinct books, no staking mechanic a slightly modified order utility-relative depth function and reward amounts isolated per market. Rewards are distributed directly to the maker’s addresses daily at midnight UTC.

## [​](#methodology) Methodology

Polymarket liquidity providers will be rewarded based on a formula that rewards participation in markets (complementary consideration!), boosts two-sided depth (single-sided orders still score), and spread (vs. mid-market, adjusted for the size cutoff!). Each market still configure a max spread and min size cutoff within which orders are considered the average of rewards earned is determined by the relative share of each participant’s Qn in market m.

| Variable | Description |
| --- | --- |
| $ | order position scoring function |
| v | max spread from midpoint (in cents) |
| s | spread from size-cutoff-adjusted midpoint |
| b | in-game multiplier |
| m | market |
| m’ | market complement (i.e NO if m = YES) |
| n | trader index |
| u | sample index |
| c | scaling factor (currently 3.0 on all markets) |
| Qne | point total for book one for a sample |
| Qno | point total for book two for a sample |
| Spread% | distance from midpoint (bps or relative) for order n in market m |
| BidSize | share-denominated quantity of bid |
| AskSize | share-denominated quantity of ask |

## [​](#equations) Equations

**Equation 1:**
S(v,s)=(v−sv)2⋅bS(v,s)= (\frac{v-s}{v})^2 \cdot bS(v,s)=(vv−s​)2⋅b
**Equation 2:**
Qone=S(v,Spreadm1)⋅BidSizem1+S(v,Spreadm2)⋅BidSizem2+…Q\_{one}= S(v,Spread\_{m\_1}) \cdot BidSize\_{m\_1} + S(v,Spread\_{m\_2}) \cdot BidSize\_{m\_2} + \dots Qone​=S(v,Spreadm1​​)⋅BidSizem1​​+S(v,Spreadm2​​)⋅BidSizem2​​+…
+S(v,Spreadm1′)⋅AskSizem1′+S(v,Spreadm2′)⋅AskSizem2′ + S(v, Spread\_{m^\prime\_1}) \cdot AskSize\_{m^\prime\_1} + S(v, Spread\_{m^\prime\_2}) \cdot AskSize\_{m^\prime\_2}+S(v,Spreadm1′​​)⋅AskSizem1′​​+S(v,Spreadm2′​​)⋅AskSizem2′​​
**Equation 3:**
Qtwo=S(v,Spreadm1)⋅AskSizem1+S(v,Spreadm2)⋅AskSizem2+…Q\_{two}= S(v,Spread\_{m\_1}) \cdot AskSize\_{m\_1} + S(v,Spread\_{m\_2}) \cdot AskSize\_{m\_2} + \dots Qtwo​=S(v,Spreadm1​​)⋅AskSizem1​​+S(v,Spreadm2​​)⋅AskSizem2​​+…
+S(v,Spreadm1′)⋅BidSizem1′+S(v,Spreadm2′)⋅BidSizem2′ + S(v, Spread\_{m^\prime\_1}) \cdot BidSize\_{m^\prime\_1} + S(v, Spread\_{m^\prime\_2}) \cdot BidSize\_{m^\prime\_2}+S(v,Spreadm1′​​)⋅BidSizem1′​​+S(v,Spreadm2′​​)⋅BidSizem2′​​
**Equation 4:**
**Equation 4a:**
If midpoint is in range [0.10,0.90] allow single sided liq to score:
Qmin⁡=max⁡(min⁡(Qone,Qtwo),max⁡(Qone/c,Qtwo/c))Q\_{\min} = \max(\min({Q\_{one}, Q\_{two}}), \max(Q\_{one}/c, Q\_{two}/c))Qmin​=max(min(Qone​,Qtwo​),max(Qone​/c,Qtwo​/c))
**Equation 4b:**
If midpoint is in either range [0,0.10) or (.90,1.0] require liq to be double sided to score:
Qmin⁡=min⁡(Qone,Qtwo)Q\_{\min} = \min({Q\_{one}, Q\_{two}})Qmin​=min(Qone​,Qtwo​)
**Equation 5:**
Qnormal=Qmin∑n=1N(Qmin)nQ\_{normal} = \frac{Q\_{min}}{\sum\_{n=1}^{N}{(Q\_{min})\_n}}Qnormal​=∑n=1N​(Qmin​)n​Qmin​​
**Equation 6:**
Qepoch=∑u=110,080(Qnormal)uQ\_{epoch} = \sum\_{u=1}^{10,080}{(Q\_{normal})\_u}Qepoch​=∑u=110,080​(Qnormal​)u​
**Equation 7:**
Qfinal=Qepoch∑n=1N(Qepoch)nQ\_{final}=\frac{Q\_{epoch}}{\sum\_{n=1}^{N}{(Q\_{epoch})\_n}}Qfinal​=∑n=1N​(Qepoch​)n​Qepoch​​

## [​](#steps) Steps

1. Quadratic scoring rule for an order based on position between the adjusted midpoint and the minimum qualifying spread
2. Calculate first market side score. Assume a trader has the following open orders:
   * 100Q bid on m @0.49 (adjusted midpoint is 0.50 then spread of this order is 0.01 or 1c)
   * 200Q bid on m @0.48
   * 100Q ask on m’ @0.51and assume an adjusted market midpoint of 0.50 and maxSpread config of 3c for both m and m’. Then the trader’s score is:
   Qne=((3−1)3)2⋅100+((3−2)3)2⋅200+((3−1)3)2⋅100Q\_{ne} = \left( \frac{(3-1)}{3} \right)^2 \cdot 100 + \left( \frac{(3-2)}{3} \right)^2 \cdot 200 + \left( \frac{(3-1)}{3} \right)^2 \cdot 100Qne​=(3(3−1)​)2⋅100+(3(3−2)​)2⋅200+(3(3−1)​)2⋅100
   QneQ\_{ne}Qne​ is calculated every minute using random sampling
3. Calculate second market side score. Assume a trader has the following open orders:
   * 100Q bid on m @0.485
   * 100Q bid on m’ @0.48
   * 200Q ask on m’ @0.505and assume an adjusted market midpoint of 0.50 and maxSpread config of 3c for both m and m’. Then the trader’s score is:
   Qno=((3−1.5)3)2⋅100+((3−2)3)2⋅100+((3−.5)3)2⋅200Q\_{no} = \left( \frac{(3-1.5)}{3} \right)^2 \cdot 100 + \left( \frac{(3-2)}{3} \right)^2 \cdot 100 + \left( \frac{(3-.5)}{3} \right)^2 \cdot 200Qno​=(3(3−1.5)​)2⋅100+(3(3−2)​)2⋅100+(3(3−.5)​)2⋅200
   QnoQ\_{no}Qno​ is calculated every minute using random sampling
4. Boosts 2-sided liquidity by taking the minimum of QneQ\_{ne}Qne​ and QnoQ\_{no}Qno​, and rewards 1-side liquidity at a reduced rate (divided by c)
   Calculated every minute
5. QnormalQ\_{normal}Qnormal​ is the QminQ\_{min}Qmin​ of a market maker divided by the sum of all the QminQ\_{min}Qmin​ of other market makers in a given sample
6. QepochQ\_{epoch}Qepoch​ is the sum of all QnormalQ\_{normal}Qnormal​ for a trader in a given epoch
7. QfinalQ\_{final}Qfinal​ normalizes QepochQ\_{epoch}Qepoch​ by dividing it by the sum of all other market maker’s QepochQ\_{epoch}Qepoch​ in a given epoch this value is multiplied by the rewards available for the market to get a trader’s reward

Both min\_incentive\_size and max\_incentive\_spread can be fetched alongside full market objects via both the CLOB API and Markets API. Reward allocations for an epoch can be fetched via the Markets API.

[Trading](/developers/market-makers/trading)[Maker Rebates Program](/developers/market-makers/maker-rebates-program)

⌘I

---


## Maker Rebates Program

> Source: https://docs.polymarket.com/developers/market-makers/maker-rebates-program

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Market Makers

Maker Rebates Program

Polymarket has enabled **taker fees** on **15-minute crypto markets**. These fees fund a **Maker Rebates** program that pays daily USDC rebates to liquidity providers.

## [​](#fee-handling-by-implementation-type) Fee Handling by Implementation Type

### [​](#option-1-official-clob-clients-recommended) Option 1: Official CLOB Clients (Recommended)

The official CLOB clients **automatically handle fees** for you. Update to the latest version:
[## TypeScript Client

npm install @polymarket/clob-client@latest](https://github.com/Polymarket/clob-client)

[## Python Client

pip install —upgrade py-clob-client](https://github.com/Polymarket/py-clob-client)[## Rust Client

cargo add polymarket-client-sdk](https://github.com/Polymarket/rs-clob-client)

**What the client does automatically:**

1. Fetches the fee rate for the market’s token ID
2. Includes `feeRateBps` in the order structure
3. Signs the order with the fee rate included

**You don’t need to do anything extra**. Just update your client and your orders will work on fee-enabled markets.

---

### [​](#option-2-rest-api-/-custom-implementations) Option 2: REST API / Custom Implementations

If you’re calling the REST API directly or building your own order signing, you must manually include the fee rate in your **signed order payload**.

#### [​](#step-1-fetch-the-fee-rate) Step 1: Fetch the Fee Rate

Query the fee rate for the token ID before creating your order:

Copy

```shiki
GET https://clob.polymarket.com/fee-rate?token_id={token_id}
```

**Response:**

Copy

```shiki
{
  "fee_rate_bps": 1000
}
```

* **Fee-enabled markets** return a value like `1000`
* **Fee-free markets** return `0`

#### [​](#step-2-include-in-your-signed-order) Step 2: Include in Your Signed Order

Add the `feeRateBps` field to your order object. This value is **part of the signed payload**, the CLOB validates your signature against it.

Copy

```shiki
{
  "salt": "12345",
  "maker": "0x...",
  "signer": "0x...",
  "taker": "0x...",
  "tokenId": "71321045679252212594626385532706912750332728571942532289631379312455583992563",
  "makerAmount": "50000000",
  "takerAmount": "100000000",
  "expiration": "0",
  "nonce": "0",
  "feeRateBps": "1000",
  "side": "0",
  "signatureType": 2,
  "signature": "0x..."
}
```

#### [​](#step-3-sign-and-submit) Step 3: Sign and Submit

1. Include `feeRateBps` in the order object **before signing**
2. Sign the complete order
3. POST to `/order` endpoint

**Important:** Always fetch `fee_rate_bps` dynamically, do not hardcode. The fee rate may vary by market or change over time. You only need to pass `feeRateBps`

See the [Create Order documentation](/developers/CLOB/orders/create-order) for full signing details.

---

## [​](#fee-behavior) Fee Behavior

Fees are calculated in USDC and vary based on the share price. The effective rate **peaks at 50%** probability and decreases symmetrically toward the extremes.

### [​](#fee-table-100-shares) Fee Table (100 shares)

| Price | Trade Value | Fee (USDC) | Effective Rate |
| --- | --- | --- | --- |
| $0.10 | $10 | $0.02 | 0.20% |
| $0.20 | $20 | $0.13 | 0.64% |
| $0.30 | $30 | $0.33 | 1.10% |
| $0.40 | $40 | $0.58 | 1.44% |
| $0.50 | $50 | $0.78 | **1.56%** |
| $0.60 | $60 | $0.86 | 1.44% |
| $0.70 | $70 | $0.77 | 1.10% |
| $0.80 | $80 | $0.51 | 0.64% |
| $0.90 | $90 | $0.18 | 0.20% |

The maximum effective fee rate is **1.56%** at 50% probability. Fees are the same for both buying and selling.

---

## [​](#maker-rebates) Maker Rebates

### [​](#how-rebates-work) How Rebates Work

* **Eligibility:** Your orders must add liquidity (maker orders) and get filled
* **Calculation:** Proportional to your share of executed maker volume in each eligible market
* **Payment:** Daily in USDC, paid directly to your wallet

### [​](#rebate-pool) Rebate Pool

The rebate pool for each market is funded by taker fees collected in that market. The payout percentage is subject to change:

| Period | Maker Rebate | Distribution Method |
| --- | --- | --- |
| Jan 9 – Jan 11, 2026 (Until Sunday Midnight UTC) | 100% | Volume-weighted |
| Jan 12 – Jan 18, 2026 | 20% | Volume-weighted |
| Jan 19, 2026 – | 20% | Fee-curve weighted |

The rebate percentage is at the sole discretion of Polymarket and may change over time.

---

## [​](#which-markets-have-fees) Which Markets Have Fees?

Currently, only **15-minute crypto markets** have fees enabled. Query the fee-rate endpoint to check:

Copy

```shiki
GET https://clob.polymarket.com/fee-rate?token_id={token_id}

# Fee-enabled: { "fee_rate_bps": 1000 }
# Fee-free:    { "fee_rate_bps": 0 }
```

---

## [​](#related-documentation) Related Documentation

[## Maker Rebates Program

User-facing overview with full fee tables](/polymarket-learn/trading/maker-rebates-program)[## Create CLOB Order via REST API

Full order structure and signing documentation](/developers/CLOB/orders/create-order)

[Liquidity Rewards](/developers/market-makers/liquidity-rewards)[Data Feeds](/developers/market-makers/data-feeds)

⌘I

---


## Builder Program Introduction

> Source: https://docs.polymarket.com/developers/builders/builder-intro

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Polymarket Builders Program

Builder Program Introduction

## [​](#what-is-a-builder) What is a Builder?

A “builder” is a person, group, or organization that routes orders from their users to Polymarket.
If you’ve created a platform that allows users to trade on Polymarket via your system, this program is for you.

---

## [​](#program-benefits) Program Benefits

## Relayer Access

All onchain operations are gasless through our relayer

## Order Attribution

Get credited for orders and compete for grants on the Builder Leaderboard

## Fee Share

Earn a share of fees on routed orders

### [​](#relayer-access) Relayer Access

We expose our relayer to builders, providing gasless transactions for users with
Polymarket’s Proxy Wallets deployed via [Relayer Client](/developers/builders/relayer-client).
When transactions are routed through proxy wallets, Polymarket pays all gas fees for:

* Deploying Gnosis Safe Wallets or Custom Proxy (Magic Link users) Wallets
* Token approvals (USDC, outcome tokens)
* CTF operations (split, merge, redeem)
* Order execution (via [CLOB API](/developers/CLOB/introduction))

EOA wallets do not have relayer access. Users trading directly from an EOA pay their own gas fees.

### [​](#trading-attribution) Trading Attribution

Attach custom headers to orders to identify your builder account:

* Orders attributed to your builder account
* Compete on the [Builder Leaderboard](https://builders.polymarket.com/) for grants
* Track performance via the Data API
  + [Leaderboard API](/api-reference/builders/get-aggregated-builder-leaderboard): Get aggregated builder rankings for a time period
  + [Volume API](/api-reference/builders/get-daily-builder-volume-time-series): Get daily time-series volume data for trend analysis

---

## [​](#getting-started) Getting Started

1. **Get Builder Credentials**: Generate API keys from your [Builder Profile](/developers/builders/builder-profile)
2. **Configure Order Attribution**: Set up CLOB client to credit trades to your account ([guide](/developers/builders/order-attribution))
3. **Enable Gasless Transactions**: Use the Relayer for gas-free wallet deployment and trading ([guide](/developers/builders/relayer-client))

See [Example Apps](/developers/builders/examples) for complete Next.js reference implementations.

---

## [​](#sdks-&-libraries) SDKs & Libraries

[## CLOB Client (TypeScript)

Place orders with builder attribution](https://github.com/Polymarket/clob-client)[## CLOB Client (Python)

Place orders with builder attribution](https://github.com/Polymarket/py-clob-client)[## CLOB Client (Rust)

Place orders with builder attribution](https://github.com/Polymarket/rs-clob-client)[## Relayer Client (TypeScript)

Gasless onchain transactions for your users](https://github.com/Polymarket/builder-relayer-client)[## Relayer Client (Python)

Gasless onchain transactions for your users](https://github.com/Polymarket/py-builder-relayer-client)[## Signing SDK (TypeScript)

Sign builder authentication headers](https://github.com/Polymarket/builder-signing-sdk)[## Signing SDK (Python)

Sign builder authentication headers](https://github.com/Polymarket/py-builder-signing-sdk)

[Inventory Management](/developers/market-makers/inventory)[Builder Tiers](/developers/builders/builder-tiers)

⌘I

---


## Builder Profile & Keys

> Source: https://docs.polymarket.com/developers/builders/builder-profile

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Polymarket Builders Program

Builder Profile & Keys

## [​](#accessing-your-builder-profile) Accessing Your Builder Profile

## Direct Link

Go to [polymarket.com/settings?tab=builder](https://polymarket.com/settings?tab=builder)

## From Profile Menu

Click your profile image and Select “Builders”

---

## [​](#builder-profile-settings) Builder Profile Settings

![Builder Settings Page](https://mintcdn.com/polymarket-292d1b1b/Quu9lXyXHL-5rjVX/images/builder-profile-image.png?fit=max&auto=format&n=Quu9lXyXHL-5rjVX&q=85&s=67176050b411016e3bfea47bc6fd8fbb)

### [​](#customize-your-builder-identity) Customize Your Builder Identity

* **Profile Picture**: Upload a custom image for the [Builder Leaderboard](https://builders.polymarket.com/)
* **Builder Name**: Set the name displayed publicly on the leaderboard

### [​](#view-your-builder-information) View Your Builder Information

* **Builder Address**: Your unique builder address for identification
* **Creation Date**: When your builder account was created
* **Current Tier**: Your rate limit tier (Unverified or Verified)

---

## [​](#builder-api-keys) Builder API Keys

Builder API keys are required to access the relayer and for CLOB order attribution.

### [​](#creating-api-keys) Creating API Keys

In the **Builder Keys** section of your profile’s **Builder Settings**:

1. View existing API keys with their creation dates and status
2. Click **”+ Create New”** to generate a new API key

Each API key includes:

| Credential | Description |
| --- | --- |
| `apiKey` | Your builder API key identifier |
| `secret` | Secret key for signing requests |
| `passphrase` | Additional authentication passphrase |

### [​](#managing-api-keys) Managing API Keys

* **Multiple Keys**: Create separate keys for different environments
* **Active Status**: Keys show “ACTIVE” when operational

---

## [​](#next-steps) Next Steps

[## Order Attribution

Start attributing customer orders to your account](/developers/builders/order-attribution)[## Builder Leaderboard

View your public profile and stats](https://builders.polymarket.com/)

[Builder Tiers](/developers/builders/builder-tiers)[Order Attribution](/developers/builders/order-attribution)

⌘I

---


## Builder Tiers

> Source: https://docs.polymarket.com/developers/builders/builder-tiers

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Polymarket Builders Program

Builder Tiers

## [​](#overview) Overview

Polymarket Builders lets anyone integrate without approval.
Tiers exist to manage rate limits while rewarding high performing integrations with weekly rewards, grants, and revenue sharing opportunities. Higher tiers also unlock engineering support, marketing promotion, and priority access.

## [​](#feature-definitions) Feature Definitions

| Feature | Description |
| --- | --- |
| **Daily Relayer Txn Limit** | Maximum Relayer transactions per day for Safe/Proxy wallet operations |
| **API Rate Limits** | Rate limits for non-relayer endpoints (CLOB, Gamma, etc.) |
| **Subsidized Transactions** | Gas fees subsidized for Relayer and CLOB operations via Safe/Proxy wallets |
| **Order Attribution** | Orders tracked and attributed to your Builder profile |
| **RevShare Protocol** | Infrastructure allowing Builders to charge fees |
| **Leaderboard Visibility** | Visibility on the [Builder leaderboard](https://builders.polymarket.com/) |
| **Weekly Rewards** | Weekly USDC rewards program for visible builders based on volume |
| **Grants** | Builder grants awarded based on innovation and exclusivity |
| **Telegram Channel** | Private Builders channel for announcements and support |
| **Badge** | Verified Builder affiliate badge on your Builder profile |
| **Engineering Support** | Direct access to engineering team |
| **Marketing Support** | Promotion via official Polymarket social accounts |
| **Weekly Rewards Boost** | Multiplier on the weekly USDC rewards program for visible builders |
| **Priority Access** | Early access to new features and products |

## [​](#tier-comparison) Tier Comparison

| Feature | Unverified | Verified | Partner |
| --- | --- | --- | --- |
| **Daily Relayer Txn Limit** | 100/day | 3,000/day | Unlimited |
| **API Rate Limits** | Standard | Standard | Highest |
| **Subsidized Transactions** | ✅ | ✅ | ✅ |
| **Order Attribution** | ✅ | ✅ | ✅ |
| **RevShare Protocol** | ❌ | ✅ | ✅ |
| **Leaderboard Visibility** | ❌ | ✅ | ✅ |
| **Weekly Rewards** | ❌ | ✅ | ✅ |
| **Telegram Channel** | ❌ | ✅ | ✅ |
| **Badge** | ❌ | ✅ | ✅ |
| **Engineering Support** | ❌ | Standard | Elevated |
| **Marketing Support** | ❌ | Standard | Elevated |
| **Grants** | ❌ | ❌ | ✅ |
| **Weekly Reward Boosts** | ❌ | ❌ | ✅ |
| **Priority Access** | ❌ | ❌ | ✅ |

---

### [​](#unverified) Unverified

## 100 transactions/day

The default tier for all new builders. Create Builder API keys instantly from your Polymarket profile.

**How to get started:**

1. Go to [polymarket.com/settings?tab=builder](https://polymarket.com/settings?tab=builder)
2. Create a builder profile and click **”+ Create New”** to generate builder API keys
3. Implement [builder signing](/developers/builders/order-attribution); required for Relayer access and CLOB order attribution

**Included:**

* Gasless trading on all CLOB orders through Safe/Proxy wallets
* Gas subsidized on all Relayer transactions through Safe/Proxy wallets up to daily limit
* Order attribution credit to your Builder profile
* Access to all client libraries and documentation

---

### [​](#verified) Verified

## 3,000 transactions/day

For builders who need higher throughput. Requires manual approval by Polymarket.

**How to upgrade:**
Contact us with your Builder API Key, use case, expected volume, and relevant info (app, docs, X profile).
**Unlocks over Unverified:**

* 15x daily Relayer transaction limit
* RevShare Protocol Access
* Telegram channel
* Leaderboard visibility
* Eligible for Weekly Rewards Program
* Promotion and verified affiliate badge from @PolymarketBuild
* Grants eligibility

---

### [​](#partner) Partner

## Unlimited transactions/day

Enterprise tier for high-volume integrations and strategic partners.

**How to apply:**
Reach out to discuss partnership opportunities.
**Unlocks over Verified:**

* Unlimited Relayer transactions
* Highest API rate limits
* Elevated engineering support
* Elevated and coordinated marketing support
* Priority access to new features and products
* Multiplier on the Weekly Rewards Program

---

## [​](#contact) Contact

Ready to upgrade or have questions?

* [[email protected]](/cdn-cgi/l/email-protection#c0a2b5a9aca4a5b280b0afacb9ada1b2aba5b4eea3afad)

---

## [​](#faq) FAQ

How do I know if I'm verified?

Verification is displayed in your [Builder Profile](https://polymarket.com/settings?tab=builder) settings.

What happens if I exceed my daily limit?

Relayer requests beyond your daily limit will be rate-limited and return an error. Consider upgrading to Verified or Partner tier if you’re hitting limits.

Can I get a temporary limit increase?

For special events or product launches, contact [[email protected]](/cdn-cgi/l/email-protection#a7c5d2cecbc3c2d5e7d7c8cbdecac6d5ccc2d389c4c8ca)

---

## [​](#next-steps) Next Steps

[## Get Your Builder Keys

Create Builder API credentials to get started](/developers/builders/builder-profile)[## Use Your Builder Keys

Configure Builder API credentials to attribute orders](/developers/builders/relayer-client)

[Builder Program Introduction](/developers/builders/builder-intro)[Builder Profile & Keys](/developers/builders/builder-profile)

⌘I

---


## Order Attribution

> Source: https://docs.polymarket.com/developers/builders/order-attribution

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Polymarket Builders Program

Order Attribution

## [​](#overview) Overview

The [CLOB (Central Limit Order Book)](/developers/CLOB/introduction) is Polymarket’s order matching system. Order attribution adds builder authentication headers when placing orders through the CLOB Client, enabling Polymarket to credit trades to your builder account. This allows you to:

* Track volume on the [Builder Leaderboard](https://builders.polymarket.com/)
* Compete for grants based on trading activity
* Monitor performance via the Data API

---

## [​](#builder-api-credentials) Builder API Credentials

Each builder receives API credentials from their [Builder Profile](/developers/builders/builder-profile):

| Credential | Description |
| --- | --- |
| `key` | Your builder API key identifier |
| `secret` | Secret key for signing requests |
| `passphrase` | Additional authentication passphrase |

**Security Notice**: Your Builder API keys must be kept secure. Never expose them in client-side code.

---

## [​](#signing-methods) Signing Methods

* Remote Signing (Recommended)
* Local Signing

Remote signing keeps your credentials secure on a server you control.**How it works:**

1. User signs an order payload
2. Payload is sent to your builder signing server
3. Your server adds builder authentication headers
4. Complete order is sent to the CLOB

### [​](#server-implementation) Server Implementation

Your signing server receives request details and returns the authentication headers. Use the `buildHmacSignature` function from the SDK:

TypeScript

Python

Copy

```shiki
import { 
  buildHmacSignature, 
  BuilderApiKeyCreds 
} from "@polymarket/builder-signing-sdk";

const BUILDER_CREDENTIALS: BuilderApiKeyCreds = {
  key: process.env.POLY_BUILDER_API_KEY!,
  secret: process.env.POLY_BUILDER_SECRET!,
  passphrase: process.env.POLY_BUILDER_PASSPHRASE!,
};

// POST /sign - receives { method, path, body } from the client SDK
export async function handleSignRequest(request) {
  const { method, path, body } = await request.json();
  
  const timestamp = Date.now().toString();
  
  const signature = buildHmacSignature(
    BUILDER_CREDENTIALS.secret,
    parseInt(timestamp),
    method,
    path,
    body
  );

  return {
    POLY_BUILDER_SIGNATURE: signature,
    POLY_BUILDER_TIMESTAMP: timestamp,
    POLY_BUILDER_API_KEY: BUILDER_CREDENTIALS.key,
    POLY_BUILDER_PASSPHRASE: BUILDER_CREDENTIALS.passphrase,
  };
}
```

Never commit credentials to version control. Use environment variables or a secrets manager.

### [​](#client-configuration) Client Configuration

Point your client to your signing server:

TypeScript

Python

Copy

```shiki
import { ClobClient } from "@polymarket/clob-client";
import { BuilderConfig } from "@polymarket/builder-signing-sdk";

// Point to your signing server
const builderConfig = new BuilderConfig({
  remoteBuilderConfig: { 
    url: "https://your-server.com/sign"
  }
});

// Or with optional authorization token
const builderConfigWithAuth = new BuilderConfig({
  remoteBuilderConfig: { 
    url: "https://your-server.com/sign", 
    token: "your-auth-token" 
  }
});

const client = new ClobClient(
  "https://clob.polymarket.com",
  137,
  signer, // ethers v5.x EOA signer
  creds, // User's API Credentials
  2, // signatureType for the Safe proxy wallet
  funderAddress, // Safe proxy wallet address
  undefined, 
  false,
  builderConfig
);

// Orders automatically use the signing server
const order = await client.createOrder({
  price: 0.40,
  side: Side.BUY,
  size: 5,
  tokenID: "YOUR_TOKEN_ID"
});

const response = await client.postOrder(order);
```

### [​](#troubleshooting) Troubleshooting

Invalid Signature Errors

**Error:** Client receives invalid signature errors**Solution:**

1. Verify the request body is passed correctly as JSON
2. Check that `path`, `body`, and `method` match what the client sends
3. Ensure your server and client use the same Builder API credentials

Missing Credentials

**Error:** `Builder credentials not configured` or undefined values**Solution:** Ensure your environment variables are set:

* `POLY_BUILDER_API_KEY`
* `POLY_BUILDER_SECRET`
* `POLY_BUILDER_PASSPHRASE`

Sign orders locally when you control the entire order placement flow.**How it works:**

1. Your system creates and signs orders on behalf of users
2. Your system uses Builder API credentials locally to add headers
3. Complete signed order is sent directly to the CLOB

TypeScript

Python

Copy

```shiki
import { ClobClient } from "@polymarket/clob-client";
import { BuilderConfig, BuilderApiKeyCreds } from "@polymarket/builder-signing-sdk";

// Configure with local builder credentials
const builderCreds: BuilderApiKeyCreds = {
  key: process.env.POLY_BUILDER_API_KEY!,
  secret: process.env.POLY_BUILDER_SECRET!,
  passphrase: process.env.POLY_BUILDER_PASSPHRASE!
};

const builderConfig = new BuilderConfig({
  localBuilderCreds: builderCreds
});

const client = new ClobClient(
  "https://clob.polymarket.com",
  137,
  signer, // ethers v5.x EOA signer
  creds, // User's API Credentials
  2, // signatureType for the Safe proxy wallet
  funderAddress, // Safe proxy wallet address
  undefined, 
  false,
  builderConfig
);

// Orders automatically include builder headers
const order = await client.createOrder({
  price: 0.40,
  side: Side.BUY,
  size: 5,
  tokenID: "YOUR_TOKEN_ID"
});

const response = await client.postOrder(order);
```

Never commit credentials to version control. Use environment variables or a secrets manager.

---

## [​](#authentication-headers) Authentication Headers

The SDK automatically generates and attaches these headers to each request:

| Header | Description |
| --- | --- |
| `POLY_BUILDER_API_KEY` | Your builder API key |
| `POLY_BUILDER_TIMESTAMP` | Unix timestamp of signature creation |
| `POLY_BUILDER_PASSPHRASE` | Your builder passphrase |
| `POLY_BUILDER_SIGNATURE` | HMAC signature of the request |

With **local signing**, the SDK constructs and attaches these headers automatically. With **remote signing**, your server must return these headers (see Server Implementation above), and the SDK attaches them to the request.

---

## [​](#next-steps) Next Steps

[## Relayer Client

Learn how to configure and use the Relay Client too!](/developers/builders/relayer-client)[## CLOB Client Methods

Explore the complete CLOB client reference](/developers/CLOB/clients/methods-overview)

[Builder Profile & Keys](/developers/builders/builder-profile)[Relayer Client](/developers/builders/relayer-client)

⌘I

---


## Relayer Client

> Source: https://docs.polymarket.com/developers/builders/relayer-client

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Polymarket Builders Program

Relayer Client

## [​](#overview) Overview

The Relayer Client routes onchain transactions through Polymarket’s infrastructure, providing gasless transactions for your users. Builder authentication is required to access the relayer.

## Gasless Transactions

Polymarket pays all gas fees

## Wallet Deployment

Deploy Safe or Proxy wallets

## CTF Operations

Split, merge, and redeem positions

---

## [​](#builder-api-credentials) Builder API Credentials

Each builder receives API credentials from their [Builder Profile](/developers/builders/builder-profile):

| Credential | Description |
| --- | --- |
| `key` | Your builder API key identifier |
| `secret` | Secret key for signing requests |
| `passphrase` | Additional authentication passphrase |

**Security Notice**: Your Builder API keys must be kept secure. Never expose them in client-side code.

---

## [​](#installation) Installation

TypeScript

Python

Copy

```shiki
npm install @polymarket/builder-relayer-client
```

---

## [​](#relayer-endpoint) Relayer Endpoint

All relayer requests are sent to Polymarket’s relayer service on Polygon:

Copy

```shiki
https://relayer-v2.polymarket.com/
```

---

## [​](#signing-methods) Signing Methods

* Remote Signing (Recommended)
* Local Signing

Remote signing keeps your credentials secure on a server you control.**How it works:**

1. Client sends request details to your signing server
2. Your server generates the HMAC signature
3. Client attaches headers and sends to relayer

### [​](#server-implementation) Server Implementation

Your signing server receives request details and returns the authentication headers:

TypeScript

Python

Copy

```shiki
import { 
  buildHmacSignature, 
  BuilderApiKeyCreds 
} from "@polymarket/builder-signing-sdk";

const BUILDER_CREDENTIALS: BuilderApiKeyCreds = {
  key: process.env.POLY_BUILDER_API_KEY!,
  secret: process.env.POLY_BUILDER_SECRET!,
  passphrase: process.env.POLY_BUILDER_PASSPHRASE!,
};

// POST /sign - receives { method, path, body } from the client SDK
export async function handleSignRequest(request) {
  const { method, path, body } = await request.json();
  
  const timestamp = Date.now().toString();
  
  const signature = buildHmacSignature(
    BUILDER_CREDENTIALS.secret,
    parseInt(timestamp),
    method,
    path,
    body
  );

  return {
    POLY_BUILDER_SIGNATURE: signature,
    POLY_BUILDER_TIMESTAMP: timestamp,
    POLY_BUILDER_API_KEY: BUILDER_CREDENTIALS.key,
    POLY_BUILDER_PASSPHRASE: BUILDER_CREDENTIALS.passphrase,
  };
}
```

Never commit credentials to version control. Use environment variables or a secrets manager.

### [​](#client-configuration) Client Configuration

Point your client to your signing server:

TypeScript

Python

Copy

```shiki
import { createWalletClient, http, Hex } from "viem";
import { privateKeyToAccount } from "viem/accounts";
import { polygon } from "viem/chains";
import { RelayClient } from "@polymarket/builder-relayer-client";
import { BuilderConfig } from "@polymarket/builder-signing-sdk";

// Create wallet
const account = privateKeyToAccount(process.env.PRIVATE_KEY as Hex);
const wallet = createWalletClient({
  account,
  chain: polygon,
  transport: http(process.env.RPC_URL)
});

// Configure remote signing
const builderConfig = new BuilderConfig({
  remoteBuilderConfig: { 
    url: "https://your-server.com/sign" 
  }
});

const RELAYER_URL = "https://relayer-v2.polymarket.com/";
const CHAIN_ID = 137;

const client = new RelayClient(
  RELAYER_URL,
  CHAIN_ID,
  wallet,
  builderConfig
);
```

Sign locally when your backend handles all transactions.**How it works:**

1. Your system creates transactions on behalf of users
2. Your system uses Builder API credentials locally to add headers
3. Complete signed request is sent directly to the relayer

TypeScript

Python

Copy

```shiki
import { createWalletClient, http, Hex } from "viem";
import { privateKeyToAccount } from "viem/accounts";
import { polygon } from "viem/chains";
import { RelayClient } from "@polymarket/builder-relayer-client";
import { BuilderConfig } from "@polymarket/builder-signing-sdk";

// Create wallet
const account = privateKeyToAccount(process.env.PRIVATE_KEY as Hex);
const wallet = createWalletClient({
  account,
  chain: polygon,
  transport: http(process.env.RPC_URL)
});

// Configure local signing
const builderConfig = new BuilderConfig({
  localBuilderCreds: {
    key: process.env.POLY_BUILDER_API_KEY!,
    secret: process.env.POLY_BUILDER_SECRET!,
    passphrase: process.env.POLY_BUILDER_PASSPHRASE!
  }
});

const RELAYER_URL = "https://relayer-v2.polymarket.com/";
const CHAIN_ID = 137;

const client = new RelayClient(
  RELAYER_URL,
  CHAIN_ID,
  wallet,
  builderConfig
);
```

Never commit credentials to version control. Use environment variables or a secrets manager.

---

## [​](#authentication-headers) Authentication Headers

The SDK automatically generates and attaches these headers to each request:

| Header | Description |
| --- | --- |
| `POLY_BUILDER_API_KEY` | Your builder API key |
| `POLY_BUILDER_TIMESTAMP` | Unix timestamp of signature creation |
| `POLY_BUILDER_PASSPHRASE` | Your builder passphrase |
| `POLY_BUILDER_SIGNATURE` | HMAC signature of the request |

With **local signing**, the SDK constructs and attaches these headers automatically. With **remote signing**, your server must return these headers (see Server Implementation above), and the SDK attaches them to the request.

---

## [​](#wallet-types) Wallet Types

Choose your wallet type before using the relayer:

* Safe Wallets
* Proxy Wallets

Gnosis Safe-based proxy wallets that require explicit deployment before use.

* **Best for:** Most builder integrations
* **Deployment:** Call `client.deploy()` before first transaction
* **Gas fees:** Paid by Polymarket

TypeScript

Python

Copy

```shiki
const client = new RelayClient(
  "https://relayer-v2.polymarket.com", 
  137,
  eoaSigner, 
  builderConfig, 
  RelayerTxType.SAFE  // Default
);

// Deploy before first use
const response = await client.deploy();
const result = await response.wait();
console.log("Safe Address:", result?.proxyAddress);
```

Custom Polymarket proxy wallets that auto-deploy on first transaction.

* **Used for:** Magic Link users from Polymarket.com
* **Deployment:** Automatic on first transaction
* **Gas fees:** Paid by Polymarket

TypeScript

Python

Copy

```shiki
const client = new RelayClient(
  "https://relayer-v2.polymarket.com", 
  137,
  eoaSigner, 
  builderConfig, 
  RelayerTxType.PROXY
);

// No deploy() needed - auto-deploys on first tx
await client.execute([transaction], "First transaction");
```

Wallet Comparison Table

| Feature | Safe Wallets | Proxy Wallets |
| --- | --- | --- |
| Deployment | Explicit `deploy()` | Auto-deploy on first tx |
| Gas Fees | Polymarket pays | Polymarket pays |
| ERC20 Approvals | ✅ | ✅ |
| CTF Operations | ✅ | ✅ |
| Send Transactions | ✅ | ✅ |

---

## [​](#usage) Usage

### [​](#deploy-a-wallet) Deploy a Wallet

For Safe wallets, deploy before executing transactions:

TypeScript

Python

Copy

```shiki
const response = await client.deploy();
const result = await response.wait();

if (result) {
  console.log("Safe deployed successfully!");
  console.log("Transaction Hash:", result.transactionHash);
  console.log("Safe Address:", result.proxyAddress);
}
```

### [​](#execute-transactions) Execute Transactions

The `execute` method sends transactions through the relayer. Pass an array of transactions to batch multiple operations in a single call.

TypeScript

Python

Copy

```shiki
interface Transaction {
  to: string;    // Target contract or wallet address
  data: string;  // Encoded function call (use "0x" for simple transfers)
  value: string; // Amount of MATIC to send (usually "0")
}

const response = await client.execute(transactions, "Description");
const result = await response.wait();

if (result) {
  console.log("Transaction confirmed:", result.transactionHash);
}
```

### [​](#transaction-examples) Transaction Examples

* Transfer
* Approve
* Redeem Positions
* Split Positions
* Merge Positions
* Batch Transactions

Transfer tokens to any address (e.g., withdrawals):

TypeScript

Python

Copy

```shiki
import { encodeFunctionData, parseUnits } from "viem";

const transferTx = {
  to: "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174", // USDCe
  data: encodeFunctionData({
    abi: [{
      name: "transfer",
      type: "function",
      inputs: [
        { name: "to", type: "address" },
        { name: "amount", type: "uint256" }
      ],
      outputs: [{ type: "bool" }]
    }],
    functionName: "transfer",
    args: [
      "0xRecipientAddressHere",
      parseUnits("100", 6) // 100 USDCe (6 decimals)
    ]
  }),
  value: "0"
};

const response = await client.execute([transferTx], "Transfer USDCe");
await response.wait();
```

Set token allowances to enable trading:

TypeScript

Python

Copy

```shiki
import { encodeFunctionData, maxUint256 } from "viem";

const approveTx = {
  to: "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174", // USDCe
  data: encodeFunctionData({
    abi: [{
      name: "approve",
      type: "function",
      inputs: [
        { name: "spender", type: "address" },
        { name: "amount", type: "uint256" }
      ],
      outputs: [{ type: "bool" }]
    }],
    functionName: "approve",
    args: [
      "0x4d97dcd97ec945f40cf65f87097ace5ea0476045", // CTF
      maxUint256
    ]
  }),
  value: "0"
};

const response = await client.execute([approveTx], "Approve USDCe for CTF");
await response.wait();
```

Redeem winning conditional tokens after market resolution:

TypeScript

Python

Copy

```shiki
import { encodeFunctionData } from "viem";

const redeemTx = {
  to: ctfAddress,
  data: encodeFunctionData({
    abi: [{
      name: "redeemPositions",
      type: "function",
      inputs: [
        { name: "collateralToken", type: "address" },
        { name: "parentCollectionId", type: "bytes32" },
        { name: "conditionId", type: "bytes32" },
        { name: "indexSets", type: "uint256[]" }
      ],
      outputs: []
    }],
    functionName: "redeemPositions",
    args: [collateralToken, parentCollectionId, conditionId, indexSets]
  }),
  value: "0"
};

const response = await client.execute([redeemTx], "Redeem positions");
await response.wait();
```

Split collateral tokens into conditional outcome tokens:

TypeScript

Python

Copy

```shiki
import { encodeFunctionData } from "viem";

const splitTx = {
  to: ctfAddress,
  data: encodeFunctionData({
    abi: [{
      name: "splitPosition",
      type: "function",
      inputs: [
        { name: "collateralToken", type: "address" },
        { name: "parentCollectionId", type: "bytes32" },
        { name: "conditionId", type: "bytes32" },
        { name: "partition", type: "uint256[]" },
        { name: "amount", type: "uint256" }
      ],
      outputs: []
    }],
    functionName: "splitPosition",
    args: [collateralToken, parentCollectionId, conditionId, partition, amount]
  }),
  value: "0"
};

const response = await client.execute([splitTx], "Split positions");
await response.wait();
```

Merge conditional tokens back into collateral:

TypeScript

Python

Copy

```shiki
import { encodeFunctionData } from "viem";

const mergeTx = {
  to: ctfAddress,
  data: encodeFunctionData({
    abi: [{
      name: "mergePositions",
      type: "function",
      inputs: [
        { name: "collateralToken", type: "address" },
        { name: "parentCollectionId", type: "bytes32" },
        { name: "conditionId", type: "bytes32" },
        { name: "partition", type: "uint256[]" },
        { name: "amount", type: "uint256" }
      ],
      outputs: []
    }],
    functionName: "mergePositions",
    args: [collateralToken, parentCollectionId, conditionId, partition, amount]
  }),
  value: "0"
};

const response = await client.execute([mergeTx], "Merge positions");
await response.wait();
```

Execute multiple transactions atomically in a single call:

TypeScript

Python

Copy

```shiki
import { encodeFunctionData, parseUnits, maxUint256 } from "viem";

const erc20Abi = [
  {
    name: "approve",
    type: "function",
    inputs: [
      { name: "spender", type: "address" },
      { name: "amount", type: "uint256" }
    ],
    outputs: [{ type: "bool" }]
  },
  {
    name: "transfer",
    type: "function",
    inputs: [
      { name: "to", type: "address" },
      { name: "amount", type: "uint256" }
    ],
    outputs: [{ type: "bool" }]
  }
] as const;

// Approve CTF to spend USDCe
const approveTx = {
  to: "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
  data: encodeFunctionData({
    abi: erc20Abi,
    functionName: "approve",
    args: ["0x4d97dcd97ec945f40cf65f87097ace5ea0476045", maxUint256]
  }),
  value: "0"
};

// Transfer some USDCe to another wallet
const transferTx = {
  to: "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
  data: encodeFunctionData({
    abi: erc20Abi,
    functionName: "transfer",
    args: ["0xRecipientAddressHere", parseUnits("50", 6)]
  }),
  value: "0"
};

// Both transactions execute in one call
const response = await client.execute(
  [approveTx, transferTx], 
  "Approve and transfer"
);
await response.wait();
```

Batching reduces latency and ensures all transactions succeed or fail together.

---

## [​](#reference) Reference

### [​](#contracts-&-approvals) Contracts & Approvals

| Contract | Address | USDCe | Outcome Tokens |
| --- | --- | --- | --- |
| USDCe | `0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174` | — | — |
| CTF | `0x4d97dcd97ec945f40cf65f87097ace5ea0476045` | ✅ | — |
| CTF Exchange | `0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E` | ✅ | ✅ |
| Neg Risk CTF Exchange | `0xC5d563A36AE78145C45a50134d48A1215220f80a` | ✅ | ✅ |
| Neg Risk Adapter | `0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296` | — | ✅ |

### [​](#transaction-states) Transaction States

| State | Description |
| --- | --- |
| `STATE_NEW` | Transaction received by relayer |
| `STATE_EXECUTED` | Transaction executed onchain |
| `STATE_MINED` | Transaction included in a block |
| `STATE_CONFIRMED` | Transaction confirmed (final ✅) |
| `STATE_FAILED` | Transaction failed (terminal ❌) |
| `STATE_INVALID` | Transaction rejected as invalid (terminal ❌) |

### [​](#typescript-types) TypeScript Types

View Type Definitions

Copy

```shiki
// Transaction type used in all examples
interface Transaction {
  to: string;
  data: string;
  value: string;
}

// Wallet type selector
enum RelayerTxType {
  SAFE = "SAFE",
  PROXY = "PROXY"
}

// Transaction states
enum RelayerTransactionState {
  STATE_NEW = "STATE_NEW",
  STATE_EXECUTED = "STATE_EXECUTED",
  STATE_MINED = "STATE_MINED",
  STATE_CONFIRMED = "STATE_CONFIRMED",
  STATE_FAILED = "STATE_FAILED",
  STATE_INVALID = "STATE_INVALID"
}

// Response from relayer
interface RelayerTransaction {
  transactionID: string;
  transactionHash: string;
  from: string;
  to: string;
  proxyAddress: string;
  data: string;
  state: string;
  type: string;
  metadata: string;
  createdAt: Date;
  updatedAt: Date;
}
```

---

## [​](#next-steps) Next Steps

[## Order Attribution

Attribute orders to your builder account](/developers/builders/order-attribution)[## Example Apps

Complete integration examples](/developers/builders/examples)

[Order Attribution](/developers/builders/order-attribution)[Examples](/developers/builders/examples)

⌘I

---


## Builder Examples

> Source: https://docs.polymarket.com/developers/builders/examples

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Polymarket Builders Program

Examples

## [​](#overview) Overview

These open-source demo applications show how to integrate Polymarket’s CLOB Client and Builder Relayer Client for gasless trading with builder order attribution.

## Authentication

Multiple wallet providers

## Gasless Trading

Safe & Proxy wallet support

## Full Integration

Orders, positions, CTF ops

---

## [​](#safe-wallet-examples) Safe Wallet Examples

Deploy Gnosis Safe wallets for your users:

[## wagmi + Safe

MetaMask, Phantom, Rabby, and other browser wallets](https://github.com/Polymarket/wagmi-safe-builder-example)[## Privy + Safe

Privy embedded wallets](https://github.com/Polymarket/privy-safe-builder-example)[## Magic Link + Safe

Magic Link email/social authentication](https://github.com/Polymarket/magic-safe-builder-example)[## Turnkey + Safe

Turnkey embedded wallets](https://github.com/Polymarket/turnkey-safe-builder-example)

## [​](#proxy-wallet-examples) Proxy Wallet Examples

For existing Magic Link users from Polymarket.com:

[## Magic Link + Proxy

Auto-deploying proxy wallets for Polymarket.com Magic users](https://github.com/Polymarket/magic-proxy-builder-example)

---

## [​](#what-each-demo-covers) What Each Demo Covers

* Authentication
* Wallet Operations
* Trading

* User sign-in via wallet provider
* User API credential derivation (L2 auth)
* Builder config with remote signing
* Signature types for Safe vs Proxy wallets

* Safe wallet deployment via Relayer
* Batch token approvals (USDC.e + outcome tokens)
* CTF operations (split, merge, redeem)
* Transaction monitoring

* CLOB client initialization
* Order placement with builder attribution
* Position and order management
* Market discovery via Gamma API

[Relayer Client](/developers/builders/relayer-client)[Blockchain Data Resources](/developers/builders/blockchain-data-resources)

⌘I

---


## Blockchain Data Resources

> Source: https://docs.polymarket.com/developers/builders/blockchain-data-resources

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Polymarket Builders Program

Blockchain Data Resources

Polymarket data that lands on the blockchain, such as trades, balances, positions, and redeems, is available through various on-chain analytics platforms and blockchain data providers. Polymarket also provides its own APIs and WebSockets. See the [API Endpoints reference](/quickstart/reference/endpoints) for more information.
The purpose of this page is to serve as a public good for Polymarket builders, researches, and analysts alike.

---

## [​](#data) Data

### [​](#goldsky) Goldsky

[Goldsky](https://docs.goldsky.com/chains/polymarket) provides real-time streaming pipelines for Polymarket on-chain activity (i.e. trades, balances, positions, etc…) into your own database/data warehouse.
Goldsky also partnered with [ClickHouse](https://clickhouse.com) to create [CryptoHouse](https://crypto.clickhouse.com), where you can query Polymarket on-chain data using SQL.

### [​](#dune) Dune

[Dune](https://dune.com) is a blockchain analytics platform that has Polymarket on-chain activity (i.e. trades, balances, positions, etc…). Query Polymarket data using SQL, create custom dashboards, and more.
Here are a few simple queries to get started:

| Query | Description | Link |
| --- | --- | --- |
| Volume | Notional Volume and Maker & Taker USDC Volume | [View Dune Query](https://dune.com/queries/6545441) |
| TVL | USDC locked in Polymarket smart contracts | [View Dune Query](https://dune.com/queries/6588784) |
| Open Interest | Estimated market open interest, and over time | [View Dune Query](https://dune.com/queries/6555478) |

### [​](#allium) Allium

[Allium](https://docs.allium.so/historical-data/predictions) is a blockchain analytics platform that has Polymarket on-chain activity (i.e. trades, balances, positions, etc…). Query Polymarket data using SQL, create custom dashboards, and more.
—

## [​](#dashboards) Dashboards

Third-party blockchain analytics platforms that aggregate and visualize Polymarket data:

[![7s2FxV2K_400x400](https://pbs.twimg.com/profile_images/1651677302634483712/7s2FxV2K_400x400.jpg)

## Blockworks](https://blockworks.com/analytics/polymarket)[![2XeO9mPb_400x400](https://pbs.twimg.com/profile_images/1896982195723546624/2XeO9mPb_400x400.png)

## Artemis](https://app.artemisanalytics.com/asset/polymarket?from=assets)[![qq80s3hx_400x400](https://pbs.twimg.com/profile_images/1986458079248986112/qq80s3hx_400x400.jpg)

## Dune](https://dune.com/discover/content/popular?q=polymarket&resource-type=dashboards)[![rAeLzZqs_400x400](https://pbs.twimg.com/profile_images/1915756547705036800/rAeLzZqs_400x400.jpg)

## DeFiLlama](https://defillama.com/protocol/polymarket)[![9babG7Df_400x400](https://pbs.twimg.com/profile_images/1944749695525425152/9babG7Df_400x400.jpg)

## The Block](https://www.theblock.co/data/decentralized-finance/prediction-markets-and-betting)[![SMum_RcQ_400x400](https://pbs.twimg.com/profile_images/1594678659222306817/SMum_RcQ_400x400.jpg)

## Token Terminal](https://tokenterminal.com/explorer/projects/polymarket)[![UEwR3lHt_400x400](https://pbs.twimg.com/profile_images/1778926940407132160/UEwR3lHt_400x400.jpg)

## Allium](https://predictions.allium.so)

### [​](#community-dashboards) Community Dashboards

Community-created Dune dashboards of Polymarket on-chain analytics:

| Dashboard | Created By | Link |
| --- | --- | --- |
| Polymarket Overview | [@datadashboards](https://x.com/datadashboards) | [View Dashboard](https://dune.com/datadashboards/polymarket-overview) |
| Polymarket Volume, OI, Markets, Addresses and TVL | [@hildobby](https://x.com/hildobby) | [View Dashboard](https://dune.com/hildobby/polymarket) |
| Polymarket Historical Accuracy | [@alexmccullaaa](https://x.com/alexmccullaaa) | [View Dashboard](https://dune.com/alexmccullough/how-accurate-is-polymarket) |
| Polymarket Builders Dashboard | [@defioasis](https://x.com/defioasis) | [View Dashboard](https://dune.com/gateresearch/pmbuilders) |

[Examples](/developers/builders/examples)[CLOB Introduction](/developers/CLOB/introduction)

⌘I

---


## RTDS Overview

> Source: https://docs.polymarket.com/developers/RTDS/RTDS-overview

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Real Time Data Stream

Real Time Data Socket

## [​](#overview) Overview

The Polymarket Real-Time Data Socket (RTDS) is a WebSocket-based streaming service that provides real-time updates for **comments** and **crypto prices**.
[## TypeScript client

Official RTDS TypeScript client (`real-time-data-client`).](https://github.com/Polymarket/real-time-data-client)

### [​](#connection-details) Connection Details

* **WebSocket URL**: `wss://ws-live-data.polymarket.com`
* **Protocol**: WebSocket
* **Data Format**: JSON

### [​](#authentication) Authentication

Some user-specific streams may require `gamma_auth`:

* `address`: User wallet address

### [​](#connection-management) Connection Management

The WebSocket connection supports:

* **Dynamic Subscriptions**: Without disconnecting from the socket users can add, remove and modify topics and filters they are subscribed to.
* **Ping/Pong**: You should send PING messages (every 5 seconds ideally) to maintain connection

## [​](#available-subscription-types) Available Subscription Types

Only the subscription types documented below are supported.

The RTDS currently supports the following subscription types:

1. **[Crypto Prices](/developers/RTDS/RTDS-crypto-prices)** - Real-time cryptocurrency price updates
2. **[Comments](/developers/RTDS/RTDS-comments)** - Comment-related events including reactions

## [​](#message-structure) Message Structure

All messages received from the WebSocket follow this structure:

Copy

```shiki
{
  "topic": "string",
  "type": "string", 
  "timestamp": "number",
  "payload": "object"
}
```

* `topic`: The subscription topic (e.g., “crypto\_prices”, “comments”)
* `type`: The message type/event (e.g., “update”, “reaction\_created”)
* `timestamp`: Unix timestamp in milliseconds
* `payload`: Event-specific data object

## [​](#subscription-management) Subscription Management

### [​](#subscribe-to-topics) Subscribe to Topics

To subscribe to data streams, send a JSON message with this structure:

Copy

```shiki
{
  "action": "subscribe",
  "subscriptions": [
    {
      "topic": "topic_name",
      "type": "message_type",
      "filters": "optional_filter_string",
      "gamma_auth": {
        "address": "wallet_address"
      }
    }
  ]
}
```

### [​](#unsubscribe-from-topics) Unsubscribe from Topics

To unsubscribe from data streams, send a similar message with `"action": "unsubscribe"`.

## [​](#error-handling) Error Handling

* Connection errors will trigger automatic reconnection attempts
* Invalid subscription messages may result in connection closure
* Authentication failures will prevent successful subscription to protected topics

[Quickstart](/developers/sports-websocket/quickstart)[RTDS Crypto Prices](/developers/RTDS/RTDS-crypto-prices)

⌘I

---


## RTDS Comments

> Source: https://docs.polymarket.com/developers/RTDS/RTDS-comments

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Real Time Data Stream

RTDS Comments

[## TypeScript client

Official RTDS TypeScript client (`real-time-data-client`).](https://github.com/Polymarket/real-time-data-client)

## [​](#overview) Overview

The comments subscription provides real-time updates for comment-related events on the Polymarket platform. This includes new comments being created, as well as other comment interactions like reactions and replies.

## [​](#subscription-details) Subscription Details

* **Topic**: `comments`
* **Type**: `comment_created` (and potentially other comment event types like `reaction_created`)
* **Authentication**: May require Gamma authentication for user-specific data
* **Filters**: Optional (can filter by specific comment IDs, users, or events)

## [​](#subscription-message) Subscription Message

Copy

```shiki
{
  "action": "subscribe",
  "subscriptions": [
    {
      "topic": "comments", 
      "type": "comment_created"
    }
  ]
}
```

## [​](#message-format) Message Format

When subscribed to comments, you’ll receive messages with the following structure:

Copy

```shiki
{
  "topic": "comments",
  "type": "comment_created",
  "timestamp": 1753454975808,
  "payload": {
    "body": "do you know what the term encircle means? it means to surround from all sides, Russia has present on only 1 side, that's the opposite of an encirclement",
    "createdAt": "2025-07-25T14:49:35.801298Z",
    "id": "1763355",
    "parentCommentID": "1763325",
    "parentEntityID": 18396,
    "parentEntityType": "Event",
    "profile": {
      "baseAddress": "0xce533188d53a16ed580fd5121dedf166d3482677",
      "displayUsernamePublic": true,
      "name": "salted.caramel",
      "proxyWallet": "0x4ca749dcfa93c87e5ee23e2d21ff4422c7a4c1ee",
      "pseudonym": "Adored-Disparity"
    },
    "reactionCount": 0,
    "replyAddress": "0x0bda5d16f76cd1d3485bcc7a44bc6fa7db004cdd",
    "reportCount": 0,
    "userAddress": "0xce533188d53a16ed580fd5121dedf166d3482677"
  }
}
```

## [​](#message-types) Message Types

### [​](#comment_created) comment\_created

Triggered when a user creates a new comment on an event or in reply to another comment.

### [​](#comment_removed) comment\_removed

Triggered when a comment is removed or deleted.

### [​](#reaction_created) reaction\_created

Triggered when a user adds a reaction to an existing comment.

### [​](#reaction_removed) reaction\_removed

Triggered when a reaction is removed from a comment.

## [​](#payload-fields) Payload Fields

| Field | Type | Description |
| --- | --- | --- |
| `body` | string | The text content of the comment |
| `createdAt` | string | ISO 8601 timestamp when the comment was created |
| `id` | string | Unique identifier for this comment |
| `parentCommentID` | string | ID of the parent comment if this is a reply (null for top-level comments) |
| `parentEntityID` | number | ID of the parent entity (event, market, etc.) |
| `parentEntityType` | string | Type of parent entity (e.g., “Event”, “Market”) |
| `profile` | object | Profile information of the user who created the comment |
| `reactionCount` | number | Current number of reactions on this comment |
| `replyAddress` | string | Polygon address for replies (may be different from userAddress) |
| `reportCount` | number | Current number of reports on this comment |
| `userAddress` | string | Polygon address of the user who created the comment |

### [​](#profile-object-fields) Profile Object Fields

| Field | Type | Description |
| --- | --- | --- |
| `baseAddress` | string | User profile address |
| `displayUsernamePublic` | boolean | Whether the username should be displayed publicly |
| `name` | string | User’s display name |
| `proxyWallet` | string | Proxy wallet address used for transactions |
| `pseudonym` | string | Generated pseudonym for the user |

## [​](#parent-entity-types) Parent Entity Types

The following parent entity types are supported:

* `Event` - Comments on prediction events
* `Market` - Comments on specific markets
* Additional entity types may be available

## [​](#example-messages) Example Messages

### [​](#new-comment-created) New Comment Created

Copy

```shiki
{
  "topic": "comments",
  "type": "comment_created",
  "timestamp": 1753454975808,
  "payload": {
    "body": "do you know what the term encircle means? it means to surround from all sides, Russia has present on only 1 side, that's the opposite of an encirclement",
    "createdAt": "2025-07-25T14:49:35.801298Z",
    "id": "1763355",
    "parentCommentID": "1763325",
    "parentEntityID": 18396,
    "parentEntityType": "Event",
    "profile": {
      "baseAddress": "0xce533188d53a16ed580fd5121dedf166d3482677",
      "displayUsernamePublic": true,
      "name": "salted.caramel",
      "proxyWallet": "0x4ca749dcfa93c87e5ee23e2d21ff4422c7a4c1ee",
      "pseudonym": "Adored-Disparity"
    },
    "reactionCount": 0,
    "replyAddress": "0x0bda5d16f76cd1d3485bcc7a44bc6fa7db004cdd",
    "reportCount": 0,
    "userAddress": "0xce533188d53a16ed580fd5121dedf166d3482677"
  }
}
```

### [​](#reply-to-existing-comment) Reply to Existing Comment

Copy

```shiki
{
  "topic": "comments",
  "type": "comment_created",
  "timestamp": 1753454985123,
  "payload": {
    "body": "That's a good point about the definition of encirclement.",
    "createdAt": "2025-07-25T14:49:45.120000Z",
    "id": "1763356",
    "parentCommentID": "1763355",
    "parentEntityID": 18396,
    "parentEntityType": "Event",
    "profile": {
      "baseAddress": "0x1234567890abcdef1234567890abcdef12345678",
      "displayUsernamePublic": true,
      "name": "trader",
      "proxyWallet": "0x9876543210fedcba9876543210fedcba98765432",
      "pseudonym": "Bright-Analysis"
    },
    "reactionCount": 0,
    "replyAddress": "0x0bda5d16f76cd1d3485bcc7a44bc6fa7db004cdd",
    "reportCount": 0,
    "userAddress": "0x1234567890abcdef1234567890abcdef12345678"
  }
}
```

## [​](#comment-hierarchy) Comment Hierarchy

Comments support nested threading:

* **Top-level comments**: `parentCommentID` is null or empty
* **Reply comments**: `parentCommentID` contains the ID of the parent comment
* All comments are associated with a `parentEntityID` and `parentEntityType`

## [​](#use-cases) Use Cases

* Real-time comment feed displays
* Discussion thread monitoring
* Community sentiment analysis

## [​](#content) Content

* Comments include `reactionCount` and `reportCount`
* Comment body contains the full text content

## [​](#notes) Notes

* The `createdAt` timestamp uses ISO 8601 format with timezone information
* The outer `timestamp` field represents when the WebSocket message was sent
* User profiles include both primary addresses and proxy wallet addresses

[RTDS Crypto Prices](/developers/RTDS/RTDS-crypto-prices)[Overview](/developers/gamma-markets-api/overview)

⌘I

---


## RTDS Crypto Prices

> Source: https://docs.polymarket.com/developers/RTDS/RTDS-crypto-prices

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Real Time Data Stream

RTDS Crypto Prices

[## TypeScript client

Official RTDS TypeScript client (`real-time-data-client`).](https://github.com/Polymarket/real-time-data-client)

## [​](#overview) Overview

The crypto prices subscription provides real-time updates for cryptocurrency price data from two different sources:

* **Binance Source** (`crypto_prices`): Real-time price data from Binance exchange
* **Chainlink Source** (`crypto_prices_chainlink`): Price data from Chainlink oracle networks

Both streams deliver current market prices for various cryptocurrency trading pairs, but use different symbol formats and subscription structures.

## [​](#binance-source-crypto_prices) Binance Source (`crypto_prices`)

### [​](#subscription-details) Subscription Details

* **Topic**: `crypto_prices`
* **Type**: `update`
* **Authentication**: Not required
* **Filters**: Optional (specific symbols can be filtered)
* **Symbol Format**: Lowercase concatenated pairs (e.g., `solusdt`, `btcusdt`)

### [​](#subscription-message) Subscription Message

Copy

```shiki
{
  "action": "subscribe",
  "subscriptions": [
    {
      "topic": "crypto_prices",
      "type": "update"
    }
  ]
}
```

### [​](#with-symbol-filter) With Symbol Filter

To subscribe to specific cryptocurrency symbols, include a filters parameter:

Copy

```shiki
{
  "action": "subscribe", 
  "subscriptions": [
    {
      "topic": "crypto_prices",
      "type": "update",
      "filters": "solusdt,btcusdt,ethusdt"
    }
  ]
}
```

## [​](#chainlink-source-crypto_prices_chainlink) Chainlink Source (`crypto_prices_chainlink`)

**Trading 15m Crypto Markets?** Get a sponsored Chainlink API key with onboarding support from Chainlink. Fill out [this form](https://pm-ds-request.streams.chain.link/).

### [​](#subscription-details-2) Subscription Details

* **Topic**: `crypto_prices_chainlink`
* **Type**: `*` (all types)
* **Authentication**: Not required
* **Filters**: Optional (JSON object with symbol specification)
* **Symbol Format**: Slash-separated pairs (e.g., `eth/usd`, `btc/usd`)

### [​](#subscription-message-2) Subscription Message

Copy

```shiki
{
  "action": "subscribe",
  "subscriptions": [
    {
      "topic": "crypto_prices_chainlink",
      "type": "*",
      "filters": ""
    }
  ]
}
```

### [​](#with-symbol-filter-2) With Symbol Filter

To subscribe to specific cryptocurrency symbols, include a JSON filters parameter:

Copy

```shiki
{
  "action": "subscribe",
  "subscriptions": [
    {
      "topic": "crypto_prices_chainlink",
      "type": "*",
      "filters": "{\"symbol\":\"eth/usd\"}"
    }
  ]
}
```

## [​](#message-format) Message Format

### [​](#binance-source-message-format) Binance Source Message Format

When subscribed to Binance crypto prices (`crypto_prices`), you’ll receive messages with the following structure:

Copy

```shiki
{
  "topic": "crypto_prices",
  "type": "update", 
  "timestamp": 1753314064237,
  "payload": {
    "symbol": "solusdt",
    "timestamp": 1753314064213,
    "value": 189.55
  }
}
```

### [​](#chainlink-source-message-format) Chainlink Source Message Format

When subscribed to Chainlink crypto prices (`crypto_prices_chainlink`), you’ll receive messages with the following structure:

Copy

```shiki
{
  "topic": "crypto_prices_chainlink",
  "type": "update", 
  "timestamp": 1753314064237,
  "payload": {
    "symbol": "eth/usd",
    "timestamp": 1753314064213,
    "value": 3456.78
  }
}
```

## [​](#payload-fields) Payload Fields

| Field | Type | Description |
| --- | --- | --- |
| `symbol` | string | Trading pair symbol **Binance**: lowercase concatenated (e.g., “solusdt”, “btcusdt”) **Chainlink**: slash-separated (e.g., “eth/usd”, “btc/usd”) |
| `timestamp` | number | Price timestamp in Unix milliseconds |
| `value` | number | Current price value in the quote currency |

## [​](#example-messages) Example Messages

### [​](#binance-source-examples) Binance Source Examples

#### [​](#solana-price-update-binance) Solana Price Update (Binance)

Copy

```shiki
{
  "topic": "crypto_prices",
  "type": "update",
  "timestamp": 1753314064237,
  "payload": {
    "symbol": "solusdt", 
    "timestamp": 1753314064213,
    "value": 189.55
  }
}
```

#### [​](#bitcoin-price-update-binance) Bitcoin Price Update (Binance)

Copy

```shiki
{
  "topic": "crypto_prices",
  "type": "update", 
  "timestamp": 1753314088421,
  "payload": {
    "symbol": "btcusdt",
    "timestamp": 1753314088395,
    "value": 67234.50
  }
}
```

### [​](#chainlink-source-examples) Chainlink Source Examples

#### [​](#ethereum-price-update-chainlink) Ethereum Price Update (Chainlink)

Copy

```shiki
{
  "topic": "crypto_prices_chainlink",
  "type": "update",
  "timestamp": 1753314064237,
  "payload": {
    "symbol": "eth/usd", 
    "timestamp": 1753314064213,
    "value": 3456.78
  }
}
```

#### [​](#bitcoin-price-update-chainlink) Bitcoin Price Update (Chainlink)

Copy

```shiki
{
  "topic": "crypto_prices_chainlink",
  "type": "update", 
  "timestamp": 1753314088421,
  "payload": {
    "symbol": "btc/usd",
    "timestamp": 1753314088395,
    "value": 67234.50
  }
}
```

## [​](#supported-symbols) Supported Symbols

### [​](#binance-source-symbols) Binance Source Symbols

The Binance source supports various cryptocurrency trading pairs using lowercase concatenated format:

* `btcusdt` - Bitcoin to USDT
* `ethusdt` - Ethereum to USDT
* `solusdt` - Solana to USDT
* `xrpusdt` - XRP to USDT

### [​](#chainlink-source-symbols) Chainlink Source Symbols

The Chainlink source supports cryptocurrency trading pairs using slash-separated format:

* `btc/usd` - Bitcoin to USD
* `eth/usd` - Ethereum to USD
* `sol/usd` - Solana to USD
* `xrp/usd` - XRP to USD

## [​](#notes) Notes

### [​](#general) General

* Price updates are sent as market prices change
* The timestamp in the payload represents when the price was recorded
* The outer timestamp represents when the message was sent via WebSocket
* No authentication is required for crypto price data

[RTDS Overview](/developers/RTDS/RTDS-overview)[RTDS Comments](/developers/RTDS/RTDS-comments)

⌘I

---


## Sports WS Overview

> Source: https://docs.polymarket.com/developers/sports-websocket/overview

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Sports Websocket

Overview

The Polymarket Sports WebSocket API provides real-time sports results updates. Clients connect to receive live match data including scores, periods, and game status as events happen.
**Endpoint:**

Copy

```shiki
wss://sports-api.polymarket.com/ws
```

No authentication is required. This is a public broadcast channel that streams updates for all active sports events.

## [​](#how-it-works) How It Works

Once connected, clients automatically receive JSON messages whenever a sports event updates. There is no subscription message required—simply connect and start receiving data.

---

## [​](#connection-management) Connection Management

### [​](#automatic-ping/pong-heartbeat) Automatic Ping/Pong Heartbeat

The server sends PING messages at regular intervals. Clients **must** respond with PONG to maintain the connection.

| Parameter | Default | Description |
| --- | --- | --- |
| PING Interval | 5 seconds | How often the server sends PING messages |
| PONG Timeout | 10 seconds | How long the server waits for a PONG response |

If your client doesn’t respond to PING within 10 seconds, the connection will be closed automatically.

### [​](#connection-health) Connection Health

* Server sends `PING` → Client must respond with `PONG`
* No response within timeout → Connection terminated
* Clients should implement automatic reconnection with exponential backoff

---

## [​](#session-affinity) Session Affinity

The server uses cookie-based session affinity (`sports-results` cookie) to ensure clients maintain connection to the same backend instance. This is handled automatically by the browser.

---

## [​](#next-steps) Next Steps

[## Message Format

Understand the structure of sports update messages](/developers/sports-websocket/message-format)[## Quickstart

Implementation examples in JavaScript and TypeScript](/developers/sports-websocket/quickstart)

[Market Channel](/developers/CLOB/websocket/market-channel)[Message Format](/developers/sports-websocket/message-format)

⌘I

---


## Sports WS Quickstart

> Source: https://docs.polymarket.com/developers/sports-websocket/quickstart

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Sports Websocket

Quickstart

Connect to the Sports WebSocket to receive real-time sports results. No authentication required—just connect and handle incoming messages.

## [​](#endpoint) Endpoint

Copy

```shiki
wss://sports-api.polymarket.com/ws
```

---

## [​](#javascript-example) JavaScript Example

JavaScript

React Hook

Copy

```shiki
const ws = new WebSocket('wss://sports-api.polymarket.com/ws');

ws.onopen = () => {
  console.log('Connected to Sports WebSocket');
};

ws.onmessage = (event) => {
  // Respond to server PING
  if (event.data === 'ping') {
    ws.send('pong');
    return;
  }

  // Parse and handle sports updates
  const data = JSON.parse(event.data);
  console.log('Update:', data.slug, data.score, data.period);
};

ws.onclose = () => {
  console.log('Disconnected');
  // Reconnect after 1 second
  setTimeout(() => location.reload(), 1000);
};

ws.onerror = (error) => {
  console.error('WebSocket error:', error);
};
```

---

## [​](#critical-ping/pong-handling) Critical: PING/PONG Handling

The server sends PING messages every 5 seconds. Your client **must** respond with PONG to stay connected.

Copy

```shiki
// CORRECT - Handle PING messages
ws.onmessage = (event) => {
  if (event.data === 'ping') {
    ws.send('pong');  // Respond immediately
    return;
  }
  // Handle other messages...
  const data = JSON.parse(event.data);
  handleUpdate(data);
};
```

Copy

```shiki
// WRONG - Ignoring PING messages will disconnect you
ws.onmessage = (event) => {
  const data = JSON.parse(event.data);  // Fails on "ping" string!
  handleUpdate(data);
};
```

If you don’t respond to PING within 10 seconds, your connection will be terminated.

---

## [​](#connection-state-management) Connection State Management

Always check connection state before sending:

Copy

```shiki
if (ws.readyState === WebSocket.OPEN) {
  ws.send('pong');
} else {
  console.warn('WebSocket not connected');
}
```

---

## [​](#browser-tab-visibility) Browser Tab Visibility

Connections may drop when browser tabs become inactive. Handle visibility changes:

Copy

```shiki
document.addEventListener('visibilitychange', () => {
  if (!document.hidden && ws.readyState !== WebSocket.OPEN) {
    console.log('Tab became visible, reconnecting...');
    connect();
  }
});
```

---

## [​](#troubleshooting) Troubleshooting

Connection drops after exactly 10 seconds

Your PING/PONG handler isn’t working correctly.**Check:**

* You’re responding to `"ping"` string messages (not JSON)
* You’re sending `"pong"` as a string response
* No errors are preventing the PONG from being sent

Copy

```shiki
// Debug PING/PONG handling
ws.onmessage = (event) => {
  console.log('Received:', event.data);
  if (event.data === 'ping') {
    console.log('Sending PONG response');
    ws.send('pong');
    return;
  }
  // Handle JSON messages...
};
```

Connection keeps dropping frequently

This may be network instability or main thread blocking.**Solutions:**

* Implement exponential backoff for reconnection
* Ensure your message handler doesn’t block the main thread
* Check network stability

Copy

```shiki
handleReconnect() {
  this.reconnectDelay = Math.min(this.reconnectDelay * 2, 30000);
  setTimeout(() => this.connect(), this.reconnectDelay);
}
```

Messages not updating UI

Ensure you’re updating state correctly based on the `slug` identifier.

Copy

```shiki
// Use slug as unique key
setSportsData(prev => {
  const index = prev.findIndex(item => item.slug === data.slug);
  if (index >= 0) {
    const updated = [...prev];
    updated[index] = data;
    return updated;
  }
  return [...prev, data];
});
```

Memory leaks with multiple connections

Clean up properly when disconnecting:

Copy

```shiki
const cleanup = () => {
  if (reconnectTimeout) {
    clearTimeout(reconnectTimeout);
  }
  if (ws) {
    ws.close();
    ws = null;
  }
};

// React: cleanup in useEffect return
// Vanilla: call on page unload
window.addEventListener('beforeunload', cleanup);
```

---

## [​](#debugging-tips) Debugging Tips

Enable verbose logging to diagnose connection issues:

Copy

```shiki
ws.onopen = () => console.log('[connected]');
ws.onclose = (e) => console.log('[closed]', e.code, e.reason);
ws.onerror = (e) => console.error('[error]', e);
ws.onmessage = (e) => console.log('[message]', e.data);
```

Monitor connection state:

Copy

```shiki
setInterval(() => {
  const states = ['CONNECTING', 'OPEN', 'CLOSING', 'CLOSED'];
  console.log('WebSocket state:', states[ws.readyState]);
}, 5000);
```

[Message Format](/developers/sports-websocket/message-format)[RTDS Overview](/developers/RTDS/RTDS-overview)

⌘I

---


## Sports WS Message Format

> Source: https://docs.polymarket.com/developers/sports-websocket/message-format

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Sports Websocket

Message Format

Once connected to the Sports WebSocket, clients receive JSON messages whenever a sports event updates. Messages are broadcast to all connected clients automatically.

---

## [​](#sport_result-message) sport\_result Message

Emitted when:

* A match goes live
* The score changes
* The period changes (e.g., halftime, overtime)
* A match ends
* Possession changes (NFL and CFB only)

### [​](#structure) Structure

[​](#param-game-id)

gameId

number

Unique identifier for the game

[​](#param-league-abbreviation)

leagueAbbreviation

string

League identifier (e.g., `"nfl"`, `"nba"`, `"cs2"`)

[​](#param-home-team)

homeTeam

string

Home team name or abbreviation

[​](#param-away-team)

awayTeam

string

Away team name or abbreviation

[​](#param-status)

status

string

Game status (e.g., `"InProgress"`, `"finished"`)

[​](#param-live)

live

boolean

`true` if the match is currently in progress

[​](#param-ended)

ended

boolean

`true` if the match has concluded

[​](#param-score)

score

string

Current score (format varies by sport)

[​](#param-period)

period

string

Current period (e.g., `"Q4"`, `"2H"`, `"2/3"`)

[​](#param-elapsed)

elapsed

string

Time elapsed in current period (e.g., `"05:09"`)

[​](#param-finished-timestamp)

finishedTimestamp

string

Timestamp when the match ended (only present when `ended: true`)

[​](#param-turn)

turn

string

Team abbreviation with possession (NFL/CFB only)

The `turn` field is only present for NFL and CFB games and indicates which team currently has the ball.

### [​](#example-messages) Example Messages

**NFL (in progress):**

Copy

```shiki
{
  "gameId": 19439,
  "leagueAbbreviation": "nfl",
  "homeTeam": "LAC",
  "awayTeam": "BUF",
  "status": "InProgress",
  "score": "3-16",
  "period": "Q4",
  "elapsed": "5:18",
  "live": true,
  "ended": false,
  "turn": "lac"
}
```

**Esports - CS2 (finished):**

Copy

```shiki
{
  "gameId": 1317359,
  "leagueAbbreviation": "cs2",
  "homeTeam": "ARCRED",
  "awayTeam": "The glecs",
  "status": "finished",
  "score": "000-000|2-0|Bo3",
  "period": "2/3",
  "live": false,
  "ended": true
}
```

---

## [​](#slug-format) Slug Format

The `slug` field follows a consistent naming convention:

Copy

```shiki
{league}-{team1}-{team2}-{date}
```

**Examples:**

* `nfl-buf-kc-2025-01-26` — NFL: Buffalo Bills vs Kansas City Chiefs
* `nba-lal-bos-2025-02-15` — NBA: LA Lakers vs Boston Celtics
* `mlb-nyy-bos-2025-04-01` — MLB: NY Yankees vs Boston Red Sox

---

## [​](#period-values) Period Values

| Period | Description |
| --- | --- |
| `1H` | First half |
| `2H` | Second half |
| `1Q`, `2Q`, `3Q`, `4Q` | Quarters (NFL, NBA) |
| `HT` | Halftime |
| `FT` | Full time (match ended in regulation) |
| `FT OT` | Full time with overtime |
| `FT NR` | Full time, no result (draw or canceled) |
| `End 1`, `End 2`, etc. | End of inning (MLB) |
| `1/3`, `2/3`, `3/3` | Map number in Bo3 series (Esports) |
| `1/5`, `2/5`, etc. | Map number in Bo5 series (Esports) |

---

## [​](#handling-updates) Handling Updates

When processing messages, use the `gameId` field as the unique identifier to update your local state:

Copy

```shiki
// Update or insert based on gameId
setSportsData(prev => {
  const existing = prev.find(item => item.gameId === data.gameId);
  if (existing) {
    return prev.map(item => 
      item.gameId === data.gameId ? data : item
    );
  }
  return [...prev, data];
});
```

[Overview](/developers/sports-websocket/overview)[Quickstart](/developers/sports-websocket/quickstart)

⌘I

---


## Subgraph Overview

> Source: https://docs.polymarket.com/developers/subgraph/overview

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

## [​](#subgraph-overview) Subgraph Overview

Polymarket has written and open sourced a subgraph that provides, via a GraphQL query interface, useful aggregate calculations and event indexing for things like volume, user position, market and liquidity data. The subgraph updates in real time to be able to be mixed, and match core data from the primary Polymarket interface, providing positional data, activity history and more. The subgraph can be hosted by anyone.

## [​](#source) Source

The Polymarket subgraph is entirely open source and can be found on the Polymarket Github.
**[Subgraph Github Repository](https://github.com/Polymarket/polymarket-subgraph)**
> Note: The available models/schemas can be found in the `schema.graphql` file.

[Get transaction status](/api-reference/bridge/get-transaction-status)[Resolution](/developers/resolution/UMA)

⌘I

---


## Bridge Overview

> Source: https://docs.polymarket.com/developers/misc-endpoints/bridge-overview

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Bridge & Swap

Overview

The Polymarket Bridge API enables seamless deposits and withdrawals between multiple networks and Polymarket.

### [​](#usdc-e-on-polygon) USDC.e on Polygon

**Polymarket uses USDC.e (Bridged USDC) on Polygon as collateral** for all trading activities. USDC.e is the bridged version of USDC from Ethereum, and it serves as the native currency for placing orders and settling trades on Polymarket.
When you deposit assets to Polymarket:

1. You can deposit from various supported chains (Ethereum, Solana, Arbitrum, Base, etc.)
2. Your assets are automatically bridged/swapped to USDC.e on Polygon
3. USDC.e is credited to your Polymarket wallet so you can trade on any market

## [​](#base-url) Base URL

Copy

```shiki
https://bridge.polymarket.com
```

## [​](#key-features) Key Features

* **Multi-chain deposits**: Bridge assets from EVM chains (Ethereum, Arbitrum, Base, etc.), Solana, and Bitcoin
* **Multi-chain withdrawals**: Withdraw USDC.e to any supported chain and token
* **Automatic conversion**: Assets are automatically bridged and swapped
* **Simple addressing**: One deposit address per blockchain type (EVM, SVM, BTC)

## [​](#endpoints) Endpoints

* `GET /supported-assets` - Get all supported chains and tokens
* `POST /quote` - Get a quote for a deposit or withdrawal
* `POST /deposit` - Create deposit addresses for bridging assets to Polymarket
* `POST /withdraw` - Create withdrawal addresses for bridging assets from Polymarket
* `GET /status/{address}` - Get transaction status for a given address

[Get daily builder volume time-series](/api-reference/builders/get-daily-builder-volume-time-series)[Get supported assets](/api-reference/bridge/get-supported-assets)

⌘I

---


## Neg Risk Overview

> Source: https://docs.polymarket.com/developers/neg-risk/overview

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Negative Risk

Overview

Certain events which meet the criteria of being “winner-take-all” may be deployed as **“negative risk”** events/markets. The Gamma API includes a boolean field on events, `negRisk`, which indicates whether the event is negative risk.
Negative risk allows for increased capital efficiency by relating all markets within events via a convert action. More explicitly, a NO share in any market can be converted into 1 YES share in all other markets. Converts can be exercised via the [Negative Adapter](https://polygonscan.com/address/0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296). You can read more about negative risk [here](https://github.com/Polymarket/neg-risk-ctf-adapter).

---

## [​](#augmented-negative-risk) Augmented Negative Risk

There is a known issue with the negative risk architecture which is that the outcome universe must be complete before conversions are made or otherwise conversion will “cost” something. In most cases, the outcome universe can be made complete by deploying all the named outcomes and then an “other” option. But in some cases this is undesirable as new outcomes can come out of nowhere and you’d rather them be directly named versus grouped together in an “other”.
To fix this, some markets use a system of **“augmented negative risk”**, where named outcomes, a collection of unnamed outcomes, and an *other* is deployed. When a new outcome needs to be added, an unnamed outcome can be clarified to be the new outcome via the bulletin board. This means the “other” in the case of augmented negative risk can effectively change definitions (outcomes can be taken out of it).
As such, trading should only happen on the named outcomes, and the other outcomes should be ignored until they are named or until resolution occurs. The Polymarket UI will not show unnamed outcomes.
If a market becomes resolvable and the correct outcome is not named (originally or via placeholder clarification), it should resolve to the *“other”* outcome. An event can be considered “augmented negative risk” when `enableNegRisk` is true **AND** `negRiskAugmented` is true.
The naming conventions are as follows:

### [​](#original-outcomes) Original Outcomes

* Outcome A
* Outcome B
* …

### [​](#placeholder-outcomes) Placeholder Outcomes

* Person A -> can be clarified to a named outcome
* Person B -> can be clarified to a named outcome
* …

### [​](#explicit-other) Explicit Other

* Other -> not meant to be traded as the definition of this changes as placeholder outcomes are clarified to named outcomes

[Proxy wallet](/developers/proxy-wallet)

⌘I

---


## Proxy Wallet

> Source: https://docs.polymarket.com/developers/proxy-wallet

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

## [​](#overview) Overview

When a user first uses Polymarket.com to trade they are prompted to create a wallet. When they do this, a 1 of 1 multisig is deployed to Polygon which is controlled/owned by the accessing EOA (either MetaMask wallet or MagicLink wallet). This proxy wallet is where all the user’s positions (ERC1155) and USDC (ERC20) are held.
Using proxy wallets allows Polymarket to provide an improved UX where multi-step transactions can be executed atomically and transactions can be relayed by relayers on the gas station network. If you are a developer looking to programmatically access positions you accumulated via the Polymarket.com interface, you can either continue using the smart contract wallet by executing transactions through it from the owner account, or you can transfer these assets to a new address using the owner account.

---

## [​](#deployments) Deployments

Each user has their own proxy wallet (and thus proxy wallet address) but the factories are available at the following deployed addresses on the **Polygon network**:

| **Address** | **Details** |
| --- | --- |
| [0xaacfeea03eb1561c4e67d661e40682bd20e3541b](https://polygonscan.com/address/0xaacfeea03eb1561c4e67d661e40682bd20e3541b) | **Gnosis safe factory** – Gnosis safes are used for all MetaMask users |
| [0xaB45c5A4B0c941a2F231C04C3f49182e1A254052](https://polygonscan.com/address/0xaB45c5A4B0c941a2F231C04C3f49182e1A254052) | **Polymarket proxy factory** – Polymarket custom proxy contracts are used for all MagicLink users |

[Deployment and Additional Information](/developers/CTF/deployment-resources)[Overview](/developers/neg-risk/overview)

⌘I

---


## UMA Resolution

> Source: https://docs.polymarket.com/developers/resolution/UMA

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Resolution

Resolution

# [​](#uma-optimistic-oracle-integration) UMA Optimistic Oracle Integration

## [​](#overview) Overview

Polymarket leverages UMA’s Optimistic Oracle (OO) to resolve arbitrary questions, permissionlessly. From [UMA’s docs](https://docs.uma.xyz/protocol-overview/how-does-umas-oracle-work):
“UMA’s Optimistic Oracle allows contracts to quickly request and receive data information … The Optimistic Oracle acts as a generalized escalation game between contracts that initiate a price request and UMA’s dispute resolution system known as the Data Verification Mechanism (DVM). Prices proposed by the Optimistic Oracle will not be sent to the DVM unless it is disputed. If a dispute is raised, a request is sent to the DVM. All contracts built on UMA use the DVM as a backstop to resolve disputes. Disputes sent to the DVM will be resolved within a few days — after UMA tokenholders vote on what the correct outcome should have been.”
To allow CTF markets to be resolved via the OO, Polymarket developed a custom adapter contract called `UmaCtfAdapter` that provides a way for the two contract systems to interface.

## [​](#clarifications) Clarifications

Recent versions (v2+) of the `UmaCtfAdapter` also include a bulletin board feature that allows market creators to issue “clarifications”. Questions that allow updates will include the sentence in their ancillary data:
“Updates made by the question creator via the bulletin board on 0x6A5D0222186C0FceA7547534cC13c3CFd9b7b6A4F74 should be considered. In summary, clarifications that do not impact the question’s intent should be considered.”
Where the [transaction](https://polygonscan.com/tx/0xa14f01b115c4913624fc3f508f960f4dea252758e73c28f5f07f8e19d7bca066) reference outlining what outlining should be considered.

## [​](#resolution-process) Resolution Process

### [​](#actions) Actions

* **Initiate** - Binary CTF markets are initialized via the `UmaCtfAdapter`’s `initialize()` function. This stores the question parameters on the contract, prepares the CTF and requests a price for a question from the OO. It returns a `questionID` that is also used to reference on the `UmaCtfAdapter`. The caller provides:
  1. `ancillaryData` - data used to resolve a question (i.e the question + clarifications)
  2. `rewardToken` - ERC20 token address used for payment of rewards and fees
  3. `reward` - Reward amount offered to a successful proposer. The caller must have set allowance so that the contract can pull this reward in.
  4. `proposalBond` - Bond required to be posted by OO proposers/disputers. If 0, the default OO bond is used.
  5. `liveness` - UMA liveness period in seconds. If 0, the default liveness period is used.
* **Propose Price** - Anyone can then propose a price to the question on the OO. To do this they must post the `proposalBond`. The liveness period begins after a price is proposed.
* **Dispute** - Anyone that disagrees with the proposed price has the opportunity to dispute the price by posting a counter bond via the OO, this proposed will now be escalated to the DVM for a voter-wide vote.

### [​](#possible-flows) Possible Flows

When the first proposed price is disputed for a `questionID` on the adapter, a callback is made and posted as the reward for this new proposal. This means a second `questionID`, making a new `questionID` to the OO (the reward is returned before the callback is made and posted as the reward for this new proposal). This allows for a second round of resolution, and correspondingly a second dispute is required for it to go to the DVM. The thinking behind this is to doubles the cost of a potential griefing vector (two disputes are required just one) and also allows far-fetched (incorrect) first price proposals to not delay the resolution. As such there are two possible flows:

* **Initialize (CTFAdapter) -> Propose (OO) -> Resolve (CTFAdapter)**
* **Initialize (CTFAdaptor) -> Propose (OO) -> Challenge (OO) -> Propose (OO) -> Resolve (CTFAdaptor)**
* **Initialize (CTFAdaptor) -> Propose (OO) -> Challenge (OO) -> Propose (OO) -> Challenge (CtfAdapter) -> Resolve (CTFAdaptor)**

## [​](#deployed-addresses) Deployed Addresses

### [​](#v3-0) v3.0

| Network | Address |
| --- | --- |
| Polygon Mainnet | [0x157Ce2d672854c848c9b79C49a8Cc6cc89176a49](https://polygonscan.com/address/0x157Ce2d672854c848c9b79C49a8Cc6cc89176a49) |

### [​](#v2-0) v2.0

| Network | Address |
| --- | --- |
| Polygon Mainnet | [0x6A9D0222186C0FceA7547534cC13c3CFd9b7b6A4F74](https://polygonscan.com/address/0x6A9D222616C90FcA5754cd1333cFD9b7fb6a4F74) |

### [​](#v1-0) v1.0

| Network | Address |
| --- | --- |
| Polygon Mainnet | [0xC8B122858a4EF82C2d4eE2E6A276C719e692995130](https://polygonscan.com/address/0xCB1822859cEF82Cd2Eb4E6276C7916e692995130) |

## [​](#additional-resources) Additional Resources

* [Audit](https://github.com/Polymarket/uma-ctf-adapter/blob/main/audit/Polymarket_UMA_Optimistic_Oracle_Adapter_Audit.pdf)
* [Source Code](https://github.com/Polymarket/uma-ctf-adapter)
* [UMA Documentation](https://docs.uma.xyz/)
* [UMA Oracle Portal](https://oracle.uma.xyz/)

[Overview](/developers/subgraph/overview)[Overview](/developers/CTF/overview)

⌘I

---


## API: Create Deposit Addresses

> Source: https://docs.polymarket.com/api-reference/bridge/create-deposit-addresses

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Bridge

Create deposit addresses

POST

/

deposit

Try it

Create deposit addresses

cURL

Copy

```shiki
curl --request POST \
  --url https://bridge.polymarket.com/deposit \
  --header 'Content-Type: application/json' \
  --data '
{
  "address": "0x56687bf447db6ffa42ffe2204a05edaa20f55839"
}
'
```

201

400

500

Copy

```shiki
{
  "address": {
    "evm": "0x23566f8b2E82aDfCf01846E54899d110e97AC053",
    "svm": "CrvTBvzryYxBHbWu2TiQpcqD5M7Le7iBKzVmEj3f36Jb",
    "btc": "bc1q8eau83qffxcj8ht4hsjdza3lha9r3egfqysj3g"
  },
  "note": "Only certain chains and tokens are supported. See /supported-assets for details."
}
```

#### Body

application/json

[​](#body-address)

address

string

required

Your Polymarket wallet address where deposited funds will be credited as USDC.e

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

#### Response

201

application/json

Deposit addresses created successfully

[​](#response-address)

address

object

Deposit addresses for different blockchain networks

Show child attributes

[​](#response-note)

note

string

Additional information about the deposit addresses

Example:

`"Only certain chains and tokens are supported. See /supported-assets for details."`

[Get a quote](/api-reference/bridge/get-a-quote)[Create withdrawal addresses](/api-reference/bridge/create-withdrawal-addresses)

⌘I

---


## API: Create Withdrawal Addresses

> Source: https://docs.polymarket.com/api-reference/bridge/create-withdrawal-addresses

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Bridge

Create withdrawal addresses

POST

/

withdraw

Try it

Create withdrawal addresses

cURL

Copy

```shiki
curl --request POST \
  --url https://bridge.polymarket.com/withdraw \
  --header 'Content-Type: application/json' \
  --data '
{
  "address": "0x9156dd10bea4c8d7e2d591b633d1694b1d764756",
  "toChainId": "1",
  "toTokenAddress": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
  "recipientAddr": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
}
'
```

201

400

500

Copy

```shiki
{
  "address": {
    "evm": "0x23566f8b2E82aDfCf01846E54899d110e97AC053",
    "svm": "CrvTBvzryYxBHbWu2TiQpcqD5M7Le7iBKzVmEj3f36Jb",
    "btc": "bc1q8eau83qffxcj8ht4hsjdza3lha9r3egfqysj3g"
  },
  "note": "Send funds to these addresses to bridge to your destination chain and token."
}
```

#### Body

application/json

[​](#body-address)

address

string

required

Source Polymarket wallet address on Polygon

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

[​](#body-to-chain-id)

toChainId

string

required

Destination chain ID (e.g., "1" for Ethereum, "8453" for Base, "1151111081099710" for Solana)

Example:

`"1"`

[​](#body-to-token-address)

toTokenAddress

string

required

Destination token contract address

Example:

`"0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"`

[​](#body-recipient-addr)

recipientAddr

string

required

Destination wallet address where funds will be sent

Example:

`"0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"`

#### Response

201

application/json

Withdrawal addresses created successfully

[​](#response-address)

address

object

Deposit addresses for different blockchain networks

Show child attributes

[​](#response-note)

note

string

Additional information about the deposit addresses

Example:

`"Only certain chains and tokens are supported. See /supported-assets for details."`

[Create deposit addresses](/api-reference/bridge/create-deposit-addresses)[Get transaction status](/api-reference/bridge/get-transaction-status)

⌘I

---


## API: Get a Quote

> Source: https://docs.polymarket.com/api-reference/bridge/get-a-quote

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Bridge

Get a quote

POST

/

quote

Try it

Get a quote

cURL

Copy

```shiki
curl --request POST \
  --url https://bridge.polymarket.com/quote \
  --header 'Content-Type: application/json' \
  --data '
{
  "fromAmountBaseUnit": "10000000",
  "fromChainId": "137",
  "fromTokenAddress": "0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359",
  "recipientAddress": "0x17eC161f126e82A8ba337f4022d574DBEaFef575",
  "toChainId": "137",
  "toTokenAddress": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"
}
'
```

200

Example

Copy

```shiki
{  
  "estCheckoutTimeMs": 25000,  
  "estFeeBreakdown": {  
    "appFeeLabel": "Fun.xyz fee",  
    "appFeePercent": 0,  
    "appFeeUsd": 0,  
    "fillCostPercent": 0,  
    "fillCostUsd": 0,  
    "gasUsd": 0.003854,  
    "maxSlippage": 0,  
    "minReceived": 14.488305,  
    "swapImpact": 0,  
    "swapImpactUsd": 0,  
    "totalImpact": 0,  
    "totalImpactUsd": 0  
  },  
  "estInputUsd": 14.488305,  
  "estOutputUsd": 14.488305,  
  "estToTokenBaseUnit": "14491203",  
  "quoteId": "0x00c34ba467184b0146406d62b0e60aaa24ed52460bd456222b6155a0d9de0ad5"  
}
```

#### Body

application/json

[​](#body-from-amount-base-unit)

fromAmountBaseUnit

string

required

Amount of tokens to send

Example:

`"10000000"`

[​](#body-from-chain-id)

fromChainId

string

required

Source Chain ID

Example:

`"137"`

[​](#body-from-token-address)

fromTokenAddress

string

required

Source token address

Example:

`"0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359"`

[​](#body-recipient-address)

recipientAddress

string

required

Address of the recipient

Example:

`"0x17eC161f126e82A8ba337f4022d574DBEaFef575"`

[​](#body-to-chain-id)

toChainId

string

required

Destination Chain ID

Example:

`"137"`

[​](#body-to-token-address)

toTokenAddress

string

required

Destination token address

Example:

`"0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"`

#### Response

200

application/json

Quote retrieved successfully

[​](#response-est-checkout-time-ms)

estCheckoutTimeMs

integer

Estimated time to complete the checkout in milliseconds

Example:

`25000`

[​](#response-est-fee-breakdown)

estFeeBreakdown

object

Breakdown of the estimated fees

Show child attributes

[​](#response-est-input-usd)

estInputUsd

number

Estimated token amount received in USD

Example:

`14.488305`

[​](#response-est-output-usd)

estOutputUsd

number

Estimated token amount sent in USD

Example:

`14.488305`

[​](#response-est-to-token-base-unit)

estToTokenBaseUnit

string

Estimated token amount received

Example:

`"14491203"`

[​](#response-quote-id)

quoteId

string

Unique quote id of the request

Example:

`"0x00c34ba467184b0146406d62b0e60aaa24ed52460bd456222b6155a0d9de0ad5"`

[Get supported assets](/api-reference/bridge/get-supported-assets)[Create deposit addresses](/api-reference/bridge/create-deposit-addresses)

⌘I

---


## API: Get Supported Assets

> Source: https://docs.polymarket.com/api-reference/bridge/get-supported-assets

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Bridge

Get supported assets

GET

/

supported-assets

Try it

Get supported assets

cURL

Copy

```shiki
curl --request GET \
  --url https://bridge.polymarket.com/supported-assets
```

200

500

Copy

```shiki
{
  "supportedAssets": [
    {
      "chainId": "1",
      "chainName": "Ethereum",
      "token": {
        "name": "USD Coin",
        "symbol": "USDC",
        "address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
        "decimals": 6
      },
      "minCheckoutUsd": 45
    }
  ]
}
```

#### Response

200

application/json

Successfully retrieved supported assets

[​](#response-supported-assets)

supportedAssets

object[]

List of supported assets with minimum amounts for deposits and withdrawals

Show child attributes

[Overview](/developers/misc-endpoints/bridge-overview)[Get a quote](/api-reference/bridge/get-a-quote)

⌘I

---


## API: Get Transaction Status

> Source: https://docs.polymarket.com/api-reference/bridge/get-transaction-status

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Bridge

Get transaction status

GET

/

status

/

{address}

Try it

Get transaction status

cURL

Copy

```shiki
curl --request GET \
  --url https://bridge.polymarket.com/status/{address}
```

200

400

500

Copy

```shiki
{
  "transactions": [
    {
      "fromChainId": "1151111081099710",
      "fromTokenAddress": "11111111111111111111111111111111",
      "fromAmountBaseUnit": "13566635",
      "toChainId": "137",
      "toTokenAddress": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
      "status": "DEPOSIT_DETECTED"
    },
    {
      "fromChainId": "1151111081099710",
      "fromTokenAddress": "11111111111111111111111111111111",
      "fromAmountBaseUnit": "13400000",
      "toChainId": "137",
      "toTokenAddress": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
      "createdTimeMs": 1757646914535,
      "status": "PROCESSING"
    },
    {
      "fromChainId": "1151111081099710",
      "fromTokenAddress": "11111111111111111111111111111111",
      "fromAmountBaseUnit": "13500152",
      "toChainId": "137",
      "toTokenAddress": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
      "txHash": "3atr19NAiNCYt24RHM1WnzZp47RXskpTDzspJoCBBaMFwUB8fk37hFkxz35P5UEnnmWz21rb2t5wJ8pq3EE2XnxU",
      "createdTimeMs": 1757531217339,
      "status": "COMPLETED"
    }
  ]
}
```

#### Path Parameters

[​](#parameter-address)

address

string

required

The address to query for transaction status (EVM, SVM, or BTC address from the `/deposit` or `/withdraw` response)

#### Response

200

application/json

Successfully retrieved transaction status

[​](#response-transactions)

transactions

object[]

List of transactions for the given address

Show child attributes

[Create withdrawal addresses](/api-reference/bridge/create-withdrawal-addresses)[Overview](/developers/subgraph/overview)

⌘I

---


## API: Get Aggregated Builder Leaderboard

> Source: https://docs.polymarket.com/api-reference/builders/get-aggregated-builder-leaderboard

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Builders

Get aggregated builder leaderboard

GET

/

v1

/

builders

/

leaderboard

Try it

Get aggregated builder leaderboard

cURL

Copy

```shiki
curl --request GET \
  --url https://data-api.polymarket.com/v1/builders/leaderboard
```

200

400

500

Copy

```shiki
[
  {
    "rank": "<string>",
    "builder": "<string>",
    "volume": 123,
    "activeUsers": 123,
    "verified": true,
    "builderLogo": "<string>"
  }
]
```

#### Query Parameters

[​](#parameter-time-period)

timePeriod

enum<string>

default:DAY

The time period to aggregate results over.

Available options:

`DAY`,

`WEEK`,

`MONTH`,

`ALL`

[​](#parameter-limit)

limit

integer

default:25

Maximum number of builders to return

Required range: `0 <= x <= 50`

[​](#parameter-offset)

offset

integer

default:0

Starting index for pagination

Required range: `0 <= x <= 1000`

#### Response

200

application/json

Success

[​](#response-items-rank)

rank

string

The rank position of the builder

[​](#response-items-builder)

builder

string

The builder name or identifier

[​](#response-items-volume)

volume

number

Total trading volume attributed to this builder

[​](#response-items-active-users)

activeUsers

integer

Number of active users for this builder

[​](#response-items-verified)

verified

boolean

Whether the builder is verified

[​](#response-items-builder-logo)

builderLogo

string

URL to the builder's logo image

[Get trader leaderboard rankings](/api-reference/core/get-trader-leaderboard-rankings)[Get daily builder volume time-series](/api-reference/builders/get-daily-builder-volume-time-series)

⌘I

---


## API: Get Daily Builder Volume Time-series

> Source: https://docs.polymarket.com/api-reference/builders/get-daily-builder-volume-time-series

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Builders

Get daily builder volume time-series

GET

/

v1

/

builders

/

volume

Try it

Get daily builder volume time-series

cURL

Copy

```shiki
curl --request GET \
  --url https://data-api.polymarket.com/v1/builders/volume
```

200

400

500

Copy

```shiki
[
  {
    "dt": "2025-11-15T00:00:00Z",
    "builder": "<string>",
    "builderLogo": "<string>",
    "verified": true,
    "volume": 123,
    "activeUsers": 123,
    "rank": "<string>"
  }
]
```

#### Query Parameters

[​](#parameter-time-period)

timePeriod

enum<string>

default:DAY

The time period to fetch daily records for.

Available options:

`DAY`,

`WEEK`,

`MONTH`,

`ALL`

#### Response

200

application/json

Success - Returns array of daily volume records

[​](#response-items-dt)

dt

string<date-time>

The timestamp for this volume entry in ISO 8601 format

Example:

`"2025-11-15T00:00:00Z"`

[​](#response-items-builder)

builder

string

The builder name or identifier

[​](#response-items-builder-logo)

builderLogo

string

URL to the builder's logo image

[​](#response-items-verified)

verified

boolean

Whether the builder is verified

[​](#response-items-volume)

volume

number

Trading volume for this builder on this date

[​](#response-items-active-users)

activeUsers

integer

Number of active users for this builder on this date

[​](#response-items-rank)

rank

string

The rank position of the builder on this date

[Get aggregated builder leaderboard](/api-reference/builders/get-aggregated-builder-leaderboard)[Overview](/developers/misc-endpoints/bridge-overview)

⌘I

---


## API: Get Comments by Comment ID

> Source: https://docs.polymarket.com/api-reference/comments/get-comments-by-comment-id

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Comments

Get comments by comment id

GET

/

comments

/

{id}

Try it

Get comments by comment id

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/comments/{id}
```

200

Copy

```shiki
[
  {
    "id": "<string>",
    "body": "<string>",
    "parentEntityType": "<string>",
    "parentEntityID": 123,
    "parentCommentID": "<string>",
    "userAddress": "<string>",
    "replyAddress": "<string>",
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "profile": {
      "name": "<string>",
      "pseudonym": "<string>",
      "displayUsernamePublic": true,
      "bio": "<string>",
      "isMod": true,
      "isCreator": true,
      "proxyWallet": "<string>",
      "baseAddress": "<string>",
      "profileImage": "<string>",
      "profileImageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "positions": [
        {
          "tokenId": "<string>",
          "positionSize": "<string>"
        }
      ]
    },
    "reactions": [
      {
        "id": "<string>",
        "commentID": 123,
        "reactionType": "<string>",
        "icon": "<string>",
        "userAddress": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "profile": {
          "name": "<string>",
          "pseudonym": "<string>",
          "displayUsernamePublic": true,
          "bio": "<string>",
          "isMod": true,
          "isCreator": true,
          "proxyWallet": "<string>",
          "baseAddress": "<string>",
          "profileImage": "<string>",
          "profileImageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "positions": [
            {
              "tokenId": "<string>",
              "positionSize": "<string>"
            }
          ]
        }
      }
    ],
    "reportCount": 123,
    "reactionCount": 123
  }
]
```

#### Path Parameters

[​](#parameter-id)

id

integer

required

#### Query Parameters

[​](#parameter-get-positions)

get\_positions

boolean

#### Response

200 - application/json

Comments

[​](#response-items-id)

id

string

[​](#response-items-body-one-of-0)

body

string | null

[​](#response-items-parent-entity-type-one-of-0)

parentEntityType

string | null

[​](#response-items-parent-entity-id-one-of-0)

parentEntityID

integer | null

[​](#response-items-parent-comment-id-one-of-0)

parentCommentID

string | null

[​](#response-items-user-address-one-of-0)

userAddress

string | null

[​](#response-items-reply-address-one-of-0)

replyAddress

string | null

[​](#response-items-created-at-one-of-0)

createdAt

string<date-time> | null

[​](#response-items-updated-at-one-of-0)

updatedAt

string<date-time> | null

[​](#response-items-profile)

profile

object

Show child attributes

[​](#response-items-reactions)

reactions

object[]

Show child attributes

[​](#response-items-report-count-one-of-0)

reportCount

integer | null

[​](#response-items-reaction-count-one-of-0)

reactionCount

integer | null

[List comments](/api-reference/comments/list-comments)[Get comments by user address](/api-reference/comments/get-comments-by-user-address)

⌘I

---


## API: Get Comments by User Address

> Source: https://docs.polymarket.com/api-reference/comments/get-comments-by-user-address

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Comments

Get comments by user address

GET

/

comments

/

user\_address

/

{user\_address}

Try it

Get comments by user address

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/comments/user_address/{user_address}
```

200

Copy

```shiki
[
  {
    "id": "<string>",
    "body": "<string>",
    "parentEntityType": "<string>",
    "parentEntityID": 123,
    "parentCommentID": "<string>",
    "userAddress": "<string>",
    "replyAddress": "<string>",
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "profile": {
      "name": "<string>",
      "pseudonym": "<string>",
      "displayUsernamePublic": true,
      "bio": "<string>",
      "isMod": true,
      "isCreator": true,
      "proxyWallet": "<string>",
      "baseAddress": "<string>",
      "profileImage": "<string>",
      "profileImageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "positions": [
        {
          "tokenId": "<string>",
          "positionSize": "<string>"
        }
      ]
    },
    "reactions": [
      {
        "id": "<string>",
        "commentID": 123,
        "reactionType": "<string>",
        "icon": "<string>",
        "userAddress": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "profile": {
          "name": "<string>",
          "pseudonym": "<string>",
          "displayUsernamePublic": true,
          "bio": "<string>",
          "isMod": true,
          "isCreator": true,
          "proxyWallet": "<string>",
          "baseAddress": "<string>",
          "profileImage": "<string>",
          "profileImageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "positions": [
            {
              "tokenId": "<string>",
              "positionSize": "<string>"
            }
          ]
        }
      }
    ],
    "reportCount": 123,
    "reactionCount": 123
  }
]
```

#### Path Parameters

[​](#parameter-user-address)

user\_address

string

required

#### Query Parameters

[​](#parameter-limit)

limit

integer

Required range: `x >= 0`

[​](#parameter-offset)

offset

integer

Required range: `x >= 0`

[​](#parameter-order)

order

string

Comma-separated list of fields to order by

[​](#parameter-ascending)

ascending

boolean

#### Response

200 - application/json

Comments

[​](#response-items-id)

id

string

[​](#response-items-body-one-of-0)

body

string | null

[​](#response-items-parent-entity-type-one-of-0)

parentEntityType

string | null

[​](#response-items-parent-entity-id-one-of-0)

parentEntityID

integer | null

[​](#response-items-parent-comment-id-one-of-0)

parentCommentID

string | null

[​](#response-items-user-address-one-of-0)

userAddress

string | null

[​](#response-items-reply-address-one-of-0)

replyAddress

string | null

[​](#response-items-created-at-one-of-0)

createdAt

string<date-time> | null

[​](#response-items-updated-at-one-of-0)

updatedAt

string<date-time> | null

[​](#response-items-profile)

profile

object

Show child attributes

[​](#response-items-reactions)

reactions

object[]

Show child attributes

[​](#response-items-report-count-one-of-0)

reportCount

integer | null

[​](#response-items-reaction-count-one-of-0)

reactionCount

integer | null

[Get comments by comment id](/api-reference/comments/get-comments-by-comment-id)[Get public profile by wallet address](/api-reference/profiles/get-public-profile-by-wallet-address)

⌘I

---


## API: List Comments

> Source: https://docs.polymarket.com/api-reference/comments/list-comments

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Comments

List comments

GET

/

comments

Try it

List comments

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/comments
```

200

Copy

```shiki
[
  {
    "id": "<string>",
    "body": "<string>",
    "parentEntityType": "<string>",
    "parentEntityID": 123,
    "parentCommentID": "<string>",
    "userAddress": "<string>",
    "replyAddress": "<string>",
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "profile": {
      "name": "<string>",
      "pseudonym": "<string>",
      "displayUsernamePublic": true,
      "bio": "<string>",
      "isMod": true,
      "isCreator": true,
      "proxyWallet": "<string>",
      "baseAddress": "<string>",
      "profileImage": "<string>",
      "profileImageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "positions": [
        {
          "tokenId": "<string>",
          "positionSize": "<string>"
        }
      ]
    },
    "reactions": [
      {
        "id": "<string>",
        "commentID": 123,
        "reactionType": "<string>",
        "icon": "<string>",
        "userAddress": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "profile": {
          "name": "<string>",
          "pseudonym": "<string>",
          "displayUsernamePublic": true,
          "bio": "<string>",
          "isMod": true,
          "isCreator": true,
          "proxyWallet": "<string>",
          "baseAddress": "<string>",
          "profileImage": "<string>",
          "profileImageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "positions": [
            {
              "tokenId": "<string>",
              "positionSize": "<string>"
            }
          ]
        }
      }
    ],
    "reportCount": 123,
    "reactionCount": 123
  }
]
```

#### Query Parameters

[​](#parameter-limit)

limit

integer

Required range: `x >= 0`

[​](#parameter-offset)

offset

integer

Required range: `x >= 0`

[​](#parameter-order)

order

string

Comma-separated list of fields to order by

[​](#parameter-ascending)

ascending

boolean

[​](#parameter-parent-entity-type)

parent\_entity\_type

enum<string>

Available options:

`Event`,

`Series`,

`market`

[​](#parameter-parent-entity-id)

parent\_entity\_id

integer

[​](#parameter-get-positions)

get\_positions

boolean

[​](#parameter-holders-only)

holders\_only

boolean

#### Response

200 - application/json

List of comments

[​](#response-items-id)

id

string

[​](#response-items-body-one-of-0)

body

string | null

[​](#response-items-parent-entity-type-one-of-0)

parentEntityType

string | null

[​](#response-items-parent-entity-id-one-of-0)

parentEntityID

integer | null

[​](#response-items-parent-comment-id-one-of-0)

parentCommentID

string | null

[​](#response-items-user-address-one-of-0)

userAddress

string | null

[​](#response-items-reply-address-one-of-0)

replyAddress

string | null

[​](#response-items-created-at-one-of-0)

createdAt

string<date-time> | null

[​](#response-items-updated-at-one-of-0)

updatedAt

string<date-time> | null

[​](#response-items-profile)

profile

object

Show child attributes

[​](#response-items-reactions)

reactions

object[]

Show child attributes

[​](#response-items-report-count-one-of-0)

reportCount

integer | null

[​](#response-items-reaction-count-one-of-0)

reactionCount

integer | null

[Get series by id](/api-reference/series/get-series-by-id)[Get comments by comment id](/api-reference/comments/get-comments-by-comment-id)

⌘I

---


## API: Get Closed Positions

> Source: https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Core

Get closed positions for a user

GET

/

closed-positions

Try it

Get closed positions for a user

cURL

Copy

```shiki
curl --request GET \
  --url https://data-api.polymarket.com/closed-positions
```

200

400

401

500

Copy

```shiki
[
  {
    "proxyWallet": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",
    "asset": "<string>",
    "conditionId": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",
    "avgPrice": 123,
    "totalBought": 123,
    "realizedPnl": 123,
    "curPrice": 123,
    "timestamp": 123,
    "title": "<string>",
    "slug": "<string>",
    "icon": "<string>",
    "eventSlug": "<string>",
    "outcome": "<string>",
    "outcomeIndex": 123,
    "oppositeOutcome": "<string>",
    "oppositeAsset": "<string>",
    "endDate": "<string>"
  }
]
```

#### Query Parameters

[​](#parameter-user)

user

string

required

The address of the user in question
User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

[​](#parameter-market)

market

string[]

The conditionId of the market in question. Supports multiple csv separated values. Cannot be used with the eventId param.

0x-prefixed 64-hex string

[​](#parameter-title)

title

string

Filter by market title

Maximum string length: `100`

[​](#parameter-event-id)

eventId

integer[]

The event id of the event in question. Supports multiple csv separated values. Returns positions for all markets for those event ids. Cannot be used with the market param.

Required range: `x >= 1`

[​](#parameter-limit)

limit

integer

default:10

The max number of positions to return

Required range: `0 <= x <= 50`

[​](#parameter-offset)

offset

integer

default:0

The starting index for pagination

Required range: `0 <= x <= 100000`

[​](#parameter-sort-by)

sortBy

enum<string>

default:REALIZEDPNL

The sort criteria

Available options:

`REALIZEDPNL`,

`TITLE`,

`PRICE`,

`AVGPRICE`,

`TIMESTAMP`

[​](#parameter-sort-direction)

sortDirection

enum<string>

default:DESC

The sort direction

Available options:

`ASC`,

`DESC`

#### Response

200

application/json

Success

[​](#response-items-proxy-wallet)

proxyWallet

string

User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

[​](#response-items-asset)

asset

string

[​](#response-items-condition-id)

conditionId

string

0x-prefixed 64-hex string

Example:

`"0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917"`

[​](#response-items-avg-price)

avgPrice

number

[​](#response-items-total-bought)

totalBought

number

[​](#response-items-realized-pnl)

realizedPnl

number

[​](#response-items-cur-price)

curPrice

number

[​](#response-items-timestamp)

timestamp

integer<int64>

[​](#response-items-title)

title

string

[​](#response-items-slug)

slug

string

[​](#response-items-icon)

icon

string

[​](#response-items-event-slug)

eventSlug

string

[​](#response-items-outcome)

outcome

string

[​](#response-items-outcome-index)

outcomeIndex

integer

[​](#response-items-opposite-outcome)

oppositeOutcome

string

[​](#response-items-opposite-asset)

oppositeAsset

string

[​](#response-items-end-date)

endDate

string

[Get total value of a user's positions](/api-reference/core/get-total-value-of-a-users-positions)[Get trader leaderboard rankings](/api-reference/core/get-trader-leaderboard-rankings)

⌘I

---


## API: Get Current Positions

> Source: https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Core

Get current positions for a user

GET

/

positions

Try it

Get current positions for a user

cURL

Copy

```shiki
curl --request GET \
  --url https://data-api.polymarket.com/positions
```

200

400

401

500

Copy

```shiki
[
  {
    "proxyWallet": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",
    "asset": "<string>",
    "conditionId": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",
    "size": 123,
    "avgPrice": 123,
    "initialValue": 123,
    "currentValue": 123,
    "cashPnl": 123,
    "percentPnl": 123,
    "totalBought": 123,
    "realizedPnl": 123,
    "percentRealizedPnl": 123,
    "curPrice": 123,
    "redeemable": true,
    "mergeable": true,
    "title": "<string>",
    "slug": "<string>",
    "icon": "<string>",
    "eventSlug": "<string>",
    "outcome": "<string>",
    "outcomeIndex": 123,
    "oppositeOutcome": "<string>",
    "oppositeAsset": "<string>",
    "endDate": "<string>",
    "negativeRisk": true
  }
]
```

#### Query Parameters

[​](#parameter-user)

user

string

required

User address (required)
User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

[​](#parameter-market)

market

string[]

Comma-separated list of condition IDs. Mutually exclusive with eventId.

0x-prefixed 64-hex string

[​](#parameter-event-id)

eventId

integer[]

Comma-separated list of event IDs. Mutually exclusive with market.

Required range: `x >= 1`

[​](#parameter-size-threshold)

sizeThreshold

number

default:1

Required range: `x >= 0`

[​](#parameter-redeemable)

redeemable

boolean

default:false

[​](#parameter-mergeable)

mergeable

boolean

default:false

[​](#parameter-limit)

limit

integer

default:100

Required range: `0 <= x <= 500`

[​](#parameter-offset)

offset

integer

default:0

Required range: `0 <= x <= 10000`

[​](#parameter-sort-by)

sortBy

enum<string>

default:TOKENS

Available options:

`CURRENT`,

`INITIAL`,

`TOKENS`,

`CASHPNL`,

`PERCENTPNL`,

`TITLE`,

`RESOLVING`,

`PRICE`,

`AVGPRICE`

[​](#parameter-sort-direction)

sortDirection

enum<string>

default:DESC

Available options:

`ASC`,

`DESC`

[​](#parameter-title)

title

string

Maximum string length: `100`

#### Response

200

application/json

Success

[​](#response-items-proxy-wallet)

proxyWallet

string

User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

[​](#response-items-asset)

asset

string

[​](#response-items-condition-id)

conditionId

string

0x-prefixed 64-hex string

Example:

`"0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917"`

[​](#response-items-size)

size

number

[​](#response-items-avg-price)

avgPrice

number

[​](#response-items-initial-value)

initialValue

number

[​](#response-items-current-value)

currentValue

number

[​](#response-items-cash-pnl)

cashPnl

number

[​](#response-items-percent-pnl)

percentPnl

number

[​](#response-items-total-bought)

totalBought

number

[​](#response-items-realized-pnl)

realizedPnl

number

[​](#response-items-percent-realized-pnl)

percentRealizedPnl

number

[​](#response-items-cur-price)

curPrice

number

[​](#response-items-redeemable)

redeemable

boolean

[​](#response-items-mergeable)

mergeable

boolean

[​](#response-items-title)

title

string

[​](#response-items-slug)

slug

string

[​](#response-items-icon)

icon

string

[​](#response-items-event-slug)

eventSlug

string

[​](#response-items-outcome)

outcome

string

[​](#response-items-outcome-index)

outcomeIndex

integer

[​](#response-items-opposite-outcome)

oppositeOutcome

string

[​](#response-items-opposite-asset)

oppositeAsset

string

[​](#response-items-end-date)

endDate

string

[​](#response-items-negative-risk)

negativeRisk

boolean

[Get live volume for an event](/api-reference/misc/get-live-volume-for-an-event)[Get trades for a user or markets](/api-reference/core/get-trades-for-a-user-or-markets)

⌘I

---


## API: Get Top Holders

> Source: https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Core

Get top holders for markets

GET

/

holders

Try it

Get top holders for markets

cURL

Copy

```shiki
curl --request GET \
  --url https://data-api.polymarket.com/holders
```

200

400

401

500

Copy

```shiki
[
  {
    "token": "<string>",
    "holders": [
      {
        "proxyWallet": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",
        "bio": "<string>",
        "asset": "<string>",
        "pseudonym": "<string>",
        "amount": 123,
        "displayUsernamePublic": true,
        "outcomeIndex": 123,
        "name": "<string>",
        "profileImage": "<string>",
        "profileImageOptimized": "<string>"
      }
    ]
  }
]
```

#### Query Parameters

[​](#parameter-limit)

limit

integer

default:20

Maximum number of holders to return per token. Capped at 20.

Required range: `0 <= x <= 20`

[​](#parameter-market)

market

string[]

required

Comma-separated list of condition IDs.

0x-prefixed 64-hex string

[​](#parameter-min-balance)

minBalance

integer

default:1

Required range: `0 <= x <= 999999`

#### Response

200

application/json

Success

[​](#response-items-token)

token

string

[​](#response-items-holders)

holders

object[]

Show child attributes

[Get user activity](/api-reference/core/get-user-activity)[Get total value of a user's positions](/api-reference/core/get-total-value-of-a-users-positions)

⌘I

---


## API: Get Total Position Value

> Source: https://docs.polymarket.com/api-reference/core/get-total-value-of-a-users-positions

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Core

Get total value of a user's positions

GET

/

value

Try it

Get total value of a user's positions

cURL

Copy

```shiki
curl --request GET \
  --url https://data-api.polymarket.com/value
```

200

400

500

Copy

```shiki
[
  {
    "user": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",
    "value": 123
  }
]
```

#### Query Parameters

[​](#parameter-user)

user

string

required

User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

[​](#parameter-market)

market

string[]

0x-prefixed 64-hex string

#### Response

200

application/json

Success

[​](#response-items-user)

user

string

User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

[​](#response-items-value)

value

number

[Get top holders for markets](/api-reference/core/get-top-holders-for-markets)[Get closed positions for a user](/api-reference/core/get-closed-positions-for-a-user)

⌘I

---


## API: Get Trader Leaderboard

> Source: https://docs.polymarket.com/api-reference/core/get-trader-leaderboard-rankings

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Core

Get trader leaderboard rankings

GET

/

v1

/

leaderboard

Try it

Get trader leaderboard rankings

cURL

Copy

```shiki
curl --request GET \
  --url https://data-api.polymarket.com/v1/leaderboard
```

200

400

500

Copy

```shiki
[
  {
    "rank": "<string>",
    "proxyWallet": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",
    "userName": "<string>",
    "vol": 123,
    "pnl": 123,
    "profileImage": "<string>",
    "xUsername": "<string>",
    "verifiedBadge": true
  }
]
```

#### Query Parameters

[​](#parameter-category)

category

enum<string>

default:OVERALL

Market category for the leaderboard

Available options:

`OVERALL`,

`POLITICS`,

`SPORTS`,

`CRYPTO`,

`CULTURE`,

`MENTIONS`,

`WEATHER`,

`ECONOMICS`,

`TECH`,

`FINANCE`

[​](#parameter-time-period)

timePeriod

enum<string>

default:DAY

Time period for leaderboard results

Available options:

`DAY`,

`WEEK`,

`MONTH`,

`ALL`

[​](#parameter-order-by)

orderBy

enum<string>

default:PNL

Leaderboard ordering criteria

Available options:

`PNL`,

`VOL`

[​](#parameter-limit)

limit

integer

default:25

Max number of leaderboard traders to return

Required range: `1 <= x <= 50`

[​](#parameter-offset)

offset

integer

default:0

Starting index for pagination

Required range: `0 <= x <= 1000`

[​](#parameter-user)

user

string

Limit leaderboard to a single user by address
User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

[​](#parameter-user-name)

userName

string

Limit leaderboard to a single username

#### Response

200

application/json

Success

[​](#response-items-rank)

rank

string

The rank position of the trader

[​](#response-items-proxy-wallet)

proxyWallet

string

User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

[​](#response-items-user-name)

userName

string

The trader's username

[​](#response-items-vol)

vol

number

Trading volume for this trader

[​](#response-items-pnl)

pnl

number

Profit and loss for this trader

[​](#response-items-profile-image)

profileImage

string

URL to the trader's profile image

[​](#response-items-x-username)

xUsername

string

The trader's X (Twitter) username

[​](#response-items-verified-badge)

verifiedBadge

boolean

Whether the trader has a verified badge

[Get closed positions for a user](/api-reference/core/get-closed-positions-for-a-user)[Get aggregated builder leaderboard](/api-reference/builders/get-aggregated-builder-leaderboard)

⌘I

---


## API: Get Trades

> Source: https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Core

Get trades for a user or markets

GET

/

trades

Try it

Get trades for a user or markets

cURL

Copy

```shiki
curl --request GET \
  --url https://data-api.polymarket.com/trades
```

200

400

401

500

Copy

```shiki
[
  {
    "proxyWallet": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",
    "side": "BUY",
    "asset": "<string>",
    "conditionId": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",
    "size": 123,
    "price": 123,
    "timestamp": 123,
    "title": "<string>",
    "slug": "<string>",
    "icon": "<string>",
    "eventSlug": "<string>",
    "outcome": "<string>",
    "outcomeIndex": 123,
    "name": "<string>",
    "pseudonym": "<string>",
    "bio": "<string>",
    "profileImage": "<string>",
    "profileImageOptimized": "<string>",
    "transactionHash": "<string>"
  }
]
```

#### Query Parameters

[​](#parameter-limit)

limit

integer

default:100

Required range: `0 <= x <= 10000`

[​](#parameter-offset)

offset

integer

default:0

Required range: `0 <= x <= 10000`

[​](#parameter-taker-only)

takerOnly

boolean

default:true

[​](#parameter-filter-type)

filterType

enum<string>

Must be provided together with filterAmount.

Available options:

`CASH`,

`TOKENS`

[​](#parameter-filter-amount)

filterAmount

number

Must be provided together with filterType.

Required range: `x >= 0`

[​](#parameter-market)

market

string[]

Comma-separated list of condition IDs. Mutually exclusive with eventId.

0x-prefixed 64-hex string

[​](#parameter-event-id)

eventId

integer[]

Comma-separated list of event IDs. Mutually exclusive with market.

Required range: `x >= 1`

[​](#parameter-user)

user

string

User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

[​](#parameter-side)

side

enum<string>

Available options:

`BUY`,

`SELL`

#### Response

200

application/json

Success

[​](#response-items-proxy-wallet)

proxyWallet

string

User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

[​](#response-items-side)

side

enum<string>

Available options:

`BUY`,

`SELL`

[​](#response-items-asset)

asset

string

[​](#response-items-condition-id)

conditionId

string

0x-prefixed 64-hex string

Example:

`"0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917"`

[​](#response-items-size)

size

number

[​](#response-items-price)

price

number

[​](#response-items-timestamp)

timestamp

integer<int64>

[​](#response-items-title)

title

string

[​](#response-items-slug)

slug

string

[​](#response-items-icon)

icon

string

[​](#response-items-event-slug)

eventSlug

string

[​](#response-items-outcome)

outcome

string

[​](#response-items-outcome-index)

outcomeIndex

integer

[​](#response-items-name)

name

string

[​](#response-items-pseudonym)

pseudonym

string

[​](#response-items-bio)

bio

string

[​](#response-items-profile-image)

profileImage

string

[​](#response-items-profile-image-optimized)

profileImageOptimized

string

[​](#response-items-transaction-hash)

transactionHash

string

[Get current positions for a user](/api-reference/core/get-current-positions-for-a-user)[Get user activity](/api-reference/core/get-user-activity)

⌘I

---


## API: Get User Activity

> Source: https://docs.polymarket.com/api-reference/core/get-user-activity

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Core

Get user activity

GET

/

activity

Try it

Get user activity

cURL

Copy

```shiki
curl --request GET \
  --url https://data-api.polymarket.com/activity
```

200

400

401

500

Copy

```shiki
[
  {
    "proxyWallet": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",
    "timestamp": 123,
    "conditionId": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",
    "type": "TRADE",
    "size": 123,
    "usdcSize": 123,
    "transactionHash": "<string>",
    "price": 123,
    "asset": "<string>",
    "side": "BUY",
    "outcomeIndex": 123,
    "title": "<string>",
    "slug": "<string>",
    "icon": "<string>",
    "eventSlug": "<string>",
    "outcome": "<string>",
    "name": "<string>",
    "pseudonym": "<string>",
    "bio": "<string>",
    "profileImage": "<string>",
    "profileImageOptimized": "<string>"
  }
]
```

#### Query Parameters

[​](#parameter-limit)

limit

integer

default:100

Required range: `0 <= x <= 500`

[​](#parameter-offset)

offset

integer

default:0

Required range: `0 <= x <= 10000`

[​](#parameter-user)

user

string

required

User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

[​](#parameter-market)

market

string[]

Comma-separated list of condition IDs. Mutually exclusive with eventId.

0x-prefixed 64-hex string

[​](#parameter-event-id)

eventId

integer[]

Comma-separated list of event IDs. Mutually exclusive with market.

Required range: `x >= 1`

[​](#parameter-type)

type

enum<string>[]

Available options:

`TRADE`,

`SPLIT`,

`MERGE`,

`REDEEM`,

`REWARD`,

`CONVERSION`,

`MAKER_REBATE`

[​](#parameter-start)

start

integer

Required range: `x >= 0`

[​](#parameter-end)

end

integer

Required range: `x >= 0`

[​](#parameter-sort-by)

sortBy

enum<string>

default:TIMESTAMP

Available options:

`TIMESTAMP`,

`TOKENS`,

`CASH`

[​](#parameter-sort-direction)

sortDirection

enum<string>

default:DESC

Available options:

`ASC`,

`DESC`

[​](#parameter-side)

side

enum<string>

Available options:

`BUY`,

`SELL`

#### Response

200

application/json

Success

[​](#response-items-proxy-wallet)

proxyWallet

string

User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

[​](#response-items-timestamp)

timestamp

integer<int64>

[​](#response-items-condition-id)

conditionId

string

0x-prefixed 64-hex string

Example:

`"0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917"`

[​](#response-items-type)

type

enum<string>

Available options:

`TRADE`,

`SPLIT`,

`MERGE`,

`REDEEM`,

`REWARD`,

`CONVERSION`,

`MAKER_REBATE`

[​](#response-items-size)

size

number

[​](#response-items-usdc-size)

usdcSize

number

[​](#response-items-transaction-hash)

transactionHash

string

[​](#response-items-price)

price

number

[​](#response-items-asset)

asset

string

[​](#response-items-side)

side

enum<string>

Available options:

`BUY`,

`SELL`

[​](#response-items-outcome-index)

outcomeIndex

integer

[​](#response-items-title)

title

string

[​](#response-items-slug)

slug

string

[​](#response-items-icon)

icon

string

[​](#response-items-event-slug)

eventSlug

string

[​](#response-items-outcome)

outcome

string

[​](#response-items-name)

name

string

[​](#response-items-pseudonym)

pseudonym

string

[​](#response-items-bio)

bio

string

[​](#response-items-profile-image)

profileImage

string

[​](#response-items-profile-image-optimized)

profileImageOptimized

string

[Get trades for a user or markets](/api-reference/core/get-trades-for-a-user-or-markets)[Get top holders for markets](/api-reference/core/get-top-holders-for-markets)

⌘I

---


## API: Data API Health Check

> Source: https://docs.polymarket.com/api-reference/data-api-status/data-api-health-check

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Data API Status

Data API Health check

GET

Try it

Data API Health check

cURL

Copy

```shiki
curl --request GET \
  --url https://data-api.polymarket.com/
```

200

Copy

```shiki
{
  "data": "OK"
}
```

#### Response

200 - application/json

OK

[​](#response-data)

data

string

Example:

`"OK"`

[Search markets, events, and profiles](/api-reference/search/search-markets-events-and-profiles)[Download an accounting snapshot (ZIP of CSVs)](/api-reference/misc/download-an-accounting-snapshot-zip-of-csvs)

⌘I

---


## API: Get Event by ID

> Source: https://docs.polymarket.com/api-reference/events/get-event-by-id

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Events

Get event by id

GET

/

events

/

{id}

Try it

Get event by id

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/events/{id}
```

200

Copy

```shiki
{
  "id": "<string>",
  "ticker": "<string>",
  "slug": "<string>",
  "title": "<string>",
  "subtitle": "<string>",
  "description": "<string>",
  "resolutionSource": "<string>",
  "startDate": "2023-11-07T05:31:56Z",
  "creationDate": "2023-11-07T05:31:56Z",
  "endDate": "2023-11-07T05:31:56Z",
  "image": "<string>",
  "icon": "<string>",
  "active": true,
  "closed": true,
  "archived": true,
  "new": true,
  "featured": true,
  "restricted": true,
  "liquidity": 123,
  "volume": 123,
  "openInterest": 123,
  "sortBy": "<string>",
  "category": "<string>",
  "subcategory": "<string>",
  "isTemplate": true,
  "templateVariables": "<string>",
  "published_at": "<string>",
  "createdBy": "<string>",
  "updatedBy": "<string>",
  "createdAt": "2023-11-07T05:31:56Z",
  "updatedAt": "2023-11-07T05:31:56Z",
  "commentsEnabled": true,
  "competitive": 123,
  "volume24hr": 123,
  "volume1wk": 123,
  "volume1mo": 123,
  "volume1yr": 123,
  "featuredImage": "<string>",
  "disqusThread": "<string>",
  "parentEvent": "<string>",
  "enableOrderBook": true,
  "liquidityAmm": 123,
  "liquidityClob": 123,
  "negRisk": true,
  "negRiskMarketID": "<string>",
  "negRiskFeeBips": 123,
  "commentCount": 123,
  "imageOptimized": {
    "id": "<string>",
    "imageUrlSource": "<string>",
    "imageUrlOptimized": "<string>",
    "imageSizeKbSource": 123,
    "imageSizeKbOptimized": 123,
    "imageOptimizedComplete": true,
    "imageOptimizedLastUpdated": "<string>",
    "relID": 123,
    "field": "<string>",
    "relname": "<string>"
  },
  "iconOptimized": {
    "id": "<string>",
    "imageUrlSource": "<string>",
    "imageUrlOptimized": "<string>",
    "imageSizeKbSource": 123,
    "imageSizeKbOptimized": 123,
    "imageOptimizedComplete": true,
    "imageOptimizedLastUpdated": "<string>",
    "relID": 123,
    "field": "<string>",
    "relname": "<string>"
  },
  "featuredImageOptimized": {
    "id": "<string>",
    "imageUrlSource": "<string>",
    "imageUrlOptimized": "<string>",
    "imageSizeKbSource": 123,
    "imageSizeKbOptimized": 123,
    "imageOptimizedComplete": true,
    "imageOptimizedLastUpdated": "<string>",
    "relID": 123,
    "field": "<string>",
    "relname": "<string>"
  },
  "subEvents": [
    "<string>"
  ],
  "markets": [
    {
      "id": "<string>",
      "question": "<string>",
      "conditionId": "<string>",
      "slug": "<string>",
      "twitterCardImage": "<string>",
      "resolutionSource": "<string>",
      "endDate": "2023-11-07T05:31:56Z",
      "category": "<string>",
      "ammType": "<string>",
      "liquidity": "<string>",
      "sponsorName": "<string>",
      "sponsorImage": "<string>",
      "startDate": "2023-11-07T05:31:56Z",
      "xAxisValue": "<string>",
      "yAxisValue": "<string>",
      "denominationToken": "<string>",
      "fee": "<string>",
      "image": "<string>",
      "icon": "<string>",
      "lowerBound": "<string>",
      "upperBound": "<string>",
      "description": "<string>",
      "outcomes": "<string>",
      "outcomePrices": "<string>",
      "volume": "<string>",
      "active": true,
      "marketType": "<string>",
      "formatType": "<string>",
      "lowerBoundDate": "<string>",
      "upperBoundDate": "<string>",
      "closed": true,
      "marketMakerAddress": "<string>",
      "createdBy": 123,
      "updatedBy": 123,
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "closedTime": "<string>",
      "wideFormat": true,
      "new": true,
      "mailchimpTag": "<string>",
      "featured": true,
      "archived": true,
      "resolvedBy": "<string>",
      "restricted": true,
      "marketGroup": 123,
      "groupItemTitle": "<string>",
      "groupItemThreshold": "<string>",
      "questionID": "<string>",
      "umaEndDate": "<string>",
      "enableOrderBook": true,
      "orderPriceMinTickSize": 123,
      "orderMinSize": 123,
      "umaResolutionStatus": "<string>",
      "curationOrder": 123,
      "volumeNum": 123,
      "liquidityNum": 123,
      "endDateIso": "<string>",
      "startDateIso": "<string>",
      "umaEndDateIso": "<string>",
      "hasReviewedDates": true,
      "readyForCron": true,
      "commentsEnabled": true,
      "volume24hr": 123,
      "volume1wk": 123,
      "volume1mo": 123,
      "volume1yr": 123,
      "gameStartTime": "<string>",
      "secondsDelay": 123,
      "clobTokenIds": "<string>",
      "disqusThread": "<string>",
      "shortOutcomes": "<string>",
      "teamAID": "<string>",
      "teamBID": "<string>",
      "umaBond": "<string>",
      "umaReward": "<string>",
      "fpmmLive": true,
      "volume24hrAmm": 123,
      "volume1wkAmm": 123,
      "volume1moAmm": 123,
      "volume1yrAmm": 123,
      "volume24hrClob": 123,
      "volume1wkClob": 123,
      "volume1moClob": 123,
      "volume1yrClob": 123,
      "volumeAmm": 123,
      "volumeClob": 123,
      "liquidityAmm": 123,
      "liquidityClob": 123,
      "makerBaseFee": 123,
      "takerBaseFee": 123,
      "customLiveness": 123,
      "acceptingOrders": true,
      "notificationsEnabled": true,
      "score": 123,
      "imageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "iconOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "events": "<array>",
      "categories": [
        {
          "id": "<string>",
          "label": "<string>",
          "parentCategory": "<string>",
          "slug": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z"
        }
      ],
      "tags": [
        {
          "id": "<string>",
          "label": "<string>",
          "slug": "<string>",
          "forceShow": true,
          "publishedAt": "<string>",
          "createdBy": 123,
          "updatedBy": 123,
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "forceHide": true,
          "isCarousel": true
        }
      ],
      "creator": "<string>",
      "ready": true,
      "funded": true,
      "pastSlugs": "<string>",
      "readyTimestamp": "2023-11-07T05:31:56Z",
      "fundedTimestamp": "2023-11-07T05:31:56Z",
      "acceptingOrdersTimestamp": "2023-11-07T05:31:56Z",
      "competitive": 123,
      "rewardsMinSize": 123,
      "rewardsMaxSpread": 123,
      "spread": 123,
      "automaticallyResolved": true,
      "oneDayPriceChange": 123,
      "oneHourPriceChange": 123,
      "oneWeekPriceChange": 123,
      "oneMonthPriceChange": 123,
      "oneYearPriceChange": 123,
      "lastTradePrice": 123,
      "bestBid": 123,
      "bestAsk": 123,
      "automaticallyActive": true,
      "clearBookOnStart": true,
      "chartColor": "<string>",
      "seriesColor": "<string>",
      "showGmpSeries": true,
      "showGmpOutcome": true,
      "manualActivation": true,
      "negRiskOther": true,
      "gameId": "<string>",
      "groupItemRange": "<string>",
      "sportsMarketType": "<string>",
      "line": 123,
      "umaResolutionStatuses": "<string>",
      "pendingDeployment": true,
      "deploying": true,
      "deployingTimestamp": "2023-11-07T05:31:56Z",
      "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
      "rfqEnabled": true,
      "eventStartTime": "2023-11-07T05:31:56Z"
    }
  ],
  "series": [
    {
      "id": "<string>",
      "ticker": "<string>",
      "slug": "<string>",
      "title": "<string>",
      "subtitle": "<string>",
      "seriesType": "<string>",
      "recurrence": "<string>",
      "description": "<string>",
      "image": "<string>",
      "icon": "<string>",
      "layout": "<string>",
      "active": true,
      "closed": true,
      "archived": true,
      "new": true,
      "featured": true,
      "restricted": true,
      "isTemplate": true,
      "templateVariables": true,
      "publishedAt": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "commentsEnabled": true,
      "competitive": "<string>",
      "volume24hr": 123,
      "volume": 123,
      "liquidity": 123,
      "startDate": "2023-11-07T05:31:56Z",
      "pythTokenID": "<string>",
      "cgAssetName": "<string>",
      "score": 123,
      "events": "<array>",
      "collections": [
        {
          "id": "<string>",
          "ticker": "<string>",
          "slug": "<string>",
          "title": "<string>",
          "subtitle": "<string>",
          "collectionType": "<string>",
          "description": "<string>",
          "tags": "<string>",
          "image": "<string>",
          "icon": "<string>",
          "headerImage": "<string>",
          "layout": "<string>",
          "active": true,
          "closed": true,
          "archived": true,
          "new": true,
          "featured": true,
          "restricted": true,
          "isTemplate": true,
          "templateVariables": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "commentsEnabled": true,
          "imageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "iconOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "headerImageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          }
        }
      ],
      "categories": [
        {
          "id": "<string>",
          "label": "<string>",
          "parentCategory": "<string>",
          "slug": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z"
        }
      ],
      "tags": [
        {
          "id": "<string>",
          "label": "<string>",
          "slug": "<string>",
          "forceShow": true,
          "publishedAt": "<string>",
          "createdBy": 123,
          "updatedBy": 123,
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "forceHide": true,
          "isCarousel": true
        }
      ],
      "commentCount": 123,
      "chats": [
        {
          "id": "<string>",
          "channelId": "<string>",
          "channelName": "<string>",
          "channelImage": "<string>",
          "live": true,
          "startTime": "2023-11-07T05:31:56Z",
          "endTime": "2023-11-07T05:31:56Z"
        }
      ]
    }
  ],
  "categories": [
    {
      "id": "<string>",
      "label": "<string>",
      "parentCategory": "<string>",
      "slug": "<string>",
      "publishedAt": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z"
    }
  ],
  "collections": [
    {
      "id": "<string>",
      "ticker": "<string>",
      "slug": "<string>",
      "title": "<string>",
      "subtitle": "<string>",
      "collectionType": "<string>",
      "description": "<string>",
      "tags": "<string>",
      "image": "<string>",
      "icon": "<string>",
      "headerImage": "<string>",
      "layout": "<string>",
      "active": true,
      "closed": true,
      "archived": true,
      "new": true,
      "featured": true,
      "restricted": true,
      "isTemplate": true,
      "templateVariables": "<string>",
      "publishedAt": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "commentsEnabled": true,
      "imageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "iconOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "headerImageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      }
    }
  ],
  "tags": [
    {
      "id": "<string>",
      "label": "<string>",
      "slug": "<string>",
      "forceShow": true,
      "publishedAt": "<string>",
      "createdBy": 123,
      "updatedBy": 123,
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "forceHide": true,
      "isCarousel": true
    }
  ],
  "cyom": true,
  "closedTime": "2023-11-07T05:31:56Z",
  "showAllOutcomes": true,
  "showMarketImages": true,
  "automaticallyResolved": true,
  "enableNegRisk": true,
  "automaticallyActive": true,
  "eventDate": "<string>",
  "startTime": "2023-11-07T05:31:56Z",
  "eventWeek": 123,
  "seriesSlug": "<string>",
  "score": "<string>",
  "elapsed": "<string>",
  "period": "<string>",
  "live": true,
  "ended": true,
  "finishedTimestamp": "2023-11-07T05:31:56Z",
  "gmpChartMode": "<string>",
  "eventCreators": [
    {
      "id": "<string>",
      "creatorName": "<string>",
      "creatorHandle": "<string>",
      "creatorUrl": "<string>",
      "creatorImage": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z"
    }
  ],
  "tweetCount": 123,
  "chats": [
    {
      "id": "<string>",
      "channelId": "<string>",
      "channelName": "<string>",
      "channelImage": "<string>",
      "live": true,
      "startTime": "2023-11-07T05:31:56Z",
      "endTime": "2023-11-07T05:31:56Z"
    }
  ],
  "featuredOrder": 123,
  "estimateValue": true,
  "cantEstimate": true,
  "estimatedValue": "<string>",
  "templates": [
    {
      "id": "<string>",
      "eventTitle": "<string>",
      "eventSlug": "<string>",
      "eventImage": "<string>",
      "marketTitle": "<string>",
      "description": "<string>",
      "resolutionSource": "<string>",
      "negRisk": true,
      "sortBy": "<string>",
      "showMarketImages": true,
      "seriesSlug": "<string>",
      "outcomes": "<string>"
    }
  ],
  "spreadsMainLine": 123,
  "totalsMainLine": 123,
  "carouselMap": "<string>",
  "pendingDeployment": true,
  "deploying": true,
  "deployingTimestamp": "2023-11-07T05:31:56Z",
  "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
  "gameStatus": "<string>"
}
```

#### Path Parameters

[​](#parameter-id)

id

integer

required

#### Query Parameters

[​](#parameter-include-chat)

include\_chat

boolean

[​](#parameter-include-template)

include\_template

boolean

#### Response

200

application/json

Event

[​](#response-id)

id

string

[​](#response-ticker-one-of-0)

ticker

string | null

[​](#response-slug-one-of-0)

slug

string | null

[​](#response-title-one-of-0)

title

string | null

[​](#response-subtitle-one-of-0)

subtitle

string | null

[​](#response-description-one-of-0)

description

string | null

[​](#response-resolution-source-one-of-0)

resolutionSource

string | null

[​](#response-start-date-one-of-0)

startDate

string<date-time> | null

[​](#response-creation-date-one-of-0)

creationDate

string<date-time> | null

[​](#response-end-date-one-of-0)

endDate

string<date-time> | null

[​](#response-image-one-of-0)

image

string | null

[​](#response-icon-one-of-0)

icon

string | null

[​](#response-active-one-of-0)

active

boolean | null

[​](#response-closed-one-of-0)

closed

boolean | null

[​](#response-archived-one-of-0)

archived

boolean | null

[​](#response-new-one-of-0)

new

boolean | null

[​](#response-featured-one-of-0)

featured

boolean | null

[​](#response-restricted-one-of-0)

restricted

boolean | null

[​](#response-liquidity-one-of-0)

liquidity

number | null

[​](#response-volume-one-of-0)

volume

number | null

[​](#response-open-interest-one-of-0)

openInterest

number | null

[​](#response-sort-by-one-of-0)

sortBy

string | null

[​](#response-category-one-of-0)

category

string | null

[​](#response-subcategory-one-of-0)

subcategory

string | null

[​](#response-is-template-one-of-0)

isTemplate

boolean | null

[​](#response-template-variables-one-of-0)

templateVariables

string | null

[​](#response-published-at-one-of-0)

published\_at

string | null

[​](#response-created-by-one-of-0)

createdBy

string | null

[​](#response-updated-by-one-of-0)

updatedBy

string | null

[​](#response-created-at-one-of-0)

createdAt

string<date-time> | null

[​](#response-updated-at-one-of-0)

updatedAt

string<date-time> | null

[​](#response-comments-enabled-one-of-0)

commentsEnabled

boolean | null

[​](#response-competitive-one-of-0)

competitive

number | null

[​](#response-volume24hr-one-of-0)

volume24hr

number | null

[​](#response-volume1wk-one-of-0)

volume1wk

number | null

[​](#response-volume1mo-one-of-0)

volume1mo

number | null

[​](#response-volume1yr-one-of-0)

volume1yr

number | null

[​](#response-featured-image-one-of-0)

featuredImage

string | null

[​](#response-disqus-thread-one-of-0)

disqusThread

string | null

[​](#response-parent-event-one-of-0)

parentEvent

string | null

[​](#response-enable-order-book-one-of-0)

enableOrderBook

boolean | null

[​](#response-liquidity-amm-one-of-0)

liquidityAmm

number | null

[​](#response-liquidity-clob-one-of-0)

liquidityClob

number | null

[​](#response-neg-risk-one-of-0)

negRisk

boolean | null

[​](#response-neg-risk-market-id-one-of-0)

negRiskMarketID

string | null

[​](#response-neg-risk-fee-bips-one-of-0)

negRiskFeeBips

integer | null

[​](#response-comment-count-one-of-0)

commentCount

integer | null

[​](#response-image-optimized)

imageOptimized

object

Show child attributes

[​](#response-icon-optimized)

iconOptimized

object

Show child attributes

[​](#response-featured-image-optimized)

featuredImageOptimized

object

Show child attributes

[​](#response-sub-events-one-of-0)

subEvents

string[] | null

[​](#response-markets)

markets

object[]

Show child attributes

[​](#response-series)

series

object[]

Show child attributes

[​](#response-categories)

categories

object[]

Show child attributes

[​](#response-collections)

collections

object[]

Show child attributes

[​](#response-tags)

tags

object[]

Show child attributes

[​](#response-cyom-one-of-0)

cyom

boolean | null

[​](#response-closed-time-one-of-0)

closedTime

string<date-time> | null

[​](#response-show-all-outcomes-one-of-0)

showAllOutcomes

boolean | null

[​](#response-show-market-images-one-of-0)

showMarketImages

boolean | null

[​](#response-automatically-resolved-one-of-0)

automaticallyResolved

boolean | null

[​](#response-enable-neg-risk-one-of-0)

enableNegRisk

boolean | null

[​](#response-automatically-active-one-of-0)

automaticallyActive

boolean | null

[​](#response-event-date-one-of-0)

eventDate

string | null

[​](#response-start-time-one-of-0)

startTime

string<date-time> | null

[​](#response-event-week-one-of-0)

eventWeek

integer | null

[​](#response-series-slug-one-of-0)

seriesSlug

string | null

[​](#response-score-one-of-0)

score

string | null

[​](#response-elapsed-one-of-0)

elapsed

string | null

[​](#response-period-one-of-0)

period

string | null

[​](#response-live-one-of-0)

live

boolean | null

[​](#response-ended-one-of-0)

ended

boolean | null

[​](#response-finished-timestamp-one-of-0)

finishedTimestamp

string<date-time> | null

[​](#response-gmp-chart-mode-one-of-0)

gmpChartMode

string | null

[​](#response-event-creators)

eventCreators

object[]

Show child attributes

[​](#response-tweet-count-one-of-0)

tweetCount

integer | null

[​](#response-chats)

chats

object[]

Show child attributes

[​](#response-featured-order-one-of-0)

featuredOrder

integer | null

[​](#response-estimate-value-one-of-0)

estimateValue

boolean | null

[​](#response-cant-estimate-one-of-0)

cantEstimate

boolean | null

[​](#response-estimated-value-one-of-0)

estimatedValue

string | null

[​](#response-templates)

templates

object[]

Show child attributes

[​](#response-spreads-main-line-one-of-0)

spreadsMainLine

number | null

[​](#response-totals-main-line-one-of-0)

totalsMainLine

number | null

[​](#response-carousel-map-one-of-0)

carouselMap

string | null

[​](#response-pending-deployment-one-of-0)

pendingDeployment

boolean | null

[​](#response-deploying-one-of-0)

deploying

boolean | null

[​](#response-deploying-timestamp-one-of-0)

deployingTimestamp

string<date-time> | null

[​](#response-scheduled-deployment-timestamp-one-of-0)

scheduledDeploymentTimestamp

string<date-time> | null

[​](#response-game-status-one-of-0)

gameStatus

string | null

[List events](/api-reference/events/list-events)[Get event tags](/api-reference/events/get-event-tags)

⌘I

---


## API: Get Event by Slug

> Source: https://docs.polymarket.com/api-reference/events/get-event-by-slug

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Events

Get event by slug

GET

/

events

/

slug

/

{slug}

Try it

Get event by slug

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/events/slug/{slug}
```

200

Copy

```shiki
{
  "id": "<string>",
  "ticker": "<string>",
  "slug": "<string>",
  "title": "<string>",
  "subtitle": "<string>",
  "description": "<string>",
  "resolutionSource": "<string>",
  "startDate": "2023-11-07T05:31:56Z",
  "creationDate": "2023-11-07T05:31:56Z",
  "endDate": "2023-11-07T05:31:56Z",
  "image": "<string>",
  "icon": "<string>",
  "active": true,
  "closed": true,
  "archived": true,
  "new": true,
  "featured": true,
  "restricted": true,
  "liquidity": 123,
  "volume": 123,
  "openInterest": 123,
  "sortBy": "<string>",
  "category": "<string>",
  "subcategory": "<string>",
  "isTemplate": true,
  "templateVariables": "<string>",
  "published_at": "<string>",
  "createdBy": "<string>",
  "updatedBy": "<string>",
  "createdAt": "2023-11-07T05:31:56Z",
  "updatedAt": "2023-11-07T05:31:56Z",
  "commentsEnabled": true,
  "competitive": 123,
  "volume24hr": 123,
  "volume1wk": 123,
  "volume1mo": 123,
  "volume1yr": 123,
  "featuredImage": "<string>",
  "disqusThread": "<string>",
  "parentEvent": "<string>",
  "enableOrderBook": true,
  "liquidityAmm": 123,
  "liquidityClob": 123,
  "negRisk": true,
  "negRiskMarketID": "<string>",
  "negRiskFeeBips": 123,
  "commentCount": 123,
  "imageOptimized": {
    "id": "<string>",
    "imageUrlSource": "<string>",
    "imageUrlOptimized": "<string>",
    "imageSizeKbSource": 123,
    "imageSizeKbOptimized": 123,
    "imageOptimizedComplete": true,
    "imageOptimizedLastUpdated": "<string>",
    "relID": 123,
    "field": "<string>",
    "relname": "<string>"
  },
  "iconOptimized": {
    "id": "<string>",
    "imageUrlSource": "<string>",
    "imageUrlOptimized": "<string>",
    "imageSizeKbSource": 123,
    "imageSizeKbOptimized": 123,
    "imageOptimizedComplete": true,
    "imageOptimizedLastUpdated": "<string>",
    "relID": 123,
    "field": "<string>",
    "relname": "<string>"
  },
  "featuredImageOptimized": {
    "id": "<string>",
    "imageUrlSource": "<string>",
    "imageUrlOptimized": "<string>",
    "imageSizeKbSource": 123,
    "imageSizeKbOptimized": 123,
    "imageOptimizedComplete": true,
    "imageOptimizedLastUpdated": "<string>",
    "relID": 123,
    "field": "<string>",
    "relname": "<string>"
  },
  "subEvents": [
    "<string>"
  ],
  "markets": [
    {
      "id": "<string>",
      "question": "<string>",
      "conditionId": "<string>",
      "slug": "<string>",
      "twitterCardImage": "<string>",
      "resolutionSource": "<string>",
      "endDate": "2023-11-07T05:31:56Z",
      "category": "<string>",
      "ammType": "<string>",
      "liquidity": "<string>",
      "sponsorName": "<string>",
      "sponsorImage": "<string>",
      "startDate": "2023-11-07T05:31:56Z",
      "xAxisValue": "<string>",
      "yAxisValue": "<string>",
      "denominationToken": "<string>",
      "fee": "<string>",
      "image": "<string>",
      "icon": "<string>",
      "lowerBound": "<string>",
      "upperBound": "<string>",
      "description": "<string>",
      "outcomes": "<string>",
      "outcomePrices": "<string>",
      "volume": "<string>",
      "active": true,
      "marketType": "<string>",
      "formatType": "<string>",
      "lowerBoundDate": "<string>",
      "upperBoundDate": "<string>",
      "closed": true,
      "marketMakerAddress": "<string>",
      "createdBy": 123,
      "updatedBy": 123,
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "closedTime": "<string>",
      "wideFormat": true,
      "new": true,
      "mailchimpTag": "<string>",
      "featured": true,
      "archived": true,
      "resolvedBy": "<string>",
      "restricted": true,
      "marketGroup": 123,
      "groupItemTitle": "<string>",
      "groupItemThreshold": "<string>",
      "questionID": "<string>",
      "umaEndDate": "<string>",
      "enableOrderBook": true,
      "orderPriceMinTickSize": 123,
      "orderMinSize": 123,
      "umaResolutionStatus": "<string>",
      "curationOrder": 123,
      "volumeNum": 123,
      "liquidityNum": 123,
      "endDateIso": "<string>",
      "startDateIso": "<string>",
      "umaEndDateIso": "<string>",
      "hasReviewedDates": true,
      "readyForCron": true,
      "commentsEnabled": true,
      "volume24hr": 123,
      "volume1wk": 123,
      "volume1mo": 123,
      "volume1yr": 123,
      "gameStartTime": "<string>",
      "secondsDelay": 123,
      "clobTokenIds": "<string>",
      "disqusThread": "<string>",
      "shortOutcomes": "<string>",
      "teamAID": "<string>",
      "teamBID": "<string>",
      "umaBond": "<string>",
      "umaReward": "<string>",
      "fpmmLive": true,
      "volume24hrAmm": 123,
      "volume1wkAmm": 123,
      "volume1moAmm": 123,
      "volume1yrAmm": 123,
      "volume24hrClob": 123,
      "volume1wkClob": 123,
      "volume1moClob": 123,
      "volume1yrClob": 123,
      "volumeAmm": 123,
      "volumeClob": 123,
      "liquidityAmm": 123,
      "liquidityClob": 123,
      "makerBaseFee": 123,
      "takerBaseFee": 123,
      "customLiveness": 123,
      "acceptingOrders": true,
      "notificationsEnabled": true,
      "score": 123,
      "imageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "iconOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "events": "<array>",
      "categories": [
        {
          "id": "<string>",
          "label": "<string>",
          "parentCategory": "<string>",
          "slug": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z"
        }
      ],
      "tags": [
        {
          "id": "<string>",
          "label": "<string>",
          "slug": "<string>",
          "forceShow": true,
          "publishedAt": "<string>",
          "createdBy": 123,
          "updatedBy": 123,
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "forceHide": true,
          "isCarousel": true
        }
      ],
      "creator": "<string>",
      "ready": true,
      "funded": true,
      "pastSlugs": "<string>",
      "readyTimestamp": "2023-11-07T05:31:56Z",
      "fundedTimestamp": "2023-11-07T05:31:56Z",
      "acceptingOrdersTimestamp": "2023-11-07T05:31:56Z",
      "competitive": 123,
      "rewardsMinSize": 123,
      "rewardsMaxSpread": 123,
      "spread": 123,
      "automaticallyResolved": true,
      "oneDayPriceChange": 123,
      "oneHourPriceChange": 123,
      "oneWeekPriceChange": 123,
      "oneMonthPriceChange": 123,
      "oneYearPriceChange": 123,
      "lastTradePrice": 123,
      "bestBid": 123,
      "bestAsk": 123,
      "automaticallyActive": true,
      "clearBookOnStart": true,
      "chartColor": "<string>",
      "seriesColor": "<string>",
      "showGmpSeries": true,
      "showGmpOutcome": true,
      "manualActivation": true,
      "negRiskOther": true,
      "gameId": "<string>",
      "groupItemRange": "<string>",
      "sportsMarketType": "<string>",
      "line": 123,
      "umaResolutionStatuses": "<string>",
      "pendingDeployment": true,
      "deploying": true,
      "deployingTimestamp": "2023-11-07T05:31:56Z",
      "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
      "rfqEnabled": true,
      "eventStartTime": "2023-11-07T05:31:56Z"
    }
  ],
  "series": [
    {
      "id": "<string>",
      "ticker": "<string>",
      "slug": "<string>",
      "title": "<string>",
      "subtitle": "<string>",
      "seriesType": "<string>",
      "recurrence": "<string>",
      "description": "<string>",
      "image": "<string>",
      "icon": "<string>",
      "layout": "<string>",
      "active": true,
      "closed": true,
      "archived": true,
      "new": true,
      "featured": true,
      "restricted": true,
      "isTemplate": true,
      "templateVariables": true,
      "publishedAt": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "commentsEnabled": true,
      "competitive": "<string>",
      "volume24hr": 123,
      "volume": 123,
      "liquidity": 123,
      "startDate": "2023-11-07T05:31:56Z",
      "pythTokenID": "<string>",
      "cgAssetName": "<string>",
      "score": 123,
      "events": "<array>",
      "collections": [
        {
          "id": "<string>",
          "ticker": "<string>",
          "slug": "<string>",
          "title": "<string>",
          "subtitle": "<string>",
          "collectionType": "<string>",
          "description": "<string>",
          "tags": "<string>",
          "image": "<string>",
          "icon": "<string>",
          "headerImage": "<string>",
          "layout": "<string>",
          "active": true,
          "closed": true,
          "archived": true,
          "new": true,
          "featured": true,
          "restricted": true,
          "isTemplate": true,
          "templateVariables": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "commentsEnabled": true,
          "imageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "iconOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "headerImageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          }
        }
      ],
      "categories": [
        {
          "id": "<string>",
          "label": "<string>",
          "parentCategory": "<string>",
          "slug": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z"
        }
      ],
      "tags": [
        {
          "id": "<string>",
          "label": "<string>",
          "slug": "<string>",
          "forceShow": true,
          "publishedAt": "<string>",
          "createdBy": 123,
          "updatedBy": 123,
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "forceHide": true,
          "isCarousel": true
        }
      ],
      "commentCount": 123,
      "chats": [
        {
          "id": "<string>",
          "channelId": "<string>",
          "channelName": "<string>",
          "channelImage": "<string>",
          "live": true,
          "startTime": "2023-11-07T05:31:56Z",
          "endTime": "2023-11-07T05:31:56Z"
        }
      ]
    }
  ],
  "categories": [
    {
      "id": "<string>",
      "label": "<string>",
      "parentCategory": "<string>",
      "slug": "<string>",
      "publishedAt": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z"
    }
  ],
  "collections": [
    {
      "id": "<string>",
      "ticker": "<string>",
      "slug": "<string>",
      "title": "<string>",
      "subtitle": "<string>",
      "collectionType": "<string>",
      "description": "<string>",
      "tags": "<string>",
      "image": "<string>",
      "icon": "<string>",
      "headerImage": "<string>",
      "layout": "<string>",
      "active": true,
      "closed": true,
      "archived": true,
      "new": true,
      "featured": true,
      "restricted": true,
      "isTemplate": true,
      "templateVariables": "<string>",
      "publishedAt": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "commentsEnabled": true,
      "imageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "iconOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "headerImageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      }
    }
  ],
  "tags": [
    {
      "id": "<string>",
      "label": "<string>",
      "slug": "<string>",
      "forceShow": true,
      "publishedAt": "<string>",
      "createdBy": 123,
      "updatedBy": 123,
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "forceHide": true,
      "isCarousel": true
    }
  ],
  "cyom": true,
  "closedTime": "2023-11-07T05:31:56Z",
  "showAllOutcomes": true,
  "showMarketImages": true,
  "automaticallyResolved": true,
  "enableNegRisk": true,
  "automaticallyActive": true,
  "eventDate": "<string>",
  "startTime": "2023-11-07T05:31:56Z",
  "eventWeek": 123,
  "seriesSlug": "<string>",
  "score": "<string>",
  "elapsed": "<string>",
  "period": "<string>",
  "live": true,
  "ended": true,
  "finishedTimestamp": "2023-11-07T05:31:56Z",
  "gmpChartMode": "<string>",
  "eventCreators": [
    {
      "id": "<string>",
      "creatorName": "<string>",
      "creatorHandle": "<string>",
      "creatorUrl": "<string>",
      "creatorImage": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z"
    }
  ],
  "tweetCount": 123,
  "chats": [
    {
      "id": "<string>",
      "channelId": "<string>",
      "channelName": "<string>",
      "channelImage": "<string>",
      "live": true,
      "startTime": "2023-11-07T05:31:56Z",
      "endTime": "2023-11-07T05:31:56Z"
    }
  ],
  "featuredOrder": 123,
  "estimateValue": true,
  "cantEstimate": true,
  "estimatedValue": "<string>",
  "templates": [
    {
      "id": "<string>",
      "eventTitle": "<string>",
      "eventSlug": "<string>",
      "eventImage": "<string>",
      "marketTitle": "<string>",
      "description": "<string>",
      "resolutionSource": "<string>",
      "negRisk": true,
      "sortBy": "<string>",
      "showMarketImages": true,
      "seriesSlug": "<string>",
      "outcomes": "<string>"
    }
  ],
  "spreadsMainLine": 123,
  "totalsMainLine": 123,
  "carouselMap": "<string>",
  "pendingDeployment": true,
  "deploying": true,
  "deployingTimestamp": "2023-11-07T05:31:56Z",
  "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
  "gameStatus": "<string>"
}
```

#### Path Parameters

[​](#parameter-slug)

slug

string

required

#### Query Parameters

[​](#parameter-include-chat)

include\_chat

boolean

[​](#parameter-include-template)

include\_template

boolean

#### Response

200

application/json

Event

[​](#response-id)

id

string

[​](#response-ticker-one-of-0)

ticker

string | null

[​](#response-slug-one-of-0)

slug

string | null

[​](#response-title-one-of-0)

title

string | null

[​](#response-subtitle-one-of-0)

subtitle

string | null

[​](#response-description-one-of-0)

description

string | null

[​](#response-resolution-source-one-of-0)

resolutionSource

string | null

[​](#response-start-date-one-of-0)

startDate

string<date-time> | null

[​](#response-creation-date-one-of-0)

creationDate

string<date-time> | null

[​](#response-end-date-one-of-0)

endDate

string<date-time> | null

[​](#response-image-one-of-0)

image

string | null

[​](#response-icon-one-of-0)

icon

string | null

[​](#response-active-one-of-0)

active

boolean | null

[​](#response-closed-one-of-0)

closed

boolean | null

[​](#response-archived-one-of-0)

archived

boolean | null

[​](#response-new-one-of-0)

new

boolean | null

[​](#response-featured-one-of-0)

featured

boolean | null

[​](#response-restricted-one-of-0)

restricted

boolean | null

[​](#response-liquidity-one-of-0)

liquidity

number | null

[​](#response-volume-one-of-0)

volume

number | null

[​](#response-open-interest-one-of-0)

openInterest

number | null

[​](#response-sort-by-one-of-0)

sortBy

string | null

[​](#response-category-one-of-0)

category

string | null

[​](#response-subcategory-one-of-0)

subcategory

string | null

[​](#response-is-template-one-of-0)

isTemplate

boolean | null

[​](#response-template-variables-one-of-0)

templateVariables

string | null

[​](#response-published-at-one-of-0)

published\_at

string | null

[​](#response-created-by-one-of-0)

createdBy

string | null

[​](#response-updated-by-one-of-0)

updatedBy

string | null

[​](#response-created-at-one-of-0)

createdAt

string<date-time> | null

[​](#response-updated-at-one-of-0)

updatedAt

string<date-time> | null

[​](#response-comments-enabled-one-of-0)

commentsEnabled

boolean | null

[​](#response-competitive-one-of-0)

competitive

number | null

[​](#response-volume24hr-one-of-0)

volume24hr

number | null

[​](#response-volume1wk-one-of-0)

volume1wk

number | null

[​](#response-volume1mo-one-of-0)

volume1mo

number | null

[​](#response-volume1yr-one-of-0)

volume1yr

number | null

[​](#response-featured-image-one-of-0)

featuredImage

string | null

[​](#response-disqus-thread-one-of-0)

disqusThread

string | null

[​](#response-parent-event-one-of-0)

parentEvent

string | null

[​](#response-enable-order-book-one-of-0)

enableOrderBook

boolean | null

[​](#response-liquidity-amm-one-of-0)

liquidityAmm

number | null

[​](#response-liquidity-clob-one-of-0)

liquidityClob

number | null

[​](#response-neg-risk-one-of-0)

negRisk

boolean | null

[​](#response-neg-risk-market-id-one-of-0)

negRiskMarketID

string | null

[​](#response-neg-risk-fee-bips-one-of-0)

negRiskFeeBips

integer | null

[​](#response-comment-count-one-of-0)

commentCount

integer | null

[​](#response-image-optimized)

imageOptimized

object

Show child attributes

[​](#response-icon-optimized)

iconOptimized

object

Show child attributes

[​](#response-featured-image-optimized)

featuredImageOptimized

object

Show child attributes

[​](#response-sub-events-one-of-0)

subEvents

string[] | null

[​](#response-markets)

markets

object[]

Show child attributes

[​](#response-series)

series

object[]

Show child attributes

[​](#response-categories)

categories

object[]

Show child attributes

[​](#response-collections)

collections

object[]

Show child attributes

[​](#response-tags)

tags

object[]

Show child attributes

[​](#response-cyom-one-of-0)

cyom

boolean | null

[​](#response-closed-time-one-of-0)

closedTime

string<date-time> | null

[​](#response-show-all-outcomes-one-of-0)

showAllOutcomes

boolean | null

[​](#response-show-market-images-one-of-0)

showMarketImages

boolean | null

[​](#response-automatically-resolved-one-of-0)

automaticallyResolved

boolean | null

[​](#response-enable-neg-risk-one-of-0)

enableNegRisk

boolean | null

[​](#response-automatically-active-one-of-0)

automaticallyActive

boolean | null

[​](#response-event-date-one-of-0)

eventDate

string | null

[​](#response-start-time-one-of-0)

startTime

string<date-time> | null

[​](#response-event-week-one-of-0)

eventWeek

integer | null

[​](#response-series-slug-one-of-0)

seriesSlug

string | null

[​](#response-score-one-of-0)

score

string | null

[​](#response-elapsed-one-of-0)

elapsed

string | null

[​](#response-period-one-of-0)

period

string | null

[​](#response-live-one-of-0)

live

boolean | null

[​](#response-ended-one-of-0)

ended

boolean | null

[​](#response-finished-timestamp-one-of-0)

finishedTimestamp

string<date-time> | null

[​](#response-gmp-chart-mode-one-of-0)

gmpChartMode

string | null

[​](#response-event-creators)

eventCreators

object[]

Show child attributes

[​](#response-tweet-count-one-of-0)

tweetCount

integer | null

[​](#response-chats)

chats

object[]

Show child attributes

[​](#response-featured-order-one-of-0)

featuredOrder

integer | null

[​](#response-estimate-value-one-of-0)

estimateValue

boolean | null

[​](#response-cant-estimate-one-of-0)

cantEstimate

boolean | null

[​](#response-estimated-value-one-of-0)

estimatedValue

string | null

[​](#response-templates)

templates

object[]

Show child attributes

[​](#response-spreads-main-line-one-of-0)

spreadsMainLine

number | null

[​](#response-totals-main-line-one-of-0)

totalsMainLine

number | null

[​](#response-carousel-map-one-of-0)

carouselMap

string | null

[​](#response-pending-deployment-one-of-0)

pendingDeployment

boolean | null

[​](#response-deploying-one-of-0)

deploying

boolean | null

[​](#response-deploying-timestamp-one-of-0)

deployingTimestamp

string<date-time> | null

[​](#response-scheduled-deployment-timestamp-one-of-0)

scheduledDeploymentTimestamp

string<date-time> | null

[​](#response-game-status-one-of-0)

gameStatus

string | null

[Get event tags](/api-reference/events/get-event-tags)[List markets](/api-reference/markets/list-markets)

⌘I

---


## API: Get Event Tags

> Source: https://docs.polymarket.com/api-reference/events/get-event-tags

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Events

Get event tags

GET

/

events

/

{id}

/

tags

Try it

Get event tags

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/events/{id}/tags
```

200

Copy

```shiki
[
  {
    "id": "<string>",
    "label": "<string>",
    "slug": "<string>",
    "forceShow": true,
    "publishedAt": "<string>",
    "createdBy": 123,
    "updatedBy": 123,
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "forceHide": true,
    "isCarousel": true
  }
]
```

#### Path Parameters

[​](#parameter-id)

id

integer

required

#### Response

200

application/json

Tags attached to the event

[​](#response-items-id)

id

string

[​](#response-items-label-one-of-0)

label

string | null

[​](#response-items-slug-one-of-0)

slug

string | null

[​](#response-items-force-show-one-of-0)

forceShow

boolean | null

[​](#response-items-published-at-one-of-0)

publishedAt

string | null

[​](#response-items-created-by-one-of-0)

createdBy

integer | null

[​](#response-items-updated-by-one-of-0)

updatedBy

integer | null

[​](#response-items-created-at-one-of-0)

createdAt

string<date-time> | null

[​](#response-items-updated-at-one-of-0)

updatedAt

string<date-time> | null

[​](#response-items-force-hide-one-of-0)

forceHide

boolean | null

[​](#response-items-is-carousel-one-of-0)

isCarousel

boolean | null

[Get event by id](/api-reference/events/get-event-by-id)[Get event by slug](/api-reference/events/get-event-by-slug)

⌘I

---


## API: List Events

> Source: https://docs.polymarket.com/api-reference/events/list-events

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Events

List events

GET

/

events

Try it

List events

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/events
```

200

Copy

```shiki
[
  {
    "id": "<string>",
    "ticker": "<string>",
    "slug": "<string>",
    "title": "<string>",
    "subtitle": "<string>",
    "description": "<string>",
    "resolutionSource": "<string>",
    "startDate": "2023-11-07T05:31:56Z",
    "creationDate": "2023-11-07T05:31:56Z",
    "endDate": "2023-11-07T05:31:56Z",
    "image": "<string>",
    "icon": "<string>",
    "active": true,
    "closed": true,
    "archived": true,
    "new": true,
    "featured": true,
    "restricted": true,
    "liquidity": 123,
    "volume": 123,
    "openInterest": 123,
    "sortBy": "<string>",
    "category": "<string>",
    "subcategory": "<string>",
    "isTemplate": true,
    "templateVariables": "<string>",
    "published_at": "<string>",
    "createdBy": "<string>",
    "updatedBy": "<string>",
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "commentsEnabled": true,
    "competitive": 123,
    "volume24hr": 123,
    "volume1wk": 123,
    "volume1mo": 123,
    "volume1yr": 123,
    "featuredImage": "<string>",
    "disqusThread": "<string>",
    "parentEvent": "<string>",
    "enableOrderBook": true,
    "liquidityAmm": 123,
    "liquidityClob": 123,
    "negRisk": true,
    "negRiskMarketID": "<string>",
    "negRiskFeeBips": 123,
    "commentCount": 123,
    "imageOptimized": {
      "id": "<string>",
      "imageUrlSource": "<string>",
      "imageUrlOptimized": "<string>",
      "imageSizeKbSource": 123,
      "imageSizeKbOptimized": 123,
      "imageOptimizedComplete": true,
      "imageOptimizedLastUpdated": "<string>",
      "relID": 123,
      "field": "<string>",
      "relname": "<string>"
    },
    "iconOptimized": {
      "id": "<string>",
      "imageUrlSource": "<string>",
      "imageUrlOptimized": "<string>",
      "imageSizeKbSource": 123,
      "imageSizeKbOptimized": 123,
      "imageOptimizedComplete": true,
      "imageOptimizedLastUpdated": "<string>",
      "relID": 123,
      "field": "<string>",
      "relname": "<string>"
    },
    "featuredImageOptimized": {
      "id": "<string>",
      "imageUrlSource": "<string>",
      "imageUrlOptimized": "<string>",
      "imageSizeKbSource": 123,
      "imageSizeKbOptimized": 123,
      "imageOptimizedComplete": true,
      "imageOptimizedLastUpdated": "<string>",
      "relID": 123,
      "field": "<string>",
      "relname": "<string>"
    },
    "subEvents": [
      "<string>"
    ],
    "markets": [
      {
        "id": "<string>",
        "question": "<string>",
        "conditionId": "<string>",
        "slug": "<string>",
        "twitterCardImage": "<string>",
        "resolutionSource": "<string>",
        "endDate": "2023-11-07T05:31:56Z",
        "category": "<string>",
        "ammType": "<string>",
        "liquidity": "<string>",
        "sponsorName": "<string>",
        "sponsorImage": "<string>",
        "startDate": "2023-11-07T05:31:56Z",
        "xAxisValue": "<string>",
        "yAxisValue": "<string>",
        "denominationToken": "<string>",
        "fee": "<string>",
        "image": "<string>",
        "icon": "<string>",
        "lowerBound": "<string>",
        "upperBound": "<string>",
        "description": "<string>",
        "outcomes": "<string>",
        "outcomePrices": "<string>",
        "volume": "<string>",
        "active": true,
        "marketType": "<string>",
        "formatType": "<string>",
        "lowerBoundDate": "<string>",
        "upperBoundDate": "<string>",
        "closed": true,
        "marketMakerAddress": "<string>",
        "createdBy": 123,
        "updatedBy": 123,
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z",
        "closedTime": "<string>",
        "wideFormat": true,
        "new": true,
        "mailchimpTag": "<string>",
        "featured": true,
        "archived": true,
        "resolvedBy": "<string>",
        "restricted": true,
        "marketGroup": 123,
        "groupItemTitle": "<string>",
        "groupItemThreshold": "<string>",
        "questionID": "<string>",
        "umaEndDate": "<string>",
        "enableOrderBook": true,
        "orderPriceMinTickSize": 123,
        "orderMinSize": 123,
        "umaResolutionStatus": "<string>",
        "curationOrder": 123,
        "volumeNum": 123,
        "liquidityNum": 123,
        "endDateIso": "<string>",
        "startDateIso": "<string>",
        "umaEndDateIso": "<string>",
        "hasReviewedDates": true,
        "readyForCron": true,
        "commentsEnabled": true,
        "volume24hr": 123,
        "volume1wk": 123,
        "volume1mo": 123,
        "volume1yr": 123,
        "gameStartTime": "<string>",
        "secondsDelay": 123,
        "clobTokenIds": "<string>",
        "disqusThread": "<string>",
        "shortOutcomes": "<string>",
        "teamAID": "<string>",
        "teamBID": "<string>",
        "umaBond": "<string>",
        "umaReward": "<string>",
        "fpmmLive": true,
        "volume24hrAmm": 123,
        "volume1wkAmm": 123,
        "volume1moAmm": 123,
        "volume1yrAmm": 123,
        "volume24hrClob": 123,
        "volume1wkClob": 123,
        "volume1moClob": 123,
        "volume1yrClob": 123,
        "volumeAmm": 123,
        "volumeClob": 123,
        "liquidityAmm": 123,
        "liquidityClob": 123,
        "makerBaseFee": 123,
        "takerBaseFee": 123,
        "customLiveness": 123,
        "acceptingOrders": true,
        "notificationsEnabled": true,
        "score": 123,
        "imageOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "iconOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "events": "<array>",
        "categories": [
          {
            "id": "<string>",
            "label": "<string>",
            "parentCategory": "<string>",
            "slug": "<string>",
            "publishedAt": "<string>",
            "createdBy": "<string>",
            "updatedBy": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z"
          }
        ],
        "tags": [
          {
            "id": "<string>",
            "label": "<string>",
            "slug": "<string>",
            "forceShow": true,
            "publishedAt": "<string>",
            "createdBy": 123,
            "updatedBy": 123,
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z",
            "forceHide": true,
            "isCarousel": true
          }
        ],
        "creator": "<string>",
        "ready": true,
        "funded": true,
        "pastSlugs": "<string>",
        "readyTimestamp": "2023-11-07T05:31:56Z",
        "fundedTimestamp": "2023-11-07T05:31:56Z",
        "acceptingOrdersTimestamp": "2023-11-07T05:31:56Z",
        "competitive": 123,
        "rewardsMinSize": 123,
        "rewardsMaxSpread": 123,
        "spread": 123,
        "automaticallyResolved": true,
        "oneDayPriceChange": 123,
        "oneHourPriceChange": 123,
        "oneWeekPriceChange": 123,
        "oneMonthPriceChange": 123,
        "oneYearPriceChange": 123,
        "lastTradePrice": 123,
        "bestBid": 123,
        "bestAsk": 123,
        "automaticallyActive": true,
        "clearBookOnStart": true,
        "chartColor": "<string>",
        "seriesColor": "<string>",
        "showGmpSeries": true,
        "showGmpOutcome": true,
        "manualActivation": true,
        "negRiskOther": true,
        "gameId": "<string>",
        "groupItemRange": "<string>",
        "sportsMarketType": "<string>",
        "line": 123,
        "umaResolutionStatuses": "<string>",
        "pendingDeployment": true,
        "deploying": true,
        "deployingTimestamp": "2023-11-07T05:31:56Z",
        "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
        "rfqEnabled": true,
        "eventStartTime": "2023-11-07T05:31:56Z"
      }
    ],
    "series": [
      {
        "id": "<string>",
        "ticker": "<string>",
        "slug": "<string>",
        "title": "<string>",
        "subtitle": "<string>",
        "seriesType": "<string>",
        "recurrence": "<string>",
        "description": "<string>",
        "image": "<string>",
        "icon": "<string>",
        "layout": "<string>",
        "active": true,
        "closed": true,
        "archived": true,
        "new": true,
        "featured": true,
        "restricted": true,
        "isTemplate": true,
        "templateVariables": true,
        "publishedAt": "<string>",
        "createdBy": "<string>",
        "updatedBy": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z",
        "commentsEnabled": true,
        "competitive": "<string>",
        "volume24hr": 123,
        "volume": 123,
        "liquidity": 123,
        "startDate": "2023-11-07T05:31:56Z",
        "pythTokenID": "<string>",
        "cgAssetName": "<string>",
        "score": 123,
        "events": "<array>",
        "collections": [
          {
            "id": "<string>",
            "ticker": "<string>",
            "slug": "<string>",
            "title": "<string>",
            "subtitle": "<string>",
            "collectionType": "<string>",
            "description": "<string>",
            "tags": "<string>",
            "image": "<string>",
            "icon": "<string>",
            "headerImage": "<string>",
            "layout": "<string>",
            "active": true,
            "closed": true,
            "archived": true,
            "new": true,
            "featured": true,
            "restricted": true,
            "isTemplate": true,
            "templateVariables": "<string>",
            "publishedAt": "<string>",
            "createdBy": "<string>",
            "updatedBy": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z",
            "commentsEnabled": true,
            "imageOptimized": {
              "id": "<string>",
              "imageUrlSource": "<string>",
              "imageUrlOptimized": "<string>",
              "imageSizeKbSource": 123,
              "imageSizeKbOptimized": 123,
              "imageOptimizedComplete": true,
              "imageOptimizedLastUpdated": "<string>",
              "relID": 123,
              "field": "<string>",
              "relname": "<string>"
            },
            "iconOptimized": {
              "id": "<string>",
              "imageUrlSource": "<string>",
              "imageUrlOptimized": "<string>",
              "imageSizeKbSource": 123,
              "imageSizeKbOptimized": 123,
              "imageOptimizedComplete": true,
              "imageOptimizedLastUpdated": "<string>",
              "relID": 123,
              "field": "<string>",
              "relname": "<string>"
            },
            "headerImageOptimized": {
              "id": "<string>",
              "imageUrlSource": "<string>",
              "imageUrlOptimized": "<string>",
              "imageSizeKbSource": 123,
              "imageSizeKbOptimized": 123,
              "imageOptimizedComplete": true,
              "imageOptimizedLastUpdated": "<string>",
              "relID": 123,
              "field": "<string>",
              "relname": "<string>"
            }
          }
        ],
        "categories": [
          {
            "id": "<string>",
            "label": "<string>",
            "parentCategory": "<string>",
            "slug": "<string>",
            "publishedAt": "<string>",
            "createdBy": "<string>",
            "updatedBy": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z"
          }
        ],
        "tags": [
          {
            "id": "<string>",
            "label": "<string>",
            "slug": "<string>",
            "forceShow": true,
            "publishedAt": "<string>",
            "createdBy": 123,
            "updatedBy": 123,
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z",
            "forceHide": true,
            "isCarousel": true
          }
        ],
        "commentCount": 123,
        "chats": [
          {
            "id": "<string>",
            "channelId": "<string>",
            "channelName": "<string>",
            "channelImage": "<string>",
            "live": true,
            "startTime": "2023-11-07T05:31:56Z",
            "endTime": "2023-11-07T05:31:56Z"
          }
        ]
      }
    ],
    "categories": [
      {
        "id": "<string>",
        "label": "<string>",
        "parentCategory": "<string>",
        "slug": "<string>",
        "publishedAt": "<string>",
        "createdBy": "<string>",
        "updatedBy": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z"
      }
    ],
    "collections": [
      {
        "id": "<string>",
        "ticker": "<string>",
        "slug": "<string>",
        "title": "<string>",
        "subtitle": "<string>",
        "collectionType": "<string>",
        "description": "<string>",
        "tags": "<string>",
        "image": "<string>",
        "icon": "<string>",
        "headerImage": "<string>",
        "layout": "<string>",
        "active": true,
        "closed": true,
        "archived": true,
        "new": true,
        "featured": true,
        "restricted": true,
        "isTemplate": true,
        "templateVariables": "<string>",
        "publishedAt": "<string>",
        "createdBy": "<string>",
        "updatedBy": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z",
        "commentsEnabled": true,
        "imageOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "iconOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "headerImageOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        }
      }
    ],
    "tags": [
      {
        "id": "<string>",
        "label": "<string>",
        "slug": "<string>",
        "forceShow": true,
        "publishedAt": "<string>",
        "createdBy": 123,
        "updatedBy": 123,
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z",
        "forceHide": true,
        "isCarousel": true
      }
    ],
    "cyom": true,
    "closedTime": "2023-11-07T05:31:56Z",
    "showAllOutcomes": true,
    "showMarketImages": true,
    "automaticallyResolved": true,
    "enableNegRisk": true,
    "automaticallyActive": true,
    "eventDate": "<string>",
    "startTime": "2023-11-07T05:31:56Z",
    "eventWeek": 123,
    "seriesSlug": "<string>",
    "score": "<string>",
    "elapsed": "<string>",
    "period": "<string>",
    "live": true,
    "ended": true,
    "finishedTimestamp": "2023-11-07T05:31:56Z",
    "gmpChartMode": "<string>",
    "eventCreators": [
      {
        "id": "<string>",
        "creatorName": "<string>",
        "creatorHandle": "<string>",
        "creatorUrl": "<string>",
        "creatorImage": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z"
      }
    ],
    "tweetCount": 123,
    "chats": [
      {
        "id": "<string>",
        "channelId": "<string>",
        "channelName": "<string>",
        "channelImage": "<string>",
        "live": true,
        "startTime": "2023-11-07T05:31:56Z",
        "endTime": "2023-11-07T05:31:56Z"
      }
    ],
    "featuredOrder": 123,
    "estimateValue": true,
    "cantEstimate": true,
    "estimatedValue": "<string>",
    "templates": [
      {
        "id": "<string>",
        "eventTitle": "<string>",
        "eventSlug": "<string>",
        "eventImage": "<string>",
        "marketTitle": "<string>",
        "description": "<string>",
        "resolutionSource": "<string>",
        "negRisk": true,
        "sortBy": "<string>",
        "showMarketImages": true,
        "seriesSlug": "<string>",
        "outcomes": "<string>"
      }
    ],
    "spreadsMainLine": 123,
    "totalsMainLine": 123,
    "carouselMap": "<string>",
    "pendingDeployment": true,
    "deploying": true,
    "deployingTimestamp": "2023-11-07T05:31:56Z",
    "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
    "gameStatus": "<string>"
  }
]
```

#### Query Parameters

[​](#parameter-limit)

limit

integer

Required range: `x >= 0`

[​](#parameter-offset)

offset

integer

Required range: `x >= 0`

[​](#parameter-order)

order

string

Comma-separated list of fields to order by

[​](#parameter-ascending)

ascending

boolean

[​](#parameter-id)

id

integer[]

[​](#parameter-tag-id)

tag\_id

integer

[​](#parameter-exclude-tag-id)

exclude\_tag\_id

integer[]

[​](#parameter-slug)

slug

string[]

[​](#parameter-tag-slug)

tag\_slug

string

[​](#parameter-related-tags)

related\_tags

boolean

[​](#parameter-active)

active

boolean

[​](#parameter-archived)

archived

boolean

[​](#parameter-featured)

featured

boolean

[​](#parameter-cyom)

cyom

boolean

[​](#parameter-include-chat)

include\_chat

boolean

[​](#parameter-include-template)

include\_template

boolean

[​](#parameter-recurrence)

recurrence

string

[​](#parameter-closed)

closed

boolean

[​](#parameter-liquidity-min)

liquidity\_min

number

[​](#parameter-liquidity-max)

liquidity\_max

number

[​](#parameter-volume-min)

volume\_min

number

[​](#parameter-volume-max)

volume\_max

number

[​](#parameter-start-date-min)

start\_date\_min

string<date-time>

[​](#parameter-start-date-max)

start\_date\_max

string<date-time>

[​](#parameter-end-date-min)

end\_date\_min

string<date-time>

[​](#parameter-end-date-max)

end\_date\_max

string<date-time>

#### Response

200 - application/json

List of events

[​](#response-items-id)

id

string

[​](#response-items-ticker-one-of-0)

ticker

string | null

[​](#response-items-slug-one-of-0)

slug

string | null

[​](#response-items-title-one-of-0)

title

string | null

[​](#response-items-subtitle-one-of-0)

subtitle

string | null

[​](#response-items-description-one-of-0)

description

string | null

[​](#response-items-resolution-source-one-of-0)

resolutionSource

string | null

[​](#response-items-start-date-one-of-0)

startDate

string<date-time> | null

[​](#response-items-creation-date-one-of-0)

creationDate

string<date-time> | null

[​](#response-items-end-date-one-of-0)

endDate

string<date-time> | null

[​](#response-items-image-one-of-0)

image

string | null

[​](#response-items-icon-one-of-0)

icon

string | null

[​](#response-items-active-one-of-0)

active

boolean | null

[​](#response-items-closed-one-of-0)

closed

boolean | null

[​](#response-items-archived-one-of-0)

archived

boolean | null

[​](#response-items-new-one-of-0)

new

boolean | null

[​](#response-items-featured-one-of-0)

featured

boolean | null

[​](#response-items-restricted-one-of-0)

restricted

boolean | null

[​](#response-items-liquidity-one-of-0)

liquidity

number | null

[​](#response-items-volume-one-of-0)

volume

number | null

[​](#response-items-open-interest-one-of-0)

openInterest

number | null

[​](#response-items-sort-by-one-of-0)

sortBy

string | null

[​](#response-items-category-one-of-0)

category

string | null

[​](#response-items-subcategory-one-of-0)

subcategory

string | null

[​](#response-items-is-template-one-of-0)

isTemplate

boolean | null

[​](#response-items-template-variables-one-of-0)

templateVariables

string | null

[​](#response-items-published-at-one-of-0)

published\_at

string | null

[​](#response-items-created-by-one-of-0)

createdBy

string | null

[​](#response-items-updated-by-one-of-0)

updatedBy

string | null

[​](#response-items-created-at-one-of-0)

createdAt

string<date-time> | null

[​](#response-items-updated-at-one-of-0)

updatedAt

string<date-time> | null

[​](#response-items-comments-enabled-one-of-0)

commentsEnabled

boolean | null

[​](#response-items-competitive-one-of-0)

competitive

number | null

[​](#response-items-volume24hr-one-of-0)

volume24hr

number | null

[​](#response-items-volume1wk-one-of-0)

volume1wk

number | null

[​](#response-items-volume1mo-one-of-0)

volume1mo

number | null

[​](#response-items-volume1yr-one-of-0)

volume1yr

number | null

[​](#response-items-featured-image-one-of-0)

featuredImage

string | null

[​](#response-items-disqus-thread-one-of-0)

disqusThread

string | null

[​](#response-items-parent-event-one-of-0)

parentEvent

string | null

[​](#response-items-enable-order-book-one-of-0)

enableOrderBook

boolean | null

[​](#response-items-liquidity-amm-one-of-0)

liquidityAmm

number | null

[​](#response-items-liquidity-clob-one-of-0)

liquidityClob

number | null

[​](#response-items-neg-risk-one-of-0)

negRisk

boolean | null

[​](#response-items-neg-risk-market-id-one-of-0)

negRiskMarketID

string | null

[​](#response-items-neg-risk-fee-bips-one-of-0)

negRiskFeeBips

integer | null

[​](#response-items-comment-count-one-of-0)

commentCount

integer | null

[​](#response-items-image-optimized)

imageOptimized

object

Show child attributes

[​](#response-items-icon-optimized)

iconOptimized

object

Show child attributes

[​](#response-items-featured-image-optimized)

featuredImageOptimized

object

Show child attributes

[​](#response-items-sub-events-one-of-0)

subEvents

string[] | null

[​](#response-items-markets)

markets

object[]

Show child attributes

[​](#response-items-series)

series

object[]

Show child attributes

[​](#response-items-categories)

categories

object[]

Show child attributes

[​](#response-items-collections)

collections

object[]

Show child attributes

[​](#response-items-tags)

tags

object[]

Show child attributes

[​](#response-items-cyom-one-of-0)

cyom

boolean | null

[​](#response-items-closed-time-one-of-0)

closedTime

string<date-time> | null

[​](#response-items-show-all-outcomes-one-of-0)

showAllOutcomes

boolean | null

[​](#response-items-show-market-images-one-of-0)

showMarketImages

boolean | null

[​](#response-items-automatically-resolved-one-of-0)

automaticallyResolved

boolean | null

[​](#response-items-enable-neg-risk-one-of-0)

enableNegRisk

boolean | null

[​](#response-items-automatically-active-one-of-0)

automaticallyActive

boolean | null

[​](#response-items-event-date-one-of-0)

eventDate

string | null

[​](#response-items-start-time-one-of-0)

startTime

string<date-time> | null

[​](#response-items-event-week-one-of-0)

eventWeek

integer | null

[​](#response-items-series-slug-one-of-0)

seriesSlug

string | null

[​](#response-items-score-one-of-0)

score

string | null

[​](#response-items-elapsed-one-of-0)

elapsed

string | null

[​](#response-items-period-one-of-0)

period

string | null

[​](#response-items-live-one-of-0)

live

boolean | null

[​](#response-items-ended-one-of-0)

ended

boolean | null

[​](#response-items-finished-timestamp-one-of-0)

finishedTimestamp

string<date-time> | null

[​](#response-items-gmp-chart-mode-one-of-0)

gmpChartMode

string | null

[​](#response-items-event-creators)

eventCreators

object[]

Show child attributes

[​](#response-items-tweet-count-one-of-0)

tweetCount

integer | null

[​](#response-items-chats)

chats

object[]

Show child attributes

[​](#response-items-featured-order-one-of-0)

featuredOrder

integer | null

[​](#response-items-estimate-value-one-of-0)

estimateValue

boolean | null

[​](#response-items-cant-estimate-one-of-0)

cantEstimate

boolean | null

[​](#response-items-estimated-value-one-of-0)

estimatedValue

string | null

[​](#response-items-templates)

templates

object[]

Show child attributes

[​](#response-items-spreads-main-line-one-of-0)

spreadsMainLine

number | null

[​](#response-items-totals-main-line-one-of-0)

totalsMainLine

number | null

[​](#response-items-carousel-map-one-of-0)

carouselMap

string | null

[​](#response-items-pending-deployment-one-of-0)

pendingDeployment

boolean | null

[​](#response-items-deploying-one-of-0)

deploying

boolean | null

[​](#response-items-deploying-timestamp-one-of-0)

deployingTimestamp

string<date-time> | null

[​](#response-items-scheduled-deployment-timestamp-one-of-0)

scheduledDeploymentTimestamp

string<date-time> | null

[​](#response-items-game-status-one-of-0)

gameStatus

string | null

[Get tags related to a tag slug](/api-reference/tags/get-tags-related-to-a-tag-slug)[Get event by id](/api-reference/events/get-event-by-id)

⌘I

---


## API: Gamma Health Check

> Source: https://docs.polymarket.com/api-reference/gamma-status/gamma-api-health-check

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Gamma Status

Gamma API Health check

GET

/

status

Try it

Gamma API Health check

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/status
```

200

Copy

```shiki
"OK"
```

#### Response

200 - text/plain

OK

The response is of type `string`.

Example:

`"OK"`

[Fetching Markets](/developers/gamma-markets-api/fetch-markets-guide)[List teams](/api-reference/sports/list-teams)

⌘I

---


## API: Get Market by ID

> Source: https://docs.polymarket.com/api-reference/markets/get-market-by-id

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Markets

Get market by id

GET

/

markets

/

{id}

Try it

Get market by id

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/markets/{id}
```

200

Copy

```shiki
{
  "id": "<string>",
  "question": "<string>",
  "conditionId": "<string>",
  "slug": "<string>",
  "twitterCardImage": "<string>",
  "resolutionSource": "<string>",
  "endDate": "2023-11-07T05:31:56Z",
  "category": "<string>",
  "ammType": "<string>",
  "liquidity": "<string>",
  "sponsorName": "<string>",
  "sponsorImage": "<string>",
  "startDate": "2023-11-07T05:31:56Z",
  "xAxisValue": "<string>",
  "yAxisValue": "<string>",
  "denominationToken": "<string>",
  "fee": "<string>",
  "image": "<string>",
  "icon": "<string>",
  "lowerBound": "<string>",
  "upperBound": "<string>",
  "description": "<string>",
  "outcomes": "<string>",
  "outcomePrices": "<string>",
  "volume": "<string>",
  "active": true,
  "marketType": "<string>",
  "formatType": "<string>",
  "lowerBoundDate": "<string>",
  "upperBoundDate": "<string>",
  "closed": true,
  "marketMakerAddress": "<string>",
  "createdBy": 123,
  "updatedBy": 123,
  "createdAt": "2023-11-07T05:31:56Z",
  "updatedAt": "2023-11-07T05:31:56Z",
  "closedTime": "<string>",
  "wideFormat": true,
  "new": true,
  "mailchimpTag": "<string>",
  "featured": true,
  "archived": true,
  "resolvedBy": "<string>",
  "restricted": true,
  "marketGroup": 123,
  "groupItemTitle": "<string>",
  "groupItemThreshold": "<string>",
  "questionID": "<string>",
  "umaEndDate": "<string>",
  "enableOrderBook": true,
  "orderPriceMinTickSize": 123,
  "orderMinSize": 123,
  "umaResolutionStatus": "<string>",
  "curationOrder": 123,
  "volumeNum": 123,
  "liquidityNum": 123,
  "endDateIso": "<string>",
  "startDateIso": "<string>",
  "umaEndDateIso": "<string>",
  "hasReviewedDates": true,
  "readyForCron": true,
  "commentsEnabled": true,
  "volume24hr": 123,
  "volume1wk": 123,
  "volume1mo": 123,
  "volume1yr": 123,
  "gameStartTime": "<string>",
  "secondsDelay": 123,
  "clobTokenIds": "<string>",
  "disqusThread": "<string>",
  "shortOutcomes": "<string>",
  "teamAID": "<string>",
  "teamBID": "<string>",
  "umaBond": "<string>",
  "umaReward": "<string>",
  "fpmmLive": true,
  "volume24hrAmm": 123,
  "volume1wkAmm": 123,
  "volume1moAmm": 123,
  "volume1yrAmm": 123,
  "volume24hrClob": 123,
  "volume1wkClob": 123,
  "volume1moClob": 123,
  "volume1yrClob": 123,
  "volumeAmm": 123,
  "volumeClob": 123,
  "liquidityAmm": 123,
  "liquidityClob": 123,
  "makerBaseFee": 123,
  "takerBaseFee": 123,
  "customLiveness": 123,
  "acceptingOrders": true,
  "notificationsEnabled": true,
  "score": 123,
  "imageOptimized": {
    "id": "<string>",
    "imageUrlSource": "<string>",
    "imageUrlOptimized": "<string>",
    "imageSizeKbSource": 123,
    "imageSizeKbOptimized": 123,
    "imageOptimizedComplete": true,
    "imageOptimizedLastUpdated": "<string>",
    "relID": 123,
    "field": "<string>",
    "relname": "<string>"
  },
  "iconOptimized": {
    "id": "<string>",
    "imageUrlSource": "<string>",
    "imageUrlOptimized": "<string>",
    "imageSizeKbSource": 123,
    "imageSizeKbOptimized": 123,
    "imageOptimizedComplete": true,
    "imageOptimizedLastUpdated": "<string>",
    "relID": 123,
    "field": "<string>",
    "relname": "<string>"
  },
  "events": [
    {
      "id": "<string>",
      "ticker": "<string>",
      "slug": "<string>",
      "title": "<string>",
      "subtitle": "<string>",
      "description": "<string>",
      "resolutionSource": "<string>",
      "startDate": "2023-11-07T05:31:56Z",
      "creationDate": "2023-11-07T05:31:56Z",
      "endDate": "2023-11-07T05:31:56Z",
      "image": "<string>",
      "icon": "<string>",
      "active": true,
      "closed": true,
      "archived": true,
      "new": true,
      "featured": true,
      "restricted": true,
      "liquidity": 123,
      "volume": 123,
      "openInterest": 123,
      "sortBy": "<string>",
      "category": "<string>",
      "subcategory": "<string>",
      "isTemplate": true,
      "templateVariables": "<string>",
      "published_at": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "commentsEnabled": true,
      "competitive": 123,
      "volume24hr": 123,
      "volume1wk": 123,
      "volume1mo": 123,
      "volume1yr": 123,
      "featuredImage": "<string>",
      "disqusThread": "<string>",
      "parentEvent": "<string>",
      "enableOrderBook": true,
      "liquidityAmm": 123,
      "liquidityClob": 123,
      "negRisk": true,
      "negRiskMarketID": "<string>",
      "negRiskFeeBips": 123,
      "commentCount": 123,
      "imageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "iconOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "featuredImageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "subEvents": [
        "<string>"
      ],
      "markets": "<array>",
      "series": [
        {
          "id": "<string>",
          "ticker": "<string>",
          "slug": "<string>",
          "title": "<string>",
          "subtitle": "<string>",
          "seriesType": "<string>",
          "recurrence": "<string>",
          "description": "<string>",
          "image": "<string>",
          "icon": "<string>",
          "layout": "<string>",
          "active": true,
          "closed": true,
          "archived": true,
          "new": true,
          "featured": true,
          "restricted": true,
          "isTemplate": true,
          "templateVariables": true,
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "commentsEnabled": true,
          "competitive": "<string>",
          "volume24hr": 123,
          "volume": 123,
          "liquidity": 123,
          "startDate": "2023-11-07T05:31:56Z",
          "pythTokenID": "<string>",
          "cgAssetName": "<string>",
          "score": 123,
          "events": "<array>",
          "collections": [
            {
              "id": "<string>",
              "ticker": "<string>",
              "slug": "<string>",
              "title": "<string>",
              "subtitle": "<string>",
              "collectionType": "<string>",
              "description": "<string>",
              "tags": "<string>",
              "image": "<string>",
              "icon": "<string>",
              "headerImage": "<string>",
              "layout": "<string>",
              "active": true,
              "closed": true,
              "archived": true,
              "new": true,
              "featured": true,
              "restricted": true,
              "isTemplate": true,
              "templateVariables": "<string>",
              "publishedAt": "<string>",
              "createdBy": "<string>",
              "updatedBy": "<string>",
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z",
              "commentsEnabled": true,
              "imageOptimized": {
                "id": "<string>",
                "imageUrlSource": "<string>",
                "imageUrlOptimized": "<string>",
                "imageSizeKbSource": 123,
                "imageSizeKbOptimized": 123,
                "imageOptimizedComplete": true,
                "imageOptimizedLastUpdated": "<string>",
                "relID": 123,
                "field": "<string>",
                "relname": "<string>"
              },
              "iconOptimized": {
                "id": "<string>",
                "imageUrlSource": "<string>",
                "imageUrlOptimized": "<string>",
                "imageSizeKbSource": 123,
                "imageSizeKbOptimized": 123,
                "imageOptimizedComplete": true,
                "imageOptimizedLastUpdated": "<string>",
                "relID": 123,
                "field": "<string>",
                "relname": "<string>"
              },
              "headerImageOptimized": {
                "id": "<string>",
                "imageUrlSource": "<string>",
                "imageUrlOptimized": "<string>",
                "imageSizeKbSource": 123,
                "imageSizeKbOptimized": 123,
                "imageOptimizedComplete": true,
                "imageOptimizedLastUpdated": "<string>",
                "relID": 123,
                "field": "<string>",
                "relname": "<string>"
              }
            }
          ],
          "categories": [
            {
              "id": "<string>",
              "label": "<string>",
              "parentCategory": "<string>",
              "slug": "<string>",
              "publishedAt": "<string>",
              "createdBy": "<string>",
              "updatedBy": "<string>",
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z"
            }
          ],
          "tags": [
            {
              "id": "<string>",
              "label": "<string>",
              "slug": "<string>",
              "forceShow": true,
              "publishedAt": "<string>",
              "createdBy": 123,
              "updatedBy": 123,
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z",
              "forceHide": true,
              "isCarousel": true
            }
          ],
          "commentCount": 123,
          "chats": [
            {
              "id": "<string>",
              "channelId": "<string>",
              "channelName": "<string>",
              "channelImage": "<string>",
              "live": true,
              "startTime": "2023-11-07T05:31:56Z",
              "endTime": "2023-11-07T05:31:56Z"
            }
          ]
        }
      ],
      "categories": [
        {
          "id": "<string>",
          "label": "<string>",
          "parentCategory": "<string>",
          "slug": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z"
        }
      ],
      "collections": [
        {
          "id": "<string>",
          "ticker": "<string>",
          "slug": "<string>",
          "title": "<string>",
          "subtitle": "<string>",
          "collectionType": "<string>",
          "description": "<string>",
          "tags": "<string>",
          "image": "<string>",
          "icon": "<string>",
          "headerImage": "<string>",
          "layout": "<string>",
          "active": true,
          "closed": true,
          "archived": true,
          "new": true,
          "featured": true,
          "restricted": true,
          "isTemplate": true,
          "templateVariables": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "commentsEnabled": true,
          "imageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "iconOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "headerImageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          }
        }
      ],
      "tags": [
        {
          "id": "<string>",
          "label": "<string>",
          "slug": "<string>",
          "forceShow": true,
          "publishedAt": "<string>",
          "createdBy": 123,
          "updatedBy": 123,
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "forceHide": true,
          "isCarousel": true
        }
      ],
      "cyom": true,
      "closedTime": "2023-11-07T05:31:56Z",
      "showAllOutcomes": true,
      "showMarketImages": true,
      "automaticallyResolved": true,
      "enableNegRisk": true,
      "automaticallyActive": true,
      "eventDate": "<string>",
      "startTime": "2023-11-07T05:31:56Z",
      "eventWeek": 123,
      "seriesSlug": "<string>",
      "score": "<string>",
      "elapsed": "<string>",
      "period": "<string>",
      "live": true,
      "ended": true,
      "finishedTimestamp": "2023-11-07T05:31:56Z",
      "gmpChartMode": "<string>",
      "eventCreators": [
        {
          "id": "<string>",
          "creatorName": "<string>",
          "creatorHandle": "<string>",
          "creatorUrl": "<string>",
          "creatorImage": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z"
        }
      ],
      "tweetCount": 123,
      "chats": [
        {
          "id": "<string>",
          "channelId": "<string>",
          "channelName": "<string>",
          "channelImage": "<string>",
          "live": true,
          "startTime": "2023-11-07T05:31:56Z",
          "endTime": "2023-11-07T05:31:56Z"
        }
      ],
      "featuredOrder": 123,
      "estimateValue": true,
      "cantEstimate": true,
      "estimatedValue": "<string>",
      "templates": [
        {
          "id": "<string>",
          "eventTitle": "<string>",
          "eventSlug": "<string>",
          "eventImage": "<string>",
          "marketTitle": "<string>",
          "description": "<string>",
          "resolutionSource": "<string>",
          "negRisk": true,
          "sortBy": "<string>",
          "showMarketImages": true,
          "seriesSlug": "<string>",
          "outcomes": "<string>"
        }
      ],
      "spreadsMainLine": 123,
      "totalsMainLine": 123,
      "carouselMap": "<string>",
      "pendingDeployment": true,
      "deploying": true,
      "deployingTimestamp": "2023-11-07T05:31:56Z",
      "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
      "gameStatus": "<string>"
    }
  ],
  "categories": [
    {
      "id": "<string>",
      "label": "<string>",
      "parentCategory": "<string>",
      "slug": "<string>",
      "publishedAt": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z"
    }
  ],
  "tags": [
    {
      "id": "<string>",
      "label": "<string>",
      "slug": "<string>",
      "forceShow": true,
      "publishedAt": "<string>",
      "createdBy": 123,
      "updatedBy": 123,
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "forceHide": true,
      "isCarousel": true
    }
  ],
  "creator": "<string>",
  "ready": true,
  "funded": true,
  "pastSlugs": "<string>",
  "readyTimestamp": "2023-11-07T05:31:56Z",
  "fundedTimestamp": "2023-11-07T05:31:56Z",
  "acceptingOrdersTimestamp": "2023-11-07T05:31:56Z",
  "competitive": 123,
  "rewardsMinSize": 123,
  "rewardsMaxSpread": 123,
  "spread": 123,
  "automaticallyResolved": true,
  "oneDayPriceChange": 123,
  "oneHourPriceChange": 123,
  "oneWeekPriceChange": 123,
  "oneMonthPriceChange": 123,
  "oneYearPriceChange": 123,
  "lastTradePrice": 123,
  "bestBid": 123,
  "bestAsk": 123,
  "automaticallyActive": true,
  "clearBookOnStart": true,
  "chartColor": "<string>",
  "seriesColor": "<string>",
  "showGmpSeries": true,
  "showGmpOutcome": true,
  "manualActivation": true,
  "negRiskOther": true,
  "gameId": "<string>",
  "groupItemRange": "<string>",
  "sportsMarketType": "<string>",
  "line": 123,
  "umaResolutionStatuses": "<string>",
  "pendingDeployment": true,
  "deploying": true,
  "deployingTimestamp": "2023-11-07T05:31:56Z",
  "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
  "rfqEnabled": true,
  "eventStartTime": "2023-11-07T05:31:56Z"
}
```

#### Path Parameters

[​](#parameter-id)

id

integer

required

#### Query Parameters

[​](#parameter-include-tag)

include\_tag

boolean

#### Response

200

application/json

Market

[​](#response-id)

id

string

[​](#response-question-one-of-0)

question

string | null

[​](#response-condition-id)

conditionId

string

[​](#response-slug-one-of-0)

slug

string | null

[​](#response-twitter-card-image-one-of-0)

twitterCardImage

string | null

[​](#response-resolution-source-one-of-0)

resolutionSource

string | null

[​](#response-end-date-one-of-0)

endDate

string<date-time> | null

[​](#response-category-one-of-0)

category

string | null

[​](#response-amm-type-one-of-0)

ammType

string | null

[​](#response-liquidity-one-of-0)

liquidity

string | null

[​](#response-sponsor-name-one-of-0)

sponsorName

string | null

[​](#response-sponsor-image-one-of-0)

sponsorImage

string | null

[​](#response-start-date-one-of-0)

startDate

string<date-time> | null

[​](#response-x-axis-value-one-of-0)

xAxisValue

string | null

[​](#response-y-axis-value-one-of-0)

yAxisValue

string | null

[​](#response-denomination-token-one-of-0)

denominationToken

string | null

[​](#response-fee-one-of-0)

fee

string | null

[​](#response-image-one-of-0)

image

string | null

[​](#response-icon-one-of-0)

icon

string | null

[​](#response-lower-bound-one-of-0)

lowerBound

string | null

[​](#response-upper-bound-one-of-0)

upperBound

string | null

[​](#response-description-one-of-0)

description

string | null

[​](#response-outcomes-one-of-0)

outcomes

string | null

[​](#response-outcome-prices-one-of-0)

outcomePrices

string | null

[​](#response-volume-one-of-0)

volume

string | null

[​](#response-active-one-of-0)

active

boolean | null

[​](#response-market-type-one-of-0)

marketType

string | null

[​](#response-format-type-one-of-0)

formatType

string | null

[​](#response-lower-bound-date-one-of-0)

lowerBoundDate

string | null

[​](#response-upper-bound-date-one-of-0)

upperBoundDate

string | null

[​](#response-closed-one-of-0)

closed

boolean | null

[​](#response-market-maker-address)

marketMakerAddress

string

[​](#response-created-by-one-of-0)

createdBy

integer | null

[​](#response-updated-by-one-of-0)

updatedBy

integer | null

[​](#response-created-at-one-of-0)

createdAt

string<date-time> | null

[​](#response-updated-at-one-of-0)

updatedAt

string<date-time> | null

[​](#response-closed-time-one-of-0)

closedTime

string | null

[​](#response-wide-format-one-of-0)

wideFormat

boolean | null

[​](#response-new-one-of-0)

new

boolean | null

[​](#response-mailchimp-tag-one-of-0)

mailchimpTag

string | null

[​](#response-featured-one-of-0)

featured

boolean | null

[​](#response-archived-one-of-0)

archived

boolean | null

[​](#response-resolved-by-one-of-0)

resolvedBy

string | null

[​](#response-restricted-one-of-0)

restricted

boolean | null

[​](#response-market-group-one-of-0)

marketGroup

integer | null

[​](#response-group-item-title-one-of-0)

groupItemTitle

string | null

[​](#response-group-item-threshold-one-of-0)

groupItemThreshold

string | null

[​](#response-question-id-one-of-0)

questionID

string | null

[​](#response-uma-end-date-one-of-0)

umaEndDate

string | null

[​](#response-enable-order-book-one-of-0)

enableOrderBook

boolean | null

[​](#response-order-price-min-tick-size-one-of-0)

orderPriceMinTickSize

number | null

[​](#response-order-min-size-one-of-0)

orderMinSize

number | null

[​](#response-uma-resolution-status-one-of-0)

umaResolutionStatus

string | null

[​](#response-curation-order-one-of-0)

curationOrder

integer | null

[​](#response-volume-num-one-of-0)

volumeNum

number | null

[​](#response-liquidity-num-one-of-0)

liquidityNum

number | null

[​](#response-end-date-iso-one-of-0)

endDateIso

string | null

[​](#response-start-date-iso-one-of-0)

startDateIso

string | null

[​](#response-uma-end-date-iso-one-of-0)

umaEndDateIso

string | null

[​](#response-has-reviewed-dates-one-of-0)

hasReviewedDates

boolean | null

[​](#response-ready-for-cron-one-of-0)

readyForCron

boolean | null

[​](#response-comments-enabled-one-of-0)

commentsEnabled

boolean | null

[​](#response-volume24hr-one-of-0)

volume24hr

number | null

[​](#response-volume1wk-one-of-0)

volume1wk

number | null

[​](#response-volume1mo-one-of-0)

volume1mo

number | null

[​](#response-volume1yr-one-of-0)

volume1yr

number | null

[​](#response-game-start-time-one-of-0)

gameStartTime

string | null

[​](#response-seconds-delay-one-of-0)

secondsDelay

integer | null

[​](#response-clob-token-ids-one-of-0)

clobTokenIds

string | null

[​](#response-disqus-thread-one-of-0)

disqusThread

string | null

[​](#response-short-outcomes-one-of-0)

shortOutcomes

string | null

[​](#response-team-aid-one-of-0)

teamAID

string | null

[​](#response-team-bid-one-of-0)

teamBID

string | null

[​](#response-uma-bond-one-of-0)

umaBond

string | null

[​](#response-uma-reward-one-of-0)

umaReward

string | null

[​](#response-fpmm-live-one-of-0)

fpmmLive

boolean | null

[​](#response-volume24hr-amm-one-of-0)

volume24hrAmm

number | null

[​](#response-volume1wk-amm-one-of-0)

volume1wkAmm

number | null

[​](#response-volume1mo-amm-one-of-0)

volume1moAmm

number | null

[​](#response-volume1yr-amm-one-of-0)

volume1yrAmm

number | null

[​](#response-volume24hr-clob-one-of-0)

volume24hrClob

number | null

[​](#response-volume1wk-clob-one-of-0)

volume1wkClob

number | null

[​](#response-volume1mo-clob-one-of-0)

volume1moClob

number | null

[​](#response-volume1yr-clob-one-of-0)

volume1yrClob

number | null

[​](#response-volume-amm-one-of-0)

volumeAmm

number | null

[​](#response-volume-clob-one-of-0)

volumeClob

number | null

[​](#response-liquidity-amm-one-of-0)

liquidityAmm

number | null

[​](#response-liquidity-clob-one-of-0)

liquidityClob

number | null

[​](#response-maker-base-fee-one-of-0)

makerBaseFee

integer | null

[​](#response-taker-base-fee-one-of-0)

takerBaseFee

integer | null

[​](#response-custom-liveness-one-of-0)

customLiveness

integer | null

[​](#response-accepting-orders-one-of-0)

acceptingOrders

boolean | null

[​](#response-notifications-enabled-one-of-0)

notificationsEnabled

boolean | null

[​](#response-score-one-of-0)

score

integer | null

[​](#response-image-optimized)

imageOptimized

object

Show child attributes

[​](#response-icon-optimized)

iconOptimized

object

Show child attributes

[​](#response-events)

events

object[]

Show child attributes

[​](#response-categories)

categories

object[]

Show child attributes

[​](#response-tags)

tags

object[]

Show child attributes

[​](#response-creator-one-of-0)

creator

string | null

[​](#response-ready-one-of-0)

ready

boolean | null

[​](#response-funded-one-of-0)

funded

boolean | null

[​](#response-past-slugs-one-of-0)

pastSlugs

string | null

[​](#response-ready-timestamp-one-of-0)

readyTimestamp

string<date-time> | null

[​](#response-funded-timestamp-one-of-0)

fundedTimestamp

string<date-time> | null

[​](#response-accepting-orders-timestamp-one-of-0)

acceptingOrdersTimestamp

string<date-time> | null

[​](#response-competitive-one-of-0)

competitive

number | null

[​](#response-rewards-min-size-one-of-0)

rewardsMinSize

number | null

[​](#response-rewards-max-spread-one-of-0)

rewardsMaxSpread

number | null

[​](#response-spread-one-of-0)

spread

number | null

[​](#response-automatically-resolved-one-of-0)

automaticallyResolved

boolean | null

[​](#response-one-day-price-change-one-of-0)

oneDayPriceChange

number | null

[​](#response-one-hour-price-change-one-of-0)

oneHourPriceChange

number | null

[​](#response-one-week-price-change-one-of-0)

oneWeekPriceChange

number | null

[​](#response-one-month-price-change-one-of-0)

oneMonthPriceChange

number | null

[​](#response-one-year-price-change-one-of-0)

oneYearPriceChange

number | null

[​](#response-last-trade-price-one-of-0)

lastTradePrice

number | null

[​](#response-best-bid-one-of-0)

bestBid

number | null

[​](#response-best-ask-one-of-0)

bestAsk

number | null

[​](#response-automatically-active-one-of-0)

automaticallyActive

boolean | null

[​](#response-clear-book-on-start-one-of-0)

clearBookOnStart

boolean | null

[​](#response-chart-color-one-of-0)

chartColor

string | null

[​](#response-series-color-one-of-0)

seriesColor

string | null

[​](#response-show-gmp-series-one-of-0)

showGmpSeries

boolean | null

[​](#response-show-gmp-outcome-one-of-0)

showGmpOutcome

boolean | null

[​](#response-manual-activation-one-of-0)

manualActivation

boolean | null

[​](#response-neg-risk-other-one-of-0)

negRiskOther

boolean | null

[​](#response-game-id-one-of-0)

gameId

string | null

[​](#response-group-item-range-one-of-0)

groupItemRange

string | null

[​](#response-sports-market-type-one-of-0)

sportsMarketType

string | null

[​](#response-line-one-of-0)

line

number | null

[​](#response-uma-resolution-statuses-one-of-0)

umaResolutionStatuses

string | null

[​](#response-pending-deployment-one-of-0)

pendingDeployment

boolean | null

[​](#response-deploying-one-of-0)

deploying

boolean | null

[​](#response-deploying-timestamp-one-of-0)

deployingTimestamp

string<date-time> | null

[​](#response-scheduled-deployment-timestamp-one-of-0)

scheduledDeploymentTimestamp

string<date-time> | null

[​](#response-rfq-enabled-one-of-0)

rfqEnabled

boolean | null

[​](#response-event-start-time-one-of-0)

eventStartTime

string<date-time> | null

[List markets](/api-reference/markets/list-markets)[Get market tags by id](/api-reference/markets/get-market-tags-by-id)

⌘I

---


## API: Get Market by Slug

> Source: https://docs.polymarket.com/api-reference/markets/get-market-by-slug

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Markets

Get market by slug

GET

/

markets

/

slug

/

{slug}

Try it

Get market by slug

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/markets/slug/{slug}
```

200

Copy

```shiki
{
  "id": "<string>",
  "question": "<string>",
  "conditionId": "<string>",
  "slug": "<string>",
  "twitterCardImage": "<string>",
  "resolutionSource": "<string>",
  "endDate": "2023-11-07T05:31:56Z",
  "category": "<string>",
  "ammType": "<string>",
  "liquidity": "<string>",
  "sponsorName": "<string>",
  "sponsorImage": "<string>",
  "startDate": "2023-11-07T05:31:56Z",
  "xAxisValue": "<string>",
  "yAxisValue": "<string>",
  "denominationToken": "<string>",
  "fee": "<string>",
  "image": "<string>",
  "icon": "<string>",
  "lowerBound": "<string>",
  "upperBound": "<string>",
  "description": "<string>",
  "outcomes": "<string>",
  "outcomePrices": "<string>",
  "volume": "<string>",
  "active": true,
  "marketType": "<string>",
  "formatType": "<string>",
  "lowerBoundDate": "<string>",
  "upperBoundDate": "<string>",
  "closed": true,
  "marketMakerAddress": "<string>",
  "createdBy": 123,
  "updatedBy": 123,
  "createdAt": "2023-11-07T05:31:56Z",
  "updatedAt": "2023-11-07T05:31:56Z",
  "closedTime": "<string>",
  "wideFormat": true,
  "new": true,
  "mailchimpTag": "<string>",
  "featured": true,
  "archived": true,
  "resolvedBy": "<string>",
  "restricted": true,
  "marketGroup": 123,
  "groupItemTitle": "<string>",
  "groupItemThreshold": "<string>",
  "questionID": "<string>",
  "umaEndDate": "<string>",
  "enableOrderBook": true,
  "orderPriceMinTickSize": 123,
  "orderMinSize": 123,
  "umaResolutionStatus": "<string>",
  "curationOrder": 123,
  "volumeNum": 123,
  "liquidityNum": 123,
  "endDateIso": "<string>",
  "startDateIso": "<string>",
  "umaEndDateIso": "<string>",
  "hasReviewedDates": true,
  "readyForCron": true,
  "commentsEnabled": true,
  "volume24hr": 123,
  "volume1wk": 123,
  "volume1mo": 123,
  "volume1yr": 123,
  "gameStartTime": "<string>",
  "secondsDelay": 123,
  "clobTokenIds": "<string>",
  "disqusThread": "<string>",
  "shortOutcomes": "<string>",
  "teamAID": "<string>",
  "teamBID": "<string>",
  "umaBond": "<string>",
  "umaReward": "<string>",
  "fpmmLive": true,
  "volume24hrAmm": 123,
  "volume1wkAmm": 123,
  "volume1moAmm": 123,
  "volume1yrAmm": 123,
  "volume24hrClob": 123,
  "volume1wkClob": 123,
  "volume1moClob": 123,
  "volume1yrClob": 123,
  "volumeAmm": 123,
  "volumeClob": 123,
  "liquidityAmm": 123,
  "liquidityClob": 123,
  "makerBaseFee": 123,
  "takerBaseFee": 123,
  "customLiveness": 123,
  "acceptingOrders": true,
  "notificationsEnabled": true,
  "score": 123,
  "imageOptimized": {
    "id": "<string>",
    "imageUrlSource": "<string>",
    "imageUrlOptimized": "<string>",
    "imageSizeKbSource": 123,
    "imageSizeKbOptimized": 123,
    "imageOptimizedComplete": true,
    "imageOptimizedLastUpdated": "<string>",
    "relID": 123,
    "field": "<string>",
    "relname": "<string>"
  },
  "iconOptimized": {
    "id": "<string>",
    "imageUrlSource": "<string>",
    "imageUrlOptimized": "<string>",
    "imageSizeKbSource": 123,
    "imageSizeKbOptimized": 123,
    "imageOptimizedComplete": true,
    "imageOptimizedLastUpdated": "<string>",
    "relID": 123,
    "field": "<string>",
    "relname": "<string>"
  },
  "events": [
    {
      "id": "<string>",
      "ticker": "<string>",
      "slug": "<string>",
      "title": "<string>",
      "subtitle": "<string>",
      "description": "<string>",
      "resolutionSource": "<string>",
      "startDate": "2023-11-07T05:31:56Z",
      "creationDate": "2023-11-07T05:31:56Z",
      "endDate": "2023-11-07T05:31:56Z",
      "image": "<string>",
      "icon": "<string>",
      "active": true,
      "closed": true,
      "archived": true,
      "new": true,
      "featured": true,
      "restricted": true,
      "liquidity": 123,
      "volume": 123,
      "openInterest": 123,
      "sortBy": "<string>",
      "category": "<string>",
      "subcategory": "<string>",
      "isTemplate": true,
      "templateVariables": "<string>",
      "published_at": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "commentsEnabled": true,
      "competitive": 123,
      "volume24hr": 123,
      "volume1wk": 123,
      "volume1mo": 123,
      "volume1yr": 123,
      "featuredImage": "<string>",
      "disqusThread": "<string>",
      "parentEvent": "<string>",
      "enableOrderBook": true,
      "liquidityAmm": 123,
      "liquidityClob": 123,
      "negRisk": true,
      "negRiskMarketID": "<string>",
      "negRiskFeeBips": 123,
      "commentCount": 123,
      "imageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "iconOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "featuredImageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "subEvents": [
        "<string>"
      ],
      "markets": "<array>",
      "series": [
        {
          "id": "<string>",
          "ticker": "<string>",
          "slug": "<string>",
          "title": "<string>",
          "subtitle": "<string>",
          "seriesType": "<string>",
          "recurrence": "<string>",
          "description": "<string>",
          "image": "<string>",
          "icon": "<string>",
          "layout": "<string>",
          "active": true,
          "closed": true,
          "archived": true,
          "new": true,
          "featured": true,
          "restricted": true,
          "isTemplate": true,
          "templateVariables": true,
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "commentsEnabled": true,
          "competitive": "<string>",
          "volume24hr": 123,
          "volume": 123,
          "liquidity": 123,
          "startDate": "2023-11-07T05:31:56Z",
          "pythTokenID": "<string>",
          "cgAssetName": "<string>",
          "score": 123,
          "events": "<array>",
          "collections": [
            {
              "id": "<string>",
              "ticker": "<string>",
              "slug": "<string>",
              "title": "<string>",
              "subtitle": "<string>",
              "collectionType": "<string>",
              "description": "<string>",
              "tags": "<string>",
              "image": "<string>",
              "icon": "<string>",
              "headerImage": "<string>",
              "layout": "<string>",
              "active": true,
              "closed": true,
              "archived": true,
              "new": true,
              "featured": true,
              "restricted": true,
              "isTemplate": true,
              "templateVariables": "<string>",
              "publishedAt": "<string>",
              "createdBy": "<string>",
              "updatedBy": "<string>",
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z",
              "commentsEnabled": true,
              "imageOptimized": {
                "id": "<string>",
                "imageUrlSource": "<string>",
                "imageUrlOptimized": "<string>",
                "imageSizeKbSource": 123,
                "imageSizeKbOptimized": 123,
                "imageOptimizedComplete": true,
                "imageOptimizedLastUpdated": "<string>",
                "relID": 123,
                "field": "<string>",
                "relname": "<string>"
              },
              "iconOptimized": {
                "id": "<string>",
                "imageUrlSource": "<string>",
                "imageUrlOptimized": "<string>",
                "imageSizeKbSource": 123,
                "imageSizeKbOptimized": 123,
                "imageOptimizedComplete": true,
                "imageOptimizedLastUpdated": "<string>",
                "relID": 123,
                "field": "<string>",
                "relname": "<string>"
              },
              "headerImageOptimized": {
                "id": "<string>",
                "imageUrlSource": "<string>",
                "imageUrlOptimized": "<string>",
                "imageSizeKbSource": 123,
                "imageSizeKbOptimized": 123,
                "imageOptimizedComplete": true,
                "imageOptimizedLastUpdated": "<string>",
                "relID": 123,
                "field": "<string>",
                "relname": "<string>"
              }
            }
          ],
          "categories": [
            {
              "id": "<string>",
              "label": "<string>",
              "parentCategory": "<string>",
              "slug": "<string>",
              "publishedAt": "<string>",
              "createdBy": "<string>",
              "updatedBy": "<string>",
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z"
            }
          ],
          "tags": [
            {
              "id": "<string>",
              "label": "<string>",
              "slug": "<string>",
              "forceShow": true,
              "publishedAt": "<string>",
              "createdBy": 123,
              "updatedBy": 123,
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z",
              "forceHide": true,
              "isCarousel": true
            }
          ],
          "commentCount": 123,
          "chats": [
            {
              "id": "<string>",
              "channelId": "<string>",
              "channelName": "<string>",
              "channelImage": "<string>",
              "live": true,
              "startTime": "2023-11-07T05:31:56Z",
              "endTime": "2023-11-07T05:31:56Z"
            }
          ]
        }
      ],
      "categories": [
        {
          "id": "<string>",
          "label": "<string>",
          "parentCategory": "<string>",
          "slug": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z"
        }
      ],
      "collections": [
        {
          "id": "<string>",
          "ticker": "<string>",
          "slug": "<string>",
          "title": "<string>",
          "subtitle": "<string>",
          "collectionType": "<string>",
          "description": "<string>",
          "tags": "<string>",
          "image": "<string>",
          "icon": "<string>",
          "headerImage": "<string>",
          "layout": "<string>",
          "active": true,
          "closed": true,
          "archived": true,
          "new": true,
          "featured": true,
          "restricted": true,
          "isTemplate": true,
          "templateVariables": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "commentsEnabled": true,
          "imageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "iconOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "headerImageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          }
        }
      ],
      "tags": [
        {
          "id": "<string>",
          "label": "<string>",
          "slug": "<string>",
          "forceShow": true,
          "publishedAt": "<string>",
          "createdBy": 123,
          "updatedBy": 123,
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "forceHide": true,
          "isCarousel": true
        }
      ],
      "cyom": true,
      "closedTime": "2023-11-07T05:31:56Z",
      "showAllOutcomes": true,
      "showMarketImages": true,
      "automaticallyResolved": true,
      "enableNegRisk": true,
      "automaticallyActive": true,
      "eventDate": "<string>",
      "startTime": "2023-11-07T05:31:56Z",
      "eventWeek": 123,
      "seriesSlug": "<string>",
      "score": "<string>",
      "elapsed": "<string>",
      "period": "<string>",
      "live": true,
      "ended": true,
      "finishedTimestamp": "2023-11-07T05:31:56Z",
      "gmpChartMode": "<string>",
      "eventCreators": [
        {
          "id": "<string>",
          "creatorName": "<string>",
          "creatorHandle": "<string>",
          "creatorUrl": "<string>",
          "creatorImage": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z"
        }
      ],
      "tweetCount": 123,
      "chats": [
        {
          "id": "<string>",
          "channelId": "<string>",
          "channelName": "<string>",
          "channelImage": "<string>",
          "live": true,
          "startTime": "2023-11-07T05:31:56Z",
          "endTime": "2023-11-07T05:31:56Z"
        }
      ],
      "featuredOrder": 123,
      "estimateValue": true,
      "cantEstimate": true,
      "estimatedValue": "<string>",
      "templates": [
        {
          "id": "<string>",
          "eventTitle": "<string>",
          "eventSlug": "<string>",
          "eventImage": "<string>",
          "marketTitle": "<string>",
          "description": "<string>",
          "resolutionSource": "<string>",
          "negRisk": true,
          "sortBy": "<string>",
          "showMarketImages": true,
          "seriesSlug": "<string>",
          "outcomes": "<string>"
        }
      ],
      "spreadsMainLine": 123,
      "totalsMainLine": 123,
      "carouselMap": "<string>",
      "pendingDeployment": true,
      "deploying": true,
      "deployingTimestamp": "2023-11-07T05:31:56Z",
      "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
      "gameStatus": "<string>"
    }
  ],
  "categories": [
    {
      "id": "<string>",
      "label": "<string>",
      "parentCategory": "<string>",
      "slug": "<string>",
      "publishedAt": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z"
    }
  ],
  "tags": [
    {
      "id": "<string>",
      "label": "<string>",
      "slug": "<string>",
      "forceShow": true,
      "publishedAt": "<string>",
      "createdBy": 123,
      "updatedBy": 123,
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "forceHide": true,
      "isCarousel": true
    }
  ],
  "creator": "<string>",
  "ready": true,
  "funded": true,
  "pastSlugs": "<string>",
  "readyTimestamp": "2023-11-07T05:31:56Z",
  "fundedTimestamp": "2023-11-07T05:31:56Z",
  "acceptingOrdersTimestamp": "2023-11-07T05:31:56Z",
  "competitive": 123,
  "rewardsMinSize": 123,
  "rewardsMaxSpread": 123,
  "spread": 123,
  "automaticallyResolved": true,
  "oneDayPriceChange": 123,
  "oneHourPriceChange": 123,
  "oneWeekPriceChange": 123,
  "oneMonthPriceChange": 123,
  "oneYearPriceChange": 123,
  "lastTradePrice": 123,
  "bestBid": 123,
  "bestAsk": 123,
  "automaticallyActive": true,
  "clearBookOnStart": true,
  "chartColor": "<string>",
  "seriesColor": "<string>",
  "showGmpSeries": true,
  "showGmpOutcome": true,
  "manualActivation": true,
  "negRiskOther": true,
  "gameId": "<string>",
  "groupItemRange": "<string>",
  "sportsMarketType": "<string>",
  "line": 123,
  "umaResolutionStatuses": "<string>",
  "pendingDeployment": true,
  "deploying": true,
  "deployingTimestamp": "2023-11-07T05:31:56Z",
  "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
  "rfqEnabled": true,
  "eventStartTime": "2023-11-07T05:31:56Z"
}
```

#### Path Parameters

[​](#parameter-slug)

slug

string

required

#### Query Parameters

[​](#parameter-include-tag)

include\_tag

boolean

#### Response

200

application/json

Market

[​](#response-id)

id

string

[​](#response-question-one-of-0)

question

string | null

[​](#response-condition-id)

conditionId

string

[​](#response-slug-one-of-0)

slug

string | null

[​](#response-twitter-card-image-one-of-0)

twitterCardImage

string | null

[​](#response-resolution-source-one-of-0)

resolutionSource

string | null

[​](#response-end-date-one-of-0)

endDate

string<date-time> | null

[​](#response-category-one-of-0)

category

string | null

[​](#response-amm-type-one-of-0)

ammType

string | null

[​](#response-liquidity-one-of-0)

liquidity

string | null

[​](#response-sponsor-name-one-of-0)

sponsorName

string | null

[​](#response-sponsor-image-one-of-0)

sponsorImage

string | null

[​](#response-start-date-one-of-0)

startDate

string<date-time> | null

[​](#response-x-axis-value-one-of-0)

xAxisValue

string | null

[​](#response-y-axis-value-one-of-0)

yAxisValue

string | null

[​](#response-denomination-token-one-of-0)

denominationToken

string | null

[​](#response-fee-one-of-0)

fee

string | null

[​](#response-image-one-of-0)

image

string | null

[​](#response-icon-one-of-0)

icon

string | null

[​](#response-lower-bound-one-of-0)

lowerBound

string | null

[​](#response-upper-bound-one-of-0)

upperBound

string | null

[​](#response-description-one-of-0)

description

string | null

[​](#response-outcomes-one-of-0)

outcomes

string | null

[​](#response-outcome-prices-one-of-0)

outcomePrices

string | null

[​](#response-volume-one-of-0)

volume

string | null

[​](#response-active-one-of-0)

active

boolean | null

[​](#response-market-type-one-of-0)

marketType

string | null

[​](#response-format-type-one-of-0)

formatType

string | null

[​](#response-lower-bound-date-one-of-0)

lowerBoundDate

string | null

[​](#response-upper-bound-date-one-of-0)

upperBoundDate

string | null

[​](#response-closed-one-of-0)

closed

boolean | null

[​](#response-market-maker-address)

marketMakerAddress

string

[​](#response-created-by-one-of-0)

createdBy

integer | null

[​](#response-updated-by-one-of-0)

updatedBy

integer | null

[​](#response-created-at-one-of-0)

createdAt

string<date-time> | null

[​](#response-updated-at-one-of-0)

updatedAt

string<date-time> | null

[​](#response-closed-time-one-of-0)

closedTime

string | null

[​](#response-wide-format-one-of-0)

wideFormat

boolean | null

[​](#response-new-one-of-0)

new

boolean | null

[​](#response-mailchimp-tag-one-of-0)

mailchimpTag

string | null

[​](#response-featured-one-of-0)

featured

boolean | null

[​](#response-archived-one-of-0)

archived

boolean | null

[​](#response-resolved-by-one-of-0)

resolvedBy

string | null

[​](#response-restricted-one-of-0)

restricted

boolean | null

[​](#response-market-group-one-of-0)

marketGroup

integer | null

[​](#response-group-item-title-one-of-0)

groupItemTitle

string | null

[​](#response-group-item-threshold-one-of-0)

groupItemThreshold

string | null

[​](#response-question-id-one-of-0)

questionID

string | null

[​](#response-uma-end-date-one-of-0)

umaEndDate

string | null

[​](#response-enable-order-book-one-of-0)

enableOrderBook

boolean | null

[​](#response-order-price-min-tick-size-one-of-0)

orderPriceMinTickSize

number | null

[​](#response-order-min-size-one-of-0)

orderMinSize

number | null

[​](#response-uma-resolution-status-one-of-0)

umaResolutionStatus

string | null

[​](#response-curation-order-one-of-0)

curationOrder

integer | null

[​](#response-volume-num-one-of-0)

volumeNum

number | null

[​](#response-liquidity-num-one-of-0)

liquidityNum

number | null

[​](#response-end-date-iso-one-of-0)

endDateIso

string | null

[​](#response-start-date-iso-one-of-0)

startDateIso

string | null

[​](#response-uma-end-date-iso-one-of-0)

umaEndDateIso

string | null

[​](#response-has-reviewed-dates-one-of-0)

hasReviewedDates

boolean | null

[​](#response-ready-for-cron-one-of-0)

readyForCron

boolean | null

[​](#response-comments-enabled-one-of-0)

commentsEnabled

boolean | null

[​](#response-volume24hr-one-of-0)

volume24hr

number | null

[​](#response-volume1wk-one-of-0)

volume1wk

number | null

[​](#response-volume1mo-one-of-0)

volume1mo

number | null

[​](#response-volume1yr-one-of-0)

volume1yr

number | null

[​](#response-game-start-time-one-of-0)

gameStartTime

string | null

[​](#response-seconds-delay-one-of-0)

secondsDelay

integer | null

[​](#response-clob-token-ids-one-of-0)

clobTokenIds

string | null

[​](#response-disqus-thread-one-of-0)

disqusThread

string | null

[​](#response-short-outcomes-one-of-0)

shortOutcomes

string | null

[​](#response-team-aid-one-of-0)

teamAID

string | null

[​](#response-team-bid-one-of-0)

teamBID

string | null

[​](#response-uma-bond-one-of-0)

umaBond

string | null

[​](#response-uma-reward-one-of-0)

umaReward

string | null

[​](#response-fpmm-live-one-of-0)

fpmmLive

boolean | null

[​](#response-volume24hr-amm-one-of-0)

volume24hrAmm

number | null

[​](#response-volume1wk-amm-one-of-0)

volume1wkAmm

number | null

[​](#response-volume1mo-amm-one-of-0)

volume1moAmm

number | null

[​](#response-volume1yr-amm-one-of-0)

volume1yrAmm

number | null

[​](#response-volume24hr-clob-one-of-0)

volume24hrClob

number | null

[​](#response-volume1wk-clob-one-of-0)

volume1wkClob

number | null

[​](#response-volume1mo-clob-one-of-0)

volume1moClob

number | null

[​](#response-volume1yr-clob-one-of-0)

volume1yrClob

number | null

[​](#response-volume-amm-one-of-0)

volumeAmm

number | null

[​](#response-volume-clob-one-of-0)

volumeClob

number | null

[​](#response-liquidity-amm-one-of-0)

liquidityAmm

number | null

[​](#response-liquidity-clob-one-of-0)

liquidityClob

number | null

[​](#response-maker-base-fee-one-of-0)

makerBaseFee

integer | null

[​](#response-taker-base-fee-one-of-0)

takerBaseFee

integer | null

[​](#response-custom-liveness-one-of-0)

customLiveness

integer | null

[​](#response-accepting-orders-one-of-0)

acceptingOrders

boolean | null

[​](#response-notifications-enabled-one-of-0)

notificationsEnabled

boolean | null

[​](#response-score-one-of-0)

score

integer | null

[​](#response-image-optimized)

imageOptimized

object

Show child attributes

[​](#response-icon-optimized)

iconOptimized

object

Show child attributes

[​](#response-events)

events

object[]

Show child attributes

[​](#response-categories)

categories

object[]

Show child attributes

[​](#response-tags)

tags

object[]

Show child attributes

[​](#response-creator-one-of-0)

creator

string | null

[​](#response-ready-one-of-0)

ready

boolean | null

[​](#response-funded-one-of-0)

funded

boolean | null

[​](#response-past-slugs-one-of-0)

pastSlugs

string | null

[​](#response-ready-timestamp-one-of-0)

readyTimestamp

string<date-time> | null

[​](#response-funded-timestamp-one-of-0)

fundedTimestamp

string<date-time> | null

[​](#response-accepting-orders-timestamp-one-of-0)

acceptingOrdersTimestamp

string<date-time> | null

[​](#response-competitive-one-of-0)

competitive

number | null

[​](#response-rewards-min-size-one-of-0)

rewardsMinSize

number | null

[​](#response-rewards-max-spread-one-of-0)

rewardsMaxSpread

number | null

[​](#response-spread-one-of-0)

spread

number | null

[​](#response-automatically-resolved-one-of-0)

automaticallyResolved

boolean | null

[​](#response-one-day-price-change-one-of-0)

oneDayPriceChange

number | null

[​](#response-one-hour-price-change-one-of-0)

oneHourPriceChange

number | null

[​](#response-one-week-price-change-one-of-0)

oneWeekPriceChange

number | null

[​](#response-one-month-price-change-one-of-0)

oneMonthPriceChange

number | null

[​](#response-one-year-price-change-one-of-0)

oneYearPriceChange

number | null

[​](#response-last-trade-price-one-of-0)

lastTradePrice

number | null

[​](#response-best-bid-one-of-0)

bestBid

number | null

[​](#response-best-ask-one-of-0)

bestAsk

number | null

[​](#response-automatically-active-one-of-0)

automaticallyActive

boolean | null

[​](#response-clear-book-on-start-one-of-0)

clearBookOnStart

boolean | null

[​](#response-chart-color-one-of-0)

chartColor

string | null

[​](#response-series-color-one-of-0)

seriesColor

string | null

[​](#response-show-gmp-series-one-of-0)

showGmpSeries

boolean | null

[​](#response-show-gmp-outcome-one-of-0)

showGmpOutcome

boolean | null

[​](#response-manual-activation-one-of-0)

manualActivation

boolean | null

[​](#response-neg-risk-other-one-of-0)

negRiskOther

boolean | null

[​](#response-game-id-one-of-0)

gameId

string | null

[​](#response-group-item-range-one-of-0)

groupItemRange

string | null

[​](#response-sports-market-type-one-of-0)

sportsMarketType

string | null

[​](#response-line-one-of-0)

line

number | null

[​](#response-uma-resolution-statuses-one-of-0)

umaResolutionStatuses

string | null

[​](#response-pending-deployment-one-of-0)

pendingDeployment

boolean | null

[​](#response-deploying-one-of-0)

deploying

boolean | null

[​](#response-deploying-timestamp-one-of-0)

deployingTimestamp

string<date-time> | null

[​](#response-scheduled-deployment-timestamp-one-of-0)

scheduledDeploymentTimestamp

string<date-time> | null

[​](#response-rfq-enabled-one-of-0)

rfqEnabled

boolean | null

[​](#response-event-start-time-one-of-0)

eventStartTime

string<date-time> | null

[Get market tags by id](/api-reference/markets/get-market-tags-by-id)[List series](/api-reference/series/list-series)

⌘I

---


## API: Get Market Tags

> Source: https://docs.polymarket.com/api-reference/markets/get-market-tags-by-id

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Markets

Get market tags by id

GET

/

markets

/

{id}

/

tags

Try it

Get market tags by id

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/markets/{id}/tags
```

200

Copy

```shiki
[
  {
    "id": "<string>",
    "label": "<string>",
    "slug": "<string>",
    "forceShow": true,
    "publishedAt": "<string>",
    "createdBy": 123,
    "updatedBy": 123,
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "forceHide": true,
    "isCarousel": true
  }
]
```

#### Path Parameters

[​](#parameter-id)

id

integer

required

#### Response

200

application/json

Tags attached to the market

[​](#response-items-id)

id

string

[​](#response-items-label-one-of-0)

label

string | null

[​](#response-items-slug-one-of-0)

slug

string | null

[​](#response-items-force-show-one-of-0)

forceShow

boolean | null

[​](#response-items-published-at-one-of-0)

publishedAt

string | null

[​](#response-items-created-by-one-of-0)

createdBy

integer | null

[​](#response-items-updated-by-one-of-0)

updatedBy

integer | null

[​](#response-items-created-at-one-of-0)

createdAt

string<date-time> | null

[​](#response-items-updated-at-one-of-0)

updatedAt

string<date-time> | null

[​](#response-items-force-hide-one-of-0)

forceHide

boolean | null

[​](#response-items-is-carousel-one-of-0)

isCarousel

boolean | null

[Get market by id](/api-reference/markets/get-market-by-id)[Get market by slug](/api-reference/markets/get-market-by-slug)

⌘I

---


## API: List Markets

> Source: https://docs.polymarket.com/api-reference/markets/list-markets

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Markets

List markets

GET

/

markets

Try it

List markets

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/markets
```

200

Copy

```shiki
[
  {
    "id": "<string>",
    "question": "<string>",
    "conditionId": "<string>",
    "slug": "<string>",
    "twitterCardImage": "<string>",
    "resolutionSource": "<string>",
    "endDate": "2023-11-07T05:31:56Z",
    "category": "<string>",
    "ammType": "<string>",
    "liquidity": "<string>",
    "sponsorName": "<string>",
    "sponsorImage": "<string>",
    "startDate": "2023-11-07T05:31:56Z",
    "xAxisValue": "<string>",
    "yAxisValue": "<string>",
    "denominationToken": "<string>",
    "fee": "<string>",
    "image": "<string>",
    "icon": "<string>",
    "lowerBound": "<string>",
    "upperBound": "<string>",
    "description": "<string>",
    "outcomes": "<string>",
    "outcomePrices": "<string>",
    "volume": "<string>",
    "active": true,
    "marketType": "<string>",
    "formatType": "<string>",
    "lowerBoundDate": "<string>",
    "upperBoundDate": "<string>",
    "closed": true,
    "marketMakerAddress": "<string>",
    "createdBy": 123,
    "updatedBy": 123,
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "closedTime": "<string>",
    "wideFormat": true,
    "new": true,
    "mailchimpTag": "<string>",
    "featured": true,
    "archived": true,
    "resolvedBy": "<string>",
    "restricted": true,
    "marketGroup": 123,
    "groupItemTitle": "<string>",
    "groupItemThreshold": "<string>",
    "questionID": "<string>",
    "umaEndDate": "<string>",
    "enableOrderBook": true,
    "orderPriceMinTickSize": 123,
    "orderMinSize": 123,
    "umaResolutionStatus": "<string>",
    "curationOrder": 123,
    "volumeNum": 123,
    "liquidityNum": 123,
    "endDateIso": "<string>",
    "startDateIso": "<string>",
    "umaEndDateIso": "<string>",
    "hasReviewedDates": true,
    "readyForCron": true,
    "commentsEnabled": true,
    "volume24hr": 123,
    "volume1wk": 123,
    "volume1mo": 123,
    "volume1yr": 123,
    "gameStartTime": "<string>",
    "secondsDelay": 123,
    "clobTokenIds": "<string>",
    "disqusThread": "<string>",
    "shortOutcomes": "<string>",
    "teamAID": "<string>",
    "teamBID": "<string>",
    "umaBond": "<string>",
    "umaReward": "<string>",
    "fpmmLive": true,
    "volume24hrAmm": 123,
    "volume1wkAmm": 123,
    "volume1moAmm": 123,
    "volume1yrAmm": 123,
    "volume24hrClob": 123,
    "volume1wkClob": 123,
    "volume1moClob": 123,
    "volume1yrClob": 123,
    "volumeAmm": 123,
    "volumeClob": 123,
    "liquidityAmm": 123,
    "liquidityClob": 123,
    "makerBaseFee": 123,
    "takerBaseFee": 123,
    "customLiveness": 123,
    "acceptingOrders": true,
    "notificationsEnabled": true,
    "score": 123,
    "imageOptimized": {
      "id": "<string>",
      "imageUrlSource": "<string>",
      "imageUrlOptimized": "<string>",
      "imageSizeKbSource": 123,
      "imageSizeKbOptimized": 123,
      "imageOptimizedComplete": true,
      "imageOptimizedLastUpdated": "<string>",
      "relID": 123,
      "field": "<string>",
      "relname": "<string>"
    },
    "iconOptimized": {
      "id": "<string>",
      "imageUrlSource": "<string>",
      "imageUrlOptimized": "<string>",
      "imageSizeKbSource": 123,
      "imageSizeKbOptimized": 123,
      "imageOptimizedComplete": true,
      "imageOptimizedLastUpdated": "<string>",
      "relID": 123,
      "field": "<string>",
      "relname": "<string>"
    },
    "events": [
      {
        "id": "<string>",
        "ticker": "<string>",
        "slug": "<string>",
        "title": "<string>",
        "subtitle": "<string>",
        "description": "<string>",
        "resolutionSource": "<string>",
        "startDate": "2023-11-07T05:31:56Z",
        "creationDate": "2023-11-07T05:31:56Z",
        "endDate": "2023-11-07T05:31:56Z",
        "image": "<string>",
        "icon": "<string>",
        "active": true,
        "closed": true,
        "archived": true,
        "new": true,
        "featured": true,
        "restricted": true,
        "liquidity": 123,
        "volume": 123,
        "openInterest": 123,
        "sortBy": "<string>",
        "category": "<string>",
        "subcategory": "<string>",
        "isTemplate": true,
        "templateVariables": "<string>",
        "published_at": "<string>",
        "createdBy": "<string>",
        "updatedBy": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z",
        "commentsEnabled": true,
        "competitive": 123,
        "volume24hr": 123,
        "volume1wk": 123,
        "volume1mo": 123,
        "volume1yr": 123,
        "featuredImage": "<string>",
        "disqusThread": "<string>",
        "parentEvent": "<string>",
        "enableOrderBook": true,
        "liquidityAmm": 123,
        "liquidityClob": 123,
        "negRisk": true,
        "negRiskMarketID": "<string>",
        "negRiskFeeBips": 123,
        "commentCount": 123,
        "imageOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "iconOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "featuredImageOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "subEvents": [
          "<string>"
        ],
        "markets": "<array>",
        "series": [
          {
            "id": "<string>",
            "ticker": "<string>",
            "slug": "<string>",
            "title": "<string>",
            "subtitle": "<string>",
            "seriesType": "<string>",
            "recurrence": "<string>",
            "description": "<string>",
            "image": "<string>",
            "icon": "<string>",
            "layout": "<string>",
            "active": true,
            "closed": true,
            "archived": true,
            "new": true,
            "featured": true,
            "restricted": true,
            "isTemplate": true,
            "templateVariables": true,
            "publishedAt": "<string>",
            "createdBy": "<string>",
            "updatedBy": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z",
            "commentsEnabled": true,
            "competitive": "<string>",
            "volume24hr": 123,
            "volume": 123,
            "liquidity": 123,
            "startDate": "2023-11-07T05:31:56Z",
            "pythTokenID": "<string>",
            "cgAssetName": "<string>",
            "score": 123,
            "events": "<array>",
            "collections": [
              {
                "id": "<string>",
                "ticker": "<string>",
                "slug": "<string>",
                "title": "<string>",
                "subtitle": "<string>",
                "collectionType": "<string>",
                "description": "<string>",
                "tags": "<string>",
                "image": "<string>",
                "icon": "<string>",
                "headerImage": "<string>",
                "layout": "<string>",
                "active": true,
                "closed": true,
                "archived": true,
                "new": true,
                "featured": true,
                "restricted": true,
                "isTemplate": true,
                "templateVariables": "<string>",
                "publishedAt": "<string>",
                "createdBy": "<string>",
                "updatedBy": "<string>",
                "createdAt": "2023-11-07T05:31:56Z",
                "updatedAt": "2023-11-07T05:31:56Z",
                "commentsEnabled": true,
                "imageOptimized": {
                  "id": "<string>",
                  "imageUrlSource": "<string>",
                  "imageUrlOptimized": "<string>",
                  "imageSizeKbSource": 123,
                  "imageSizeKbOptimized": 123,
                  "imageOptimizedComplete": true,
                  "imageOptimizedLastUpdated": "<string>",
                  "relID": 123,
                  "field": "<string>",
                  "relname": "<string>"
                },
                "iconOptimized": {
                  "id": "<string>",
                  "imageUrlSource": "<string>",
                  "imageUrlOptimized": "<string>",
                  "imageSizeKbSource": 123,
                  "imageSizeKbOptimized": 123,
                  "imageOptimizedComplete": true,
                  "imageOptimizedLastUpdated": "<string>",
                  "relID": 123,
                  "field": "<string>",
                  "relname": "<string>"
                },
                "headerImageOptimized": {
                  "id": "<string>",
                  "imageUrlSource": "<string>",
                  "imageUrlOptimized": "<string>",
                  "imageSizeKbSource": 123,
                  "imageSizeKbOptimized": 123,
                  "imageOptimizedComplete": true,
                  "imageOptimizedLastUpdated": "<string>",
                  "relID": 123,
                  "field": "<string>",
                  "relname": "<string>"
                }
              }
            ],
            "categories": [
              {
                "id": "<string>",
                "label": "<string>",
                "parentCategory": "<string>",
                "slug": "<string>",
                "publishedAt": "<string>",
                "createdBy": "<string>",
                "updatedBy": "<string>",
                "createdAt": "2023-11-07T05:31:56Z",
                "updatedAt": "2023-11-07T05:31:56Z"
              }
            ],
            "tags": [
              {
                "id": "<string>",
                "label": "<string>",
                "slug": "<string>",
                "forceShow": true,
                "publishedAt": "<string>",
                "createdBy": 123,
                "updatedBy": 123,
                "createdAt": "2023-11-07T05:31:56Z",
                "updatedAt": "2023-11-07T05:31:56Z",
                "forceHide": true,
                "isCarousel": true
              }
            ],
            "commentCount": 123,
            "chats": [
              {
                "id": "<string>",
                "channelId": "<string>",
                "channelName": "<string>",
                "channelImage": "<string>",
                "live": true,
                "startTime": "2023-11-07T05:31:56Z",
                "endTime": "2023-11-07T05:31:56Z"
              }
            ]
          }
        ],
        "categories": [
          {
            "id": "<string>",
            "label": "<string>",
            "parentCategory": "<string>",
            "slug": "<string>",
            "publishedAt": "<string>",
            "createdBy": "<string>",
            "updatedBy": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z"
          }
        ],
        "collections": [
          {
            "id": "<string>",
            "ticker": "<string>",
            "slug": "<string>",
            "title": "<string>",
            "subtitle": "<string>",
            "collectionType": "<string>",
            "description": "<string>",
            "tags": "<string>",
            "image": "<string>",
            "icon": "<string>",
            "headerImage": "<string>",
            "layout": "<string>",
            "active": true,
            "closed": true,
            "archived": true,
            "new": true,
            "featured": true,
            "restricted": true,
            "isTemplate": true,
            "templateVariables": "<string>",
            "publishedAt": "<string>",
            "createdBy": "<string>",
            "updatedBy": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z",
            "commentsEnabled": true,
            "imageOptimized": {
              "id": "<string>",
              "imageUrlSource": "<string>",
              "imageUrlOptimized": "<string>",
              "imageSizeKbSource": 123,
              "imageSizeKbOptimized": 123,
              "imageOptimizedComplete": true,
              "imageOptimizedLastUpdated": "<string>",
              "relID": 123,
              "field": "<string>",
              "relname": "<string>"
            },
            "iconOptimized": {
              "id": "<string>",
              "imageUrlSource": "<string>",
              "imageUrlOptimized": "<string>",
              "imageSizeKbSource": 123,
              "imageSizeKbOptimized": 123,
              "imageOptimizedComplete": true,
              "imageOptimizedLastUpdated": "<string>",
              "relID": 123,
              "field": "<string>",
              "relname": "<string>"
            },
            "headerImageOptimized": {
              "id": "<string>",
              "imageUrlSource": "<string>",
              "imageUrlOptimized": "<string>",
              "imageSizeKbSource": 123,
              "imageSizeKbOptimized": 123,
              "imageOptimizedComplete": true,
              "imageOptimizedLastUpdated": "<string>",
              "relID": 123,
              "field": "<string>",
              "relname": "<string>"
            }
          }
        ],
        "tags": [
          {
            "id": "<string>",
            "label": "<string>",
            "slug": "<string>",
            "forceShow": true,
            "publishedAt": "<string>",
            "createdBy": 123,
            "updatedBy": 123,
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z",
            "forceHide": true,
            "isCarousel": true
          }
        ],
        "cyom": true,
        "closedTime": "2023-11-07T05:31:56Z",
        "showAllOutcomes": true,
        "showMarketImages": true,
        "automaticallyResolved": true,
        "enableNegRisk": true,
        "automaticallyActive": true,
        "eventDate": "<string>",
        "startTime": "2023-11-07T05:31:56Z",
        "eventWeek": 123,
        "seriesSlug": "<string>",
        "score": "<string>",
        "elapsed": "<string>",
        "period": "<string>",
        "live": true,
        "ended": true,
        "finishedTimestamp": "2023-11-07T05:31:56Z",
        "gmpChartMode": "<string>",
        "eventCreators": [
          {
            "id": "<string>",
            "creatorName": "<string>",
            "creatorHandle": "<string>",
            "creatorUrl": "<string>",
            "creatorImage": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z"
          }
        ],
        "tweetCount": 123,
        "chats": [
          {
            "id": "<string>",
            "channelId": "<string>",
            "channelName": "<string>",
            "channelImage": "<string>",
            "live": true,
            "startTime": "2023-11-07T05:31:56Z",
            "endTime": "2023-11-07T05:31:56Z"
          }
        ],
        "featuredOrder": 123,
        "estimateValue": true,
        "cantEstimate": true,
        "estimatedValue": "<string>",
        "templates": [
          {
            "id": "<string>",
            "eventTitle": "<string>",
            "eventSlug": "<string>",
            "eventImage": "<string>",
            "marketTitle": "<string>",
            "description": "<string>",
            "resolutionSource": "<string>",
            "negRisk": true,
            "sortBy": "<string>",
            "showMarketImages": true,
            "seriesSlug": "<string>",
            "outcomes": "<string>"
          }
        ],
        "spreadsMainLine": 123,
        "totalsMainLine": 123,
        "carouselMap": "<string>",
        "pendingDeployment": true,
        "deploying": true,
        "deployingTimestamp": "2023-11-07T05:31:56Z",
        "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
        "gameStatus": "<string>"
      }
    ],
    "categories": [
      {
        "id": "<string>",
        "label": "<string>",
        "parentCategory": "<string>",
        "slug": "<string>",
        "publishedAt": "<string>",
        "createdBy": "<string>",
        "updatedBy": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z"
      }
    ],
    "tags": [
      {
        "id": "<string>",
        "label": "<string>",
        "slug": "<string>",
        "forceShow": true,
        "publishedAt": "<string>",
        "createdBy": 123,
        "updatedBy": 123,
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z",
        "forceHide": true,
        "isCarousel": true
      }
    ],
    "creator": "<string>",
    "ready": true,
    "funded": true,
    "pastSlugs": "<string>",
    "readyTimestamp": "2023-11-07T05:31:56Z",
    "fundedTimestamp": "2023-11-07T05:31:56Z",
    "acceptingOrdersTimestamp": "2023-11-07T05:31:56Z",
    "competitive": 123,
    "rewardsMinSize": 123,
    "rewardsMaxSpread": 123,
    "spread": 123,
    "automaticallyResolved": true,
    "oneDayPriceChange": 123,
    "oneHourPriceChange": 123,
    "oneWeekPriceChange": 123,
    "oneMonthPriceChange": 123,
    "oneYearPriceChange": 123,
    "lastTradePrice": 123,
    "bestBid": 123,
    "bestAsk": 123,
    "automaticallyActive": true,
    "clearBookOnStart": true,
    "chartColor": "<string>",
    "seriesColor": "<string>",
    "showGmpSeries": true,
    "showGmpOutcome": true,
    "manualActivation": true,
    "negRiskOther": true,
    "gameId": "<string>",
    "groupItemRange": "<string>",
    "sportsMarketType": "<string>",
    "line": 123,
    "umaResolutionStatuses": "<string>",
    "pendingDeployment": true,
    "deploying": true,
    "deployingTimestamp": "2023-11-07T05:31:56Z",
    "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
    "rfqEnabled": true,
    "eventStartTime": "2023-11-07T05:31:56Z"
  }
]
```

#### Query Parameters

[​](#parameter-limit)

limit

integer

Required range: `x >= 0`

[​](#parameter-offset)

offset

integer

Required range: `x >= 0`

[​](#parameter-order)

order

string

Comma-separated list of fields to order by

[​](#parameter-ascending)

ascending

boolean

[​](#parameter-id)

id

integer[]

[​](#parameter-slug)

slug

string[]

[​](#parameter-clob-token-ids)

clob\_token\_ids

string[]

[​](#parameter-condition-ids)

condition\_ids

string[]

[​](#parameter-market-maker-address)

market\_maker\_address

string[]

[​](#parameter-liquidity-num-min)

liquidity\_num\_min

number

[​](#parameter-liquidity-num-max)

liquidity\_num\_max

number

[​](#parameter-volume-num-min)

volume\_num\_min

number

[​](#parameter-volume-num-max)

volume\_num\_max

number

[​](#parameter-start-date-min)

start\_date\_min

string<date-time>

[​](#parameter-start-date-max)

start\_date\_max

string<date-time>

[​](#parameter-end-date-min)

end\_date\_min

string<date-time>

[​](#parameter-end-date-max)

end\_date\_max

string<date-time>

[​](#parameter-tag-id)

tag\_id

integer

[​](#parameter-related-tags)

related\_tags

boolean

[​](#parameter-cyom)

cyom

boolean

[​](#parameter-uma-resolution-status)

uma\_resolution\_status

string

[​](#parameter-game-id)

game\_id

string

[​](#parameter-sports-market-types)

sports\_market\_types

string[]

[​](#parameter-rewards-min-size)

rewards\_min\_size

number

[​](#parameter-question-ids)

question\_ids

string[]

[​](#parameter-include-tag)

include\_tag

boolean

[​](#parameter-closed)

closed

boolean

#### Response

200 - application/json

List of markets

[​](#response-items-id)

id

string

[​](#response-items-question-one-of-0)

question

string | null

[​](#response-items-condition-id)

conditionId

string

[​](#response-items-slug-one-of-0)

slug

string | null

[​](#response-items-twitter-card-image-one-of-0)

twitterCardImage

string | null

[​](#response-items-resolution-source-one-of-0)

resolutionSource

string | null

[​](#response-items-end-date-one-of-0)

endDate

string<date-time> | null

[​](#response-items-category-one-of-0)

category

string | null

[​](#response-items-amm-type-one-of-0)

ammType

string | null

[​](#response-items-liquidity-one-of-0)

liquidity

string | null

[​](#response-items-sponsor-name-one-of-0)

sponsorName

string | null

[​](#response-items-sponsor-image-one-of-0)

sponsorImage

string | null

[​](#response-items-start-date-one-of-0)

startDate

string<date-time> | null

[​](#response-items-x-axis-value-one-of-0)

xAxisValue

string | null

[​](#response-items-y-axis-value-one-of-0)

yAxisValue

string | null

[​](#response-items-denomination-token-one-of-0)

denominationToken

string | null

[​](#response-items-fee-one-of-0)

fee

string | null

[​](#response-items-image-one-of-0)

image

string | null

[​](#response-items-icon-one-of-0)

icon

string | null

[​](#response-items-lower-bound-one-of-0)

lowerBound

string | null

[​](#response-items-upper-bound-one-of-0)

upperBound

string | null

[​](#response-items-description-one-of-0)

description

string | null

[​](#response-items-outcomes-one-of-0)

outcomes

string | null

[​](#response-items-outcome-prices-one-of-0)

outcomePrices

string | null

[​](#response-items-volume-one-of-0)

volume

string | null

[​](#response-items-active-one-of-0)

active

boolean | null

[​](#response-items-market-type-one-of-0)

marketType

string | null

[​](#response-items-format-type-one-of-0)

formatType

string | null

[​](#response-items-lower-bound-date-one-of-0)

lowerBoundDate

string | null

[​](#response-items-upper-bound-date-one-of-0)

upperBoundDate

string | null

[​](#response-items-closed-one-of-0)

closed

boolean | null

[​](#response-items-market-maker-address)

marketMakerAddress

string

[​](#response-items-created-by-one-of-0)

createdBy

integer | null

[​](#response-items-updated-by-one-of-0)

updatedBy

integer | null

[​](#response-items-created-at-one-of-0)

createdAt

string<date-time> | null

[​](#response-items-updated-at-one-of-0)

updatedAt

string<date-time> | null

[​](#response-items-closed-time-one-of-0)

closedTime

string | null

[​](#response-items-wide-format-one-of-0)

wideFormat

boolean | null

[​](#response-items-new-one-of-0)

new

boolean | null

[​](#response-items-mailchimp-tag-one-of-0)

mailchimpTag

string | null

[​](#response-items-featured-one-of-0)

featured

boolean | null

[​](#response-items-archived-one-of-0)

archived

boolean | null

[​](#response-items-resolved-by-one-of-0)

resolvedBy

string | null

[​](#response-items-restricted-one-of-0)

restricted

boolean | null

[​](#response-items-market-group-one-of-0)

marketGroup

integer | null

[​](#response-items-group-item-title-one-of-0)

groupItemTitle

string | null

[​](#response-items-group-item-threshold-one-of-0)

groupItemThreshold

string | null

[​](#response-items-question-id-one-of-0)

questionID

string | null

[​](#response-items-uma-end-date-one-of-0)

umaEndDate

string | null

[​](#response-items-enable-order-book-one-of-0)

enableOrderBook

boolean | null

[​](#response-items-order-price-min-tick-size-one-of-0)

orderPriceMinTickSize

number | null

[​](#response-items-order-min-size-one-of-0)

orderMinSize

number | null

[​](#response-items-uma-resolution-status-one-of-0)

umaResolutionStatus

string | null

[​](#response-items-curation-order-one-of-0)

curationOrder

integer | null

[​](#response-items-volume-num-one-of-0)

volumeNum

number | null

[​](#response-items-liquidity-num-one-of-0)

liquidityNum

number | null

[​](#response-items-end-date-iso-one-of-0)

endDateIso

string | null

[​](#response-items-start-date-iso-one-of-0)

startDateIso

string | null

[​](#response-items-uma-end-date-iso-one-of-0)

umaEndDateIso

string | null

[​](#response-items-has-reviewed-dates-one-of-0)

hasReviewedDates

boolean | null

[​](#response-items-ready-for-cron-one-of-0)

readyForCron

boolean | null

[​](#response-items-comments-enabled-one-of-0)

commentsEnabled

boolean | null

[​](#response-items-volume24hr-one-of-0)

volume24hr

number | null

[​](#response-items-volume1wk-one-of-0)

volume1wk

number | null

[​](#response-items-volume1mo-one-of-0)

volume1mo

number | null

[​](#response-items-volume1yr-one-of-0)

volume1yr

number | null

[​](#response-items-game-start-time-one-of-0)

gameStartTime

string | null

[​](#response-items-seconds-delay-one-of-0)

secondsDelay

integer | null

[​](#response-items-clob-token-ids-one-of-0)

clobTokenIds

string | null

[​](#response-items-disqus-thread-one-of-0)

disqusThread

string | null

[​](#response-items-short-outcomes-one-of-0)

shortOutcomes

string | null

[​](#response-items-team-aid-one-of-0)

teamAID

string | null

[​](#response-items-team-bid-one-of-0)

teamBID

string | null

[​](#response-items-uma-bond-one-of-0)

umaBond

string | null

[​](#response-items-uma-reward-one-of-0)

umaReward

string | null

[​](#response-items-fpmm-live-one-of-0)

fpmmLive

boolean | null

[​](#response-items-volume24hr-amm-one-of-0)

volume24hrAmm

number | null

[​](#response-items-volume1wk-amm-one-of-0)

volume1wkAmm

number | null

[​](#response-items-volume1mo-amm-one-of-0)

volume1moAmm

number | null

[​](#response-items-volume1yr-amm-one-of-0)

volume1yrAmm

number | null

[​](#response-items-volume24hr-clob-one-of-0)

volume24hrClob

number | null

[​](#response-items-volume1wk-clob-one-of-0)

volume1wkClob

number | null

[​](#response-items-volume1mo-clob-one-of-0)

volume1moClob

number | null

[​](#response-items-volume1yr-clob-one-of-0)

volume1yrClob

number | null

[​](#response-items-volume-amm-one-of-0)

volumeAmm

number | null

[​](#response-items-volume-clob-one-of-0)

volumeClob

number | null

[​](#response-items-liquidity-amm-one-of-0)

liquidityAmm

number | null

[​](#response-items-liquidity-clob-one-of-0)

liquidityClob

number | null

[​](#response-items-maker-base-fee-one-of-0)

makerBaseFee

integer | null

[​](#response-items-taker-base-fee-one-of-0)

takerBaseFee

integer | null

[​](#response-items-custom-liveness-one-of-0)

customLiveness

integer | null

[​](#response-items-accepting-orders-one-of-0)

acceptingOrders

boolean | null

[​](#response-items-notifications-enabled-one-of-0)

notificationsEnabled

boolean | null

[​](#response-items-score-one-of-0)

score

integer | null

[​](#response-items-image-optimized)

imageOptimized

object

Show child attributes

[​](#response-items-icon-optimized)

iconOptimized

object

Show child attributes

[​](#response-items-events)

events

object[]

Show child attributes

[​](#response-items-categories)

categories

object[]

Show child attributes

[​](#response-items-tags)

tags

object[]

Show child attributes

[​](#response-items-creator-one-of-0)

creator

string | null

[​](#response-items-ready-one-of-0)

ready

boolean | null

[​](#response-items-funded-one-of-0)

funded

boolean | null

[​](#response-items-past-slugs-one-of-0)

pastSlugs

string | null

[​](#response-items-ready-timestamp-one-of-0)

readyTimestamp

string<date-time> | null

[​](#response-items-funded-timestamp-one-of-0)

fundedTimestamp

string<date-time> | null

[​](#response-items-accepting-orders-timestamp-one-of-0)

acceptingOrdersTimestamp

string<date-time> | null

[​](#response-items-competitive-one-of-0)

competitive

number | null

[​](#response-items-rewards-min-size-one-of-0)

rewardsMinSize

number | null

[​](#response-items-rewards-max-spread-one-of-0)

rewardsMaxSpread

number | null

[​](#response-items-spread-one-of-0)

spread

number | null

[​](#response-items-automatically-resolved-one-of-0)

automaticallyResolved

boolean | null

[​](#response-items-one-day-price-change-one-of-0)

oneDayPriceChange

number | null

[​](#response-items-one-hour-price-change-one-of-0)

oneHourPriceChange

number | null

[​](#response-items-one-week-price-change-one-of-0)

oneWeekPriceChange

number | null

[​](#response-items-one-month-price-change-one-of-0)

oneMonthPriceChange

number | null

[​](#response-items-one-year-price-change-one-of-0)

oneYearPriceChange

number | null

[​](#response-items-last-trade-price-one-of-0)

lastTradePrice

number | null

[​](#response-items-best-bid-one-of-0)

bestBid

number | null

[​](#response-items-best-ask-one-of-0)

bestAsk

number | null

[​](#response-items-automatically-active-one-of-0)

automaticallyActive

boolean | null

[​](#response-items-clear-book-on-start-one-of-0)

clearBookOnStart

boolean | null

[​](#response-items-chart-color-one-of-0)

chartColor

string | null

[​](#response-items-series-color-one-of-0)

seriesColor

string | null

[​](#response-items-show-gmp-series-one-of-0)

showGmpSeries

boolean | null

[​](#response-items-show-gmp-outcome-one-of-0)

showGmpOutcome

boolean | null

[​](#response-items-manual-activation-one-of-0)

manualActivation

boolean | null

[​](#response-items-neg-risk-other-one-of-0)

negRiskOther

boolean | null

[​](#response-items-game-id-one-of-0)

gameId

string | null

[​](#response-items-group-item-range-one-of-0)

groupItemRange

string | null

[​](#response-items-sports-market-type-one-of-0)

sportsMarketType

string | null

[​](#response-items-line-one-of-0)

line

number | null

[​](#response-items-uma-resolution-statuses-one-of-0)

umaResolutionStatuses

string | null

[​](#response-items-pending-deployment-one-of-0)

pendingDeployment

boolean | null

[​](#response-items-deploying-one-of-0)

deploying

boolean | null

[​](#response-items-deploying-timestamp-one-of-0)

deployingTimestamp

string<date-time> | null

[​](#response-items-scheduled-deployment-timestamp-one-of-0)

scheduledDeploymentTimestamp

string<date-time> | null

[​](#response-items-rfq-enabled-one-of-0)

rfqEnabled

boolean | null

[​](#response-items-event-start-time-one-of-0)

eventStartTime

string<date-time> | null

[Get event by slug](/api-reference/events/get-event-by-slug)[Get market by id](/api-reference/markets/get-market-by-id)

⌘I

---


## API: Download Accounting Snapshot

> Source: https://docs.polymarket.com/api-reference/misc/download-an-accounting-snapshot-zip-of-csvs

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Misc

Download an accounting snapshot (ZIP of CSVs)

GET

/

v1

/

accounting

/

snapshot

Try it

Download an accounting snapshot (ZIP of CSVs)

cURL

Copy

```shiki
curl --request GET \
  --url https://data-api.polymarket.com/v1/accounting/snapshot
```

200

400

500

Copy

```shiki
"<string>"
```

#### Query Parameters

[​](#parameter-user)

user

string

required

User address (0x-prefixed)
User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

#### Response

200

application/zip

ZIP file containing `positions.csv` and `equity.csv`.

The response is of type `file`.

[Data API Health check](/api-reference/data-api-status/data-api-health-check)[Get total markets a user has traded](/api-reference/misc/get-total-markets-a-user-has-traded)

⌘I

---


## API: Get Live Volume

> Source: https://docs.polymarket.com/api-reference/misc/get-live-volume-for-an-event

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Misc

Get live volume for an event

GET

/

live-volume

Try it

Get live volume for an event

cURL

Copy

```shiki
curl --request GET \
  --url https://data-api.polymarket.com/live-volume
```

200

400

500

Copy

```shiki
[
  {
    "total": 123,
    "markets": [
      {
        "market": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",
        "value": 123
      }
    ]
  }
]
```

#### Query Parameters

[​](#parameter-id)

id

integer

required

Required range: `x >= 1`

#### Response

200

application/json

Success

[​](#response-items-total)

total

number

[​](#response-items-markets)

markets

object[]

Show child attributes

[Get open interest](/api-reference/misc/get-open-interest)[Get current positions for a user](/api-reference/core/get-current-positions-for-a-user)

⌘I

---


## API: Get Open Interest

> Source: https://docs.polymarket.com/api-reference/misc/get-open-interest

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Misc

Get open interest

GET

/

oi

Try it

Get open interest

cURL

Copy

```shiki
curl --request GET \
  --url https://data-api.polymarket.com/oi
```

200

400

500

Copy

```shiki
[
  {
    "market": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",
    "value": 123
  }
]
```

#### Query Parameters

[​](#parameter-market)

market

string[]

0x-prefixed 64-hex string

#### Response

200

application/json

Success

[​](#response-items-market)

market

string

0x-prefixed 64-hex string

Example:

`"0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917"`

[​](#response-items-value)

value

number

[Get total markets a user has traded](/api-reference/misc/get-total-markets-a-user-has-traded)[Get live volume for an event](/api-reference/misc/get-live-volume-for-an-event)

⌘I

---


## API: Get Total Markets Traded

> Source: https://docs.polymarket.com/api-reference/misc/get-total-markets-a-user-has-traded

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Misc

Get total markets a user has traded

GET

/

traded

Try it

Get total markets a user has traded

cURL

Copy

```shiki
curl --request GET \
  --url https://data-api.polymarket.com/traded
```

200

400

401

500

Copy

```shiki
{
  "user": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",
  "traded": 123
}
```

#### Query Parameters

[​](#parameter-user)

user

string

required

User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

#### Response

200

application/json

Success

[​](#response-user)

user

string

User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

[​](#response-traded)

traded

integer

[Download an accounting snapshot (ZIP of CSVs)](/api-reference/misc/download-an-accounting-snapshot-zip-of-csvs)[Get open interest](/api-reference/misc/get-open-interest)

⌘I

---


## API: Get Multiple Orderbook Summaries

> Source: https://docs.polymarket.com/api-reference/orderbook/get-multiple-order-books-summaries-by-request

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Orderbook

Get multiple order books summaries by request

POST

/

books

Try it

Get multiple order books summaries by request

cURL

Copy

```shiki
curl --request POST \
  --url https://clob.polymarket.com/books \
  --header 'Content-Type: application/json' \
  --data '
[
  {
    "token_id": "1234567890"
  },
  {
    "token_id": "0987654321"
  }
]
'
```

200

Example

Copy

```shiki
[  
  {  
    "market": "0x1b6f76e5b8587ee896c35847e12d11e75290a8c3934c5952e8a9d6e4c6f03cfa",  
    "asset_id": "1234567890",  
    "timestamp": "2023-10-01T12:00:00Z",  
    "hash": "0xabc123def456...",  
    "bids": [  
      {  
        "price": "1800.50",  
        "size": "10.5"  
      }  
    ],  
    "asks": [  
      {  
        "price": "1800.50",  
        "size": "10.5"  
      }  
    ],  
    "min_order_size": "0.001",  
    "tick_size": "0.01",  
    "neg_risk": false  
  }  
]
```

#### Body

application/json

Maximum array length: `500`

[​](#body-items-token-id)

token\_id

string

required

The unique identifier for the token

Example:

`"1234567890"`

[​](#body-items-side)

side

enum<string>

Optional side parameter for certain operations

Available options:

`BUY`,

`SELL`

Example:

`"BUY"`

#### Response

200

application/json

Successful response

[​](#response-items-market)

market

string

required

Market identifier

Example:

`"0x1b6f76e5b8587ee896c35847e12d11e75290a8c3934c5952e8a9d6e4c6f03cfa"`

[​](#response-items-asset-id)

asset\_id

string

required

Asset identifier

Example:

`"1234567890"`

[​](#response-items-timestamp)

timestamp

string<date-time>

required

Timestamp of the order book snapshot

Example:

`"2023-10-01T12:00:00Z"`

[​](#response-items-hash)

hash

string

required

Hash of the order book state

Example:

`"0xabc123def456..."`

[​](#response-items-bids)

bids

object[]

required

Array of bid levels

Show child attributes

[​](#response-items-asks)

asks

object[]

required

Array of ask levels

Show child attributes

[​](#response-items-min-order-size)

min\_order\_size

string

required

Minimum order size for this market

Example:

`"0.001"`

[​](#response-items-tick-size)

tick\_size

string

required

Minimum price increment

Example:

`"0.01"`

[​](#response-items-neg-risk)

neg\_risk

boolean

required

Whether negative risk is enabled

Example:

`false`

[Get order book summary](/api-reference/orderbook/get-order-book-summary)[Get market price](/api-reference/pricing/get-market-price)

⌘I

---


## API: Get Orderbook Summary

> Source: https://docs.polymarket.com/api-reference/orderbook/get-order-book-summary

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Orderbook

Get order book summary

GET

/

book

Try it

Get order book summary

cURL

Copy

```shiki
curl --request GET \
  --url https://clob.polymarket.com/book
```

200

400

404

500

Copy

```shiki
{
  "market": "0x1b6f76e5b8587ee896c35847e12d11e75290a8c3934c5952e8a9d6e4c6f03cfa",
  "asset_id": "1234567890",
  "timestamp": "2023-10-01T12:00:00Z",
  "hash": "0xabc123def456...",
  "bids": [
    {
      "price": "1800.50",
      "size": "10.5"
    }
  ],
  "asks": [
    {
      "price": "1800.50",
      "size": "10.5"
    }
  ],
  "min_order_size": "0.001",
  "tick_size": "0.01",
  "neg_risk": false
}
```

#### Query Parameters

[​](#parameter-token-id)

token\_id

string

required

The unique identifier for the token

#### Response

200

application/json

Successful response

[​](#response-market)

market

string

required

Market identifier

Example:

`"0x1b6f76e5b8587ee896c35847e12d11e75290a8c3934c5952e8a9d6e4c6f03cfa"`

[​](#response-asset-id)

asset\_id

string

required

Asset identifier

Example:

`"1234567890"`

[​](#response-timestamp)

timestamp

string<date-time>

required

Timestamp of the order book snapshot

Example:

`"2023-10-01T12:00:00Z"`

[​](#response-hash)

hash

string

required

Hash of the order book state

Example:

`"0xabc123def456..."`

[​](#response-bids)

bids

object[]

required

Array of bid levels

Show child attributes

[​](#response-asks)

asks

object[]

required

Array of ask levels

Show child attributes

[​](#response-min-order-size)

min\_order\_size

string

required

Minimum order size for this market

Example:

`"0.001"`

[​](#response-tick-size)

tick\_size

string

required

Minimum price increment

Example:

`"0.01"`

[​](#response-neg-risk)

neg\_risk

boolean

required

Whether negative risk is enabled

Example:

`false`

[Builder Methods](/developers/CLOB/clients/methods-builder)[Get multiple order books summaries by request](/api-reference/orderbook/get-multiple-order-books-summaries-by-request)

⌘I

---


## API: Get Market Price

> Source: https://docs.polymarket.com/api-reference/pricing/get-market-price

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Pricing

Get market price

GET

/

price

Try it

Get market price

cURL

Copy

```shiki
curl --request GET \
  --url https://clob.polymarket.com/price
```

200

Example

Copy

```shiki
{  
  "price": "1800.50"  
}
```

#### Query Parameters

[​](#parameter-token-id)

token\_id

string

required

The unique identifier for the token

[​](#parameter-side)

side

enum<string>

required

The side of the market (BUY or SELL)

Available options:

`BUY`,

`SELL`

#### Response

200

application/json

Successful response

[​](#response-price)

price

string

required

The market price (as string to maintain precision)

Example:

`"1800.50"`

[Get multiple order books summaries by request](/api-reference/orderbook/get-multiple-order-books-summaries-by-request)[Get multiple market prices](/api-reference/pricing/get-multiple-market-prices)

⌘I

---


## API: Get Midpoint Price

> Source: https://docs.polymarket.com/api-reference/pricing/get-midpoint-price

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Pricing

Get midpoint price

GET

/

midpoint

Try it

Get midpoint price

cURL

Copy

```shiki
curl --request GET \
  --url https://clob.polymarket.com/midpoint
```

200

400

404

500

Copy

```shiki
{
  "mid": "1800.75"
}
```

#### Query Parameters

[​](#parameter-token-id)

token\_id

string

required

The unique identifier for the token

#### Response

200

application/json

Successful response

[​](#response-mid)

mid

string

required

The midpoint price (as string to maintain precision)

Example:

`"1800.75"`

[Get multiple market prices by request](/api-reference/pricing/get-multiple-market-prices-by-request)[Get price history for a traded token](/api-reference/pricing/get-price-history-for-a-traded-token)

⌘I

---


## API: Get Multiple Market Prices

> Source: https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Pricing

Get multiple market prices

GET

/

prices

Try it

Get multiple market prices

cURL

Copy

```shiki
curl --request GET \
  --url https://clob.polymarket.com/prices
```

200

400

500

Copy

```shiki
{
  "1234567890": {
    "BUY": "1800.50",
    "SELL": "1801.00"
  },
  "0987654321": {
    "BUY": "50.25",
    "SELL": "50.30"
  }
}
```

#### Response

200

application/json

Successful response

Map of token\_id to side to price

[​](#response-additional-properties)

{key}

object

Show child attributes

[Get market price](/api-reference/pricing/get-market-price)[Get multiple market prices by request](/api-reference/pricing/get-multiple-market-prices-by-request)

⌘I

---


## API: Get Multiple Market Prices by Request

> Source: https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Pricing

Get multiple market prices by request

POST

/

prices

Try it

Get multiple market prices by request

cURL

Copy

```shiki
curl --request POST \
  --url https://clob.polymarket.com/prices \
  --header 'Content-Type: application/json' \
  --data '
[
  {
    "token_id": "1234567890",
    "side": "BUY"
  },
  {
    "token_id": "0987654321",
    "side": "SELL"
  }
]
'
```

200

Example

Copy

```shiki
{  
  "1234567890": {  
    "BUY": "1800.50",  
    "SELL": "1801.00"  
  },  
  "0987654321": {  
    "BUY": "50.25",  
    "SELL": "50.30"  
  }  
}
```

#### Body

application/json

Maximum array length: `500`

[​](#body-items-token-id)

token\_id

string

required

The unique identifier for the token

Example:

`"1234567890"`

[​](#body-items-side)

side

enum<string>

required

The side of the market (BUY or SELL)

Available options:

`BUY`,

`SELL`

Example:

`"BUY"`

#### Response

200

application/json

Successful response

Map of token\_id to side to price

[​](#response-additional-properties)

{key}

object

Show child attributes

[Get multiple market prices](/api-reference/pricing/get-multiple-market-prices)[Get midpoint price](/api-reference/pricing/get-midpoint-price)

⌘I

---


## API: Get Price History

> Source: https://docs.polymarket.com/api-reference/pricing/get-price-history-for-a-traded-token

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Pricing

Get price history for a traded token

GET

/

prices-history

Try it

Get price history for a traded token

cURL

Copy

```shiki
curl --request GET \
  --url https://clob.polymarket.com/prices-history
```

200

400

404

500

Copy

```shiki
{
  "history": [
    {
      "t": 1697875200,
      "p": 1800.75
    }
  ]
}
```

#### Query Parameters

[​](#parameter-market)

market

string

required

The CLOB token ID for which to fetch price history

[​](#parameter-start-ts)

startTs

number

The start time, a Unix timestamp in UTC

[​](#parameter-end-ts)

endTs

number

The end time, a Unix timestamp in UTC

[​](#parameter-interval)

interval

enum<string>

A string representing a duration ending at the current time. Mutually exclusive with startTs and endTs

Available options:

`1m`,

`1w`,

`1d`,

`6h`,

`1h`,

`max`

[​](#parameter-fidelity)

fidelity

number

The resolution of the data, in minutes

#### Response

200

application/json

A list of timestamp/price pairs

[​](#response-history)

history

object[]

required

Show child attributes

[Get midpoint price](/api-reference/pricing/get-midpoint-price)[Get bid-ask spreads](/api-reference/spreads/get-bid-ask-spreads)

⌘I

---


## API: Get Public Profile

> Source: https://docs.polymarket.com/api-reference/profiles/get-public-profile-by-wallet-address

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Profiles

Get public profile by wallet address

GET

/

public-profile

Try it

Get public profile by wallet address

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/public-profile
```

200

400

404

Copy

```shiki
{
  "createdAt": "2023-11-07T05:31:56Z",
  "proxyWallet": "<string>",
  "profileImage": "<string>",
  "displayUsernamePublic": true,
  "bio": "<string>",
  "pseudonym": "<string>",
  "name": "<string>",
  "users": [
    {
      "id": "<string>",
      "creator": true,
      "mod": true
    }
  ],
  "xUsername": "<string>",
  "verifiedBadge": true
}
```

#### Query Parameters

[​](#parameter-address)

address

string

required

The wallet address (proxy wallet or user address)

#### Response

200

application/json

Public profile information

[​](#response-created-at-one-of-0)

createdAt

string<date-time> | null

ISO 8601 timestamp of when the profile was created

[​](#response-proxy-wallet-one-of-0)

proxyWallet

string | null

The proxy wallet address

[​](#response-profile-image-one-of-0)

profileImage

string<uri> | null

URL to the profile image

[​](#response-display-username-public-one-of-0)

displayUsernamePublic

boolean | null

Whether the username is displayed publicly

[​](#response-bio-one-of-0)

bio

string | null

Profile bio

[​](#response-pseudonym-one-of-0)

pseudonym

string | null

Auto-generated pseudonym

[​](#response-name-one-of-0)

name

string | null

User-chosen display name

[​](#response-users-one-of-0)

users

object[] | null

Array of associated user objects

Show child attributes

[​](#response-x-username-one-of-0)

xUsername

string | null

X (Twitter) username

[​](#response-verified-badge-one-of-0)

verifiedBadge

boolean | null

Whether the profile has a verified badge

[Get comments by user address](/api-reference/comments/get-comments-by-user-address)[Search markets, events, and profiles](/api-reference/search/search-markets-events-and-profiles)

⌘I

---


## API: Search

> Source: https://docs.polymarket.com/api-reference/search/search-markets-events-and-profiles

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Search

Search markets, events, and profiles

GET

/

public-search

Try it

Search markets, events, and profiles

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/public-search
```

200

Copy

```shiki
{
  "events": [
    {
      "id": "<string>",
      "ticker": "<string>",
      "slug": "<string>",
      "title": "<string>",
      "subtitle": "<string>",
      "description": "<string>",
      "resolutionSource": "<string>",
      "startDate": "2023-11-07T05:31:56Z",
      "creationDate": "2023-11-07T05:31:56Z",
      "endDate": "2023-11-07T05:31:56Z",
      "image": "<string>",
      "icon": "<string>",
      "active": true,
      "closed": true,
      "archived": true,
      "new": true,
      "featured": true,
      "restricted": true,
      "liquidity": 123,
      "volume": 123,
      "openInterest": 123,
      "sortBy": "<string>",
      "category": "<string>",
      "subcategory": "<string>",
      "isTemplate": true,
      "templateVariables": "<string>",
      "published_at": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "commentsEnabled": true,
      "competitive": 123,
      "volume24hr": 123,
      "volume1wk": 123,
      "volume1mo": 123,
      "volume1yr": 123,
      "featuredImage": "<string>",
      "disqusThread": "<string>",
      "parentEvent": "<string>",
      "enableOrderBook": true,
      "liquidityAmm": 123,
      "liquidityClob": 123,
      "negRisk": true,
      "negRiskMarketID": "<string>",
      "negRiskFeeBips": 123,
      "commentCount": 123,
      "imageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "iconOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "featuredImageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "subEvents": [
        "<string>"
      ],
      "markets": [
        {
          "id": "<string>",
          "question": "<string>",
          "conditionId": "<string>",
          "slug": "<string>",
          "twitterCardImage": "<string>",
          "resolutionSource": "<string>",
          "endDate": "2023-11-07T05:31:56Z",
          "category": "<string>",
          "ammType": "<string>",
          "liquidity": "<string>",
          "sponsorName": "<string>",
          "sponsorImage": "<string>",
          "startDate": "2023-11-07T05:31:56Z",
          "xAxisValue": "<string>",
          "yAxisValue": "<string>",
          "denominationToken": "<string>",
          "fee": "<string>",
          "image": "<string>",
          "icon": "<string>",
          "lowerBound": "<string>",
          "upperBound": "<string>",
          "description": "<string>",
          "outcomes": "<string>",
          "outcomePrices": "<string>",
          "volume": "<string>",
          "active": true,
          "marketType": "<string>",
          "formatType": "<string>",
          "lowerBoundDate": "<string>",
          "upperBoundDate": "<string>",
          "closed": true,
          "marketMakerAddress": "<string>",
          "createdBy": 123,
          "updatedBy": 123,
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "closedTime": "<string>",
          "wideFormat": true,
          "new": true,
          "mailchimpTag": "<string>",
          "featured": true,
          "archived": true,
          "resolvedBy": "<string>",
          "restricted": true,
          "marketGroup": 123,
          "groupItemTitle": "<string>",
          "groupItemThreshold": "<string>",
          "questionID": "<string>",
          "umaEndDate": "<string>",
          "enableOrderBook": true,
          "orderPriceMinTickSize": 123,
          "orderMinSize": 123,
          "umaResolutionStatus": "<string>",
          "curationOrder": 123,
          "volumeNum": 123,
          "liquidityNum": 123,
          "endDateIso": "<string>",
          "startDateIso": "<string>",
          "umaEndDateIso": "<string>",
          "hasReviewedDates": true,
          "readyForCron": true,
          "commentsEnabled": true,
          "volume24hr": 123,
          "volume1wk": 123,
          "volume1mo": 123,
          "volume1yr": 123,
          "gameStartTime": "<string>",
          "secondsDelay": 123,
          "clobTokenIds": "<string>",
          "disqusThread": "<string>",
          "shortOutcomes": "<string>",
          "teamAID": "<string>",
          "teamBID": "<string>",
          "umaBond": "<string>",
          "umaReward": "<string>",
          "fpmmLive": true,
          "volume24hrAmm": 123,
          "volume1wkAmm": 123,
          "volume1moAmm": 123,
          "volume1yrAmm": 123,
          "volume24hrClob": 123,
          "volume1wkClob": 123,
          "volume1moClob": 123,
          "volume1yrClob": 123,
          "volumeAmm": 123,
          "volumeClob": 123,
          "liquidityAmm": 123,
          "liquidityClob": 123,
          "makerBaseFee": 123,
          "takerBaseFee": 123,
          "customLiveness": 123,
          "acceptingOrders": true,
          "notificationsEnabled": true,
          "score": 123,
          "imageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "iconOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "events": "<array>",
          "categories": [
            {
              "id": "<string>",
              "label": "<string>",
              "parentCategory": "<string>",
              "slug": "<string>",
              "publishedAt": "<string>",
              "createdBy": "<string>",
              "updatedBy": "<string>",
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z"
            }
          ],
          "tags": [
            {
              "id": "<string>",
              "label": "<string>",
              "slug": "<string>",
              "forceShow": true,
              "publishedAt": "<string>",
              "createdBy": 123,
              "updatedBy": 123,
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z",
              "forceHide": true,
              "isCarousel": true
            }
          ],
          "creator": "<string>",
          "ready": true,
          "funded": true,
          "pastSlugs": "<string>",
          "readyTimestamp": "2023-11-07T05:31:56Z",
          "fundedTimestamp": "2023-11-07T05:31:56Z",
          "acceptingOrdersTimestamp": "2023-11-07T05:31:56Z",
          "competitive": 123,
          "rewardsMinSize": 123,
          "rewardsMaxSpread": 123,
          "spread": 123,
          "automaticallyResolved": true,
          "oneDayPriceChange": 123,
          "oneHourPriceChange": 123,
          "oneWeekPriceChange": 123,
          "oneMonthPriceChange": 123,
          "oneYearPriceChange": 123,
          "lastTradePrice": 123,
          "bestBid": 123,
          "bestAsk": 123,
          "automaticallyActive": true,
          "clearBookOnStart": true,
          "chartColor": "<string>",
          "seriesColor": "<string>",
          "showGmpSeries": true,
          "showGmpOutcome": true,
          "manualActivation": true,
          "negRiskOther": true,
          "gameId": "<string>",
          "groupItemRange": "<string>",
          "sportsMarketType": "<string>",
          "line": 123,
          "umaResolutionStatuses": "<string>",
          "pendingDeployment": true,
          "deploying": true,
          "deployingTimestamp": "2023-11-07T05:31:56Z",
          "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
          "rfqEnabled": true,
          "eventStartTime": "2023-11-07T05:31:56Z"
        }
      ],
      "series": [
        {
          "id": "<string>",
          "ticker": "<string>",
          "slug": "<string>",
          "title": "<string>",
          "subtitle": "<string>",
          "seriesType": "<string>",
          "recurrence": "<string>",
          "description": "<string>",
          "image": "<string>",
          "icon": "<string>",
          "layout": "<string>",
          "active": true,
          "closed": true,
          "archived": true,
          "new": true,
          "featured": true,
          "restricted": true,
          "isTemplate": true,
          "templateVariables": true,
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "commentsEnabled": true,
          "competitive": "<string>",
          "volume24hr": 123,
          "volume": 123,
          "liquidity": 123,
          "startDate": "2023-11-07T05:31:56Z",
          "pythTokenID": "<string>",
          "cgAssetName": "<string>",
          "score": 123,
          "events": "<array>",
          "collections": [
            {
              "id": "<string>",
              "ticker": "<string>",
              "slug": "<string>",
              "title": "<string>",
              "subtitle": "<string>",
              "collectionType": "<string>",
              "description": "<string>",
              "tags": "<string>",
              "image": "<string>",
              "icon": "<string>",
              "headerImage": "<string>",
              "layout": "<string>",
              "active": true,
              "closed": true,
              "archived": true,
              "new": true,
              "featured": true,
              "restricted": true,
              "isTemplate": true,
              "templateVariables": "<string>",
              "publishedAt": "<string>",
              "createdBy": "<string>",
              "updatedBy": "<string>",
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z",
              "commentsEnabled": true,
              "imageOptimized": {
                "id": "<string>",
                "imageUrlSource": "<string>",
                "imageUrlOptimized": "<string>",
                "imageSizeKbSource": 123,
                "imageSizeKbOptimized": 123,
                "imageOptimizedComplete": true,
                "imageOptimizedLastUpdated": "<string>",
                "relID": 123,
                "field": "<string>",
                "relname": "<string>"
              },
              "iconOptimized": {
                "id": "<string>",
                "imageUrlSource": "<string>",
                "imageUrlOptimized": "<string>",
                "imageSizeKbSource": 123,
                "imageSizeKbOptimized": 123,
                "imageOptimizedComplete": true,
                "imageOptimizedLastUpdated": "<string>",
                "relID": 123,
                "field": "<string>",
                "relname": "<string>"
              },
              "headerImageOptimized": {
                "id": "<string>",
                "imageUrlSource": "<string>",
                "imageUrlOptimized": "<string>",
                "imageSizeKbSource": 123,
                "imageSizeKbOptimized": 123,
                "imageOptimizedComplete": true,
                "imageOptimizedLastUpdated": "<string>",
                "relID": 123,
                "field": "<string>",
                "relname": "<string>"
              }
            }
          ],
          "categories": [
            {
              "id": "<string>",
              "label": "<string>",
              "parentCategory": "<string>",
              "slug": "<string>",
              "publishedAt": "<string>",
              "createdBy": "<string>",
              "updatedBy": "<string>",
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z"
            }
          ],
          "tags": [
            {
              "id": "<string>",
              "label": "<string>",
              "slug": "<string>",
              "forceShow": true,
              "publishedAt": "<string>",
              "createdBy": 123,
              "updatedBy": 123,
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z",
              "forceHide": true,
              "isCarousel": true
            }
          ],
          "commentCount": 123,
          "chats": [
            {
              "id": "<string>",
              "channelId": "<string>",
              "channelName": "<string>",
              "channelImage": "<string>",
              "live": true,
              "startTime": "2023-11-07T05:31:56Z",
              "endTime": "2023-11-07T05:31:56Z"
            }
          ]
        }
      ],
      "categories": [
        {
          "id": "<string>",
          "label": "<string>",
          "parentCategory": "<string>",
          "slug": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z"
        }
      ],
      "collections": [
        {
          "id": "<string>",
          "ticker": "<string>",
          "slug": "<string>",
          "title": "<string>",
          "subtitle": "<string>",
          "collectionType": "<string>",
          "description": "<string>",
          "tags": "<string>",
          "image": "<string>",
          "icon": "<string>",
          "headerImage": "<string>",
          "layout": "<string>",
          "active": true,
          "closed": true,
          "archived": true,
          "new": true,
          "featured": true,
          "restricted": true,
          "isTemplate": true,
          "templateVariables": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "commentsEnabled": true,
          "imageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "iconOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "headerImageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          }
        }
      ],
      "tags": [
        {
          "id": "<string>",
          "label": "<string>",
          "slug": "<string>",
          "forceShow": true,
          "publishedAt": "<string>",
          "createdBy": 123,
          "updatedBy": 123,
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "forceHide": true,
          "isCarousel": true
        }
      ],
      "cyom": true,
      "closedTime": "2023-11-07T05:31:56Z",
      "showAllOutcomes": true,
      "showMarketImages": true,
      "automaticallyResolved": true,
      "enableNegRisk": true,
      "automaticallyActive": true,
      "eventDate": "<string>",
      "startTime": "2023-11-07T05:31:56Z",
      "eventWeek": 123,
      "seriesSlug": "<string>",
      "score": "<string>",
      "elapsed": "<string>",
      "period": "<string>",
      "live": true,
      "ended": true,
      "finishedTimestamp": "2023-11-07T05:31:56Z",
      "gmpChartMode": "<string>",
      "eventCreators": [
        {
          "id": "<string>",
          "creatorName": "<string>",
          "creatorHandle": "<string>",
          "creatorUrl": "<string>",
          "creatorImage": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z"
        }
      ],
      "tweetCount": 123,
      "chats": [
        {
          "id": "<string>",
          "channelId": "<string>",
          "channelName": "<string>",
          "channelImage": "<string>",
          "live": true,
          "startTime": "2023-11-07T05:31:56Z",
          "endTime": "2023-11-07T05:31:56Z"
        }
      ],
      "featuredOrder": 123,
      "estimateValue": true,
      "cantEstimate": true,
      "estimatedValue": "<string>",
      "templates": [
        {
          "id": "<string>",
          "eventTitle": "<string>",
          "eventSlug": "<string>",
          "eventImage": "<string>",
          "marketTitle": "<string>",
          "description": "<string>",
          "resolutionSource": "<string>",
          "negRisk": true,
          "sortBy": "<string>",
          "showMarketImages": true,
          "seriesSlug": "<string>",
          "outcomes": "<string>"
        }
      ],
      "spreadsMainLine": 123,
      "totalsMainLine": 123,
      "carouselMap": "<string>",
      "pendingDeployment": true,
      "deploying": true,
      "deployingTimestamp": "2023-11-07T05:31:56Z",
      "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
      "gameStatus": "<string>"
    }
  ],
  "tags": [
    {
      "id": "<string>",
      "label": "<string>",
      "slug": "<string>",
      "event_count": 123
    }
  ],
  "profiles": [
    {
      "id": "<string>",
      "name": "<string>",
      "user": 123,
      "referral": "<string>",
      "createdBy": 123,
      "updatedBy": 123,
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "utmSource": "<string>",
      "utmMedium": "<string>",
      "utmCampaign": "<string>",
      "utmContent": "<string>",
      "utmTerm": "<string>",
      "walletActivated": true,
      "pseudonym": "<string>",
      "displayUsernamePublic": true,
      "profileImage": "<string>",
      "bio": "<string>",
      "proxyWallet": "<string>",
      "profileImageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "isCloseOnly": true,
      "isCertReq": true,
      "certReqDate": "2023-11-07T05:31:56Z"
    }
  ],
  "pagination": {
    "hasMore": true,
    "totalResults": 123
  }
}
```

#### Query Parameters

[​](#parameter-q)

q

string

required

[​](#parameter-cache)

cache

boolean

[​](#parameter-events-status)

events\_status

string

[​](#parameter-limit-per-type)

limit\_per\_type

integer

[​](#parameter-page)

page

integer

[​](#parameter-events-tag)

events\_tag

string[]

[​](#parameter-keep-closed-markets)

keep\_closed\_markets

integer

[​](#parameter-sort)

sort

string

[​](#parameter-ascending)

ascending

boolean

[​](#parameter-search-tags)

search\_tags

boolean

[​](#parameter-search-profiles)

search\_profiles

boolean

[​](#parameter-recurrence)

recurrence

string

[​](#parameter-exclude-tag-id)

exclude\_tag\_id

integer[]

[​](#parameter-optimized)

optimized

boolean

#### Response

200 - application/json

Search results

[​](#response-events-one-of-0)

events

object[] | null

Show child attributes

[​](#response-tags-one-of-0)

tags

object[] | null

Show child attributes

[​](#response-profiles-one-of-0)

profiles

object[] | null

Show child attributes

[​](#response-pagination)

pagination

object

Show child attributes

[Get public profile by wallet address](/api-reference/profiles/get-public-profile-by-wallet-address)[Data API Health check](/api-reference/data-api-status/data-api-health-check)

⌘I

---


## API: Get Series by ID

> Source: https://docs.polymarket.com/api-reference/series/get-series-by-id

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Series

Get series by id

GET

/

series

/

{id}

Try it

Get series by id

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/series/{id}
```

200

Copy

```shiki
{
  "id": "<string>",
  "ticker": "<string>",
  "slug": "<string>",
  "title": "<string>",
  "subtitle": "<string>",
  "seriesType": "<string>",
  "recurrence": "<string>",
  "description": "<string>",
  "image": "<string>",
  "icon": "<string>",
  "layout": "<string>",
  "active": true,
  "closed": true,
  "archived": true,
  "new": true,
  "featured": true,
  "restricted": true,
  "isTemplate": true,
  "templateVariables": true,
  "publishedAt": "<string>",
  "createdBy": "<string>",
  "updatedBy": "<string>",
  "createdAt": "2023-11-07T05:31:56Z",
  "updatedAt": "2023-11-07T05:31:56Z",
  "commentsEnabled": true,
  "competitive": "<string>",
  "volume24hr": 123,
  "volume": 123,
  "liquidity": 123,
  "startDate": "2023-11-07T05:31:56Z",
  "pythTokenID": "<string>",
  "cgAssetName": "<string>",
  "score": 123,
  "events": [
    {
      "id": "<string>",
      "ticker": "<string>",
      "slug": "<string>",
      "title": "<string>",
      "subtitle": "<string>",
      "description": "<string>",
      "resolutionSource": "<string>",
      "startDate": "2023-11-07T05:31:56Z",
      "creationDate": "2023-11-07T05:31:56Z",
      "endDate": "2023-11-07T05:31:56Z",
      "image": "<string>",
      "icon": "<string>",
      "active": true,
      "closed": true,
      "archived": true,
      "new": true,
      "featured": true,
      "restricted": true,
      "liquidity": 123,
      "volume": 123,
      "openInterest": 123,
      "sortBy": "<string>",
      "category": "<string>",
      "subcategory": "<string>",
      "isTemplate": true,
      "templateVariables": "<string>",
      "published_at": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "commentsEnabled": true,
      "competitive": 123,
      "volume24hr": 123,
      "volume1wk": 123,
      "volume1mo": 123,
      "volume1yr": 123,
      "featuredImage": "<string>",
      "disqusThread": "<string>",
      "parentEvent": "<string>",
      "enableOrderBook": true,
      "liquidityAmm": 123,
      "liquidityClob": 123,
      "negRisk": true,
      "negRiskMarketID": "<string>",
      "negRiskFeeBips": 123,
      "commentCount": 123,
      "imageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "iconOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "featuredImageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "subEvents": [
        "<string>"
      ],
      "markets": [
        {
          "id": "<string>",
          "question": "<string>",
          "conditionId": "<string>",
          "slug": "<string>",
          "twitterCardImage": "<string>",
          "resolutionSource": "<string>",
          "endDate": "2023-11-07T05:31:56Z",
          "category": "<string>",
          "ammType": "<string>",
          "liquidity": "<string>",
          "sponsorName": "<string>",
          "sponsorImage": "<string>",
          "startDate": "2023-11-07T05:31:56Z",
          "xAxisValue": "<string>",
          "yAxisValue": "<string>",
          "denominationToken": "<string>",
          "fee": "<string>",
          "image": "<string>",
          "icon": "<string>",
          "lowerBound": "<string>",
          "upperBound": "<string>",
          "description": "<string>",
          "outcomes": "<string>",
          "outcomePrices": "<string>",
          "volume": "<string>",
          "active": true,
          "marketType": "<string>",
          "formatType": "<string>",
          "lowerBoundDate": "<string>",
          "upperBoundDate": "<string>",
          "closed": true,
          "marketMakerAddress": "<string>",
          "createdBy": 123,
          "updatedBy": 123,
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "closedTime": "<string>",
          "wideFormat": true,
          "new": true,
          "mailchimpTag": "<string>",
          "featured": true,
          "archived": true,
          "resolvedBy": "<string>",
          "restricted": true,
          "marketGroup": 123,
          "groupItemTitle": "<string>",
          "groupItemThreshold": "<string>",
          "questionID": "<string>",
          "umaEndDate": "<string>",
          "enableOrderBook": true,
          "orderPriceMinTickSize": 123,
          "orderMinSize": 123,
          "umaResolutionStatus": "<string>",
          "curationOrder": 123,
          "volumeNum": 123,
          "liquidityNum": 123,
          "endDateIso": "<string>",
          "startDateIso": "<string>",
          "umaEndDateIso": "<string>",
          "hasReviewedDates": true,
          "readyForCron": true,
          "commentsEnabled": true,
          "volume24hr": 123,
          "volume1wk": 123,
          "volume1mo": 123,
          "volume1yr": 123,
          "gameStartTime": "<string>",
          "secondsDelay": 123,
          "clobTokenIds": "<string>",
          "disqusThread": "<string>",
          "shortOutcomes": "<string>",
          "teamAID": "<string>",
          "teamBID": "<string>",
          "umaBond": "<string>",
          "umaReward": "<string>",
          "fpmmLive": true,
          "volume24hrAmm": 123,
          "volume1wkAmm": 123,
          "volume1moAmm": 123,
          "volume1yrAmm": 123,
          "volume24hrClob": 123,
          "volume1wkClob": 123,
          "volume1moClob": 123,
          "volume1yrClob": 123,
          "volumeAmm": 123,
          "volumeClob": 123,
          "liquidityAmm": 123,
          "liquidityClob": 123,
          "makerBaseFee": 123,
          "takerBaseFee": 123,
          "customLiveness": 123,
          "acceptingOrders": true,
          "notificationsEnabled": true,
          "score": 123,
          "imageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "iconOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "events": "<array>",
          "categories": [
            {
              "id": "<string>",
              "label": "<string>",
              "parentCategory": "<string>",
              "slug": "<string>",
              "publishedAt": "<string>",
              "createdBy": "<string>",
              "updatedBy": "<string>",
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z"
            }
          ],
          "tags": [
            {
              "id": "<string>",
              "label": "<string>",
              "slug": "<string>",
              "forceShow": true,
              "publishedAt": "<string>",
              "createdBy": 123,
              "updatedBy": 123,
              "createdAt": "2023-11-07T05:31:56Z",
              "updatedAt": "2023-11-07T05:31:56Z",
              "forceHide": true,
              "isCarousel": true
            }
          ],
          "creator": "<string>",
          "ready": true,
          "funded": true,
          "pastSlugs": "<string>",
          "readyTimestamp": "2023-11-07T05:31:56Z",
          "fundedTimestamp": "2023-11-07T05:31:56Z",
          "acceptingOrdersTimestamp": "2023-11-07T05:31:56Z",
          "competitive": 123,
          "rewardsMinSize": 123,
          "rewardsMaxSpread": 123,
          "spread": 123,
          "automaticallyResolved": true,
          "oneDayPriceChange": 123,
          "oneHourPriceChange": 123,
          "oneWeekPriceChange": 123,
          "oneMonthPriceChange": 123,
          "oneYearPriceChange": 123,
          "lastTradePrice": 123,
          "bestBid": 123,
          "bestAsk": 123,
          "automaticallyActive": true,
          "clearBookOnStart": true,
          "chartColor": "<string>",
          "seriesColor": "<string>",
          "showGmpSeries": true,
          "showGmpOutcome": true,
          "manualActivation": true,
          "negRiskOther": true,
          "gameId": "<string>",
          "groupItemRange": "<string>",
          "sportsMarketType": "<string>",
          "line": 123,
          "umaResolutionStatuses": "<string>",
          "pendingDeployment": true,
          "deploying": true,
          "deployingTimestamp": "2023-11-07T05:31:56Z",
          "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
          "rfqEnabled": true,
          "eventStartTime": "2023-11-07T05:31:56Z"
        }
      ],
      "series": "<array>",
      "categories": [
        {
          "id": "<string>",
          "label": "<string>",
          "parentCategory": "<string>",
          "slug": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z"
        }
      ],
      "collections": [
        {
          "id": "<string>",
          "ticker": "<string>",
          "slug": "<string>",
          "title": "<string>",
          "subtitle": "<string>",
          "collectionType": "<string>",
          "description": "<string>",
          "tags": "<string>",
          "image": "<string>",
          "icon": "<string>",
          "headerImage": "<string>",
          "layout": "<string>",
          "active": true,
          "closed": true,
          "archived": true,
          "new": true,
          "featured": true,
          "restricted": true,
          "isTemplate": true,
          "templateVariables": "<string>",
          "publishedAt": "<string>",
          "createdBy": "<string>",
          "updatedBy": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "commentsEnabled": true,
          "imageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "iconOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          },
          "headerImageOptimized": {
            "id": "<string>",
            "imageUrlSource": "<string>",
            "imageUrlOptimized": "<string>",
            "imageSizeKbSource": 123,
            "imageSizeKbOptimized": 123,
            "imageOptimizedComplete": true,
            "imageOptimizedLastUpdated": "<string>",
            "relID": 123,
            "field": "<string>",
            "relname": "<string>"
          }
        }
      ],
      "tags": [
        {
          "id": "<string>",
          "label": "<string>",
          "slug": "<string>",
          "forceShow": true,
          "publishedAt": "<string>",
          "createdBy": 123,
          "updatedBy": 123,
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z",
          "forceHide": true,
          "isCarousel": true
        }
      ],
      "cyom": true,
      "closedTime": "2023-11-07T05:31:56Z",
      "showAllOutcomes": true,
      "showMarketImages": true,
      "automaticallyResolved": true,
      "enableNegRisk": true,
      "automaticallyActive": true,
      "eventDate": "<string>",
      "startTime": "2023-11-07T05:31:56Z",
      "eventWeek": 123,
      "seriesSlug": "<string>",
      "score": "<string>",
      "elapsed": "<string>",
      "period": "<string>",
      "live": true,
      "ended": true,
      "finishedTimestamp": "2023-11-07T05:31:56Z",
      "gmpChartMode": "<string>",
      "eventCreators": [
        {
          "id": "<string>",
          "creatorName": "<string>",
          "creatorHandle": "<string>",
          "creatorUrl": "<string>",
          "creatorImage": "<string>",
          "createdAt": "2023-11-07T05:31:56Z",
          "updatedAt": "2023-11-07T05:31:56Z"
        }
      ],
      "tweetCount": 123,
      "chats": [
        {
          "id": "<string>",
          "channelId": "<string>",
          "channelName": "<string>",
          "channelImage": "<string>",
          "live": true,
          "startTime": "2023-11-07T05:31:56Z",
          "endTime": "2023-11-07T05:31:56Z"
        }
      ],
      "featuredOrder": 123,
      "estimateValue": true,
      "cantEstimate": true,
      "estimatedValue": "<string>",
      "templates": [
        {
          "id": "<string>",
          "eventTitle": "<string>",
          "eventSlug": "<string>",
          "eventImage": "<string>",
          "marketTitle": "<string>",
          "description": "<string>",
          "resolutionSource": "<string>",
          "negRisk": true,
          "sortBy": "<string>",
          "showMarketImages": true,
          "seriesSlug": "<string>",
          "outcomes": "<string>"
        }
      ],
      "spreadsMainLine": 123,
      "totalsMainLine": 123,
      "carouselMap": "<string>",
      "pendingDeployment": true,
      "deploying": true,
      "deployingTimestamp": "2023-11-07T05:31:56Z",
      "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
      "gameStatus": "<string>"
    }
  ],
  "collections": [
    {
      "id": "<string>",
      "ticker": "<string>",
      "slug": "<string>",
      "title": "<string>",
      "subtitle": "<string>",
      "collectionType": "<string>",
      "description": "<string>",
      "tags": "<string>",
      "image": "<string>",
      "icon": "<string>",
      "headerImage": "<string>",
      "layout": "<string>",
      "active": true,
      "closed": true,
      "archived": true,
      "new": true,
      "featured": true,
      "restricted": true,
      "isTemplate": true,
      "templateVariables": "<string>",
      "publishedAt": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "commentsEnabled": true,
      "imageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "iconOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      },
      "headerImageOptimized": {
        "id": "<string>",
        "imageUrlSource": "<string>",
        "imageUrlOptimized": "<string>",
        "imageSizeKbSource": 123,
        "imageSizeKbOptimized": 123,
        "imageOptimizedComplete": true,
        "imageOptimizedLastUpdated": "<string>",
        "relID": 123,
        "field": "<string>",
        "relname": "<string>"
      }
    }
  ],
  "categories": [
    {
      "id": "<string>",
      "label": "<string>",
      "parentCategory": "<string>",
      "slug": "<string>",
      "publishedAt": "<string>",
      "createdBy": "<string>",
      "updatedBy": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z"
    }
  ],
  "tags": [
    {
      "id": "<string>",
      "label": "<string>",
      "slug": "<string>",
      "forceShow": true,
      "publishedAt": "<string>",
      "createdBy": 123,
      "updatedBy": 123,
      "createdAt": "2023-11-07T05:31:56Z",
      "updatedAt": "2023-11-07T05:31:56Z",
      "forceHide": true,
      "isCarousel": true
    }
  ],
  "commentCount": 123,
  "chats": [
    {
      "id": "<string>",
      "channelId": "<string>",
      "channelName": "<string>",
      "channelImage": "<string>",
      "live": true,
      "startTime": "2023-11-07T05:31:56Z",
      "endTime": "2023-11-07T05:31:56Z"
    }
  ]
}
```

#### Path Parameters

[​](#parameter-id)

id

integer

required

#### Query Parameters

[​](#parameter-include-chat)

include\_chat

boolean

#### Response

200

application/json

Series

[​](#response-id)

id

string

[​](#response-ticker-one-of-0)

ticker

string | null

[​](#response-slug-one-of-0)

slug

string | null

[​](#response-title-one-of-0)

title

string | null

[​](#response-subtitle-one-of-0)

subtitle

string | null

[​](#response-series-type-one-of-0)

seriesType

string | null

[​](#response-recurrence-one-of-0)

recurrence

string | null

[​](#response-description-one-of-0)

description

string | null

[​](#response-image-one-of-0)

image

string | null

[​](#response-icon-one-of-0)

icon

string | null

[​](#response-layout-one-of-0)

layout

string | null

[​](#response-active-one-of-0)

active

boolean | null

[​](#response-closed-one-of-0)

closed

boolean | null

[​](#response-archived-one-of-0)

archived

boolean | null

[​](#response-new-one-of-0)

new

boolean | null

[​](#response-featured-one-of-0)

featured

boolean | null

[​](#response-restricted-one-of-0)

restricted

boolean | null

[​](#response-is-template-one-of-0)

isTemplate

boolean | null

[​](#response-template-variables-one-of-0)

templateVariables

boolean | null

[​](#response-published-at-one-of-0)

publishedAt

string | null

[​](#response-created-by-one-of-0)

createdBy

string | null

[​](#response-updated-by-one-of-0)

updatedBy

string | null

[​](#response-created-at-one-of-0)

createdAt

string<date-time> | null

[​](#response-updated-at-one-of-0)

updatedAt

string<date-time> | null

[​](#response-comments-enabled-one-of-0)

commentsEnabled

boolean | null

[​](#response-competitive-one-of-0)

competitive

string | null

[​](#response-volume24hr-one-of-0)

volume24hr

number | null

[​](#response-volume-one-of-0)

volume

number | null

[​](#response-liquidity-one-of-0)

liquidity

number | null

[​](#response-start-date-one-of-0)

startDate

string<date-time> | null

[​](#response-pyth-token-id-one-of-0)

pythTokenID

string | null

[​](#response-cg-asset-name-one-of-0)

cgAssetName

string | null

[​](#response-score-one-of-0)

score

integer | null

[​](#response-events)

events

object[]

Show child attributes

[​](#response-collections)

collections

object[]

Show child attributes

[​](#response-categories)

categories

object[]

Show child attributes

[​](#response-tags)

tags

object[]

Show child attributes

[​](#response-comment-count-one-of-0)

commentCount

integer | null

[​](#response-chats)

chats

object[]

Show child attributes

[List series](/api-reference/series/list-series)[List comments](/api-reference/comments/list-comments)

⌘I

---


## API: List Series

> Source: https://docs.polymarket.com/api-reference/series/list-series

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Series

List series

GET

/

series

Try it

List series

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/series
```

200

Copy

```shiki
[
  {
    "id": "<string>",
    "ticker": "<string>",
    "slug": "<string>",
    "title": "<string>",
    "subtitle": "<string>",
    "seriesType": "<string>",
    "recurrence": "<string>",
    "description": "<string>",
    "image": "<string>",
    "icon": "<string>",
    "layout": "<string>",
    "active": true,
    "closed": true,
    "archived": true,
    "new": true,
    "featured": true,
    "restricted": true,
    "isTemplate": true,
    "templateVariables": true,
    "publishedAt": "<string>",
    "createdBy": "<string>",
    "updatedBy": "<string>",
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "commentsEnabled": true,
    "competitive": "<string>",
    "volume24hr": 123,
    "volume": 123,
    "liquidity": 123,
    "startDate": "2023-11-07T05:31:56Z",
    "pythTokenID": "<string>",
    "cgAssetName": "<string>",
    "score": 123,
    "events": [
      {
        "id": "<string>",
        "ticker": "<string>",
        "slug": "<string>",
        "title": "<string>",
        "subtitle": "<string>",
        "description": "<string>",
        "resolutionSource": "<string>",
        "startDate": "2023-11-07T05:31:56Z",
        "creationDate": "2023-11-07T05:31:56Z",
        "endDate": "2023-11-07T05:31:56Z",
        "image": "<string>",
        "icon": "<string>",
        "active": true,
        "closed": true,
        "archived": true,
        "new": true,
        "featured": true,
        "restricted": true,
        "liquidity": 123,
        "volume": 123,
        "openInterest": 123,
        "sortBy": "<string>",
        "category": "<string>",
        "subcategory": "<string>",
        "isTemplate": true,
        "templateVariables": "<string>",
        "published_at": "<string>",
        "createdBy": "<string>",
        "updatedBy": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z",
        "commentsEnabled": true,
        "competitive": 123,
        "volume24hr": 123,
        "volume1wk": 123,
        "volume1mo": 123,
        "volume1yr": 123,
        "featuredImage": "<string>",
        "disqusThread": "<string>",
        "parentEvent": "<string>",
        "enableOrderBook": true,
        "liquidityAmm": 123,
        "liquidityClob": 123,
        "negRisk": true,
        "negRiskMarketID": "<string>",
        "negRiskFeeBips": 123,
        "commentCount": 123,
        "imageOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "iconOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "featuredImageOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "subEvents": [
          "<string>"
        ],
        "markets": [
          {
            "id": "<string>",
            "question": "<string>",
            "conditionId": "<string>",
            "slug": "<string>",
            "twitterCardImage": "<string>",
            "resolutionSource": "<string>",
            "endDate": "2023-11-07T05:31:56Z",
            "category": "<string>",
            "ammType": "<string>",
            "liquidity": "<string>",
            "sponsorName": "<string>",
            "sponsorImage": "<string>",
            "startDate": "2023-11-07T05:31:56Z",
            "xAxisValue": "<string>",
            "yAxisValue": "<string>",
            "denominationToken": "<string>",
            "fee": "<string>",
            "image": "<string>",
            "icon": "<string>",
            "lowerBound": "<string>",
            "upperBound": "<string>",
            "description": "<string>",
            "outcomes": "<string>",
            "outcomePrices": "<string>",
            "volume": "<string>",
            "active": true,
            "marketType": "<string>",
            "formatType": "<string>",
            "lowerBoundDate": "<string>",
            "upperBoundDate": "<string>",
            "closed": true,
            "marketMakerAddress": "<string>",
            "createdBy": 123,
            "updatedBy": 123,
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z",
            "closedTime": "<string>",
            "wideFormat": true,
            "new": true,
            "mailchimpTag": "<string>",
            "featured": true,
            "archived": true,
            "resolvedBy": "<string>",
            "restricted": true,
            "marketGroup": 123,
            "groupItemTitle": "<string>",
            "groupItemThreshold": "<string>",
            "questionID": "<string>",
            "umaEndDate": "<string>",
            "enableOrderBook": true,
            "orderPriceMinTickSize": 123,
            "orderMinSize": 123,
            "umaResolutionStatus": "<string>",
            "curationOrder": 123,
            "volumeNum": 123,
            "liquidityNum": 123,
            "endDateIso": "<string>",
            "startDateIso": "<string>",
            "umaEndDateIso": "<string>",
            "hasReviewedDates": true,
            "readyForCron": true,
            "commentsEnabled": true,
            "volume24hr": 123,
            "volume1wk": 123,
            "volume1mo": 123,
            "volume1yr": 123,
            "gameStartTime": "<string>",
            "secondsDelay": 123,
            "clobTokenIds": "<string>",
            "disqusThread": "<string>",
            "shortOutcomes": "<string>",
            "teamAID": "<string>",
            "teamBID": "<string>",
            "umaBond": "<string>",
            "umaReward": "<string>",
            "fpmmLive": true,
            "volume24hrAmm": 123,
            "volume1wkAmm": 123,
            "volume1moAmm": 123,
            "volume1yrAmm": 123,
            "volume24hrClob": 123,
            "volume1wkClob": 123,
            "volume1moClob": 123,
            "volume1yrClob": 123,
            "volumeAmm": 123,
            "volumeClob": 123,
            "liquidityAmm": 123,
            "liquidityClob": 123,
            "makerBaseFee": 123,
            "takerBaseFee": 123,
            "customLiveness": 123,
            "acceptingOrders": true,
            "notificationsEnabled": true,
            "score": 123,
            "imageOptimized": {
              "id": "<string>",
              "imageUrlSource": "<string>",
              "imageUrlOptimized": "<string>",
              "imageSizeKbSource": 123,
              "imageSizeKbOptimized": 123,
              "imageOptimizedComplete": true,
              "imageOptimizedLastUpdated": "<string>",
              "relID": 123,
              "field": "<string>",
              "relname": "<string>"
            },
            "iconOptimized": {
              "id": "<string>",
              "imageUrlSource": "<string>",
              "imageUrlOptimized": "<string>",
              "imageSizeKbSource": 123,
              "imageSizeKbOptimized": 123,
              "imageOptimizedComplete": true,
              "imageOptimizedLastUpdated": "<string>",
              "relID": 123,
              "field": "<string>",
              "relname": "<string>"
            },
            "events": "<array>",
            "categories": [
              {
                "id": "<string>",
                "label": "<string>",
                "parentCategory": "<string>",
                "slug": "<string>",
                "publishedAt": "<string>",
                "createdBy": "<string>",
                "updatedBy": "<string>",
                "createdAt": "2023-11-07T05:31:56Z",
                "updatedAt": "2023-11-07T05:31:56Z"
              }
            ],
            "tags": [
              {
                "id": "<string>",
                "label": "<string>",
                "slug": "<string>",
                "forceShow": true,
                "publishedAt": "<string>",
                "createdBy": 123,
                "updatedBy": 123,
                "createdAt": "2023-11-07T05:31:56Z",
                "updatedAt": "2023-11-07T05:31:56Z",
                "forceHide": true,
                "isCarousel": true
              }
            ],
            "creator": "<string>",
            "ready": true,
            "funded": true,
            "pastSlugs": "<string>",
            "readyTimestamp": "2023-11-07T05:31:56Z",
            "fundedTimestamp": "2023-11-07T05:31:56Z",
            "acceptingOrdersTimestamp": "2023-11-07T05:31:56Z",
            "competitive": 123,
            "rewardsMinSize": 123,
            "rewardsMaxSpread": 123,
            "spread": 123,
            "automaticallyResolved": true,
            "oneDayPriceChange": 123,
            "oneHourPriceChange": 123,
            "oneWeekPriceChange": 123,
            "oneMonthPriceChange": 123,
            "oneYearPriceChange": 123,
            "lastTradePrice": 123,
            "bestBid": 123,
            "bestAsk": 123,
            "automaticallyActive": true,
            "clearBookOnStart": true,
            "chartColor": "<string>",
            "seriesColor": "<string>",
            "showGmpSeries": true,
            "showGmpOutcome": true,
            "manualActivation": true,
            "negRiskOther": true,
            "gameId": "<string>",
            "groupItemRange": "<string>",
            "sportsMarketType": "<string>",
            "line": 123,
            "umaResolutionStatuses": "<string>",
            "pendingDeployment": true,
            "deploying": true,
            "deployingTimestamp": "2023-11-07T05:31:56Z",
            "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
            "rfqEnabled": true,
            "eventStartTime": "2023-11-07T05:31:56Z"
          }
        ],
        "series": "<array>",
        "categories": [
          {
            "id": "<string>",
            "label": "<string>",
            "parentCategory": "<string>",
            "slug": "<string>",
            "publishedAt": "<string>",
            "createdBy": "<string>",
            "updatedBy": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z"
          }
        ],
        "collections": [
          {
            "id": "<string>",
            "ticker": "<string>",
            "slug": "<string>",
            "title": "<string>",
            "subtitle": "<string>",
            "collectionType": "<string>",
            "description": "<string>",
            "tags": "<string>",
            "image": "<string>",
            "icon": "<string>",
            "headerImage": "<string>",
            "layout": "<string>",
            "active": true,
            "closed": true,
            "archived": true,
            "new": true,
            "featured": true,
            "restricted": true,
            "isTemplate": true,
            "templateVariables": "<string>",
            "publishedAt": "<string>",
            "createdBy": "<string>",
            "updatedBy": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z",
            "commentsEnabled": true,
            "imageOptimized": {
              "id": "<string>",
              "imageUrlSource": "<string>",
              "imageUrlOptimized": "<string>",
              "imageSizeKbSource": 123,
              "imageSizeKbOptimized": 123,
              "imageOptimizedComplete": true,
              "imageOptimizedLastUpdated": "<string>",
              "relID": 123,
              "field": "<string>",
              "relname": "<string>"
            },
            "iconOptimized": {
              "id": "<string>",
              "imageUrlSource": "<string>",
              "imageUrlOptimized": "<string>",
              "imageSizeKbSource": 123,
              "imageSizeKbOptimized": 123,
              "imageOptimizedComplete": true,
              "imageOptimizedLastUpdated": "<string>",
              "relID": 123,
              "field": "<string>",
              "relname": "<string>"
            },
            "headerImageOptimized": {
              "id": "<string>",
              "imageUrlSource": "<string>",
              "imageUrlOptimized": "<string>",
              "imageSizeKbSource": 123,
              "imageSizeKbOptimized": 123,
              "imageOptimizedComplete": true,
              "imageOptimizedLastUpdated": "<string>",
              "relID": 123,
              "field": "<string>",
              "relname": "<string>"
            }
          }
        ],
        "tags": [
          {
            "id": "<string>",
            "label": "<string>",
            "slug": "<string>",
            "forceShow": true,
            "publishedAt": "<string>",
            "createdBy": 123,
            "updatedBy": 123,
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z",
            "forceHide": true,
            "isCarousel": true
          }
        ],
        "cyom": true,
        "closedTime": "2023-11-07T05:31:56Z",
        "showAllOutcomes": true,
        "showMarketImages": true,
        "automaticallyResolved": true,
        "enableNegRisk": true,
        "automaticallyActive": true,
        "eventDate": "<string>",
        "startTime": "2023-11-07T05:31:56Z",
        "eventWeek": 123,
        "seriesSlug": "<string>",
        "score": "<string>",
        "elapsed": "<string>",
        "period": "<string>",
        "live": true,
        "ended": true,
        "finishedTimestamp": "2023-11-07T05:31:56Z",
        "gmpChartMode": "<string>",
        "eventCreators": [
          {
            "id": "<string>",
            "creatorName": "<string>",
            "creatorHandle": "<string>",
            "creatorUrl": "<string>",
            "creatorImage": "<string>",
            "createdAt": "2023-11-07T05:31:56Z",
            "updatedAt": "2023-11-07T05:31:56Z"
          }
        ],
        "tweetCount": 123,
        "chats": [
          {
            "id": "<string>",
            "channelId": "<string>",
            "channelName": "<string>",
            "channelImage": "<string>",
            "live": true,
            "startTime": "2023-11-07T05:31:56Z",
            "endTime": "2023-11-07T05:31:56Z"
          }
        ],
        "featuredOrder": 123,
        "estimateValue": true,
        "cantEstimate": true,
        "estimatedValue": "<string>",
        "templates": [
          {
            "id": "<string>",
            "eventTitle": "<string>",
            "eventSlug": "<string>",
            "eventImage": "<string>",
            "marketTitle": "<string>",
            "description": "<string>",
            "resolutionSource": "<string>",
            "negRisk": true,
            "sortBy": "<string>",
            "showMarketImages": true,
            "seriesSlug": "<string>",
            "outcomes": "<string>"
          }
        ],
        "spreadsMainLine": 123,
        "totalsMainLine": 123,
        "carouselMap": "<string>",
        "pendingDeployment": true,
        "deploying": true,
        "deployingTimestamp": "2023-11-07T05:31:56Z",
        "scheduledDeploymentTimestamp": "2023-11-07T05:31:56Z",
        "gameStatus": "<string>"
      }
    ],
    "collections": [
      {
        "id": "<string>",
        "ticker": "<string>",
        "slug": "<string>",
        "title": "<string>",
        "subtitle": "<string>",
        "collectionType": "<string>",
        "description": "<string>",
        "tags": "<string>",
        "image": "<string>",
        "icon": "<string>",
        "headerImage": "<string>",
        "layout": "<string>",
        "active": true,
        "closed": true,
        "archived": true,
        "new": true,
        "featured": true,
        "restricted": true,
        "isTemplate": true,
        "templateVariables": "<string>",
        "publishedAt": "<string>",
        "createdBy": "<string>",
        "updatedBy": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z",
        "commentsEnabled": true,
        "imageOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "iconOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        },
        "headerImageOptimized": {
          "id": "<string>",
          "imageUrlSource": "<string>",
          "imageUrlOptimized": "<string>",
          "imageSizeKbSource": 123,
          "imageSizeKbOptimized": 123,
          "imageOptimizedComplete": true,
          "imageOptimizedLastUpdated": "<string>",
          "relID": 123,
          "field": "<string>",
          "relname": "<string>"
        }
      }
    ],
    "categories": [
      {
        "id": "<string>",
        "label": "<string>",
        "parentCategory": "<string>",
        "slug": "<string>",
        "publishedAt": "<string>",
        "createdBy": "<string>",
        "updatedBy": "<string>",
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z"
      }
    ],
    "tags": [
      {
        "id": "<string>",
        "label": "<string>",
        "slug": "<string>",
        "forceShow": true,
        "publishedAt": "<string>",
        "createdBy": 123,
        "updatedBy": 123,
        "createdAt": "2023-11-07T05:31:56Z",
        "updatedAt": "2023-11-07T05:31:56Z",
        "forceHide": true,
        "isCarousel": true
      }
    ],
    "commentCount": 123,
    "chats": [
      {
        "id": "<string>",
        "channelId": "<string>",
        "channelName": "<string>",
        "channelImage": "<string>",
        "live": true,
        "startTime": "2023-11-07T05:31:56Z",
        "endTime": "2023-11-07T05:31:56Z"
      }
    ]
  }
]
```

#### Query Parameters

[​](#parameter-limit)

limit

integer

Required range: `x >= 0`

[​](#parameter-offset)

offset

integer

Required range: `x >= 0`

[​](#parameter-order)

order

string

Comma-separated list of fields to order by

[​](#parameter-ascending)

ascending

boolean

[​](#parameter-slug)

slug

string[]

[​](#parameter-categories-ids)

categories\_ids

integer[]

[​](#parameter-categories-labels)

categories\_labels

string[]

[​](#parameter-closed)

closed

boolean

[​](#parameter-include-chat)

include\_chat

boolean

[​](#parameter-recurrence)

recurrence

string

#### Response

200 - application/json

List of series

[​](#response-items-id)

id

string

[​](#response-items-ticker-one-of-0)

ticker

string | null

[​](#response-items-slug-one-of-0)

slug

string | null

[​](#response-items-title-one-of-0)

title

string | null

[​](#response-items-subtitle-one-of-0)

subtitle

string | null

[​](#response-items-series-type-one-of-0)

seriesType

string | null

[​](#response-items-recurrence-one-of-0)

recurrence

string | null

[​](#response-items-description-one-of-0)

description

string | null

[​](#response-items-image-one-of-0)

image

string | null

[​](#response-items-icon-one-of-0)

icon

string | null

[​](#response-items-layout-one-of-0)

layout

string | null

[​](#response-items-active-one-of-0)

active

boolean | null

[​](#response-items-closed-one-of-0)

closed

boolean | null

[​](#response-items-archived-one-of-0)

archived

boolean | null

[​](#response-items-new-one-of-0)

new

boolean | null

[​](#response-items-featured-one-of-0)

featured

boolean | null

[​](#response-items-restricted-one-of-0)

restricted

boolean | null

[​](#response-items-is-template-one-of-0)

isTemplate

boolean | null

[​](#response-items-template-variables-one-of-0)

templateVariables

boolean | null

[​](#response-items-published-at-one-of-0)

publishedAt

string | null

[​](#response-items-created-by-one-of-0)

createdBy

string | null

[​](#response-items-updated-by-one-of-0)

updatedBy

string | null

[​](#response-items-created-at-one-of-0)

createdAt

string<date-time> | null

[​](#response-items-updated-at-one-of-0)

updatedAt

string<date-time> | null

[​](#response-items-comments-enabled-one-of-0)

commentsEnabled

boolean | null

[​](#response-items-competitive-one-of-0)

competitive

string | null

[​](#response-items-volume24hr-one-of-0)

volume24hr

number | null

[​](#response-items-volume-one-of-0)

volume

number | null

[​](#response-items-liquidity-one-of-0)

liquidity

number | null

[​](#response-items-start-date-one-of-0)

startDate

string<date-time> | null

[​](#response-items-pyth-token-id-one-of-0)

pythTokenID

string | null

[​](#response-items-cg-asset-name-one-of-0)

cgAssetName

string | null

[​](#response-items-score-one-of-0)

score

integer | null

[​](#response-items-events)

events

object[]

Show child attributes

[​](#response-items-collections)

collections

object[]

Show child attributes

[​](#response-items-categories)

categories

object[]

Show child attributes

[​](#response-items-tags)

tags

object[]

Show child attributes

[​](#response-items-comment-count-one-of-0)

commentCount

integer | null

[​](#response-items-chats)

chats

object[]

Show child attributes

[Get market by slug](/api-reference/markets/get-market-by-slug)[Get series by id](/api-reference/series/get-series-by-id)

⌘I

---


## API: Get Sports Metadata

> Source: https://docs.polymarket.com/api-reference/sports/get-sports-metadata-information

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Sports

Get sports metadata information

GET

/

sports

Try it

Get sports metadata information

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/sports
```

200

Copy

```shiki
[
  {
    "sport": "<string>",
    "image": "<string>",
    "resolution": "<string>",
    "ordering": "<string>",
    "tags": "<string>",
    "series": "<string>"
  }
]
```

#### Response

200 - application/json

List of sports metadata objects containing sport configuration details, visual assets, and related identifiers

[​](#response-items-sport)

sport

string

The sport identifier or abbreviation

[​](#response-items-image)

image

string<uri>

URL to the sport's logo or image asset

[​](#response-items-resolution)

resolution

string<uri>

URL to the official resolution source for the sport (e.g., league website)

[​](#response-items-ordering)

ordering

string

Preferred ordering for sport display, typically "home" or "away"

[​](#response-items-tags)

tags

string

Comma-separated list of tag IDs associated with the sport for categorization and filtering

[​](#response-items-series)

series

string

Series identifier linking the sport to a specific tournament or season series

[List teams](/api-reference/sports/list-teams)[Get valid sports market types](/api-reference/sports/get-valid-sports-market-types)

⌘I

---


## API: Get Sports Market Types

> Source: https://docs.polymarket.com/api-reference/sports/get-valid-sports-market-types

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Sports

Get valid sports market types

GET

/

sports

/

market-types

Try it

Get valid sports market types

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/sports/market-types
```

200

Copy

```shiki
{
  "marketTypes": [
    "<string>"
  ]
}
```

#### Response

200 - application/json

List of valid sports market types

[​](#response-market-types)

marketTypes

string[]

List of all valid sports market types

[Get sports metadata information](/api-reference/sports/get-sports-metadata-information)[List tags](/api-reference/tags/list-tags)

⌘I

---


## API: List Teams

> Source: https://docs.polymarket.com/api-reference/sports/list-teams

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Sports

List teams

GET

/

teams

Try it

List teams

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/teams
```

200

Copy

```shiki
[
  {
    "id": 123,
    "name": "<string>",
    "league": "<string>",
    "record": "<string>",
    "logo": "<string>",
    "abbreviation": "<string>",
    "alias": "<string>",
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z"
  }
]
```

#### Query Parameters

[​](#parameter-limit)

limit

integer

Required range: `x >= 0`

[​](#parameter-offset)

offset

integer

Required range: `x >= 0`

[​](#parameter-order)

order

string

Comma-separated list of fields to order by

[​](#parameter-ascending)

ascending

boolean

[​](#parameter-league)

league

string[]

[​](#parameter-name)

name

string[]

[​](#parameter-abbreviation)

abbreviation

string[]

#### Response

200 - application/json

List of teams

[​](#response-items-id)

id

integer

[​](#response-items-name-one-of-0)

name

string | null

[​](#response-items-league-one-of-0)

league

string | null

[​](#response-items-record-one-of-0)

record

string | null

[​](#response-items-logo-one-of-0)

logo

string | null

[​](#response-items-abbreviation-one-of-0)

abbreviation

string | null

[​](#response-items-alias-one-of-0)

alias

string | null

[​](#response-items-created-at-one-of-0)

createdAt

string<date-time> | null

[​](#response-items-updated-at-one-of-0)

updatedAt

string<date-time> | null

[Gamma API Health check](/api-reference/gamma-status/gamma-api-health-check)[Get sports metadata information](/api-reference/sports/get-sports-metadata-information)

⌘I

---


## API: Get Bid-Ask Spreads

> Source: https://docs.polymarket.com/api-reference/spreads/get-bid-ask-spreads

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Spreads

Get bid-ask spreads

POST

/

spreads

Try it

Get bid-ask spreads

cURL

Copy

```shiki
curl --request POST \
  --url https://clob.polymarket.com/spreads \
  --header 'Content-Type: application/json' \
  --data '
[
  {
    "token_id": "1234567890"
  },
  {
    "token_id": "0987654321"
  }
]
'
```

200

Example

Copy

```shiki
{  
  "1234567890": "0.50",  
  "0987654321": "0.05"  
}
```

#### Body

application/json

Maximum array length: `500`

[​](#body-items-token-id)

token\_id

string

required

The unique identifier for the token

Example:

`"1234567890"`

[​](#body-items-side)

side

enum<string>

Optional side parameter for certain operations

Available options:

`BUY`,

`SELL`

Example:

`"BUY"`

#### Response

200

application/json

Successful response

Map of token\_id to spread value

[​](#response-additional-properties)

{key}

string

[Get price history for a traded token](/api-reference/pricing/get-price-history-for-a-traded-token)[Historical Timeseries Data](/developers/CLOB/timeseries)

⌘I

---


## API: Get Related Tags by ID

> Source: https://docs.polymarket.com/api-reference/tags/get-related-tags-relationships-by-tag-id

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Tags

Get related tags (relationships) by tag id

GET

/

tags

/

{id}

/

related-tags

Try it

Get related tags (relationships) by tag id

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/tags/{id}/related-tags
```

200

Copy

```shiki
[
  {
    "id": "<string>",
    "tagID": 123,
    "relatedTagID": 123,
    "rank": 123
  }
]
```

#### Path Parameters

[​](#parameter-id)

id

integer

required

#### Query Parameters

[​](#parameter-omit-empty)

omit\_empty

boolean

[​](#parameter-status)

status

enum<string>

Available options:

`active`,

`closed`,

`all`

#### Response

200 - application/json

Related tag relationships

[​](#response-items-id)

id

string

[​](#response-items-tag-id-one-of-0)

tagID

integer | null

[​](#response-items-related-tag-id-one-of-0)

relatedTagID

integer | null

[​](#response-items-rank-one-of-0)

rank

integer | null

[Get tag by slug](/api-reference/tags/get-tag-by-slug)[Get related tags (relationships) by tag slug](/api-reference/tags/get-related-tags-relationships-by-tag-slug)

⌘I

---


## API: Get Related Tags by Slug

> Source: https://docs.polymarket.com/api-reference/tags/get-related-tags-relationships-by-tag-slug

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Tags

Get related tags (relationships) by tag slug

GET

/

tags

/

slug

/

{slug}

/

related-tags

Try it

Get related tags (relationships) by tag slug

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/tags/slug/{slug}/related-tags
```

200

Copy

```shiki
[
  {
    "id": "<string>",
    "tagID": 123,
    "relatedTagID": 123,
    "rank": 123
  }
]
```

#### Path Parameters

[​](#parameter-slug)

slug

string

required

#### Query Parameters

[​](#parameter-omit-empty)

omit\_empty

boolean

[​](#parameter-status)

status

enum<string>

Available options:

`active`,

`closed`,

`all`

#### Response

200 - application/json

Related tag relationships

[​](#response-items-id)

id

string

[​](#response-items-tag-id-one-of-0)

tagID

integer | null

[​](#response-items-related-tag-id-one-of-0)

relatedTagID

integer | null

[​](#response-items-rank-one-of-0)

rank

integer | null

[Get related tags (relationships) by tag id](/api-reference/tags/get-related-tags-relationships-by-tag-id)[Get tags related to a tag id](/api-reference/tags/get-tags-related-to-a-tag-id)

⌘I

---


## API: Get Tag by ID

> Source: https://docs.polymarket.com/api-reference/tags/get-tag-by-id

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Tags

Get tag by id

GET

/

tags

/

{id}

Try it

Get tag by id

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/tags/{id}
```

200

Copy

```shiki
{
  "id": "<string>",
  "label": "<string>",
  "slug": "<string>",
  "forceShow": true,
  "publishedAt": "<string>",
  "createdBy": 123,
  "updatedBy": 123,
  "createdAt": "2023-11-07T05:31:56Z",
  "updatedAt": "2023-11-07T05:31:56Z",
  "forceHide": true,
  "isCarousel": true
}
```

#### Path Parameters

[​](#parameter-id)

id

integer

required

#### Query Parameters

[​](#parameter-include-template)

include\_template

boolean

#### Response

200

application/json

Tag

[​](#response-id)

id

string

[​](#response-label-one-of-0)

label

string | null

[​](#response-slug-one-of-0)

slug

string | null

[​](#response-force-show-one-of-0)

forceShow

boolean | null

[​](#response-published-at-one-of-0)

publishedAt

string | null

[​](#response-created-by-one-of-0)

createdBy

integer | null

[​](#response-updated-by-one-of-0)

updatedBy

integer | null

[​](#response-created-at-one-of-0)

createdAt

string<date-time> | null

[​](#response-updated-at-one-of-0)

updatedAt

string<date-time> | null

[​](#response-force-hide-one-of-0)

forceHide

boolean | null

[​](#response-is-carousel-one-of-0)

isCarousel

boolean | null

[List tags](/api-reference/tags/list-tags)[Get tag by slug](/api-reference/tags/get-tag-by-slug)

⌘I

---


## API: Get Tag by Slug

> Source: https://docs.polymarket.com/api-reference/tags/get-tag-by-slug

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Tags

Get tag by slug

GET

/

tags

/

slug

/

{slug}

Try it

Get tag by slug

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/tags/slug/{slug}
```

200

Copy

```shiki
{
  "id": "<string>",
  "label": "<string>",
  "slug": "<string>",
  "forceShow": true,
  "publishedAt": "<string>",
  "createdBy": 123,
  "updatedBy": 123,
  "createdAt": "2023-11-07T05:31:56Z",
  "updatedAt": "2023-11-07T05:31:56Z",
  "forceHide": true,
  "isCarousel": true
}
```

#### Path Parameters

[​](#parameter-slug)

slug

string

required

#### Query Parameters

[​](#parameter-include-template)

include\_template

boolean

#### Response

200

application/json

Tag

[​](#response-id)

id

string

[​](#response-label-one-of-0)

label

string | null

[​](#response-slug-one-of-0)

slug

string | null

[​](#response-force-show-one-of-0)

forceShow

boolean | null

[​](#response-published-at-one-of-0)

publishedAt

string | null

[​](#response-created-by-one-of-0)

createdBy

integer | null

[​](#response-updated-by-one-of-0)

updatedBy

integer | null

[​](#response-created-at-one-of-0)

createdAt

string<date-time> | null

[​](#response-updated-at-one-of-0)

updatedAt

string<date-time> | null

[​](#response-force-hide-one-of-0)

forceHide

boolean | null

[​](#response-is-carousel-one-of-0)

isCarousel

boolean | null

[Get tag by id](/api-reference/tags/get-tag-by-id)[Get related tags (relationships) by tag id](/api-reference/tags/get-related-tags-relationships-by-tag-id)

⌘I

---


## API: Get Tags Related to Tag ID

> Source: https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-id

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Tags

Get tags related to a tag id

GET

/

tags

/

{id}

/

related-tags

/

tags

Try it

Get tags related to a tag id

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/tags/{id}/related-tags/tags
```

200

Copy

```shiki
[
  {
    "id": "<string>",
    "label": "<string>",
    "slug": "<string>",
    "forceShow": true,
    "publishedAt": "<string>",
    "createdBy": 123,
    "updatedBy": 123,
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "forceHide": true,
    "isCarousel": true
  }
]
```

#### Path Parameters

[​](#parameter-id)

id

integer

required

#### Query Parameters

[​](#parameter-omit-empty)

omit\_empty

boolean

[​](#parameter-status)

status

enum<string>

Available options:

`active`,

`closed`,

`all`

#### Response

200 - application/json

Related tags

[​](#response-items-id)

id

string

[​](#response-items-label-one-of-0)

label

string | null

[​](#response-items-slug-one-of-0)

slug

string | null

[​](#response-items-force-show-one-of-0)

forceShow

boolean | null

[​](#response-items-published-at-one-of-0)

publishedAt

string | null

[​](#response-items-created-by-one-of-0)

createdBy

integer | null

[​](#response-items-updated-by-one-of-0)

updatedBy

integer | null

[​](#response-items-created-at-one-of-0)

createdAt

string<date-time> | null

[​](#response-items-updated-at-one-of-0)

updatedAt

string<date-time> | null

[​](#response-items-force-hide-one-of-0)

forceHide

boolean | null

[​](#response-items-is-carousel-one-of-0)

isCarousel

boolean | null

[Get related tags (relationships) by tag slug](/api-reference/tags/get-related-tags-relationships-by-tag-slug)[Get tags related to a tag slug](/api-reference/tags/get-tags-related-to-a-tag-slug)

⌘I

---


## API: Get Tags Related to Tag Slug

> Source: https://docs.polymarket.com/api-reference/tags/get-tags-related-to-a-tag-slug

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Tags

Get tags related to a tag slug

GET

/

tags

/

slug

/

{slug}

/

related-tags

/

tags

Try it

Get tags related to a tag slug

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/tags/slug/{slug}/related-tags/tags
```

200

Copy

```shiki
[
  {
    "id": "<string>",
    "label": "<string>",
    "slug": "<string>",
    "forceShow": true,
    "publishedAt": "<string>",
    "createdBy": 123,
    "updatedBy": 123,
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "forceHide": true,
    "isCarousel": true
  }
]
```

#### Path Parameters

[​](#parameter-slug)

slug

string

required

#### Query Parameters

[​](#parameter-omit-empty)

omit\_empty

boolean

[​](#parameter-status)

status

enum<string>

Available options:

`active`,

`closed`,

`all`

#### Response

200 - application/json

Related tags

[​](#response-items-id)

id

string

[​](#response-items-label-one-of-0)

label

string | null

[​](#response-items-slug-one-of-0)

slug

string | null

[​](#response-items-force-show-one-of-0)

forceShow

boolean | null

[​](#response-items-published-at-one-of-0)

publishedAt

string | null

[​](#response-items-created-by-one-of-0)

createdBy

integer | null

[​](#response-items-updated-by-one-of-0)

updatedBy

integer | null

[​](#response-items-created-at-one-of-0)

createdAt

string<date-time> | null

[​](#response-items-updated-at-one-of-0)

updatedAt

string<date-time> | null

[​](#response-items-force-hide-one-of-0)

forceHide

boolean | null

[​](#response-items-is-carousel-one-of-0)

isCarousel

boolean | null

[Get tags related to a tag id](/api-reference/tags/get-tags-related-to-a-tag-id)[List events](/api-reference/events/list-events)

⌘I

---


## API: List Tags

> Source: https://docs.polymarket.com/api-reference/tags/list-tags

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Tags

List tags

GET

/

tags

Try it

List tags

cURL

Copy

```shiki
curl --request GET \
  --url https://gamma-api.polymarket.com/tags
```

200

Copy

```shiki
[
  {
    "id": "<string>",
    "label": "<string>",
    "slug": "<string>",
    "forceShow": true,
    "publishedAt": "<string>",
    "createdBy": 123,
    "updatedBy": 123,
    "createdAt": "2023-11-07T05:31:56Z",
    "updatedAt": "2023-11-07T05:31:56Z",
    "forceHide": true,
    "isCarousel": true
  }
]
```

#### Query Parameters

[​](#parameter-limit)

limit

integer

Required range: `x >= 0`

[​](#parameter-offset)

offset

integer

Required range: `x >= 0`

[​](#parameter-order)

order

string

Comma-separated list of fields to order by

[​](#parameter-ascending)

ascending

boolean

[​](#parameter-include-template)

include\_template

boolean

[​](#parameter-is-carousel)

is\_carousel

boolean

#### Response

200 - application/json

List of tags

[​](#response-items-id)

id

string

[​](#response-items-label-one-of-0)

label

string | null

[​](#response-items-slug-one-of-0)

slug

string | null

[​](#response-items-force-show-one-of-0)

forceShow

boolean | null

[​](#response-items-published-at-one-of-0)

publishedAt

string | null

[​](#response-items-created-by-one-of-0)

createdBy

integer | null

[​](#response-items-updated-by-one-of-0)

updatedBy

integer | null

[​](#response-items-created-at-one-of-0)

createdAt

string<date-time> | null

[​](#response-items-updated-at-one-of-0)

updatedAt

string<date-time> | null

[​](#response-items-force-hide-one-of-0)

forceHide

boolean | null

[​](#response-items-is-carousel-one-of-0)

isCarousel

boolean | null

[Get valid sports market types](/api-reference/sports/get-valid-sports-market-types)[Get tag by id](/api-reference/tags/get-tag-by-id)

⌘I

---


## Changelog

> Source: https://docs.polymarket.com/changelog/changelog

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Main Changes

Polymarket Changelog

[​](#jan-28%2C-2026)

Jan 28, 2026

Bridge API: Withdrawal Endpoint

* **Withdrawal Endpoint**: New `/withdraw` endpoint to bridge USDC.e from Polymarket to any supported chain and token.
* **Multi-chain withdrawals**: Withdraw to EVM chains (Ethereum, Arbitrum, Base, etc.), Solana, and Bitcoin.
* **Updated documentation**: Bridge API docs updated to reflect deposit and withdrawal functionality.

[​](#jan-16%2C-2026)

Jan 16, 2026

Docs Update: RTDS documentation

* RTDS docs updated to reflect RTDS supports **comments** and **crypto prices** only.
* Removed legacy CLOB references and `clob_auth` from RTDS docs.

[​](#jan-16%2C-2026-2)

Jan 16, 2026

Docs Update: Maker Rebates Program

* **Maker Rebates Program**: Updated funding schedule with distribution method (volume-weighted vs fee-curve weighted).
* **Fee-curve weighted rebates**: Documented fee-equivalent formula and rebate calculation.
* **FAQ**: Clarified how rebates are calculated during fee-curve weighted periods.

[​](#jan-6%2C-2026)

Jan 6, 2026

New API Features

* **Releases**: Daily Releases timing
* **HeartBeats API**: HeartBeats endpoint for monitoring connection status and canceling orders
* **Post Only Orders**: Orders that are rejected if they would immediately match against an existing order

[​](#jan-5%2C-2026)

Jan 5, 2026

Taker Fees & Maker Rebates

* **Taker Fees**: Enabled on 15-minute crypto markets. Fees vary by price and peak at 1.56% at 50% probability.
* **Maker Rebates**: Daily USDC rebates paid to liquidity providers, funded by taker fees.

[​](#sept-24%2C-2025)

Sept 24, 2025

Polymarket Real-Time Data Socket (RTDS) official release

* **Crypto Price Feeds**: Access real-time cryptocurrency prices from two sources (Binance & Chainlink)
* **Comment Streaming**: Real-time updates for comment events including new comments, replies, and reactions
* **Dynamic Subscriptions**: Add, remove, and modify subscriptions without reconnecting
* **TypeScript Client**: Official TypeScript client available at [real-time-data-client](https://github.com/Polymarket/real-time-data-client)
  For complete documentation, see [RTDS Overview](/developers/RTDS/RTDS-overview).

[​](#september-15%2C-2025)

September 15, 2025

WSS price\_change event update

* There has been a significant change to the structure of the price change message. This update will be applied at 11PM UTC September 15, 2025. We apologize for the short notice
  + Please see the [migration guide](/developers/CLOB/websocket/market-channel-migration-guide) for details.

[​](#august-26%2C-2025)

August 26, 2025

Updated /trades and /activity endpoints

* Reduced maximum values for query parameters on Data-API /trades and /activity:
  + `limit`: 500
  + `offset`: 1,000

[​](#august-21%2C-2025)

August 21, 2025

Batch Orders Increase

* The batch orders limit has been increased from from 5 -> 15. Read more about the batch orders functionality [here](/developers/CLOB/orders/create-order-batch).

[​](#july-23%2C-2025)

July 23, 2025

Get Book(s) update

* We’re adding new fields to the `get-book` and `get-books` CLOB endpoints to include key market metadata that previously required separate queries.
  + `min_order_size`
    - type: string
    - description: Minimum allowed order size.
  + `neg_risk`
    - type: boolean
    - description: Boolean indicating whether the market is neg\_risk.
  + `tick_size`
    - type: string
    - description: Minimum allowed order size.

[​](#june-3%2C-2025)

June 3, 2025

New Batch Orders Endpoint

* We’re excited to roll out a highly requested feature: **order batching**. With this new endpoint, users can now submit up to five trades in a single request. To help you get started, we’ve included sample code demonstrating how to use it. Please see [Place Multiple Orders (Batching)](/developers/CLOB/orders/create-order-batch) for more details.

[​](#june-3%2C-2025-2)

June 3, 2025

Change to /data/trades

* We’re adding a new `side` field to the `MakerOrder` portion of the trade object. This field will indicate whether the maker order is a `buy` or `sell`, helping to clarify trade events where the maker side was previously ambiguous. For more details, refer to the MakerOrder object on the [Get Trades](/developers/CLOB/trades/trades) page.

[​](#may-28%2C-2025)

May 28, 2025

Websocket Changes

* The 100 token subscription limit has been removed for the Markets channel. You can now subscribe to as many token IDs as needed for your use case.
* New Subscribe Field `initial_dump`
  + Optional field to indicate whether you want to receive the initial order book state when subscribing to a token or list of tokens.
  + `default: true`

[​](#may-28%2C-2025-2)

May 28, 2025

New FAK Order Type

We’re excited to introduce a new order type soon to be available to all users: Fill and Kill (FAK). FAK orders behave similarly to the well-known Fill or Kil(FOK) orders, but with a key difference:

* FAK will fill as many shares as possible immediately at your specified price, and any remaining unfilled portion will be canceled.
* Unlike FOK, which requires the entire order to fill instantly or be canceled, FAK is more flexible and aims to capture partial fills if possible.

[​](#may-15%2C-2025)

May 15, 2025

Increased API Rate Limits

All API users will enjoy increased rate limits for the CLOB endpoints.

* CLOB - /books (website) (300req - 10s / Throttle requests over the maximum configured rate)
* CLOB - /books (50 req - 10s / Throttle requests over the maximum configured rate)
* CLOB - /price (100req - 10s / Throttle requests over the maximum configured rate)
* CLOB markets/0x (50req / 10s - Throttle requests over the maximum configured rate)
* CLOB POST /order - 500 every 10s (50/s) - (BURST) - Throttle requests over the maximum configured rateed
* CLOB POST /order - 3000 every 10 minutes (5/s) - Throttle requests over the maximum configured rate
* CLOB DELETE /order - 500 every 10s (50/s) - (BURST) - Throttle requests over the maximum configured rate
* DELETE /order - 3000 every 10 minutes (5/s) - Throttle requests over the maximum configured rate

⌘I

---


## FAQ: Does Polymarket have an API?

> Source: https://docs.polymarket.com/polymarket-learn/FAQ/does-polymarket-have-an-api

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

FAQs

Does Polymarket have an API?

Yes! Developers can find all the information they need for interacting with Polymarket. This includes [documentation on market discovery, resolution, trading etc.](/quickstart/overview)
Whether you are an academic researcher a market maker or an indepedent developer, this documentation should provide you what you need to get started. All the code you find linked here and on our [GitHub](https://github.com/polymarket) is open source and free to use.

If you have any questions please join our [Discord](https://discord.com/invite/polymarket) and direct your questions to the #devs channel.

[Does Polymarket Have a Token?](/polymarket-learn/FAQ/wen-token)[How Do I Contact Support?](/polymarket-learn/FAQ/support)

⌘I

---


## FAQ: How To Use Embeds

> Source: https://docs.polymarket.com/polymarket-learn/FAQ/embeds

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

FAQs

How To Use Embeds

Polymarket allows you to embed a live-updating widget displaying the latest odds for markets in many places around the web.

### [​](#web) Web

Navigate to the individual market you want to embed and click the embed (< >) link.
Select light or dark mode, and copy the auto-generated code
Paste the code into your code editor or CMS and publish as normal

### [​](#twitter-/-x) Twitter / X

Navigate to any Polymarket market
Copy the URL from your browser
Paste the URL into the compose window

### [​](#substack) Substack

The embeds feature currently supports single markets only (eg “USA to Win Most Gold Medals”, not “Most Gold Medals at Paris Olympics’)

To embed a market, navigate on Polymarket.com to the single market you want to embed and click “copy link.”
Navigate to your Substack editor and paste the link directly into the body of your newsletter. The editor will recognize the market and convert it to a widget that automatically refreshes with the latest odds.

### [​](#ticker) Ticker

The Polymarket Live Ticker displays real-time prediction market data for your livestream or website. Navigate to <https://ticker.polymarket.com/> to create a custom ticker by category (Breaking News, Politics, etc.) and copy the embed code to add it to your site.

[Geographic Restrictions](/polymarket-learn/FAQ/geoblocking)[Polymarket vs. Polling](/polymarket-learn/FAQ/polling)

⌘I

---


## FAQ: Geographic Restrictions

> Source: https://docs.polymarket.com/polymarket-learn/FAQ/geoblocking

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

FAQs

Geographic Restrictions

## [​](#overview) Overview

Polymarket is not available in certain countries and regions due to regulatory requirements and compliance with international sanctions. This page provides a comprehensive list of all geographically restricted locations.

## [​](#server-infrastructure) Server Infrastructure

* **Primary Servers**: eu-west-2
* **Closest Non-Georestricted Region**: eu-west-1

## [​](#blocked-countries) Blocked Countries

The following **33 countries** are completely restricted from accessing Polymarket:

| Country Code | Country Name |
| --- | --- |
| AU | Australia |
| BE | Belgium |
| BY | Belarus |
| BI | Burundi |
| CF | Central African Republic |
| CD | Congo (Kinshasa) |
| CU | Cuba |
| DE | Germany |
| ET | Ethiopia |
| FR | France |
| GB | United Kingdom |
| IR | Iran |
| IQ | Iraq |
| IT | Italy |
| KP | North Korea |
| LB | Lebanon |
| LY | Libya |
| MM | Myanmar |
| NI | Nicaragua |
| PL | Poland |
| RU | Russia |
| SG | Singapore |
| SO | Somalia |
| SS | South Sudan |
| SD | Sudan |
| SY | Syria |
| TH | Thailand |
| TW | Taiwan |
| UM | United States Minor Outlying Islands |
| US | United States |
| VE | Venezuela |
| YE | Yemen |
| ZW | Zimbabwe |

## [​](#blocked-regions) Blocked Regions

In addition to fully blocked countries, the following specific regions within otherwise accessible countries are also restricted:

| Country | Region | Region Code |
| --- | --- | --- |
| Canada (CA) | Ontario | ON |
| Ukraine (UA) | Crimea | 43 |
| Ukraine (UA) | Donetsk | 14 |
| Ukraine (UA) | Luhansk | 09 |

## [​](#blocking-logic) Blocking Logic

The geoblocking system includes:

1. **OFAC-Sanctioned Countries**: Countries sanctioned by the U.S. Office of Foreign Assets Control (OFAC)
2. **Additional Regulatory Restrictions**: Countries added for specific regulatory compliance reasons

### [​](#close-only-countries) Close-Only Countries

Some countries have a **“close-only”** restriction status. Users in these countries can:

* ✅ Close existing positions
* ❌ Open new positions

Countries with close-only status include:

* Singapore (SG)
* Poland (PL)
* Thailand (TH)
* Taiwan (TW)

## [​](#why-these-restrictions) Why These Restrictions?

Geographic restrictions are implemented to ensure compliance with:

* International sanctions and embargoes
* Local financial regulations
* Gambling and prediction market laws
* Anti-money laundering (AML) requirements
* Know Your Customer (KYC) regulations

## [​](#need-help) Need Help?

If you believe you are incorrectly restricted or have questions about geographic availability, please contact [Polymarket Support](https://polymarket.com/support).

[Using the Order Book](/polymarket-learn/trading/using-the-orderbook)[How To Use Embeds](/polymarket-learn/FAQ/embeds)

⌘I

---


## FAQ: How Do I Export My Key?

> Source: https://docs.polymarket.com/polymarket-learn/FAQ/how-to-export-private-key

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

FAQs

How Do I Export My Key?

Exporting your private key gives you direct control and security over your funds. This process is applicable if you’ve signed up via email.

**DO NOT** share your private key with other parties, platforms, or people. We will never ask for your private key.

1. Access the Export Link while signed into Polymarket: <https://reveal.magic.link/polymarket>
2. Sign-in on Magic.Link
3. Export Private Key. Once revealed, you should securely store the private key displayed, where others can’t access it.
4. Log out of Magic.Link

[How Do I Contact Support?](/polymarket-learn/FAQ/support)[Is My Money Safe?](/polymarket-learn/FAQ/is-my-money-safe)

⌘I

---


## FAQ: Is My Money Safe?

> Source: https://docs.polymarket.com/polymarket-learn/FAQ/is-my-money-safe

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

FAQs

Is My Money Safe?

#### [​](#non-custodial-you’re-in-control) Non-custodial, you’re in control

Polymarket recognizes the importance of a trustworthy environment for managing your funds. To ensure this, Polymarket uses non-custodial wallets, meaning we never take possession of your USDC. This approach gives you full control over your assets, providing protection against potential security threats like hacks, misuse, and unauthorized transactions.

### [​](#your-keys-=-your-funds) Your keys = your funds

A private key acts like a highly secure password, essential for managing and moving your assets without restrictions. You can export your private key at any time, ensuring sole access to your funds. Learn how to export your private key [here](../FAQ/how-to-export-private-key/).

### [​](#keep-your-private-keys-private) Keep your private keys private.

**Do not share your private key with others**. While Polymarket provides the infrastructure, the security of your assets depends on how securely you handle your private key and passwords. Losing your private key or passwords can result in losing access to your funds. It’s crucial to store this information in a safe and secure environment.

### [​](#our-commitment) Our Commitment

Polymarket aims to give you peace of mind, knowing that your assets are safe and fully under your control at all times. We encourage you to take necessary precautions to secure your digital assets effectively. The ability to manage your private key means you are not reliant on Polymarket to secure your assets; you have the control to ensure your financial security.

[How Do I Export My Key?](/polymarket-learn/FAQ/how-to-export-private-key)[Is Polymarket The House?](/polymarket-learn/FAQ/is-polymarket-the-house)

⌘I

---


## FAQ: Is Polymarket The House?

> Source: https://docs.polymarket.com/polymarket-learn/FAQ/is-polymarket-the-house

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

FAQs

Is Polymarket The House?

## [​](#polymarket-is-different-in-three-ways) Polymarket is different in three ways:

### [​](#1-traders-interact-directly-with-each-other-not-with-polymarket) 1. Traders interact directly with each other, not with Polymarket.

Polymarket is a marketplace comprised of traders on both sides of any given market. This means you’re always trading with other users, not against a centralized entity or “house.” Prices on Polymarket are determined by supply and demand. As traders buy and sell shares in outcomes, prices fluctuate to reflect the collective sentiment and knowledge of market participants.

### [​](#2-polymarket-does-not-charge-trading-fees) 2. Polymarket does not charge trading fees.

Unlike bookmakers or wagering operations, Polymarket does not charge deposit/withdrawal fees, or any type of trading fees. This means that Polymarket does not stand to benefit from the outcome of any market or usage of any trader.

### [​](#3-transact-at-any-time) 3. Transact at any time.

Polymarket enables you to sell your position at any time before the market resolves, provided there is a willing buyer of your shares. This offers flexibility and allows you to manage your risk and lock in profits or cut losses as you see fit.
In essence, Polymarket empowers you to trade based on your own knowledge and research, without going up against a “house” with potentially unfair advantages.

[Is My Money Safe?](/polymarket-learn/FAQ/is-my-money-safe)[Why Crypto?](/polymarket-learn/FAQ/why-do-i-need-crypto)

⌘I

---


## FAQ: Polymarket vs. Polling

> Source: https://docs.polymarket.com/polymarket-learn/FAQ/polling

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

FAQs

Polymarket vs. Polling

While legacy polls capture a snapshot of opinion at a specific moment, they are often outdated by the time they’re published—sometimes lagging by several days. In contrast, Polymarket reflects real-time sentiment as events unfold, offering continuous updates and a more dynamic understanding of public opinion.
Studies show that prediction markets like Polymarket tend to outperform traditional pollsters because participants are financially incentivized to be correct. This creates more thoughtful, data-driven predictions. Research by James Surowiecki, author of The Wisdom of Crowds, has highlighted how markets like these can be more accurate than polls due to the “collective intelligence” of diverse participants. Additionally, the Iowa Electronic Markets, an academic research project at the University of Iowa, has consistently demonstrated the superior accuracy of prediction markets like Polymarket over traditional polling in predicting political outcomes.
Polymarket provides a constantly updating picture of public sentiment, offering a degree of accuracy and timeliness that traditional pollsters, who typically report data that is days old, simply cannot match.

[How To Use Embeds](/polymarket-learn/FAQ/embeds)[Recover Missing Deposit](/polymarket-learn/FAQ/recover-missing-deposit)

⌘I

---


## FAQ: Recover Missing Deposit

> Source: https://docs.polymarket.com/polymarket-learn/FAQ/recover-missing-deposit

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

FAQs

Recover Missing Deposit

### [​](#recover-on-ethereum) Recover on Ethereum

Use this tool if you deposited the wrong token on Ethereum.

1. Go to <https://recovery.polymarket.com/> and sign in with your Polymarket account or connect the wallet you use on Polymarket.
2. Select the asset you incorrectly deposited.
3. You’ll then see the asset balance displayed, and will have the ability to recover those funds to your specified wallet.

### [​](#recover-on-polygon) Recover on Polygon

Use this tool if you deposited the wrong token on Polygon.

1. Go to <https://matic-recovery.polymarket.com/> and sign in with your Polymarket account or connect the wallet you use on Polymarket.
2. Select the asset you incorrectly deposited.
3. You’ll then see the asset balance displayed, and will have the ability to recover those funds to your specified wallet.

[Polymarket vs. Polling](/polymarket-learn/FAQ/polling)[Can I Sell Early?](/polymarket-learn/FAQ/sell-early)

⌘I

---


## FAQ: Can I Sell Early?

> Source: https://docs.polymarket.com/polymarket-learn/FAQ/sell-early

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

FAQs

Can I Sell Early?

**Yes, you can sell or close your position early.**
You may sell shares at any point before the market is resolved by either placing a market order to sell shares at the prevailing bid price in the orderbook, or by placing a limit order for how many shares you wish to sell and at what price.
The limit order will only be executed if/when there is a willing buyer for your shares at the price you set.

[Recover Missing Deposit](/polymarket-learn/FAQ/recover-missing-deposit)[Does Polymarket Have a Token?](/polymarket-learn/FAQ/wen-token)

⌘I

---


## FAQ: How Do I Contact Support?

> Source: https://docs.polymarket.com/polymarket-learn/FAQ/support

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

FAQs

How Do I Contact Support?

To contact support through our website:

* Navigate to [Polymarket](https://polymarket.com).
* Click the blue chat icon in the bottom right and start your chat session.

For technical support on Discord:

* Join the [Polymarket Discord server](https://discord.gg/polymarket)
* Navigate to the Support sidebar and click #open-a-ticket. This will open a private conversation with a Polymarket team member.

Be aware of numerous scams and malicious links. Polymarket team members will never DM you first or ask for private keys or personal information. Polymarket team members are identified in blue font on Discord.

[Does Polymarket have an API?](/polymarket-learn/FAQ/does-polymarket-have-an-api)[How Do I Export My Key?](/polymarket-learn/FAQ/how-to-export-private-key)

⌘I

---


## FAQ: Does Polymarket Have a Token?

> Source: https://docs.polymarket.com/polymarket-learn/FAQ/wen-token

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

FAQs

Does Polymarket Have a Token?

**Polymarket does not have a token.**
All trading and liquidity rewards are in USDC, a USD-pegged stablecoin.
Polymarket has not announced plans for any airdrop or token generation event. Be wary of scams claiming airdrops, giveaways, etc.
If in doubt, refer to official Polymarket communication channels:

* Web: <https://polymarket.com>
* Twitter / X: <https://x.com/polymarket>
* Discord: <https://discord.gg/polymarket>

[Can I Sell Early?](/polymarket-learn/FAQ/sell-early)[Does Polymarket have an API?](/polymarket-learn/FAQ/does-polymarket-have-an-api)

⌘I

---


## FAQ: What is a Prediction Market?

> Source: https://docs.polymarket.com/polymarket-learn/FAQ/what-are-prediction-markets

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

FAQs

What is a Prediction Market?

A prediction market is a platform where people can bet on the outcome of future events. By buying and selling shares in the outcomes, participants collectively forecast the likelihood of events such as sports results, political elections, or entertainment awards.

### [​](#how-it-works) How it works

Market Prices = Probabilities: The price of shares in a prediction market represents the current probability of an event happening. For example, if shares of an event are trading at 20 cents, it indicates a 20% chance of that event occurring.

### [​](#making-predictions) Making predictions

If you believe the actual probability of an event is higher than the market price suggests, you can buy shares. For instance, if you think a team has a better than 20% chance of winning, you would buy shares at 20 cents. If the event occurs, each share becomes worth $1, yielding a profit.

### [​](#free-market-trading) Free-market trading

You can buy or sell shares at any time before the event concludes, based on new information or changing circumstances. This flexibility allows the market prices to continuously reflect the most current and accurate probabilities.

### [​](#trust-the-markets) Trust the markets

Prediction markets provide unbiased and accurate probabilities in real time, cutting through the noise of human and media biases. Traditional sources often have their own incentives and slants, but prediction markets operate on the principle of “put your money where your mouth is.” Here, participants are financially motivated to provide truthful insights, as their profits depend on the accuracy of their predictions.
In a prediction market, prices reflect the aggregated sentiment of all participants, weighing news, data, expert opinions, and culture to determine the true odds. Unlike media narratives, which can be swayed by various biases, prediction markets offer a transparent view of where people genuinely believe we’re heading.

#### [​](#why-use-prediction-markets) Why use prediction markets?

Prediction markets are often more accurate than traditional polls and expert predictions. The collective wisdom of diverse participants, each motivated by the potential for profit, leads to highly reliable forecasts. This makes prediction markets an excellent tool for gauging real-time probabilities of future events.
Polymarket, the world’s largest prediction market, offers a user-friendly platform to bet on a wide range of topics, from sports to politics. By participating, you can profit from your knowledge while contributing to the accuracy of market predictions.

[Why Crypto?](/polymarket-learn/FAQ/why-do-i-need-crypto)

⌘I

---


## FAQ: Why Crypto?

> Source: https://docs.polymarket.com/polymarket-learn/FAQ/why-do-i-need-crypto

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

FAQs

Why Crypto?

Polymarket operates on Polygon, a proof-of-stake layer two blockchain built on [Ethereum](https://ethereum.org). All transactions are denominated in USDC, a US-dollar pegged stablecoin.
This architecture offers several advantages over traditional prediction markets:

## [​](#why-usdc) Why USDC?

### [​](#stable-value) Stable Value

Polymarket denominates trades in USDC, which is pegged 1:1 to the US Dollar. This shields you from the volatility associated with other cryptocurrencies and offers a stable medium for trading.

### [​](#regulated-reserves) Regulated Reserves

USDC operates in adherence to regulatory standards and is backed by reserved assets.

### [​](#transparency) Transparency

Blockchain technology facilitates transparency, as all transactions are recorded publicly.

### [​](#global-reach) Global Reach

Research has shown that wide availability of prediction markets increases their accuracy. Using decentralized blockchain technology removes the need for a central authority in trading, which fosters fairness and open participation around the globe.

[Is Polymarket The House?](/polymarket-learn/FAQ/is-polymarket-the-house)[What is a Prediction Market?](/polymarket-learn/FAQ/what-are-prediction-markets)

⌘I

---


## Deposit with Coinbase

> Source: https://docs.polymarket.com/polymarket-learn/deposits/coinbase

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Deposits and Withdrawals

Deposit with Coinbase

## [​](#buying-usdc) Buying USDC

**How to buy and deposit USDC to your Polymarket account using Coinbase.**
Depositing directly to Polymarket from Coinbase is simple and easy. If you need help creating a Coinbase account, see their [guide on Coinbase.com](https://help.coinbase.com/en/coinbase/getting-started)
If something went wrong along the way, we recommend reaching to Coinbase support.

## [​](#transfering-to-polymarket) Transfering to Polymarket

[Deposit by Transfering Crypto](/polymarket-learn/deposits/supported-tokens)[Deposit Using Your Card](/polymarket-learn/deposits/moonpay)

⌘I

---


## How to Withdraw

> Source: https://docs.polymarket.com/polymarket-learn/deposits/how-to-withdraw

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Deposits and Withdrawals

How to Withdraw

Withdrawing from Polymarket is simple, instant, and free.

Note: When withdrawing USDC.e (bridged USDC) is swapped through the [Uniswap v3 pool](https://polygonscan.com/address/0xd36ec33c8bed5a9f7b6630855f1533455b98a418)
for USDC (native) (the UI enforces less than 10bp difference in output
amount). At times, this pool may be exhausted and for extremely large deposits
there might not be enough liquidity. If you are having withdraw issues, try
breaking your withdraw into smaller amounts or waiting for the pool to be
rebalanced. Additionally, you can select to withdraw USDC.e directly which
does not require any Uniswap liquidity; just be aware that some exchanges no
longer allow USDC.e to be deposited directly.

[Large Cross Chain Deposits](/polymarket-learn/deposits/large-cross-chain-deposits)[How Are Markets Created?](/polymarket-learn/markets/how-are-markets-created)

⌘I

---


## Large Cross Chain Deposits

> Source: https://docs.polymarket.com/polymarket-learn/deposits/large-cross-chain-deposits

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Deposits and Withdrawals

Large Cross Chain Deposits

**For deposits over $50,000 we recommended to use bridges and ensure minimal fee’s (slippage).**

## [​](#recommended-bridges) Recommended Bridges

* [DeBridge](https://app.debridge.finance/?inputChain=1&outputChain=137&inputCurrency=0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48&outputCurrency=0x3c499c542cef5e3811e1192ce70d8cc03d5c3359&dlnMode=simple)
* [Across](https://app.across.to/bridge?)
* [Portal](https://portalbridge.com/)

For large deposits (>$50,000) originating from a chain other than Polygon, we recommend using one of the aforementioned bridges. Ensure you bridge to your Polymarket USDC (Polygon) [deposit address](https://polymarket.com/wallet) (screenshot below). Please be mindful of potential slippage during the transaction.

Polymarket is not affiliated with, responsible for, or makes any guarantees regarding any third-party bridge. Users are advised to review the Terms of Use or other relevant documentation for third-party bridges.

## [​](#important-notes) Important Notes

You can deposit USDC or USDC.e to your Polymarket Polygon wallet.
If you deposit USDC (native), you will be prompted to “activate funds,” which will swap this to USDC.e via the lowest fee Uniswap pool, ensuring slippage of less than 10 basis points (bps).
If you encounter any issues with the deposit process, please reach out to us on Discord for assistance.

[Deposit USDC on Ethereum](/polymarket-learn/deposits/usdc-on-eth)[How to Withdraw](/polymarket-learn/deposits/how-to-withdraw)

⌘I

---


## Deposit Using Your Card

> Source: https://docs.polymarket.com/polymarket-learn/deposits/moonpay

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Deposits and Withdrawals

Deposit Using Your Card

**Use MoonPay to deposit cash using your Visa, Mastercard, or bank account.**
Access MoonPay by clicking “Buy USDC” on the [Deposit Page](https://polymarket.com/wallet)
Check out [MoonPay’s guide](https://support.moonpay.com/customers/docs/how-to-buy-cryptocurrency-with-moonpay) for further instructions.

[Deposit with Coinbase](/polymarket-learn/deposits/coinbase)[Deposit USDC on Ethereum](/polymarket-learn/deposits/usdc-on-eth)

⌘I

---


## Deposit by Transferring Crypto

> Source: https://docs.polymarket.com/polymarket-learn/deposits/supported-tokens

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Deposits and Withdrawals

Deposit by Transfering Crypto

## [​](#how-do-i-use-transfer-crypto) **How do I use Transfer Crypto?**

The feature was designed to be one of the simplest ways to transfer your tokens into a dApp.
![polymarket.comxd.png](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/images/polymarket.comxd.png?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=b0bfcc917f51f03c422947be7abcc5fc "polymarket.comxd.png")

1. **Click on the Deposit button** and **select Transfer Crypto** as a source option
2. **Select which supported token and chain** your assets are on from the dropdown
   * Depending on your combination, this **may update the deposit address**
   * Only send **supported token-chain combinations**
     + Sending non-supported tokens may cause an irrecoverable loss
3. **Scan the QR code or copy the deposit address** and paste as the recipient in the withdrawal/transfer page of your exchange/wallet
   * This is where you’ll specify how much crypto you’re transferring
   * You **must send more than the minimum deposit** amount or the funds will not process
   * Always ensure to **double check the pasted address** versus that is shown on the widget to protect against clickjacking attempts
   * You can click on the **collapsible section at the bottom of the widget** for estimated price impact, slippage, delivery time, and our help guide
4. **Withdraw/transfer the tokens** from your exchange/wallet and wait until they’re reflected on the dApp
   * You will receive notifications on the Fun widget as your withdraw/transfer processes and completes as shown below

![polymarket.com_portfolio 1.png](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/images/polymarket.com_portfolio1.png?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=43ea11c20e25e45584d3ab0f1c1f0b4c "polymarket.com_portfolio 1.png")
![polymarket.com_portfolio 2.png](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/images/polymarket.com_portfolio2.png?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=91e6dfeb4bb5cdada8d9b62fef23f487 "polymarket.com_portfolio 2.png")

## [​](#what-can-i-transfer) **What can I transfer?**

Transfer Crypto is compatible with a range of supported tokens and chains:

|  | **Ethereum** | **Polygon** | **Base** | **Arbitrum** | **Solana** |
| --- | --- | --- | --- | --- | --- |
| **USDC** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **USDC.e** |  | ✅ |  |  |  |
| **USDT** | ✅ | ✅ | ✅ | ✅ |  |
| **DAI** | ✅ | ✅ | ✅ | ✅ |  |
| **ETH** | ✅ |  | ✅ | ✅ |  |
| **WETH** | ✅ | ✅ | ✅ | ✅ |  |
| **MATIC** | ✅ | ✅ |  |  |  |
| **POL** | ✅ | ✅ |  |  |  |
| **SOL** |  |  |  |  | ✅ |
| **CBBTC** | ✅ |  | ✅ |  |  |
| **ARB** |  |  |  | ✅ |  |

## [​](#need-help-with-your-deposit) Need help with your deposit?

Please contact us using the live chat button on the bottom right on [**Polymarket.com**](http://Polymarket.com)\*\* or email us on [[email protected]](/cdn-cgi/l/email-protection#5c2f292c2c332e281c2c333025313d2e373928723f3331)\*\*
![imagee.png](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/images/imagee.png?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=e862c32062cd7b8a7198714241c162dd)

[Making Your First Trade](/polymarket-learn/get-started/making-your-first-trade)[Deposit with Coinbase](/polymarket-learn/deposits/coinbase)

⌘I

---


## Deposit USDC on Ethereum

> Source: https://docs.polymarket.com/polymarket-learn/deposits/usdc-on-eth

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Deposits and Withdrawals

Deposit USDC on Ethereum

Depositing USDC on the Ethereum network to Polymarket will automatically bridge your funds to the Polygon network.

[Deposit Using Your Card](/polymarket-learn/deposits/moonpay)[Large Cross Chain Deposits](/polymarket-learn/deposits/large-cross-chain-deposits)

⌘I

---


## How to Deposit

> Source: https://docs.polymarket.com/polymarket-learn/get-started/how-to-deposit

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Get Started

How to Deposit

## [​](#depositing-funds-on-polymarket) Depositing funds on Polymarket

This guide will walk you through the deposit process for Polymarket, covering popular methods and step-by-step instructions for buying and depositing USDC.

Need Help? For assistance, reach out to us on [Discord](https://discord.gg/polymarket).

## [​](#about-usdc-and-polygon) About USDC and Polygon

Polymarket uses [USDC (USD Coin)](https://circle.com/en/usdc), a federally regulated “stable coin” backed by the US dollar.
Polymarket utilizes USDC on the Polygon network for transactions. By using USDC on Polygon, Polymarket ensures fast and reliable transactions, enhancing the overall user experience.

### [​](#how-to-purchase-and-deposit-usdc) How to purchase and deposit USDC

USDC is available on most major exchanges, including Coinbase.
If your exchange supports sending or withdrawing to Polygon, we recommend this option for faster and fee-free transactions. Alternatively, you can deposit USDC via the Ethereum network.

### [​](#deposit-with-crypto-exchanges) Deposit with crypto exchanges

For detailed instructions, check out our guides for purchasing and depositing USDC using popular exchanges:

* [Deposit from Coinbase](../deposits/coinbase) (recommended)

If you decide to use an exchange to purchase and send (deposit) USDC to your Polygon deposit address, please ensure you’re sending on Polygon Network. If you’re unsure, please reach out to support on [Discord](https://discord.com/invite/polymarket).

### [​](#deposit-with-visa-or-mastercard) Deposit with Visa or Mastercard

MoonPay enables you to buy USDC (on Polygon) using your Visa, Mastercard, and select bank cards. Please be aware that payment options and transaction limits may vary depending on your region. [How to use MoonPay](../deposits/moonpay/).

### [​](#depositing-on-etheruem-and-polygon) Depositing on Etheruem and Polygon

You can send USDC with your wallet on Ethereum or USDC.e on Polygon to your respective deposit addresses found on the Deposit page. [Learn more](../deposits/usdc-on-eth/).

[How to Sign-Up](/polymarket-learn/get-started/how-to-signup)[Making Your First Trade](/polymarket-learn/get-started/making-your-first-trade)

⌘I

---


## How to Sign-Up

> Source: https://docs.polymarket.com/polymarket-learn/get-started/how-to-signup

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Get Started

How to Sign-Up

Need Help?
We’re available to guide you through the sign-up process on [Discord](https://discord.gg/polymarket)

### [​](#email-or-google-sign-up) Email or Google Sign-Up

Signing up for Polymarket with your email address or Google account is quick, simple, and secure.

### [​](#crypto-wallet-sign-up) Crypto Wallet Sign-Up

Polymarket supports most crypto wallets, including MetaMask, Coinbase Wallet, and others via WalletConnect.

If you have MetaMask or Coinbase Wallet browser extensions installed but wish to connect using their mobile apps, you’ll need to disable the extensions in your browser settings and reload Polymarket.

[What is Polymarket?](/polymarket-learn/get-started/what-is-polymarket)[How to Deposit](/polymarket-learn/get-started/how-to-deposit)

⌘I

---


## Making Your First Trade

> Source: https://docs.polymarket.com/polymarket-learn/get-started/making-your-first-trade

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Get Started

Making Your First Trade

Once you’ve [signed up](../get-started/how-to-signup) and [deposited funds](../get-started/how-to-deposit), you’re ready to start trading on Polymarket. Here’s a step-by-step guide to get you started.

## [​](#video-guide) Video guide

## [​](#walkthrough) Walkthrough

Before trading, you’ll have to visit the [markets page](https://polymarket.com/markets) to see all available markets. Use the search, sort, and filter tools to narrow down your options and find a market that interests you.
screen shot.Simple, right? If you think you’ve got the hang of it, it’s time to learn about more advanced trading and order types. [Limit Orders](../trading/limit-orders/).

[How to Deposit](/polymarket-learn/get-started/how-to-deposit)[Deposit by Transfering Crypto](/polymarket-learn/deposits/supported-tokens)

⌘I

---


## What is Polymarket?

> Source: https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Get Started

What is Polymarket?

Polymarket is the world’s largest prediction market, allowing you to stay informed and profit from your knowledge by betting on future events across various topics.
Studies show prediction markets are often more accurate than pundits because they combine news, polls, and expert opinions into a single value that represents the market’s view of an event’s odds. Our markets reflect *accurate, unbiased, and real-time probabilities* for the events that matter most to you. Markets seek truth.

## [​](#quick-overview) Quick Overview

* On Polymarket, you can [buy and sell shares](making-your-first-trade) representing future event outcomes (i.e. “Will TikTok be banned in the U.S. this year?”)
* Shares in event outcomes are [always priced](what-is-polymarket/#understanding-prices) between 0.00 and 1.00 [USDC](../FAQ/why-do-i-need-crypto/#why-usdc), and every pair of event outcomes (i.e. each pair of “YES” + “NO” shares) is fully collateralized by $1.00 USDC.
* Shares are created when [opposing sides come to an agreement on odds](../trading/limit-orders), such that the sum of what each side is willing to pay is equal to $1.00.
* The shares representing the *correct, final outcome* are paid out $1.00 USDC each upon [market resolution](../markets/how-are-markets-resolved).
* Unlike sportsbooks, you are not betting against “the house” – the counterparty to each trade is another Polymarket user. As such:
  + Shares can be sold before the event outcome is known\_ (i.e. to lock in profits or cut losses)
  + *There is no “house” to ban you for winning too much.*

### [​](#understanding-prices) Understanding Prices

Prices = Probabilities.

*Prices (odds) on Polymarket represent the current probability of an event occurring.* For example, in a market predicting whether the Miami Heat will win the 2025 NBA Finals, if YES shares are trading at 18 cents, it indicates a 18% chance of Miami winning.
These odds are determined by what price other Polymarket users are currently willing to buy & sell those shares at. Just how stock exchanges don’t “set” the prices of stocks, Polymarket does not set prices / odds - they’re a function of supply & demand.
[Learn more](../trading/how-are-prices-calculated)

### [​](#making-money-on-markets) Making money on markets

In the example above, if you believe Miami’s chances of winning are higher than 18%, you would buy “Yes” shares at 18 cents each. If Miami wins, each “Yes” share would be worth $1, resulting in an 82-cent profit per share. Conversely, any trader who owned “No” shares would see their investment become worthless once the game is over.
Since it’s a market, you’re not locked into your trade. You can sell your shares at any time at the current market price. As the news changes, the supply and demand for shares fluctuates, causing the share price to reflect the new odds for the event.

### [​](#how-accurate-are-polymarket-odds) How accurate are Polymarket odds?

Research shows prediction markets are often more accurate than experts, polls, and pundits. Traders aggregate news, polls, and expert opinions, making informed trades. Their economic incentives ensure market prices adjust to reflect true odds as more knowledgeable participants join.
This makes prediction markets the best source of real-time event probabilities. People use Polymarket for the most accurate odds, gaining the ability to make informed decisions about the future.
If you’re an expert on a certain topic, Polymarket is your opportunity to profit from trading based on your knowledge, while improving the market’s accuracy.

[How to Sign-Up](/polymarket-learn/get-started/how-to-signup)

⌘I

---


## How Are Markets Disputed?

> Source: https://docs.polymarket.com/polymarket-learn/markets/dispute

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Markets

How Are Markets Disputed?

**Anyone can dispute a proposed market resolution if they feel it was proposed in error.**
Once a market is proposed for resolution it goes into a challenge period of 2 hours.
If no one challenges the proposal the resolution is deemed valid and the proposer receives their bond back plus the reward.
During the 2-hour challenge period, anyone may dispute the proposal on the [UMA dapp](https://oracle.uma.xyz/) by posting a challenge bond of the same amount as the proposer bond (usually $750).
This begins the debate period of 24-48 hours (votes happen every other day and there will always be at least 24 hours for discussion). Anyone wishing to contribute evidence to the discussion can do so in the Uma Discord server in the #evidence-rationale and #voting-discussion channels.
After the debate period, Uma token holders vote (this process takes approximately 48 hours) and one of four outcomes happens:

## [​](#outcomes) Outcomes

### [​](#proposer-wins) Proposer wins

Proposer receives their bond back plus half the disputer’s bond as a bounty. Disputer loses their bond.

### [​](#disputer-wins) Disputer wins

Disputer receives their bond back plus half the proposer’s bond as a bounty. Proposer loses their bond.

### [​](#too-early) Too Early

This outcome is for proposals for which the underlying event has not yet happened. Eg the result of a sports match that is still ongoing. Disputer receives their bond back plus half the proposer’s bond as a bounty. Proposer loses their bond.

### [​](#unknown/50-50) Unknown/50-50

This (rarely used) outcome is for events where none of the other options are appropriate. In this case the market price resolves to 50 yes and 50 no. Disputer receives their bond back plus half the proposer’s bond as a bounty. Proposer loses their bond.

[How Are Markets Clarified?](/polymarket-learn/markets/how-are-markets-clarified)[Limit Orders](/polymarket-learn/trading/limit-orders)

⌘I

---


## How Are Markets Clarified?

> Source: https://docs.polymarket.com/polymarket-learn/markets/how-are-markets-clarified

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Markets

How Are Markets Clarified?

## [​](#overview) Overview

* Markets are resolved according to the rules set forth on the market page.
* The rules specify the resolution source, the market end date, and they outline how the market should resolve in various edge-cases.
* The market title describes the market, but the rules define how it should be resolved.

![](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/polymarket-learn/markets/market-rules.png?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=22ee2dab424287bd8ffe4ee8017dff4e)

---

## [​](#clarifications) Clarifications

In rare cases, circumstances occur that were not foreseen at a market’s creation and it becomes necessary to clarify rules after trading has begun. In these cases Polymarket may issue an “Additional context” update to the rules.

If you believe a clarification is necessary for a market, the best place to request a clarification is in the [Polymarket Discord](https://discord.com/invite/polymarket) **#market-review** channel.

![](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/polymarket-learn/markets/additional-context.png?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=c541cfe17203de08a547da32d0995804)

[How Are Prediction Markets Resolved?](/polymarket-learn/markets/how-are-markets-resolved)[How Are Markets Disputed?](/polymarket-learn/markets/dispute)

⌘I

---


## How Are Markets Created?

> Source: https://docs.polymarket.com/polymarket-learn/markets/how-are-markets-created

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Markets

How Are Markets Created?

## [​](#can-i-create-my-own-market) Can I create my own market?

While users cannot directly create their own markets, they are encouraged to suggest ideas for new markets.

### [​](#submit-your-market-proposal) Submit your market proposal

To give your proposal the best chance of being listed, include as much information as possible, such as:

* What is the market title?
* What is the [resolution source](../markets/how-are-markets-resolved)?
* Evidence of demand for trading that market

The best ways to propose a new market are:

* On [Discord](https://discord.com/invite/polymarket) in the **#market-suggestion** channel
* On Twitter / X by tagging [@polymarket](https://twitter.com/intent/tweet?text=I+have+an+idea+for+a+new+market+@polymarket)

[How to Withdraw](/polymarket-learn/deposits/how-to-withdraw)[How Are Prices Calculated?](/polymarket-learn/trading/how-are-prices-calculated)

⌘I

---


## How Are Markets Resolved?

> Source: https://docs.polymarket.com/polymarket-learn/markets/how-are-markets-resolved

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Markets

How Are Prediction Markets Resolved?

## [​](#overview) Overview

* When the result of a market becomes clear, the market can be “resolved,” or permanently finalized.
* Markets are resolved according to the market’s pre-defined rules, which can be found under market’s the order book.
* When a market is resolved, holders of winning shares receive $1 per share, losing shares become worthless, and trading of shares is no longer possible.
* To resolve a market, an outcome must first be “proposed,” which involves putting up a bond in USDC.e which will be forfeited if the proposal is unsuccessful.
* If the proposal is validated as accurate, the proposer will receive a reward for your proposal.

If you propose a market too early, or are unsuccessful in your proposal, you will lose all of your $750 bond. Do not propose a resolution unless you understand the process and are confident in your view.

### [​](#to-propose-a-market-resolution) To propose a market resolution

Once in the verification process, UMA will review the transaction to ensure it was proposed correctly. If approved, you will receive your bond amount back in your wallet plus the reward. If not approved, it will enter Uma’s dispute resolution process, which is described in detail here.

### [​](#to-dispute-a-proposed-resolution) To dispute a proposed resolution

Once a market is proposed for resolution it goes into a challenge period of 2 hours.
If you do not agree with a proposed resolution, you can [dispute the outcome](../markets/dispute).

[How Are Prices Calculated?](/polymarket-learn/trading/how-are-prices-calculated)[How Are Markets Clarified?](/polymarket-learn/markets/how-are-markets-clarified)

⌘I

---


## Trading Fees

> Source: https://docs.polymarket.com/polymarket-learn/trading/fees

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Trading

Trading Fees

Polymarket does not charge fees on most markets. However, **15-minute crypto markets** have taker fees enabled to fund the [Maker Rebates Program](/polymarket-learn/trading/maker-rebates-program).

## [​](#fee-free-markets) Fee-Free Markets

The vast majority of Polymarket markets have **no trading fees**:

* No fees to deposit or withdraw USDC (though intermediaries like Coinbase or MoonPay may charge their own fees)
* No fees to trade shares

## [​](#markets-with-fees) Markets With Fees

**15-minute crypto markets** charge a small taker fee on each trade. These fees are collected and redistributed daily to market makers as rebates, incentivizing deeper liquidity and tighter spreads.
[## Maker Rebates Program

Learn how taker fees fund daily USDC rebates for liquidity providers](/polymarket-learn/trading/maker-rebates-program)

[Liquidity Rewards](/polymarket-learn/trading/liquidity-rewards)[Maker Rebates Program](/polymarket-learn/trading/maker-rebates-program)

⌘I

---


## Holding Rewards

> Source: https://docs.polymarket.com/polymarket-learn/trading/holding-rewards

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Trading

Holding Rewards

## [​](#what-are-we-doing) What are we doing?

To keep long-term pricing accurate, we’re paying 4.00% annualized Holding Reward based on your total position value in certain polymarkets. We anticipate rolling out a new reward and oracle-resolution system later this year — at which point there will be a simple 1-click migration.

## [​](#reward-rate-and-conditions) Reward Rate and Conditions

The current rate is set at 4.00% and applies to all eligible positions. This rate is variable and subject to change at Polymarket’s discretion. We also reserve the right to introduce limits to the total amount of rewards paid out at any time. This iteration of rewards is funded through the Polymarket Treasury.
Your total position value is randomly sampled once each hour, and the reward is distributed daily. Your rewards are calculated based on the total position value of your eligible positions at the time of evaluation.

### [​](#total-position-value-computation) **Total Position Value Computation**

For each eligible polymarket, we calculate the eligible position in the following way:
**Position Valuation**:

* Based on your current “Yes” and “No” shares and the most recent mid-price for each outcome.

### [​](#example) **Example**

If you hold at time of sample:

* 30,000 “Yes” shares at a price of **$0.53**
* 10,000 “No” shares at a price of **$0.45**

**Total Position Value** =
→ `(30000 × 0.53) + (10000 × 0.45)`
→ `$15,900 + $4,500 = $20,400`
**Hourly Holding Reward Calculation** (based on 4.00% Annual Reward):
→ `$20400 × (0.04 / 365 / 24) ≈ $.09315068493`

## [​](#eligible-events) Eligible Events:

* [Presidential Election Winner 2028](https://polymarket.com/event/presidential-election-winner-2028)
* [Republican Presidential Nominee 2028](https://polymarket.com/event/republican-presidential-nominee-2028)
* [Democratic Presidential Nominee 2028](https://polymarket.com/event/democratic-presidential-nominee-2028)
* [Which party wins 2028 US Presidential Election?](https://polymarket.com/event/which-party-wins-2028-us-presidential-election)
* [Balance of Power: 2026 Midterms](https://polymarket.com/event/balance-of-power-2026-midterms)
* [Which party will win the Senate in 2026?](https://polymarket.com/event/which-party-will-win-the-senate-in-2026)
* [Which party will win the House in 2026?](https://polymarket.com/event/which-party-will-win-the-house-in-2026)
* [Erdoğan out before 2027?](https://polymarket.com/event/erdoan-out-before-2027)
* [Zelenskyy out as Ukraine president before 2027?](https://polymarket.com/event/zelenskyy-out-as-ukraine-president-before-2027)
* [Netanyahu out before 2027?](https://polymarket.com/event/netanyahu-out-before-2027)
* [Xi Jinping out before 2027?](https://polymarket.com/event/xi-jinping-out-before-2027)
* [Putin out as President of Russia before 2027?](https://polymarket.com/event/putin-out-before-2027)
* [Russia x Ukraine ceasefire before 2027?](https://polymarket.com/event/russia-x-ukraine-ceasefire-before-2027)

[Market Orders](/polymarket-learn/trading/market-orders)[Liquidity Rewards](/polymarket-learn/trading/liquidity-rewards)

⌘I

---


## How Are Prices Calculated?

> Source: https://docs.polymarket.com/polymarket-learn/trading/how-are-prices-calculated

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Markets

How Are Prices Calculated?

## [​](#initial-price) Initial Price

* When a market is created, there are initially zero shares and no pre-defined prices or odds.
* Market makers (a fancy term for traders placing limit orders) interested in buying YES or NO shares can place [Limit Orders](../trading/limit-orders) at the price they’re willing to pay
* When offers for the YES and NO side equal $1.00, the order is “matched” and that $1.00 is converted into 1 YES and 1 NO share, each going to their respective buyers.

For example, if you place a limit order at $0.60 for YES, that order is matched when someone places a NO order at $0.40. *This becomes the initial market price.*

## [​](#future-price) Future Price

The prices displayed on Polymarket are the midpoint of the bid-ask spread in the orderbook — unless that spread is over $0.10, in which case the last traded price is used.
Like the stock market, prices on Polymarket are a function of realtime supply & demand.

### [​](#prices-=-probabilities) Prices = Probabilities

In the market below, the probability of 37% is the midpoint between the 34¢ bid and 40¢ ask. If the bid-ask spread is wider than 10¢, the probability is shown as the last traded price.

![](https://polymarket-upload.s3.us-east-2.amazonaws.com/how_are_prices_calculated.png)

You may not be able to buy shares at the displayed probability / price because there is a bid-ask spread. In the above example, a trader wanting to buy shares would pay 40¢ for up to 4,200 shares, after which the price would rise to 43¢.

[How Are Markets Created?](/polymarket-learn/markets/how-are-markets-created)[How Are Prediction Markets Resolved?](/polymarket-learn/markets/how-are-markets-resolved)

⌘I

---


## Limit Orders

> Source: https://docs.polymarket.com/polymarket-learn/trading/limit-orders

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Trading

Limit Orders

## [​](#video-guide) Video guide

## [​](#what-are-limit-orders) What are Limit Orders?

Limit orders are open orders (pending trades) that only execute when the market trades at your desired price.
For example, if the highest you’re willing to pay for a share of Trump “Yes” in the 2024 Republican Nomination is 72c, but the current market price is 73c, you could create a limit order at 72c and wait until someone is willing to sell Yes shares at your desired price.

It’s not necessary for the entire order to execute at once. Limit orders can ‘partially fill’ as individual traders fill parts of your order.

## [​](#managing-limit-orders) Managing limit orders

When you have an open order, you’ll find it displayed just below the Order Book on the market’s page.
If you have open orders across multiple markets, you can easily manage and monitor them all from the [Portfolio page](https://polymarket.com/portfolio?tab=Open+orders).

Specifically for sports markets, any outstanding limit orders are automatically cancelled once the game begins, clearing the entire order book at the official start time. Be aware, game start times can shift so it’s important to always monitor your orders closely in case they are not cleared due to game changes or other circumstances.

Additionally, sports markets include a 3-second delay on the placement of marketable orders.

## [​](#canceling-limit-orders) Canceling limit orders

When you have an open order, you’ll find it displayed just below the Order Book on the market’s page.
To cancel the order, you can simply click the red **x** button alongside the order.

If you have open orders across multiple markets, you can easily manage and monitor them all from the [Portfolio page](https://polymarket.com/portfolio?tab=Open+orders).
Nice! You can officially call yourself an advanced trader.

If some of this still isn’t making sense, feel free to reach out to us on [Discord](https://discord.com/invite/polymarket). We’re happy to help get you up to speed.

[How Are Markets Disputed?](/polymarket-learn/markets/dispute)[Market Orders](/polymarket-learn/trading/market-orders)

⌘I

---


## Liquidity Rewards (Learn)

> Source: https://docs.polymarket.com/polymarket-learn/trading/liquidity-rewards

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Trading

Liquidity Rewards

With Polymarket’s Liquidity Rewards Program, you can earn money by placing limit orders that help keep the market active and balanced.

## [​](#overview) Overview

* The closer your orders are to the market’s average price, the more you earn.
* The reward amount depends on how helpful your orders are in terms of size and pricing compared to others.
* The more competitive your limit orders, the more you can make.
* You get paid daily based on how much your orders add to the market, and can use our [Rewards page](https://polymarket.com/rewards) to check your current earnings for the day, which markets have rewards in place, as well as how much.
* The minimum reward payout is $1; amounts below this will not be paid.

![](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/polymarket-learn/media/liquidity-rewards-earnings.png?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=ebcb693900b79d2c23356b0f087b5941)

Simply put, the more you help the market by placing good orders, the more rewards you earn!

## [​](#seeing-rewards-in-the-order-book) Seeing Rewards in the Order Book

### [​](#viewing-rewards) Viewing Rewards

The total rewards, max spread, and minimum shares required to earn rewards vary by market. You can view the rewards for a given market in its Order Book.

* On the Polymarket order book, you can hover over the Rewards text to see the amount of rewards available in total on each market.
* The blue highlighted lines correspond to the max spread — meaning the farthest distance your limit order can be from the midpoint of the market to earn rewards.
* In the example below, because the max spread is 3c, every order within 3c of the midpoint is eligible for rewards. If the midpoint is < $0.10, you need to have orders on both sides to qualify.

![](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/polymarket-learn/media/liquidity-rewards-market.png?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=12202bc1af31cdc1935ee816ca00f308)

### [​](#earning-rewards) Earning Rewards

When your orders are earning rewards you’ll see a blue highlight around the clock icon, as shown below:

![](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/polymarket-learn/media/earning-liquidity-rewards.png?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=1a0c05e93f37c95c66b4ad67ff66c320)

## [​](#learn-more) Learn more

Rewards are paid out automatically every day at ~midnight UTC. Your history on your portfolio page will reflect rewards paid to your address.
To read more about the specific calculations and formulas that determine rewards, visit our [Liquidity Rewards Documentation](/developers/market-makers/liquidity-rewards).

[Holding Rewards](/polymarket-learn/trading/holding-rewards)[Fees](/polymarket-learn/trading/fees)

⌘I

---


## Maker Rebates Program (Learn)

> Source: https://docs.polymarket.com/polymarket-learn/trading/maker-rebates-program

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Trading

Maker Rebates Program

We’re rolling out **Maker Rebates** for **15-minute crypto markets**; a program designed to make these fast-moving markets deeper, tighter, and easier to trade.
Market makers who provide **active liquidity** (orders that get filled) earn **daily USDC rebates**, proportional to the liquidity they provide.

## [​](#why-maker-rebates) Why Maker Rebates?

15-minute markets move quickly. When liquidity is deeper:

* Spreads tend to be tighter
* Price impact is lower
* Fills are more reliable
* Markets are more resilient during volatility

Maker Rebates incentivize **consistent, competitive quoting** so everyone gets a better trading experience.

## [​](#how-maker-rebates-work) How Maker Rebates Work

* **Paid daily in USDC:** Rebates are calculated and distributed every day.
* **Performance-based:** You earn based on the share of liquidity you provided that actually got taken.

### [​](#funding) Funding

Maker Rebates are funded by **taker fees collected in 15-minute crypto markets**. A percentage of these fees are redistributed to makers who keep the markets liquid.

| Period | Maker Rebate | Distribution Method |
| --- | --- | --- |
| Jan 9 – Jan 11, 2026 (Until Sunday Midnight UTC) | 100% | Volume-weighted |
| Jan 12 – Jan 18, 2026 | 20% | Volume-weighted |
| Jan 19+ | 20% | Fee-curve weighted |

Polymarket collects taker fees **only** in 15-minute crypto markets. The rebate percentage is at the sole discretion of Polymarket and may change over time.

## [​](#fee-curve-weighted-rebates) Fee-Curve Weighted Rebates

Rebates are distributed using the **same formula as taker fees**. This ensures makers are rewarded proportionally to the fee value their liquidity generates.
For each filled maker order:

Copy

```shiki
fee_equivalent = shares * price * 0.25 * (price * (1 - price))^2
```

Your daily rebate:

Copy

```shiki
rebate = (your_fee_equivalent / total_fee_equivalent) * rebate_pool
```

## [​](#taker-fee-structure) Taker Fee Structure

Taker fees are calculated in USDC and vary based on the share price. Fees are **highest at 50%** probability and **lowest at the extremes** (near 0% or 100%).
![Fee Curve](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/polymarket-learn/media/fee_image.png?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=5a4bdaf810ad1dafafd7c6f2be20719e)

### [​](#fee-table-100-shares) Fee Table (100 shares)

| Price | Trade Value | Fee (USDC) | Effective Rate |
| --- | --- | --- | --- |
| $0.01 | $1 | $0.00 | 0.00% |
| $0.05 | $5 | $0.003 | 0.06% |
| $0.10 | $10 | $0.02 | 0.20% |
| $0.15 | $15 | $0.06 | 0.41% |
| $0.20 | $20 | $0.13 | 0.64% |
| $0.25 | $25 | $0.22 | 0.88% |
| $0.30 | $30 | $0.33 | 1.10% |
| $0.35 | $35 | $0.45 | 1.29% |
| $0.40 | $40 | $0.58 | 1.44% |
| $0.45 | $45 | $0.69 | 1.53% |
| $0.50 | $50 | $0.78 | **1.56%** |
| $0.55 | $55 | $0.84 | 1.53% |
| $0.60 | $60 | $0.86 | 1.44% |
| $0.65 | $65 | $0.84 | 1.29% |
| $0.70 | $70 | $0.77 | 1.10% |
| $0.75 | $75 | $0.66 | 0.88% |
| $0.80 | $80 | $0.51 | 0.64% |
| $0.85 | $85 | $0.35 | 0.41% |
| $0.90 | $90 | $0.18 | 0.20% |
| $0.95 | $95 | $0.05 | 0.06% |
| $0.99 | $99 | $0.00 | 0.00% |

The maximum effective fee rate is **1.56%** at 50% probability. Fees decrease symmetrically toward both extremes.

### [​](#fee-precision) Fee Precision

Fees are rounded to 4 decimal places. The smallest fee charged is **0.0001 USDC**. Anything smaller rounds to zero, so very small trades near the extremes may incur no fee at all.

## [​](#faq) FAQ

How do I qualify for maker rebates?

Place orders that add liquidity to the book and get filled (i.e., your liquidity is taken by another trader).

When are rebates paid?

Daily, in USDC.

How are rebates calculated?

Rebates are proportional to your share of executed maker liquidity in each eligible market. During fee-curve weighted periods, this is based on fee-equivalent using the formula above.

Where does the rebate pool come from?

Taker fees collected in eligible markets are allocated to the maker rebate pool and distributed daily.

Which markets have fees enabled?

Currently, only 15-minute crypto markets have taker fees enabled.

Is Polymarket charging fees on all markets?

No. Polymarket is collecting taker fees **only** on 15-minute crypto markets. All other markets remain fee-free.

## [​](#for-api-users) For API Users

If you trade programmatically, you’ll need to update your client to handle fees correctly.
[## Developer Guide: Maker Rebates

Technical documentation for handling fees in your trading code](/developers/market-makers/maker-rebates-program)

[Fees](/polymarket-learn/trading/fees)[Does Polymarket Have Trading Limits?](/polymarket-learn/trading/no-limits)

⌘I

---


## Market Orders

> Source: https://docs.polymarket.com/polymarket-learn/trading/market-orders

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Trading

Market Orders

# [​](#market-orders) Market Orders

Once you’ve [signed up](../get-started/how-to-signup) and [deposited funds](../get-started/how-to-deposit), you’re ready to start trading on Polymarket. Here’s a step-by-step guide to get you started.

## [​](#video-walkthrough) Video Walkthrough

## [​](#placing-a-market-order) Placing a Market Order

\_Before trading, you’ll want to visit the [markets page](https://polymarket.com/markets) to find a market that interests you.Simple, right? If you think you’ve got the hang of it, it’s time to learn about more advanced trading and order types. [Limit Orders](../trading/limit-orders/).

[Limit Orders](/polymarket-learn/trading/limit-orders)[Holding Rewards](/polymarket-learn/trading/holding-rewards)

⌘I

---


## Does Polymarket Have Trading Limits?

> Source: https://docs.polymarket.com/polymarket-learn/trading/no-limits

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Trading

Does Polymarket Have Trading Limits?

By design, the Polymarket orderbook **does not** have trading size limits. It matches willing buyers and sellers of any amount.
However, there is no guarantee that it will be possible to transact a desired amount of shares without impacting the price significantly, or at all if there are no willing counterparties. Before trading in any market, especially in large size, it is valuable to look at the orderbook to understand depth of liquidity, ie how many buyers or sellers are in the market and their desired trade size and price.

[Maker Rebates Program](/polymarket-learn/trading/maker-rebates-program)[Using the Order Book](/polymarket-learn/trading/using-the-orderbook)

⌘I

---


## Using the Order Book

> Source: https://docs.polymarket.com/polymarket-learn/trading/using-the-orderbook

[Polymarket Documentation home page](/)

Search...

⌘K

Search...

Navigation

Trading

Using the Order Book

In the Getting Started tutorial on [Making your First Trade](../get-started/making-your-first-trade/), we learned about market orders.
In a market order, your trade executes instantly at the current market price.
But what if you think the market price is too high and want to set a specific price that you would be willing to accept? These are called [Limit Orders](../trading/limit-orders/).

## [​](#viewing-the-order-book) Viewing the Order Book

The order book is a list of every open order to buy or sell shares in a particular market.

![](https://polymarket-upload.s3.us-east-2.amazonaws.com/Orderbook-light.png)

In this market, **“Presidential Election Winner 2024”**, we are viewing the order book for Trump Yes shares.
The green side represents the Bids: the highest price traders are willing to pay to buy Trump Yes
shares.
The red side represents the Asks: the lowest price traders are willing to accept to sell Trump Yes shares.

Notice that there is a 0.3c gap between the highest bid and the lowest ask price. This is referred to as the spread.

## [​](#managing-open-orders) Managing open orders

When you have an open order, you’ll find it displayed just below the Order Book on the market’s page.
If you have open orders across multiple markets, you can easily manage and monitor them all from the [Portfolio page](https://polymarket.com/portfolio?tab=Open+orders).

## [​](#canceling-open-orders) Canceling open orders

When you have an open order, you’ll find it displayed just below the Order Book on the market’s page.
To cancel the order, you can simply click the red **x** button alongside the order.If you have open orders across multiple markets, you can easily manage and monitor them all from the [Portfolio page](https://polymarket.com/portfolio?tab=Open+orders).
Nice! You can officially call yourself an advanced trader.

If some of this still isn’t making sense, feel free to reach out to us on [Discord](https://discord.com/invite/polymarket). We’re happy to help get you up to speed.

[Does Polymarket Have Trading Limits?](/polymarket-learn/trading/no-limits)[Geographic Restrictions](/polymarket-learn/FAQ/geoblocking)

⌘I

---
