#!/usr/bin/env python3
"""Apply reviewed transition records to the canonical Architectonic skills ledger.

Transition files are immutable instructions and evidence. `operations/ledger.json`
remains the only current-work authority. Applied transition IDs are recorded in the
ledger so reruns are idempotent.
"""
from __future__ import annotations

from argparse import ArgumentParser
from copy import deepcopy
from pathlib import Path
from typing import Any
import json

ROOT = Path(__file__).resolve().parent.parent
LEDGER_PATH = ROOT / "operations" / "ledger.json"
TRANSITIONS_DIR = ROOT / "operations" / "ledger-transitions"
ALLOWED_STATUSES = {"ready", "blocked", "in_progress", "done", "cancelled"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(payload, dict), f"{path.relative_to(ROOT)} must contain an object")
    return payload


def transition_files() -> list[Path]:
    if not TRANSITIONS_DIR.exists():
        return []
    return sorted(TRANSITIONS_DIR.glob("*.json"))


def item_map(ledger: dict[str, Any]) -> dict[str, dict[str, Any]]:
    items = ledger.get("items")
    require(isinstance(items, list), "ledger items must be a list")
    mapped: dict[str, dict[str, Any]] = {}
    for item in items:
        require(isinstance(item, dict), "every ledger item must be an object")
        item_id = str(item.get("id") or "")
        require(item_id, "every ledger item requires an id")
        require(item_id not in mapped, f"duplicate ledger item id: {item_id}")
        mapped[item_id] = item
    return mapped


def validate_ledger(ledger: dict[str, Any]) -> None:
    require(ledger.get("schema") == "architectonic-rail", "ledger schema must be architectonic-rail")
    require(ledger.get("schema_version") == "0.3", "ledger schema_version must be 0.3")
    mapped = item_map(ledger)
    for item_id, item in mapped.items():
        status = str(item.get("status") or "")
        require(status in ALLOWED_STATUSES, f"{item_id} has unsupported status {status!r}")
        dependencies = item.get("dependencies") or []
        require(isinstance(dependencies, list), f"{item_id} dependencies must be a list")
        for dependency in dependencies:
            require(str(dependency) in mapped, f"{item_id} depends on missing item {dependency}")
        evidence = item.get("evidence") or []
        require(isinstance(evidence, list), f"{item_id} evidence must be a list")
        sources = item.get("sources") or []
        require(isinstance(sources, list), f"{item_id} sources must be a list")
        artifacts = item.get("artifacts") or []
        require(isinstance(artifacts, list), f"{item_id} artifacts must be a list")


def apply_set(item: dict[str, Any], values: dict[str, Any]) -> None:
    require(isinstance(values, dict), "transition set payload must be an object")
    for key, value in values.items():
        if key == "extensions":
            require(isinstance(value, dict), "extensions transition value must be an object")
            extensions = item.setdefault("extensions", {})
            require(isinstance(extensions, dict), "ledger item extensions must be an object")
            extensions.update(deepcopy(value))
            continue
        item[key] = deepcopy(value)


def apply_transition(
    ledger: dict[str, Any],
    transition: dict[str, Any],
    source_path: Path,
) -> bool:
    source_name = source_path.relative_to(ROOT).as_posix()
    require(transition.get("schema_version") == "0.1", f"{source_name} schema_version must be 0.1")
    require(transition.get("ledger_id") == ledger.get("id"), f"{source_name} ledger_id mismatch")
    transition_id = str(transition.get("transition_id") or "")
    require(transition_id, f"{source_name} requires transition_id")

    extensions = ledger.setdefault("extensions", {})
    require(isinstance(extensions, dict), "ledger extensions must be an object")
    applied = extensions.setdefault("applied_transition_ids", [])
    require(isinstance(applied, list), "applied_transition_ids must be a list")
    if transition_id in applied:
        return False

    mapped = item_map(ledger)
    updates = transition.get("updates") or []
    require(isinstance(updates, list), f"{source_name} updates must be a list")
    for update in updates:
        require(isinstance(update, dict), f"{source_name} update must be an object")
        item_id = str(update.get("id") or "")
        require(item_id in mapped, f"{source_name} update references missing item {item_id!r}")
        item = mapped[item_id]
        expected_status = update.get("expect_status")
        if expected_status is not None:
            require(
                item.get("status") == expected_status,
                f"{source_name} expected {item_id} status {expected_status!r}, got {item.get('status')!r}",
            )
        apply_set(item, update.get("set") or {})

    append_items = transition.get("append_items") or []
    require(isinstance(append_items, list), f"{source_name} append_items must be a list")
    items = ledger["items"]
    for new_item in append_items:
        require(isinstance(new_item, dict), f"{source_name} appended item must be an object")
        item_id = str(new_item.get("id") or "")
        require(item_id, f"{source_name} appended item requires id")
        require(item_id not in mapped, f"{source_name} would duplicate ledger item {item_id}")
        copied = deepcopy(new_item)
        items.append(copied)
        mapped[item_id] = copied

    recorded_at = str(transition.get("recorded_at") or "")
    require(recorded_at, f"{source_name} requires recorded_at")
    ledger["updated_at"] = recorded_at
    applied.append(transition_id)
    transition_records = extensions.setdefault("transition_records", [])
    require(isinstance(transition_records, list), "transition_records must be a list")
    transition_records.append(
        {
            "transition_id": transition_id,
            "source": source_name,
            "recorded_at": recorded_at,
        }
    )
    return True


def render(ledger: dict[str, Any]) -> str:
    return json.dumps(ledger, indent=2, ensure_ascii=False) + "\n"


def transitioned_ledger() -> tuple[dict[str, Any], int]:
    ledger = load_json(LEDGER_PATH)
    validate_ledger(ledger)
    applied_count = 0
    for path in transition_files():
        transition = load_json(path)
        if apply_transition(ledger, transition, path):
            applied_count += 1
    validate_ledger(ledger)
    return ledger, applied_count


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write the transitioned canonical ledger")
    args = parser.parse_args()

    ledger, applied_count = transitioned_ledger()
    expected = render(ledger)
    current = LEDGER_PATH.read_text(encoding="utf-8")

    if args.write:
        if current != expected:
            LEDGER_PATH.write_text(expected, encoding="utf-8")
            print(f"Applied {applied_count} ledger transition(s)")
        else:
            print("Canonical ledger already reflects all transitions")
        return 0

    require(current == expected, "canonical ledger does not reflect all transition files")
    print("Canonical ledger transition parity passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
