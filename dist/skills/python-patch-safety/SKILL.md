---
name: python-patch-safety
description: Safe editing of Python files — patch discipline, git rollback checkpoints, py_compile verification. Prevents accidental function loss, stale checkouts, and uncommitted work destruction.
type: Playbook
---

# python-patch-safety
# Python File Safety

## The `patch` Tool Is Dangerous on Python

The `patch` tool's `replace` mode uses fuzzy matching. When editing near Python function definitions (`def foo():`), it can:
- Match the wrong indentation level
- Merge with an adjacent function's body
- Remove the `def` line entirely while keeping the body
- Leave orphaned code blocks that cause `NameError` at runtime

**The patch tool is BANNED for structural Python edits** (adding/removing functions, editing near `def` lines, changing indents). It is safe for JSON, YAML, CSS, and other non-indentation-sensitive formats.

For Python structural edits, use `write_file` or an `execute_code` Python script that does exact string replacement.

## py_compile Is Blocking

After ANY edit to a `.py` file — patch, write_file, execute_code — run:

```
python3 -c "import py_compile; compile('<file.py>', doraise=True)"
```

Do not proceed to the next action until py_compile passes.

## Git Rollback Checkpoints

Before `git checkout HEAD -- <file>`:

1. **Check what you'll erase:** `git diff HEAD -- <file>`
   If the diff shows work from THIS session, DO NOT checkout. Find the specific change to roll back instead.

2. **Check commit age:** `git log -1 --format="%ar" -- <file>`
   "2 hours old" = you're erasing 2 hours of work. Roll back selectively.

3. **Save before destroy:** `git diff HEAD -- <file> > /tmp/save.patch`
   Restore selectively later with `git apply /tmp/save.patch`.

## Commit Discipline

- Commit every slice: `git add -A && git commit -m "<what changed>"`
- After model switches: `git status` + `git diff HEAD` FIRST
- Before any rollback: `git diff HEAD` — know what you're throwing away
- Checkout orphans immediately: if `git status` shows `??` files from old model runs, `git clean -fd` or commit them

## Recovery

If you accidentally removed a Python function:
1. Save current broken state: `git diff HEAD -- <file> > /tmp/broken.patch`
2. Restore: `git checkout HEAD -- <file>`
3. Re-apply using `write_file` with correct content
4. Verify: py_compile

## References

- `references/python-edit-checklist.md` — full pre-flight checklist
- `references/git-rollback-patterns.md` — git recovery recipes
