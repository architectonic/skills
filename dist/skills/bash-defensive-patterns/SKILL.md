---
name: Bash Defensive Patterns
description: Master defensive Bash programming techniques for production-grade scripts. Use when writing robust shell scripts, CI/CD pipelines, or system utilities requiring fault tolerance and safety.
source: SWE-Skills-Bench (SWE-Skills-Bench/skills/bash-defensive-patterns/SKILL.md)
license: MIT
tags: [agent-operations, bash, shell, scripting, defensive-programming, ci-cd, reliability]
type: Playbook
---

# Bash Defensive Patterns

Production-ready Bash scripts using defensive programming techniques, error handling, and safety best practices.

## When to Use This Skill

- Writing production automation scripts
- Building CI/CD pipeline scripts
- Creating system administration utilities
- Developing error-resilient deployment automation
- Writing scripts that must handle edge cases safely

## Core Defensive Principles

### 1. Strict Mode

```bash
#!/bin/bash
set -Eeuo pipefail  # Exit on error, unset variables, pipe failures
```

- `set -E`: Inherit ERR trap in functions
- `set -e`: Exit on any error
- `set -u`: Exit on undefined variable reference
- `set -o pipefail`: Pipe fails if any command fails

### 2. Error Trapping and Cleanup

```bash
trap 'echo "Error on line $LINENO"' ERR
trap 'echo "Cleaning up..."; rm -rf "$TMPDIR"' EXIT
TMPDIR=$(mktemp -d)
```

### 3. Variable Safety

```bash
# Always quote variables
cp "$source" "$dest"

# Required variables - fail with message if unset
: "${REQUIRED_VAR:?REQUIRED_VAR is not set}"
```

### 4. Conditional Safety

```bash
# Bash - safer
if [[ -f "$file" && -r "$file" ]]; then
    content=$(<"$file")
fi

# POSIX - portable
if [ -f "$file" ] && [ -r "$file" ]; then
    content=$(cat "$file")
fi
```

## Key Patterns

### Safe Script Directory Detection

```bash
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
SCRIPT_NAME="$(basename -- "${BASH_SOURCE[0]}")"
```

### Safe Temporary File Handling

```bash
trap 'rm -rf -- "$TMPDIR"' EXIT
TMPDIR=$(mktemp -d) || { echo "ERROR: Failed to create temp directory" >&2; exit 1; }
```

### Robust Argument Parsing

```bash
VERBOSE=false
DRY_RUN=false
OUTPUT_FILE=""

usage() {
    cat <<EOF
Usage: $0 [OPTIONS]
Options:
    -v, --verbose       Enable verbose output
    -d, --dry-run       Run without making changes
    -o, --output FILE   Output file path
    -h, --help          Show this help message
EOF
    exit "${1:-0}"
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        -v|--verbose) VERBOSE=true; shift ;;
        -d|--dry-run) DRY_RUN=true; shift ;;
        -o|--output) OUTPUT_FILE="$2"; shift 2 ;;
        -h|--help) usage 0 ;;
        *) echo "ERROR: Unknown option: $1" >&2; usage 1 ;;
    esac
done

[[ -n "$OUTPUT_FILE" ]] || { echo "ERROR: -o/--output is required" >&2; usage 1; }
```

### Structured Logging

```bash
log_info()  { echo "[$(date +'%Y-%m-%d %H:%M:%S')] INFO: $*" >&2; }
log_warn()  { echo "[$(date +'%Y-%m-%d %H:%M:%S')] WARN: $*" >&2; }
log_error() { echo "[$(date +'%Y-%m-%d %H:%M:%S')] ERROR: $*" >&2; }
log_debug() { [[ "${DEBUG:-0}" == "1" ]] && echo "[$(date +'%Y-%m-%d %H:%M:%S')] DEBUG: $*" >&2; }
```

### Process Orchestration with Signals

```bash
PIDS=()
cleanup() {
    log_info "Shutting down..."
    for pid in "${PIDS[@]}"; do
        kill -TERM "$pid" 2>/dev/null || true
    done
    for pid in "${PIDS[@]}"; do
        wait "$pid" 2>/dev/null || true
    done
}
trap cleanup SIGTERM SIGINT

background_task &
PIDS+=($!)
```

### Atomic File Writes

```bash
atomic_write() {
    local -r target="$1"
    local tmpfile
    tmpfile=$(mktemp) || return 1
    cat > "$tmpfile"
    mv "$tmpfile" "$target"
}
```

### Idempotent Script Design

```bash
ensure_directory() {
    local -r dir="$1"
    if [[ -d "$dir" ]]; then
        log_info "Directory already exists: $dir"
        return 0
    fi
    mkdir -p "$dir" || { log_error "Failed to create directory: $dir"; return 1; }
}
```

### Dry-Run Support

```bash
DRY_RUN="${DRY_RUN:-false}"
run_cmd() {
    if [[ "$DRY_RUN" == "true" ]]; then
        echo "[DRY RUN] Would execute: $*"
        return 0
    fi
    "$@"
}
```

### Dependency Checking

```bash
check_dependencies() {
    local -a missing_deps=()
    local -a required=("jq" "curl" "git")
    for cmd in "${required[@]}"; do
        if ! command -v "$cmd" &>/dev/null; then
            missing_deps+=("$cmd")
        fi
    done
    if [[ ${#missing_deps[@]} -gt 0 ]]; then
        echo "ERROR: Missing required commands: ${missing_deps[*]}" >&2
        return 1
    fi
}
```

## Best Practices Summary

1. **Always use strict mode** — `set -Eeuo pipefail`
2. **Quote all variables** — `"$variable"` prevents word splitting
3. **Use `[[]] conditionals** — More robust than `[ ]`
4. **Implement error trapping** — Catch and handle errors gracefully
5. **Validate all inputs** — Check file existence, permissions, formats
6. **Use functions for reusability** — Prefix with meaningful names
7. **Implement structured logging** — Include timestamps and levels
8. **Support dry-run mode** — Allow users to preview changes
9. **Handle temporary files safely** — Use mktemp, cleanup with trap
10. **Design for idempotency** — Scripts should be safe to rerun
11. **Use `command -v`** — Safer than `which` for checking executables
12. **Prefer printf over echo** — More predictable across systems

## Resources

- **Bash Strict Mode**: http://redsymbol.net/articles/unofficial-bash-strict-mode/
- **Google Shell Style Guide**: https://google.github.io/styleguide/shellguide.html
