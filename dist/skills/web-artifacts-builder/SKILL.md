---
name: web-artifacts-builder
description: Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components — not for simple single-file HTML/JSX artifacts.
type: Playbook
---

# Web Artifacts Builder

Build powerful frontend claude.ai artifacts using React 18 + TypeScript + Vite + Parcel + Tailwind CSS + shadcn/ui.

## Stack

React 18 + TypeScript + Vite + Parcel (bundling) + Tailwind CSS + shadcn/ui

## Workflow

1. **Initialize:** `bash scripts/init-artifact.sh <project-name>` — creates fully configured project
2. **Develop:** Edit the generated code
3. **Bundle:** `bash scripts/bundle-artifact.sh` — creates `bundle.html` (self-contained)
4. **Share:** Display the bundled HTML to the user

## Design Guidelines

Avoid "AI slop": no excessive centered layouts, purple gradients, uniform rounded corners, or Inter font.

## What You Get

- React + TypeScript (via Vite)
- Tailwind CSS 3.4.1 with shadcn/ui theming
- Path aliases (`@/`)
- 40+ shadcn/ui components pre-installed
- All Radix UI dependencies
- Parcel configured for bundling
- Node 18+ compatibility

## Output

Single self-contained HTML file with all JS, CSS, and dependencies inlined. Works directly in claude.ai artifacts or any browser.
