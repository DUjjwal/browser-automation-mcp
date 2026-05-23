# 🤖 AI-Powered Browser Automation MCP Server
A **Model Context Protocol (MCP) server** built with Python and Playwright that exposes browser automation capabilities as structured tools for AI agents and LLMs. Enables AI systems to navigate, interact with, and extract structured data from live web pages in real time.

## 🚀 Tech Stack
**Python**, **Playwright (async)**, **FastMCP**, **Pydantic**
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
 
