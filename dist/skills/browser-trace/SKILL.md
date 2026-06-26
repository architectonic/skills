---
name: Browser Trace
description: Capture a full DevTools-protocol trace of any browser automation — CDP firehose, screenshots, and DOM dumps — then bisect into per-page searchable buckets. Use when debugging failed browser automation runs, auditing network/console/DOM activity, or feeding structured per-page summaries back into agent loops.
tags: [software-development, debugging, browser, cdevtools, cdp, tracing, automation, o11y]
source: mxyhi/ok-skills (MIT)
distilled: 2026-06-22
type: Playbook
---

# Browser Trace

Attach a **second, read-only CDP client** to a browser session that is already being driven by your main automation. The trace records the full DevTools firehose to NDJSON, polls for screenshots and DOM dumps in parallel, and slices everything into a directory tree that bash tools can search.

This skill does **not** drive pages — it only listens. Pair it with the `browser` skill, Playwright, or anything else that speaks CDP.

## When to Use

- Debug a browser-automation run (failing form, missing element, hung navigation, JS exception)
- Attach a trace mid-flight to a running automation without restarting
- Split a CDP firehose into network / console / DOM / page buckets
- Get screenshots + DOM snapshots over time, joined to CDP events by timestamp

If the user just wants to **drive** the browser, use the `browser` skill instead.

## Requirements

- Node 18+
- `browse` CLI (`npm install -g browse`) with `browse cdp` subcommand
- `jq` optional — for ad-hoc querying of bisected JSONL files
- For remote Browserbase sessions: `BROWSERBASE_API_KEY`

## How It Works

Every Chrome DevTools target accepts **multiple concurrent CDP clients**. Your main automation is one client; this skill adds a second that only enables observation domains (Network, Console, Runtime, Log, Page) and never sends action commands.

Three pieces:
1. **Firehose**: streams every CDP event as one JSON object per line to `cdp/raw.ndjson`
2. **Sampler**: polling loop takes screenshots and DOM dumps at intervals (default 2s)
3. **Bisector**: after the run, slices `raw.ndjson` into per-bucket JSONL files keyed by CDP method, and per-page using `Page.frameNavigated` events

## Quickstart (Local Chrome)

```bash
# 1. Launch Chrome with debugger port
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-o11y \
  about:blank &

# 2. Start the tracer
node scripts/start-capture.mjs 9222 my-run

# 3. Run your main automation against port 9222
browse open https://example.com --cdp 9222

# 4. Stop and bisect
node scripts/stop-capture.mjs my-run
node scripts/bisect-cdp.mjs my-run
```

## Filesystem Layout

```
.o11y/<run-id>/
  manifest.json                 run metadata
  index.jsonl                   one line per sample: {ts, screenshot, dom, url}
  cdp/
    raw.ndjson                  full CDP firehose
    summary.json                {sessionId, duration, totalEvents, pages[]}
    network/{requests,responses,finished,failed,websocket}.jsonl
    console/{logs,exceptions}.jsonl
    runtime/all.jsonl
    page/{navigations,lifecycle,frames,dialogs,all}.jsonl
    pages/                      per-page slices
      000/                      first concrete page (navigation order)
        url.txt, summary.json, raw.jsonl
        network/, console/, page/  (only non-empty files)
  screenshots/<iso-ts>.png
  dom/<iso-ts>.html
```

## Querying the Trace

```bash
# Use the query helper
node scripts/query.mjs my-run list                    # pages table
node scripts/query.mjs my-run page 1                  # page 1 summary
node scripts/query.mjs my-run page 1 network/failed   # failed requests
node scripts/query.mjs my-run errors                  # all errors
node scripts/query.mjs my-run hosts                   # top hosts
node scripts/query.mjs my-run host api.example.com    # requests for host

# Or raw jq
jq -c '.params' .o11y/<run>/cdp/network/failed.jsonl
jq -c 'select(.params.response.status >= 400)' .o11y/<run>/cdp/network/responses.jsonl
jq -c 'select(.params.type == "error")' .o11y/<run>/cdp/console/logs.jsonl
jq -r '.params.frame.url' .o11y/<run>/cdp/page/navigations.jsonl
```

## Best Practices

1. Use `bb-capture.mjs` on Browserbase (enforces `--keep-alive`, captures debugger URL)
2. Don't `--release` a session you don't own
3. On Browserbase: attach automation client before/with the tracer
4. Don't poll faster than ~1s (2s default)
5. Pick domains deliberately: `Network Console Runtime Log Page` covers most debugging
6. Always run `stop-capture.mjs` even after crashes
7. `bisect-cdp.mjs` is idempotent — safe to re-run
