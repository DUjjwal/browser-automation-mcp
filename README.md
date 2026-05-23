# 🤖 AI-Powered Browser Automation MCP Server
A **Model Context Protocol (MCP) server** built with Python and Playwright that exposes browser automation capabilities as structured tools for AI agents and LLMs. Enables AI systems to navigate, interact with, and extract structured data from live web pages in real time.
 - -
## 🚀 Tech Stack
| Technology | Purpose |
| - -| - -|
| **Python** | Core language |
| **Playwright (async)** | Browser automation engine |
| **FastMCP** | MCP server framework |
| **Pydantic** | Data validation & modeling |
| **Chromium / Chrome** | Browser runtime |
| **ARIA Accessibility API** | Semantic element targeting |
 - -
## ✨ Features
- 🌐 **Page Management** - Open, reload, navigate, close browser pages with unique session IDs
- ✍️ **Smart Fill** - Fill input fields by text, label, placeholder, title, or ARIA role
- 🖱️ **Smart Click** - Single/double click elements by text, label, placeholder, title, role, or (x, y) coordinates
- ☑️ **Checkbox & Radio** - Check/uncheck elements by text, label, title, or ARIA role
- 📋 **Select Dropdowns** - Select options in `<select>` elements by text, label, placeholder, title, or role
- ⌨️ **Keyboard Input** - Simulate key presses and keyboard shortcuts
- 📜 **Scroll** - Scroll pages horizontally and vertically
- 🔍 **Page Summarizer** - Token-efficient structured page summary for LLM context, capturing:
 - Headings, Buttons, Links, Inputs, Checkboxes
 - Interactive widgets (tabs, menus, sliders, tree items)
 - Dialogs, Alerts, Forms, and Text Preview
 - -
## 🛠️ Installation
### Prerequisites
- Python 3.9+
- Google Chrome installed
### Setup
```bash
# Clone the repository
git clone <your-repo-url>
cd browser-automation-mcp
# Install dependencies
pip install mcp[cli] playwright pydantic
# Install Playwright browsers
playwright install chrome
```
 - -
## ▶️ Usage
### Run the MCP Server
```bash
python script.py
```
### Connect to Claude Desktop / Any MCP Client
Add to your MCP client config (e.g., `claude_desktop_config.json`):
```json
{
 "mcpServers": {
 "BrowserAutomation": {
 "command": "python",
 "args": ["/path/to/script.py"]
 }
 }
}
```
 - -
## 🧰 Available Tools
### Page Navigation
| Tool | Description |
| - -| - -|
| `open_page(url)` | Opens a URL and returns a `pageId` |
| `navigate_to(pageId, url)` | Navigate existing page to new URL |
| `reload_page(pageId)` | Reload the page |
| `previous_page(pageId)` | Go back in history |
| `next_page(pageId)` | Go forward in history |
| `close_page(pageId)` | Close the page |
| `scroll_screen(pageId, deltaX, deltaY)` | Scroll the page |
### Fill Input Fields
| Tool | Description |
| - -| - -|
| `fill_by_text` | Fill by visible text |
| `fill_by_label` | Fill by label text |
| `fill_by_placeholder` | Fill by placeholder |
| `fill_by_title` | Fill by title attribute |
| `fill_by_role` | Fill by ARIA role + optional name |
### Click Elements
| Tool | Description |
| - -| - -|
| `click_by_text` | Click by visible text |
| `click_by_label` | Click by label |
| `click_by_placeholder` | Click by placeholder |
| `click_by_title` | Click by title attribute |
| `click_by_role` | Click by ARIA role + optional name |
| `click_by_x_y` | Click at pixel coordinates |
### Checkboxes & Selects
| Tool | Description |
| - -| - -|
| `select_checked_by_*` | Check/uncheck by text, label, title, role |
| `select_option_by_*` | Select dropdown options by text, label, placeholder, title, role |
### Utilities
| Tool | Description |
| - -| - -|
| `key_press(pageId, keys)` | Simulate keyboard input |
| `get_page_summary_tool(pageId)` | Get structured LLM-friendly page summary |
 - -
## 📊 Page Summary Output
The `get_page_summary_tool` returns a structured JSON with:
```json
{
 "meta": { "url": "…", "title": "…" },
 "headings": […],
 "buttons": […],
 "links": […],
 "inputs": […],
 "checkboxes": […],
 "interactives": […],
 "dialogs": […],
 "alerts": […],
 "forms": […],
 "textPreview": "…",
 "counts": { "buttons": 3, "inputs": 2, … }
}
```
 - -
## 📁 Project Structure
```
.
├── script.py # Main MCP server with all browser automation tools
└── README.md # Project documentation
```
 
