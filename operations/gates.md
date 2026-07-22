# Skills Value Gates

## Purpose

The Skills loop must produce installable, reviewable, discoverable skill value. Catalog metadata is useful only when it improves package safety, discoverability, installability, or reviewability.

The work ledger of record is `operations/ledger.json`. Historical run evidence
does not select current work.

## Promotion ladder

```text
discovery source
-> source profile / skip note
-> risk + license review
-> normalized skill
-> catalog parity
-> install verification
-> package / registry publication
```

## Priority order

1. High-risk package-facing skill review.
2. Discovery handoff restoration or bounded manual discovery fallback.
3. Catalog parity after real metadata/skill changes.
4. Bounded metadata backlog cleanup.
5. Publication/registry work only after review, discovery, and catalog gates are clean.

## Done definition

A Skills ticket is done only if it:

- restores or repairs discovery;
- reviews a source or candidate;
- creates a source profile or skip note;
- normalizes a useful non-generic skill;
- removes a risk blocker;
- improves package-facing metadata that changes discoverability/reviewability;
- verifies catalog/install-manifest parity;
- verifies an installable/published surface.

Status-only updates and repeated catalog checks after parity is known are low value.

## Safety gates

Do not copy third-party content unless license, attribution, usefulness, and safety review are clear.

High-risk surfaces must be review-gated or quarantined before package/publication endorsement, including:

- credential access;
- phishing/session hijack;
- SSRF/internal probing;
- offensive C2/red-team infra;
- lateral movement;
- exploit execution;
- account mutation;
- private/leaked material;
- executable browser/account workflows.

## Supervisor authority

The Portfolio Supervisor may:

- block publication while discovery handoff is absent;
- block metadata backlog cleanup while a high-risk ticket is open;
- create risk-review tickets;
- mark catalog/status-only churn low value;
- require local-agent/CI repair if connector-only execution cannot regenerate surfaces.
