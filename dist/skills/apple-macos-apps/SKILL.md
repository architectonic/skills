---
name: apple-macos-apps
description: Operate Apple user-facing macOS apps from the terminal or GUI bridge — Notes, Reminders, Messages, Find My, and adjacent app-specific automation.
type: Playbook
---

# apple-macos-apps
# Apple macOS Apps

Use this umbrella when the user wants Hermes to act on Apple-first personal apps rather than generic cross-platform tools.

## Scope

This class covers:
- **Notes** — create, search, edit, move, export notes
- **Reminders** — add tasks, due dates, alarms, list management
- **Messages / SMS** — inspect chats and send messages with the local Messages.app account
- **Find My** — locate Apple devices and AirTags through app automation / screenshots

Keep **macos-computer-use** separate as the general desktop-driving skill; load it when GUI automation is needed beyond the app-specific recipes here.

## Selection guide

- User says "put this in Notes" or "search my Apple Notes" → Notes section
- User wants a task to land on iPhone/iPad Reminders → Reminders section
- User wants a local iMessage/SMS sent from their Mac identity → Messages section
- User asks where a device, keys, bag, or AirTag is → Find My section

## Shared prerequisites

- macOS host with the target Apple app signed in and usable manually
- Expect privacy/automation prompts the first time a CLI or GUI automation path is used
- Prefer native app-specific CLIs when they exist; fall back to GUI automation when no robust CLI exists

## Notes

Preferred tool: `memo`
- Install: `brew tap antoniorodr/memo && brew install antoniorodr/memo/memo`
- Typical actions: list/search notes, create a note, edit, move, export
- Use when the user wants Apple Notes specifically, not generic note-taking

## Reminders

Preferred tool: `remindctl`
- Install: `brew install steipete/tap/remindctl`
- Distinguish **due time** from **alarm time**; set `--alarm` explicitly for early nudges
- Use this when the reminder should sync to the user's Apple devices, not when the user wants a Hermes cron alert

## Messages / SMS

Preferred tool: `imsg`
- Install: `brew install steipete/tap/imsg`
- Requires Full Disk Access + Messages permissions
- Good for listing chats, reading history, sending a targeted message, optionally with attachment
- Not for bulk messaging or group-chat administration

## Find My

No stable first-party CLI; use app activation + screenshot / GUI automation
- Open Find My with AppleScript
- Capture the app state with screenshot or GUI automation
- Use vision analysis to read locations from the rendered app
- Prefer a dedicated GUI automation helper when installed; otherwise use screenshot-based inspection

## Operating rules

1. Confirm the user really means the Apple-native app, not a generic category (for example, Apple Reminders vs agent reminders).
2. Prefer narrow native CLIs over raw desktop automation.
3. When there is no good CLI, treat the app as a GUI workflow: activate, navigate, capture, verify.
4. Report concrete outcomes: note title created, reminder list + due time, recipient + send result, device/item location read from Find My.
5. If running on non-macOS, stop immediately and state the platform blocker.

## Pitfalls

- These skills are platform-specific; do not route them on Windows/Linux.
- Notes/Reminders/Messages can fail due to OS permission prompts rather than tool bugs.
- Find My output is visual state, not structured API data; always verify from the captured screen.
- "Remind me" often means a scheduled agent alert, not Apple Reminders — use context.
