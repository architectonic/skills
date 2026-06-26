---
name: spreadsheets
description: Create, modify, and analyze spreadsheets (.xlsx, .xls, .csv). Use when the user needs to build workbooks, write formulas, format data, perform analysis, create charts, or query tabular data with SQL. Covers both openpyxl/Python-native and DuckDB/SQL workflows.
tags: [productivity, agent-skill]
type: Playbook
---

# spreadsheets

Create, modify, and analyze spreadsheets (.xlsx, .xls, .csv).

## Two workflows

### Workflow A: Python-native (openpyxl / artifact_tool)

Use when building spreadsheets programmatically with Python.

```python
# Create new workbook
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "Data"
ws["A1"] = "Header"
wb.save("output.xlsx")

# Read existing workbook
from openpyxl import load_workbook
wb = load_workbook("input.xlsx")
ws = wb.active
for row in ws.iter_rows(values_only=True):
    print(row)
```

If `artifact_tool` is available, use its workbook APIs for structured editing.

### Workflow B: SQL analysis (DuckDB)

Use when analyzing data with SQL queries, especially for large files or multi-file joins.

```bash
# Install
pip install duckdb pandas openpyxl

# Inspect file structure
python scripts/analyze.py --files data.xlsx --action inspect

# Run SQL query
python scripts/analyze.py --files data.xlsx --action query \
  --sql "SELECT category, COUNT(*), AVG(amount) FROM Sheet1 GROUP BY category"

# Statistical summary
python scripts/analyze.py --files data.xlsx --action summary --table Sheet1

# Export results
python scripts/analyze.py --files data.xlsx --action query \
  --sql "SELECT * FROM Sheet1 WHERE amount > 1000" \
  --output-file results.csv
```

**Table naming:**
- Excel sheets: table name = sheet name (e.g., `Sheet1`, `Sales`)
- CSV files: table name = filename without extension
- Multiple files: all tables available in same query context for cross-file joins

**DuckDB SQL patterns:**

```sql
-- Aggregation
SELECT category, SUM(revenue) as total FROM Sales GROUP BY category ORDER BY total DESC

-- Window functions
SELECT order_date, amount,
       SUM(amount) OVER (ORDER BY order_date) as running_total,
       RANK() OVER (ORDER BY amount DESC) as amount_rank
FROM Sales

-- Cross-file joins
SELECT s.order_id, s.amount, c.customer_name, c.region
FROM sales s JOIN customers c ON s.customer_id = c.id
WHERE s.amount > 500
```

## Formatting baseline

- Content columns: ~10-24 width
- Text-heavy columns: cap ~32-40
- Row heights: ~15-20 (titles may be larger)
- Avoid oversized body fonts (>12pt) except intentional titles
- Add whitespace between sections
- Use fill colors, borders, and merged cells judiciously
- Add data validation for categorical columns (Status, Priority, Owner)
- Use conditional formatting when useful

## Quality floor

- Keep layout readable and bounded
- Prefer formula-driven logic over manual painted cells
- Derived values must be formulas (not hardcoded)
- No magic numbers in formulas; reference cells
- Include at least one visual summary for tracker/planning requests
- If writing literal text starting with `=`, prefix with single quote (`'=high-low`)
- Keep workbook structurally valid (unique table names)

## Verification

```python
# Inspect key ranges
check = wb.inspect({
  "kind": "table",
  "range": "Dashboard!A1:H20",
  "include": "values,formulas",
})

# Scan formula errors
errors = wb.inspect({
  "kind": "match",
  "search_term": "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  "options": {"use_regex": True, "max_results": 300},
})
```

## Completion criteria

- Workbook content is populated and formulas compute
- No obvious formula errors in key scanned ranges
- `.xlsx` saved to output path
- Layout is organized, legible, and aligned to request style
