---
name: jupyter-notebook-creation
description: Create, scaffold, and edit Jupyter notebooks (.ipynb) for experiments, explorations, or tutorials. Use when the user needs to generate clean, reproducible notebooks with proper structure. Complements jupyter-live-kernel which focuses on execution.
tags: [data-science, jupyter, notebook, experiment, tutorial, ipynb]
source: openai/skills jupyter-notebook
type: Playbook
---

# Jupyter Notebook Creation

Create clean, reproducible Jupyter notebooks for experiments and tutorials.

## When to use
- Create a new `.ipynb` notebook from scratch
- Convert rough notes or scripts into a structured notebook
- Refactor an existing notebook for reproducibility
- Build experiments or tutorials for others to read/re-run

## Decision tree
- **Exploratory/analytical/hypothesis-driven** → `experiment` template
- **Instructional/step-by-step/audience-specific** → `tutorial` template
- **Editing existing notebook** → refactor: preserve intent, improve structure

## Workflow

### 1. Lock the intent
Identify the notebook kind: `experiment` or `tutorial`.
Capture the objective, audience, and what "done" looks like.

### 2. Scaffold from template
Use the helper script to avoid hand-authoring raw notebook JSON:
```bash
uv run --python 3.12 python new_notebook.py \
  --kind experiment \
  --title "Compare prompt variants" \
  --out output/compare-prompt-variants.ipynb
```

```bash
uv run --python 3.12 python new_notebook.py \
  --kind tutorial \
  --title "Intro to embeddings" \
  --out output/intro-to-embeddings.ipynb
```

### 3. Fill with small, runnable steps
- Keep each code cell focused on one step
- Add short markdown cells explaining purpose and expected result
- Avoid large, noisy outputs when a short summary works

### 4. Edit safely
- Preserve notebook structure; avoid reordering cells unless it improves the story
- Prefer targeted edits over full rewrites
- If editing raw JSON, review notebook structure docs first

### 5. Validate
- Run the notebook top-to-bottom when the environment allows
- If execution isn't possible, say so explicitly and call out how to validate locally

## Templates
- **Experiment**: Hypothesis → Data → Analysis → Conclusion
- **Tutorial**: Concept → Example → Exercise → Summary

## Dependencies (install only when needed)
```bash
uv pip install jupyterlab ipykernel
```

## Temp and output conventions
- Use `tmp/jupyter-notebook/` for intermediate files; delete when done
- Write final artifacts under `output/jupyter-notebook/`
- Use stable, descriptive filenames (e.g., `ablation-temperature.ipynb`)
