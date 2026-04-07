# Workspace

## Overview

pnpm workspace monorepo using TypeScript. Each package manages its own dependencies.

## Stack

- **Monorepo tool**: pnpm workspaces
- **Node.js version**: 24
- **Package manager**: pnpm
- **TypeScript version**: 5.9
- **API framework**: Express 5
- **Database**: PostgreSQL + Drizzle ORM
- **Validation**: Zod (`zod/v4`), `drizzle-zod`
- **API codegen**: Orval (from OpenAPI spec)
- **Build**: esbuild (CJS bundle)

## Key Commands

- `pnpm run typecheck` — full typecheck across all packages
- `pnpm run build` — typecheck + build all packages
- `pnpm --filter @workspace/api-spec run codegen` — regenerate API hooks and Zod schemas from OpenAPI spec
- `pnpm --filter @workspace/db run push` — push DB schema changes (dev only)
- `pnpm --filter @workspace/api-server run dev` — run API server locally

See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details.

## Artifacts

### Facebook Management Dashboard (`artifacts/fb-dashboard`)
- **Type**: React + Vite web app
- **Preview Path**: `/`
- **Pages**:
  - `/` — Dashboard with summary stats, top performing posts, post pipeline
  - `/pages` — Manage Facebook Pages and Access Tokens
  - `/posts` — Create, schedule, and manage posts
  - `/insights` — Analytics per page and top posts leaderboard
  - `/ai-generator` — AI Content Generator (Gemini caption/hashtags + Hugging Face image generation)
  - `/ads` — Meta Ads Manager (Gemini audience analysis, campaign creation via Marketing API, CPC/CTR metrics, toggle ACTIVE/PAUSED)
  - `/settings` — API Keys (Gemini, Hugging Face, Facebook App ID/Secret, Ad Account ID)

### API Server (`artifacts/api-server`)
- **Type**: Express 5 + TypeScript
- **Routes**: `/api/settings`, `/api/pages`, `/api/posts`, `/api/insights/*`, `/api/ai/*`, `/api/ads/*`, `/api/oauth/*`
- **AI Routes** (`artifacts/api-server/src/routes/ai.ts`):
  - `POST /api/ai/generate-content` — Uses Gemini API (key from settings) to generate caption, hashtags, contact recommendations, image suggestion
  - `POST /api/ai/generate-image` — Uses Hugging Face Inference API (SDXL model, key from settings) to generate image from prompt
- **OAuth Routes** (`artifacts/api-server/src/routes/oauth.ts`):
  - `POST /api/oauth/facebook/exchange-token` — Short-lived → long-lived token exchange
  - `POST /api/oauth/facebook/sync-pages` — Fetch and upsert all managed Facebook Pages
- **Ads Routes** (`artifacts/api-server/src/routes/ads.ts`):
  - `POST /api/ads/analyze-audience` — Gemini AI audience analysis from business description
  - `POST /api/ads/search-interests` — Search Facebook Ad Interests by keyword via Meta API
  - `GET/POST /api/ads/campaigns` — List all campaigns / Create campaign (Campaign → Ad Set → Creative → Ad)
  - `PATCH /api/ads/campaigns/:id/status` — Toggle ACTIVE/PAUSED via Meta API
  - `GET /api/ads/campaigns/:id/insights` — Fetch CPC, CTR, impressions, spend from Meta API
- **Dependencies**: `@google/generative-ai` for Gemini SDK
- **Facebook API version**: v18.0

## Database Schema

Tables in `lib/db/src/schema/`:
- `settings` — API keys (Gemini, Hugging Face, Facebook App ID/Secret, Ad Account ID, Facebook User Token)
- `pages` — Facebook Pages with access tokens, follower count, category
- `posts` — Posts with status (draft/scheduled/published/failed), metrics
- `adCampaigns` — Meta Ad campaigns with IDs, status, budget, targeting, metrics cache

## Folder Structure

```
artifacts/
  fb-dashboard/src/
    pages/       # Dashboard, Pages, Posts, Insights, AI Generator, Ads, Settings
    components/  # Layout (sidebar), shared UI
  api-server/src/
    routes/      # settings.ts, pages.ts, posts.ts, insights.ts, ai.ts, oauth.ts, ads.ts
    lib/         # logger.ts, serialize.ts
lib/
  api-spec/      # openapi.yaml (single source of truth)
  api-client-react/  # Generated React Query hooks
  api-zod/       # Generated Zod schemas
  db/            # Drizzle ORM schema + client
```
