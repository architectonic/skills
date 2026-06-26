---
name: screenshot-automation
description: Capture desktop, window, application, or pixel-region screenshots across macOS, Linux, and Windows. Use when the user explicitly asks for screenshots, for visual inspection of desktop apps, or when tool-specific capture capabilities are unavailable.
tags: [creative, screenshot, desktop, automation, cross-platform]
source: openai/skills screenshot
type: Playbook
---

# Screenshot Automation

Capture desktop, window, application, or pixel-region screenshots across macOS, Linux, and Windows.

## When to use
- User explicitly asks for a desktop/system screenshot
- Visual inspection of desktop apps
- Tool-specific capture capabilities (Figma MCP, Playwright, browser tools) are unavailable
- Pixel-region captures for documentation or bug reports

## Tool priority
1. Prefer tool-specific screenshot capabilities when available (Figma MCP for Figma files, Playwright/agent-browser for browsers/Electron apps)
2. Use this skill for whole-system desktop captures or when tool-specific capture cannot get what you need
3. Default for desktop apps without a better-integrated capture tool

## Save-location rules
1. If the user specifies a path → save there
2. If no path specified → save to OS default screenshot location
3. If for agent inspection → save to temp directory

## macOS

### Permission preflight
```bash
bash <path-to-skill>/scripts/ensure_macos_permissions.sh
```

### Capture via Python helper
```bash
python3 <path-to-skill>/scripts/take_screenshot.py [options]
```

Common patterns:
```bash
# Default location
python3 take_screenshot.py

# Temp location (agent inspection)
python3 take_screenshot.py --mode temp

# Explicit path
python3 take_screenshot.py --path output/screen.png

# App/window capture (substring match)
python3 take_screenshot.py --app "Safari"

# Specific window title
python3 take_screenshot.py --app "Safari" --window-name "Settings"

# Pixel region (x,y,w,h)
python3 take_screenshot.py --mode temp --region 100,200,800,600

# Focused/active window
python3 take_screenshot.py --mode temp --active-window

# List window IDs first
python3 take_screenshot.py --list-windows --app "Safari"
```

### Direct macOS commands (fallbacks)
```bash
# Full screen
screencapture -x output/screen.png

# Pixel region
screencapture -x -R100,200,800,600 output/region.png

# Specific window
screencapture -x -l12345 output/window.png

# Interactive selection
screencapture -x -i output/interactive.png
```

## Linux

### Python helper (auto-detects available tool)
```bash
python3 take_screenshot.py
```

Selection order: `scrot` → `gnome-screenshot` → ImageMagick `import`

### Direct Linux commands
```bash
# Full screen
scrot output/screen.png
gnome-screenshot -f output/screen.png
import -window root output/screen.png

# Pixel region
scrot -a 100,200,800,600 output/region.png

# Active window
scrot -u output/window.png
```

## Windows

### PowerShell helper
```powershell
powershell -ExecutionPolicy Bypass -File <path-to-skill>/scripts/take_screenshot.ps1
```

Common patterns:
```powershell
# Default location
powershell -ExecutionPolicy Bypass -File take_screenshot.ps1

# Temp location
powershell -ExecutionPolicy Bypass -File take_screenshot.ps1 -Mode temp

# Explicit path
powershell -ExecutionPolicy Bypass -File take_screenshot.ps1 -Path "C:\Temp\screen.png"

# Pixel region
powershell -ExecutionPolicy Bypass -File take_screenshot.ps1 -Mode temp -Region 100,200,800,600

# Active window
powershell -ExecutionPolicy Bypass -File take_screenshot.ps1 -Mode temp -ActiveWindow
```

## Multi-display behavior
- **macOS**: Full-screen captures save one file per display
- **Linux/Windows**: Full-screen captures use the virtual desktop (all monitors in one image); use `--region` to isolate a single display

## Error handling
- **macOS**: Run permission preflight first; if "screen capture checks are blocked in sandbox", rerun with escalated permissions
- **Linux**: Check tool availability with `command -v scrot`, `command -v gnome-screenshot`, `command -v import`
- **Windows**: Ensure PowerShell execution policy allows script execution
- Always report the saved file path in the response
