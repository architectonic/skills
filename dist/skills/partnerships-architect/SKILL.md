---
name: partnerships-architect
title: Partnerships Architect
description: 'Evaluate and structure business partnerships. Answers four questions
  when a prospective partner shows up:'
type: Playbook
domain: business
tags:
- business
- okf
risk_level: low
requires_review: false
---

# Partnerships Architect

Evaluate and structure business partnerships. Answers four questions when a prospective partner shows up:

1. **Is this a real partner, or someone hunting preferential terms without independent demand?**
2. **At what tier should we sign them?** (Referral / Reseller / OEM / SI-Consulting / Strategic Alliance)
3. **What's the 90-day joint GTM plan that proves the partnership works?**
4. **What revshare makes economic sense — and at what point does the partnership beat direct sale?**

Outputs tier verdict + GTM plan + revshare band with explicit kill criteria. Does **not** sign the deal.

## Workflow

1. **Intake** — Partner name, type, evidence of independent demand (named accounts, end-customer relationships, sales team size), strategic value, commitments
2. **Tier classify** — 5-tier classifier with deterministic floors (STRATEGIC requires ≥5 named accounts AND multi-year commit AND dedicated resources)
3. **Joint GTM plan** — 90-day plan with pre-launch milestones, launch motion, checkpoint, success criteria
4. **Revshare model** — Margin per deal direct vs. via partner, recommended revshare band, break-even ROI
5. **Decide** — Document kill criteria in the contract so unwind is mechanical when triggered

## Forcing Questions (one at a time)

1. **"Name 5 end customers this partner sold to in the last 12 months."** → If they cannot, no independent demand. Sign at REFERRAL tier only. Canon: Joe Hessling.
2. **"Asking for preferential terms, or asking how to bring you customers?"** → Discount hunters lead with terms; real partners lead with accounts. Canon: Forrester.
3. **"What's the joint value proposition in one sentence, and who's the named end-customer?"** → No joint value prop = no partnership. Canon: Geoffrey Moore.
4. **"At what % discount/revshare does this beat direct-sale economics, at what scale?"** → Model break-even pipeline volume. Canon: Chintagunta.
5. **"What are the named kill criteria, and are they in the contract?"** → Minimum pipeline floor, certified resources, joint deals closed, 90-day cure. Canon: IBM channel-conflict cases.
6. **"If partner sells to YOUR direct account, who wins?"** → Rules of Engagement in writing, signed before kickoff. Canon: Jay McBain.
7. **"Is this a partnership, or should this be an acquisition?"** → If partner has independent moat you can't replicate AND requires equity-like alignment, route to M&A. Canon: HP channel post-mortems.

## Anti-Patterns

- **"Partner = anyone who asked"** — No independent demand = discount hunter. Use REFERRAL tier.
- **OEM/white-label without margin for support** — OEM means supporting a customer you don't own
- **Paying sourced-tier revshare on influenced-only deals** — Influenced ≠ sourced
- **No kill criteria** — "Strategic alliances" without sunset clauses become permanent obligations
- **Channel conflict ignored until reps quit** — Decide rules of engagement before, not after
- **Exclusive territory to weak partner** — Locks out the strong partner
- **MDF without ROI accountability** — Subsidy, not investment
- **No offboarding plan** — Customer continuity, data hand-back, IP cleanup must be pre-negotiated

## Distinct From

| Neighbor | Difference |
|---|---|
| `channel-economics` | Quantifies whether a signed partner is profitable; this decides whether to sign |
| `sales-engineer` | Technical demos/POCs after partnership decision |
| `cro-advisor` | Strategic CRO judgment; this is per-partnership |
| `deal-desk` | Per-deal discount on signed contracts |
