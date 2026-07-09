---
name: Code Complexity Scanner
description: Measure cyclomatic complexity, cognitive complexity, and function length across codebases to identify maintenance hotspots. Use when analyzing code quality, finding complex functions, or prioritizing refactoring targets.
tags: [software-development, code-quality, complexity, metrics, static-analysis]
domain: software-engineering
risk_level: low
requires_review: false
source: terminal-skills (terminalskills.io)
source_status: reviewed-metadata-only
license: Apache-2.0
distilled: 2026-06-22
type: Metric
---

# Code Complexity Scanner

## Overview

Analyze source code to measure cyclomatic complexity, cognitive complexity, and function length. Identify the most complex functions and files to focus refactoring efforts on code that's hardest to maintain and most likely to harbor bugs.

## Measurement Method

### Cyclomatic Complexity

For each function/method, count:
- `if`, `elif`/`else if` → +1 each
- `for`, `while`, `do-while` → +1 each
- `case` in switch → +1 each
- `catch` → +1
- `&&`, `||` in conditions → +1 each
- Ternary `?:` → +1
- Base complexity starts at 1

### Cognitive Complexity

More nuanced — penalizes nesting:
- Each control flow break: +1
- Each nesting level: +1 additional per level
- Recursion: +1
- Boolean operator sequences that switch: +1

### Hotspot Ranking

Rank files by:
1. Maximum function complexity in the file
2. Average complexity across all functions
3. Number of functions above threshold (default: 15)
4. Total lines of code

## Output Tiers

- 🔴 **Critical** (complexity > 25): Must refactor — these functions are untestable
- 🟡 **Warning** (complexity 15–25): Should refactor when next modifying
- 🟢 **OK** (complexity < 15): Acceptable maintainability

## Guidelines

- **Thresholds are configurable** — default 15 works for most teams
- **Cognitive > cyclomatic for human readability** — cognitive complexity better captures how hard code is to understand
- **Context matters** — a parser with complexity 20 might be acceptable; a controller with complexity 20 needs splitting
- **Combine with change frequency** — complex code that never changes is less urgent than complex code edited weekly
- **Don't count generated code** — exclude auto-generated files, migrations, and schema definitions
- **Suggest specific refactorings** — "Extract method" for long functions, "Replace conditional with polymorphism" for deep switch statements, "Introduce parameter object" for functions with 5+ parameters
