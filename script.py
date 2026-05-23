'from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel


from playwright.async_api import async_playwright
from time import sleep
from typing import Literal, List
import base64

mcp=FastMCP("BrowserAutomation")


class PageId(BaseModel):
    pageId: int

session={}

playwright_instance = None
browser = None

async def get_browser():
    global playwright_instance, browser
    if browser is None:
        playwright_instance = await async_playwright().start()
        browser = await playwright_instance.chromium.launch(
            channel="chrome",
            headless=False,
            slow_mo=500
        )
    return browser


current_id=0

# Open Page Tool

@mcp.tool()
async def open_page(url: str) -> PageId:
    """Opens a web page at the given URL using a Chromium browser.

    Args:
        url (str): The URL of the web page to open.

    Returns:
        PageId: An object containing:
            - pageId (int): A unique identifier for the opened page, used in subsequent operations.
    """
    global current_id, session
    
        

    browser = await get_browser()
    page = await browser.new_page()
    
    await page.goto(url)
    current_id = current_id + 1
    

    session[f'Page{current_id}']=page

    return PageId(pageId=current_id)
    
# Fill Input Field Tools

@mcp.tool()
async def fill_by_text(pageId: int, text: str, fill: str) -> str:
    """Fills an input field on a specific page, identified by its visible text.

    Args:
        pageId (int): The ID of the page to interact with.
        text (str): The visible text used to locate the input element.
        fill (str): The value to type into the input field.
    
    """
    global session
    if f"Page{pageId}" not in session: 
        return "Invalid Page Id"
    
    try:
        page=session.get(f"Page{pageId}")
        await page.get_by_text(text).fill(fill)
        return "succes"
    except Exception as e:
        
        return f"Unable to fill input fi{e}eld"
    
@mcp.tool()
async def fill_by_label(pageId: int, label: str, fill: str) -> str:
    """Fills an input field on a specific page, identified by its associated label text.

    Args:
        pageId (int): The ID of the page to interact with.
        label (str): The label text associated with the input element.
        fill (str): The value to type into the input field.

    """
    global session
    if f"Page{pageId}" not in session: 
        return "Invalid Page Id"
    
    try:
        page=session.get(f"Page{pageId}")
        await page.get_by_label(label).fill(fill)
        return "succes"
    except Exception as e:
        
        return f"Unable to fill input fi{e}eld"

@mcp.tool()
async def fill_by_placeholder(pageId: int, placeholder: str, fill: str) -> str:
    """Fills an input field on a specific page, identified by its placeholder text.

    Args:
        pageId (int): The ID of the page to interact with.
        placeholder (str): The placeholder text of the input element.
        fill (str): The value to type into the input field.

    """
    global session
    if f"Page{pageId}" not in session: 
        return "Invalid Page Id"
    
    try:
        page=session.get(f"Page{pageId}")
        await page.get_by_placeholder(placeholder).fill(fill)
        return "succes"
    except Exception as e:
        
        return f"Unable to fill input fi{e}eld"

@mcp.tool()
async def fill_by_title(pageId: int, title: str, fill: str) -> str:
    """Fills an input field on a specific page, identified by its title attribute.

    Args:
        pageId (int): The ID of the page to interact with.
        title (str): The title attribute value of the input element.
        fill (str): The value to type into the input field.

    """
    global session
    if f"Page{pageId}" not in session: 
        return "Invalid Page Id"
    
    try:
        page=session.get(f"Page{pageId}")
        await page.get_by_title(title).fill(fill)
        return "succes"
    except Exception as e:
        
        return f"Unable to fill input fi{e}eld"

@mcp.tool()
async def fill_by_role(pageId: int, role: str, fill: str, name: str = "") -> str:
    """
    Fill an editable element on a page by locating it using its accessibility role
    and optional accessible name.

    This tool finds an element the way users and assistive technologies perceive it,
    using ARIA role semantics and implicit HTML accessibility roles similar to
    Playwright's `page.get_by_role()`.

    Use this tool when the target is a text-capable or value-editable control that
    can be identified by its role, such as `textbox`, `searchbox`, `combobox`, or
    `spinbutton`. Supplying `name` is strongly recommended when multiple elements
    share the same role, because it helps uniquely identify the intended target by
    its accessible name.

    Parameters:
        pageid (int):
            Identifier of the browser page or session where the element should be found.

        role (str):
            Accessibility role used to locate the target element.

            Allowed role values:
            - alert
            - alertdialog
            - application
            - article
            - banner
            - blockquote
            - button
            - caption
            - cell
            - checkbox
            - code
            - columnheader
            - combobox
            - complementary
            - contentinfo
            - definition
            - deletion
            - dialog
            - directory
            - document
            - emphasis
            - feed
            - figure
            - form
            - generic
            - grid
            - gridcell
            - group
            - heading
            - img
            - insertion
            - link
            - list
            - listbox
            - listitem
            - log
            - main
            - marquee
            - math
            - meter
            - menu
            - menubar
            - menuitem
            - menuitemcheckbox
            - menuitemradio
            - navigation
            - none
            - note
            - option
            - paragraph
            - presentation
            - progressbar
            - radio
            - radiogroup
            - region
            - row
            - rowgroup
            - rowheader
            - scrollbar
            - search
            - searchbox
            - separator
            - slider
            - spinbutton
            - status
            - strong
            - subscript
            - superscript
            - switch
            - tab
            - table
            - tablist
            - tabpanel
            - term
            - textbox
            - time
            - timer
            - toolbar
            - tooltip
            - tree
            - treegrid
            - treeitem

            Important:
            Not all roles represent elements that can accept text input. This tool is
            intended for editable or value-settable controls. The most appropriate roles
            for filling are usually:
            - textbox
            - searchbox
            - combobox
            - spinbutton

            In some applications, filling may also be meaningful for custom widgets that
            behave like editable controls, but roles such as `button`, `link`, `heading`,
            `image`, `list`, or `table` are generally not valid text-fill targets.

        fill (str):
            The text value to enter into the located element.

        name (str | None, optional):
            Accessible name used to narrow the role match to a specific element.
            This is typically the user-facing label announced by assistive technology,
            such as "Email", "Search", or "Age"."""
    global session
    if f"Page{pageId}" not in session: 
        return "Invalid Page Id"
    
    try:
        page=session.get(f"Page{pageId}")
        if name == "":
            await page.get_by_role(role).fill(fill)
        else:
            await page.get_by_role(role, name=name).fill(fill)
        
        return "succes"
    except Exception as e:
        
        return f"Unable to fill input fi{e}eld"

# Click Button &mdash; single click, double click, wheel &mdash; left, right, middle

@mcp.tool()
async def click_by_text(pageId: int, text: str, type: str, button: str = 'left', modifiers: List[str] = []) -> str:
    """Click an input field on a specific page, identified by its visible text.

    Args:
        pageId (int): The ID of the page to interact with.
        text (str): The visible text used to locate the input element.
        type (str): For Single Click - click 
                    For double Click - dblclick
        button (str): left, right, middle button (default=left)
        modifiers Array<"Alt" | "Control" | "ControlOrMeta" | "Meta" | "Shift"> (optional)#

    Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS.
    
    """
    global session
    if f"Page{pageId}" not in session: 
        return "Invalid Page Id"
    
    try:
        page=session[f"Page{pageId}"]
        if type == 'dblclick':
            await page.get_by_text(text).dblclick(modifiers=modifiers, button=button)
        else:
            await page.get_by_text(text).click(modifiers=modifiers, button=button)
        return "success"

    except Exception as e:
        
        return f"Unable to click input f{e}ield"
    
@mcp.tool()
async def click_by_label(pageId: int, label: str, type: str, button: str = 'left', modifiers: List[str] = []) -> str:
    """
    Finds an element by label and performs a single or double click, with optional keyboard modifiers.
    Args:
        pageId (int): The ID of the page to interact with.
        label (str): The visible label used to locate the element.
        type (str): For Single Click &mdash; click 
                    For double Click &mdash; dblclick
        button (str): left, right, middle button (default=left)

        modifiers Array<"Alt" | "Control" | "ControlOrMeta" | "Meta" | "Shift"> (optional)#

    Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS.
    
    """
    global session
    if f"Page{pageId}" not in session: 
        return "Invalid Page Id"
    
    try:
        page=session[f"Page{pageId}"]
        if type == 'dblclick':
            await page.get_by_label(label).dblclick(modifiers=modifiers, button=button)
        else:
            await page.get_by_label(label).click(modifiers=modifiers, button=button)
        return "success"

    except Exception as e:
        
        return f"Unable to click element{e}"

@mcp.tool()
async def click_by_placeholder(pageId: int, placeholder: str, type: str, button: str = 'left', modifiers: List[str] = []) -> str:
    """Clicks an input field on a specific page, identified by its placeholder text.

    Args:
        pageId (int): The ID of the page to interact with.
        placeholder (str): The placeholder text of the input element.
        type (str): For Single Click - click 
                    For double Click - dblclick
        button (str): left, right, middle button (default=left)

        modifiers Array<"Alt" | "Control" | "ControlOrMeta" | "Meta" | "Shift"> (optional)#

    Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS.
    
    """
    global session
    if f"Page{pageId}" not in session: 
        return "Invalid Page Id"
    
    try:
        page=session[f"Page{pageId}"]
        if type == 'dblclick':
            await page.get_by_placeholder(placeholder).dblclick(modifiers=modifiers, button=button)
        else:
            await page.get_by_placeholder(placeholder).click(modifiers=modifiers, button=button)
        return "success"

    except Exception as e:
        
        return f"Unable to click element{e}"

@mcp.tool()
async def click_by_title(pageId: int, title: str, type: str, button: str = 'left', modifiers: List[str] = []) -> str:
    """Clicks an element on a specific page, identified by its title attribute.

    Args:
        pageId (int): The ID of the page to interact with.
        title (str): The title attribute value of the element.
        type (str): For Single Click - click 
                    For double Click - dblclick
        button (str): left, right, middle button (default=left)
        modifiers Array<"Alt" | "Control" | "ControlOrMeta" | "Meta" | "Shift"> (optional)#

    Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS.
    
    """
    global session
    if f"Page{pageId}" not in session: 
        return "Invalid Page Id"
    
    try:
        page=session[f"Page{pageId}"]
        if type == 'dblclick':
            await page.get_by_title(title).dblclick(modifiers=modifiers, button=button)
        else:
            await page.get_by_title(title).click(modifiers=modifiers, button=button)
        return "success"
    except Exception as e:
        
        return f"Unable to click element{e}"

@mcp.tool()
async def click_by_role(pageId: int, role: str, type: str, button:str='left', modifiers: List[str] = [], name: str = "") -> str:
    """
    Click an element on a page by locating it using its accessibility role
    and optional accessible name.

    This tool finds an element the way users and assistive technologies perceive it,
    using ARIA role semantics and implicit HTML accessibility roles similar to
    Playwright's `page.get_by_role()`.

    Use this tool when the target is a text-capable or value-editable control that
    can be identified by its role, such as `textbox`, `searchbox`, `combobox`, or
    `spinbutton`. Supplying `name` is strongly recommended when multiple elements
    share the same role, because it helps uniquely identify the intended target by
    its accessible name.

    Parameters:
        pageid (int):
            Identifier of the browser page or session where the element should be found.

        role (str):
            Accessibility role used to locate the target element.

            Allowed role values:
            - alert
            - alertdialog
            - application
            - article
            - banner
            - blockquote
            - button
            - caption
            - cell
            - checkbox
            - code
            - columnheader
            - combobox
            - complementary
            - contentinfo
            - definition
            - deletion
            - dialog
            - directory
            - document
            - emphasis
            - feed
            - figure
            - form
            - generic
            - grid
            - gridcell
            - group
            - heading
            - img
            - insertion
            - link
            - list
            - listbox
            - listitem
            - log
            - main
            - marquee
            - math
            - meter
            - menu
            - menubar
            - menuitem
            - menuitemcheckbox
            - menuitemradio
            - navigation
            - none
            - note
            - option
            - paragraph
            - presentation
            - progressbar
            - radio
            - radiogroup
            - region
            - row
            - rowgroup
            - rowheader
            - scrollbar
            - search
            - searchbox
            - separator
            - slider
            - spinbutton
            - status
            - strong
            - subscript
            - superscript
            - switch
            - tab
            - table
            - tablist
            - tabpanel
            - term
            - textbox
            - time
            - timer
            - toolbar
            - tooltip
            - tree
            - treegrid
            - treeitem

            Important:
            Not all roles represent elements that can accept text input. This tool is
            intended for editable or value-settable controls. The most appropriate roles
            for filling are usually:
            - textbox
            - searchbox
            - combobox
            - spinbutton

            In some applications, filling may also be meaningful for custom widgets that
            behave like editable controls, but roles such as `button`, `link`, `heading`,
            `image`, `list`, or `table` are generally not valid text-fill targets.

        

        name (str | None, optional):
            Accessible name used to narrow the role match to a specific element.
            This is typically the user-facing label announced by assistive technology,
            such as "Email", "Search", or "Age".
            
        type (str): For Single Click - click 
                    For double Click - dblclick
        button (str): left, right, middle button (default=left)

        modifiers Array<"Alt" | "Control" | "ControlOrMeta" | "Meta" | "Shift"> (optional)#

        Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS.
            """
    
    global session
    if f"Page{pageId}" not in session: 
        return "Invalid Page Id"
    
    try:
        page=session.get(f"Page{pageId}")
        if name == "":
            if type == 'dblclick':
                await page.get_by_role(role).dblclick(modifiers=modifiers, button=button)
            else:
                await page.get_by_role(role).click(modifiers=modifiers, button=button)
        else:
            if type == 'dblclick':
                await page.get_by_role(role, name=name).dblclick(modifiers=modifiers, button=button)
            else:
                await page.get_by_role(role, name=name).click(modifiers=modifiers, button=button)
        
        return "succes"
    except Exception as e:
        
        return f"Unable to click element{e}"

@mcp.tool()
async def click_by_x_y(pageId: int, x: float, y: float, type: str, button:str = 'left', modifiers: List[str] = []) -> str:
    """
    Clicks at a specific (x, y) pixel coordinate on the page.


    Args:
        pageId (int): The ID of the page to interact with.
        x (float): X coordinate relative to the main frame's viewport in CSS pixels.
        y (float): Y coordinate relative to the main frame's viewport in CSS pixels.
        
        type (str): For Single Click - click 
                    For double Click - dblclick
        button (str): left, right, middle button (default=left)
        modifiers Array<"Alt" | "Control" | "ControlOrMeta" | "Meta" | "Shift"> (optional)#

    Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS.
    
    """
    global session
    if f"Page{pageId}" not in session: 
        return "Invalid Page Id"
    
    try:
        page=session[f"Page{pageId}"]
        if type == 'dblclick':
            await page.mouse.dblclick(x,y,button=type, modifiers=modifiers)
        else:
            await page.mouse.click(x,y,button=type, modifiers=modifiers)
        return "success"
    except Exception as e:
        
        return f"Unable to click element{e}"



async def get_page_summary(page) -> dict:
    """
    Returns a compact, structured, token-efficient page summary designed for LLM usage.

    The summary is specifically built to support Playwright locator strategies:
        - get_by_text(...)
        - get_by_placeholder(...)
        - get_by_title(...)
        - get_by_label(...)
        - get_by_role(...)

    All data is extracted in a single browser-side `page.evaluate()` call for
    maximum efficiency. Both in-viewport and off-screen (but rendered) interactive
    elements are included. Lists are capped to avoid token explosion. Text fields
    are truncated.

    Args:
        page: A Playwright async Page object.

    Returns:
        dict: A JSON-serialisable summary with the following top-level keys:
            - meta         : url, title
            - headings     : list of heading elements
            - buttons      : list of button/submit elements
            - links        : list of anchor elements
            - inputs       : list of input/textarea/select elements (with value & options)
            - checkboxes   : list of checkbox/radio/switch elements (with checked state)
            - interactives : list of tabs, menu items, sliders, tree items, list options
            - dialogs      : list of dialog/alertdialog elements
            - alerts       : list of alert/status elements
            - forms        : list of form elements with compact field list
            - textPreview  : first ~300 chars of visible body text
            - counts       : element counts per category

    Example output:
        {
            "meta": {"url": "https://example.com/login", "title": "Login"},
            "headings": [{"text": "Sign In", "role": "heading", "title": ""}],
            "buttons": [{
                "tag": "button", "type": "submit", "role": "button",
                "text": "Login", "name": "Login", "label": "",
                "placeholder": "", "title": "Submit form",
                "ariaLabel": "", "id": "btn-login", "nameAttr": "",
                "testId": "", "disabled": false
            }],
            "links": [{
                "tag": "a", "role": "link", "text": "Forgot password?",
                "name": "Forgot password?", "title": "", "ariaLabel": "",
                "href": "/forgot"
            }],
            "inputs": [{
                "tag": "input", "type": "email", "role": "textbox",
                "text": "", "name": "Email", "label": "Email",
                "placeholder": "Enter your email", "title": "",
                "ariaLabel": "", "id": "email", "nameAttr": "email",
                "testId": "", "value": "", "required": true, "disabled": false,
                "options": []
            }],
            "checkboxes": [{
                "tag": "input", "type": "checkbox", "role": "checkbox",
                "name": "Remember me", "label": "Remember me",
                "title": "", "ariaLabel": "", "id": "remember",
                "nameAttr": "remember", "testId": "",
                "checked": false, "disabled": false
            }],
            "interactives": [{
                "tag": "div", "role": "tab", "text": "Settings",
                "name": "Settings", "label": "", "title": "",
                "ariaLabel": "", "id": "tab-settings", "testId": "",
                "selected": false, "expanded": null, "disabled": false
            }],
            "dialogs": [],
            "alerts": [],
            "forms": [{"action": "/login", "method": "post", "fields": ["email","password"]}],
            "textPreview": "Sign In  Welcome back! Please enter your credentials...",
            "counts": {
                "headings": 1, "buttons": 1, "links": 1, "inputs": 2,
                "checkboxes": 1, "interactives": 3,
                "dialogs": 0, "alerts": 0, "forms": 1
            }
        }
    """
    try:
        summary = await page.evaluate("""
        () => {
            const TRUNC = 80;
            const LIST_LIMIT = 50;
            const HEADING_LIMIT = 20;
            const DIALOG_LIMIT = 10;
            const FORM_LIMIT = 10;
            const TEXT_PREVIEW_LEN = 300;
            const OPTIONS_LIMIT = 30;

            // ── Helpers ──────────────────────────────────────────────────────

            function cleanText(el) {
                if (!el) return "";
                const t = (el.innerText || el.textContent || "").replace(/\\s+/g, " ").trim();
                return t.length > TRUNC ? t.slice(0, TRUNC) + "…" : t;
            }

            function truncate(str, len) {
                if (!str) return "";
                str = str.trim();
                return str.length > len ? str.slice(0, len) + "…" : str;
            }

            // Checks that the element is rendered (not display:none / visibility:hidden / opacity:0)
            // but does NOT require it to be inside the current viewport scroll position,
            // so off-screen interactive elements are still captured.
            function isRendered(el) {
                if (!el) return false;
                let node = el;
                while (node && node !== document.body) {
                    const style = window.getComputedStyle(node);
                    if (style.display === "none") return false;
                    if (style.visibility === "hidden") return false;
                    if (parseFloat(style.opacity) === 0) return false;
                    node = node.parentElement;
                }
                // Must have non-zero layout dimensions
                const rect = el.getBoundingClientRect();
                return rect.width > 0 || rect.height > 0;
            }

            // Stricter check: element must also have a non-zero bounding box
            // (used for headings / text-preview where we want truly visible content)
            function isVisible(el) {
                if (!isRendered(el)) return false;
                const rect = el.getBoundingClientRect();
                return rect.width > 0 && rect.height > 0;
            }

            function inferRole(el) {
                const explicit = (el.getAttribute("role") || "").toLowerCase();
                if (explicit) return explicit;
                const tag = el.tagName.toLowerCase();
                const type = (el.getAttribute("type") || "").toLowerCase();
                if (tag === "button") return "button";
                if (tag === "a") return "link";
                if (tag === "select") return "combobox";
                if (tag === "textarea") return "textbox";
                if (tag === "input") {
                    if (type === "checkbox") return "checkbox";
                    if (type === "radio") return "radio";
                    if (type === "submit" || type === "button" || type === "reset") return "button";
                    if (type === "search") return "searchbox";
                    if (type === "range") return "slider";
                    if (type === "number") return "spinbutton";
                    return "textbox";
                }
                if (/^h[1-6]$/.test(tag)) return "heading";
                if (tag === "dialog") return "dialog";
                return tag;
            }

            function getLabel(el) {
                // 1. aria-label attribute
                const ariaLabel = el.getAttribute("aria-label");
                if (ariaLabel) return ariaLabel.trim();

                // 2. aria-labelledby
                const labelledBy = el.getAttribute("aria-labelledby");
                if (labelledBy) {
                    const parts = labelledBy.split(/\\s+/).map(id => {
                        const ref = document.getElementById(id);
                        return ref ? (ref.innerText || ref.textContent || "").trim() : "";
                    }).filter(Boolean);
                    if (parts.length) return parts.join(" ");
                }

                // 3. label[for=id]
                const id = el.id;
                if (id) {
                    const lbl = document.querySelector(`label[for="${id}"]`);
                    if (lbl) return cleanText(lbl);
                }

                // 4. wrapping <label>
                const parent = el.closest("label");
                if (parent) {
                    const clone = parent.cloneNode(true);
                    clone.querySelectorAll("input,select,textarea,button").forEach(c => c.remove());
                    const t = (clone.innerText || clone.textContent || "").replace(/\\s+/g, " ").trim();
                    if (t) return truncate(t, TRUNC);
                }

                return "";
            }

            function getAccessibleName(el) {
                const ariaLabel = el.getAttribute("aria-label");
                if (ariaLabel) return ariaLabel.trim();

                const labelledBy = el.getAttribute("aria-labelledby");
                if (labelledBy) {
                    const parts = labelledBy.split(/\\s+/).map(id => {
                        const ref = document.getElementById(id);
                        return ref ? (ref.innerText || ref.textContent || "").trim() : "";
                    }).filter(Boolean);
                    if (parts.length) return parts.join(" ");
                }

                const lbl = getLabel(el);
                if (lbl) return lbl;

                const title = el.getAttribute("title");
                if (title) return title.trim();

                const text = cleanText(el);
                if (text) return text;

                return (el.value || "").trim();
            }

            function getTestId(el) {
                return el.getAttribute("data-testid") ||
                       el.getAttribute("data-test-id") ||
                       el.getAttribute("data-test") ||
                       el.getAttribute("data-cy") ||
                       "";
            }

            function dedup(arr, keyFn) {
                const seen = new Set();
                return arr.filter(item => {
                    const k = keyFn(item);
                    if (seen.has(k)) return false;
                    seen.add(k);
                    return true;
                });
            }

            // ── Headings ─────────────────────────────────────────────────────

            const headingEls = Array.from(
                document.querySelectorAll("h1,h2,h3,h4,h5,h6,[role=heading]")
            ).filter(isVisible).slice(0, HEADING_LIMIT);

            const headings = headingEls.map(el => ({
                text:  cleanText(el),
                role:  inferRole(el),
                title: el.getAttribute("title") || ""
            }));

            // ── Buttons ──────────────────────────────────────────────────────

            const buttonEls = Array.from(document.querySelectorAll(
                'button, input[type="button"], input[type="submit"], input[type="reset"], [role="button"]'
            )).filter(isRendered).slice(0, LIST_LIMIT);

            const buttons = buttonEls.map(el => ({
                tag:         el.tagName.toLowerCase(),
                type:        el.getAttribute("type") || "",
                role:        inferRole(el),
                text:        cleanText(el) || (el.value || "").trim(),
                name:        getAccessibleName(el),
                label:       getLabel(el),
                placeholder: el.getAttribute("placeholder") || "",
                title:       el.getAttribute("title") || "",
                ariaLabel:   el.getAttribute("aria-label") || "",
                id:          el.id || "",
                nameAttr:    el.getAttribute("name") || "",
                testId:      getTestId(el),
                disabled:    el.disabled || el.getAttribute("aria-disabled") === "true" || false
            }));

            // ── Links ────────────────────────────────────────────────────────

            const linkEls = Array.from(document.querySelectorAll(
                'a[href], [role="link"]'
            )).filter(isRendered).slice(0, LIST_LIMIT);

            const links = dedup(linkEls.map(el => ({
                tag:       el.tagName.toLowerCase(),
                role:      inferRole(el),
                text:      cleanText(el),
                name:      getAccessibleName(el),
                title:     el.getAttribute("title") || "",
                ariaLabel: el.getAttribute("aria-label") || "",
                testId:    getTestId(el),
                href:      el.getAttribute("href") || ""
            })), item => item.text + item.href);

            // ── Inputs (text-like, selects, textareas) ───────────────────────
            // Excludes checkboxes/radios — those go into the dedicated checkboxes section.

            const inputEls = Array.from(document.querySelectorAll(
                'input:not([type="hidden"]):not([type="button"]):not([type="submit"])' +
                ':not([type="reset"]):not([type="checkbox"]):not([type="radio"]), ' +
                'textarea, select, ' +
                '[role="textbox"], [role="combobox"], [role="spinbutton"], [role="searchbox"]'
            )).filter(isRendered).slice(0, LIST_LIMIT);

            const inputs = inputEls.map(el => {
                // Collect <select> options
                let options = [];
                if (el.tagName.toLowerCase() === "select") {
                    options = Array.from(el.options).slice(0, OPTIONS_LIMIT).map(o => ({
                        value: o.value,
                        label: o.text.trim(),
                        selected: o.selected
                    }));
                }
                return {
                    tag:         el.tagName.toLowerCase(),
                    type:        el.getAttribute("type") || el.tagName.toLowerCase(),
                    role:        inferRole(el),
                    text:        cleanText(el),
                    name:        getAccessibleName(el),
                    label:       getLabel(el),
                    placeholder: el.getAttribute("placeholder") || "",
                    title:       el.getAttribute("title") || "",
                    ariaLabel:   el.getAttribute("aria-label") || "",
                    id:          el.id || "",
                    nameAttr:    el.getAttribute("name") || "",
                    testId:      getTestId(el),
                    value:       (el.value !== undefined ? String(el.value) : ""),
                    required:    el.required || false,
                    disabled:    el.disabled || el.getAttribute("aria-disabled") === "true" || false,
                    options:     options
                };
            });

            // ── Checkboxes & Radios & Switches ───────────────────────────────

            const checkboxEls = Array.from(document.querySelectorAll(
                'input[type="checkbox"], input[type="radio"], ' +
                '[role="checkbox"], [role="radio"], [role="switch"], [role="menuitemcheckbox"], [role="menuitemradio"]'
            )).filter(isRendered).slice(0, LIST_LIMIT);

            const checkboxes = checkboxEls.map(el => {
                const ariaChecked = el.getAttribute("aria-checked");
                const checked = el.checked !== undefined
                    ? el.checked
                    : (ariaChecked === "true" || ariaChecked === "mixed");
                return {
                    tag:       el.tagName.toLowerCase(),
                    type:      el.getAttribute("type") || inferRole(el),
                    role:      inferRole(el),
                    text:      cleanText(el),
                    name:      getAccessibleName(el),
                    label:     getLabel(el),
                    title:     el.getAttribute("title") || "",
                    ariaLabel: el.getAttribute("aria-label") || "",
                    id:        el.id || "",
                    nameAttr:  el.getAttribute("name") || "",
                    testId:    getTestId(el),
                    checked:   checked,
                    disabled:  el.disabled || el.getAttribute("aria-disabled") === "true" || false
                };
            });

            // ── Interactive Widgets (tabs, menu items, sliders, tree items, options) ──

            const interactiveEls = Array.from(document.querySelectorAll(
                '[role="tab"], [role="menuitem"], [role="option"], ' +
                '[role="treeitem"], [role="slider"], [role="listitem"], ' +
                '[role="gridcell"], [role="row"], [role="columnheader"], ' +
                '[role="rowheader"], [role="tabpanel"]'
            )).filter(isRendered).slice(0, LIST_LIMIT);

            const interactives = interactiveEls.map(el => {
                const ariaSelected = el.getAttribute("aria-selected");
                const ariaExpanded = el.getAttribute("aria-expanded");
                return {
                    tag:       el.tagName.toLowerCase(),
                    role:      inferRole(el),
                    text:      cleanText(el),
                    name:      getAccessibleName(el),
                    label:     getLabel(el),
                    title:     el.getAttribute("title") || "",
                    ariaLabel: el.getAttribute("aria-label") || "",
                    id:        el.id || "",
                    testId:    getTestId(el),
                    selected:  ariaSelected === "true",
                    expanded:  ariaExpanded === null ? null : ariaExpanded === "true",
                    disabled:  el.getAttribute("aria-disabled") === "true" || false
                };
            });

            // ── Dialogs ──────────────────────────────────────────────────────

            const dialogEls = Array.from(document.querySelectorAll(
                '[role="dialog"], [role="alertdialog"], dialog'
            )).filter(isRendered).slice(0, DIALOG_LIMIT);

            const dialogs = dialogEls.map(el => ({
                role:      inferRole(el),
                text:      truncate(cleanText(el), 120),
                name:      getAccessibleName(el),
                title:     el.getAttribute("title") || "",
                ariaLabel: el.getAttribute("aria-label") || ""
            }));

            // ── Alerts / Status ──────────────────────────────────────────────

            const alertEls = Array.from(document.querySelectorAll(
                '[role="alert"], [role="status"], [role="log"]'
            )).filter(isRendered).slice(0, DIALOG_LIMIT);

            const alerts = alertEls.map(el => ({
                role:      el.getAttribute("role") || "",
                text:      truncate(cleanText(el), 120),
                title:     el.getAttribute("title") || "",
                ariaLabel: el.getAttribute("aria-label") || ""
            }));

            // ── Forms ────────────────────────────────────────────────────────

            const formEls = Array.from(document.querySelectorAll("form"))
                .filter(isRendered).slice(0, FORM_LIMIT);

            const forms = formEls.map(form => {
                const fields = Array.from(
                    form.querySelectorAll('input:not([type="hidden"]), textarea, select')
                ).map(f => f.getAttribute("name") || f.id || f.getAttribute("placeholder") || "")
                 .filter(Boolean);
                return {
                    action: form.getAttribute("action") || "",
                    method: (form.getAttribute("method") || "get").toLowerCase(),
                    fields: [...new Set(fields)]
                };
            });

            // ── Text Preview ─────────────────────────────────────────────────

            const bodyText = (document.body.innerText || "")
                .replace(/\\s+/g, " ").trim();
            const textPreview = bodyText.slice(0, TEXT_PREVIEW_LEN) +
                (bodyText.length > TEXT_PREVIEW_LEN ? "…" : "");

            // ── Counts ───────────────────────────────────────────────────────

            const counts = {
                headings:     headings.length,
                buttons:      buttons.length,
                links:        links.length,
                inputs:       inputs.length,
                checkboxes:   checkboxes.length,
                interactives: interactives.length,
                dialogs:      dialogs.length,
                alerts:       alerts.length,
                forms:        forms.length
            };

            return {
                meta: {
                    url:   window.location.href,
                    title: document.title
                },
                headings,
                buttons,
                links,
                inputs,
                checkboxes,
                interactives,
                dialogs,
                alerts,
                forms,
                textPreview,
                counts
            };
        }
        """)
        return summary
    except Exception as e:
        return {"error": f"Failed to extract page summary: {str(e)}"}


@mcp.tool()
async def get_page_summary_tool(pageId: int) -> dict:
    """
    Returns a compact, structured, token-efficient page summary for LLM usage.

    Extracts all interactive and semantic elements from the page in a single
    browser-side evaluation. Captures both in-viewport AND off-screen (but rendered)
    elements so nothing interactive is missed. The summary is specifically designed
    to help an LLM choose the correct Playwright locator strategy:
        - get_by_text(...)       → use 'text' or 'name' fields
        - get_by_placeholder(...)→ use 'placeholder' field
        - get_by_title(...)      → use 'title' field
        - get_by_label(...)      → use 'label' field
        - get_by_role(...)       → use 'role' + 'name' fields

    Args:
        pageId (int): The ID of the page to summarise (from open_page).

    Returns:
        dict: A JSON-serialisable summary containing:
            - meta         : { url, title }
            - headings     : list of heading elements
            - buttons      : list of button/submit elements with locator hints
                             Fields: tag, type, role, text, name, label, placeholder,
                                     title, ariaLabel, id, nameAttr, testId, disabled
            - links        : list of anchor elements with locator hints
                             Fields: tag, role, text, name, title, ariaLabel, testId, href
            - inputs       : list of text inputs / textareas / selects with locator hints
                             Fields: tag, type, role, text, name, label, placeholder,
                                     title, ariaLabel, id, nameAttr, testId, value,
                                     required, disabled, options (for <select>)
            - checkboxes   : list of checkbox / radio / switch elements
                             Fields: tag, type, role, text, name, label, title,
                                     ariaLabel, id, nameAttr, testId, checked, disabled
            - interactives : list of tabs, menu items, options, tree items, sliders,
                             grid cells, rows, column/row headers, tab panels
                             Fields: tag, role, text, name, label, title, ariaLabel,
                                     id, testId, selected, expanded, disabled
            - dialogs      : list of visible dialog/alertdialog elements
            - alerts       : list of visible alert/status elements
            - forms        : list of forms with action, method, and field names
            - textPreview  : first ~300 chars of visible body text
            - counts       : element counts per category
    """
    global session
    if f"Page{pageId}" not in session:
        return {"error": "Invalid Page Id"}

    try:
        page = session[f"Page{pageId}"]
        return await get_page_summary(page)
    except Exception as e:
        return {"error": f"Unable to get page summary: {str(e)}"}


# Keyboard Events
@mcp.tool()
async def key_press(pageId: int, keys: List[str] = []) -> str:
    """
    Simulates a keyboard key press on a specific page

    This tool dispatches a keyboard event for the given key on the page.

    Useful for:
        - Submitting forms (Enter)
        - Closing modals (Escape)
        - Navigating between fields (Tab)
        - Triggering keyboard shortcuts (Control+A, Meta+C, etc.)
        - Interacting with dropdowns, sliders, and custom widgets (Arrow keys)

    Args:
        pageId (int):
            The ID of the page to interact with (returned by open_page).

        key (str):
            List Of Keys to press at once

            - "ArrowUp"         Move up in lists, dropdowns, sliders
            - "ArrowDown"       Move down in lists, dropdowns, sliders
            - "ArrowLeft"       Move left / navigate back
            - "ArrowRight"      Move right / navigate forward
            - "Tab"             Move focus to the next element
            - "Home"            Jump to the beginning of a field or page
            - "End"             Jump to the end of a field or page
            - "PageUp"          Scroll up one page
            - "PageDown"        Scroll down one page

            - "Enter"           Submit forms, confirm dialogs, activate buttons
            - "Space"           Activate buttons, checkboxes, scroll down
            - "Escape"          Close modals, cancel actions, dismiss dropdowns

            - "Backspace"       Delete character before the cursor
            - "Delete"          Delete character after the cursor
            - "Insert"          Toggle insert/overwrite mode

            - "Shift"           Uppercase / extend selection
            - "Control"         Trigger shortcuts (Windows/Linux)
            - "Meta"            Trigger shortcuts (macOS Command key)
            - "Alt"             Alternate actions / access keys
            - "ControlOrMeta"   Resolves to Control on Windows/Linux, Meta on macOS

            - "F1"              Help
            - "F2"              Rename / edit
            - "F3"              Find / search
            - "F4"              Address bar (browsers) / close (Alt+F4)
            - "F5"              Reload the page
            - "F6"              Focus address bar
            - "F7"              Caret browsing toggle
            - "F8"              (App-specific)
            - "F9"              (App-specific)
            - "F10"             Menu bar focus
            - "F11"             Toggle fullscreen
            - "F12"             Open DevTools

            -"Digit0"          Digit 0
            -"Digit9"          Digit 9
            -"KeyA"            Letter A
            -"KeyB"            Letter B
            -"Backquote"       Backquote
            -"Minus"           "Minus"

            - "Tab"             Tab / indent
            - "Enter"           Newline in textarea
            - "Space"           Space character

            - ["Control","KeyA"]           Select all
            - ["Control","KeyC"]           Copy
            - ["Control","KeyV"]           Paste
            - ["Control","KeyX"]           Cut
            - ["Control","KeyZ"]           Undo
            - ["Control","KeyY"]           Redo
            - ["Control","KeyS"]           Save
            - ["Control","KeyF"]           Find / search on page
            - ["Control","KeyT"]           New tab
            - ["Control","KeyW"]           Close tab
            - ["Control","KeyR"]           Reload
            - ["Control","KeyL"]           Focus address bar
            - ["Control","Enter"]       Submit / open in new tab
            - ["Shift","Tab"]           Move focus to the previous element
            - ["Shift","Enter"]         New line (in some editors)
            - ["Alt","ArrowLeft"]       Browser back
            - ["Alt","ArrowRight"]      Browser forward
            - ["Meta","KeyA"]              Select all (macOS)
            - ["Meta","KeyC"]              Copy (macOS)
            - ["Meta","KeyV"]              Paste (macOS)
            - ["Meta","KeyZ"]              Undo (macOS)
            - ["Meta","ArrowLeft"]      Go to beginning of line (macOS)
            - ["Meta","ArrowRight"]     Go to end of line (macOS)
            """

    global session
    if f"Page{pageId}" not in session:
        return "Invalid Page ID"

    try:
        page=session.get(f"Page{pageId}")
        final_key="+".join(keys)
        await page.keyboard.press(final_key)
        return "success"
    except Exception as e:
        
        return f"Unbale to press key{e}"

# Done &mdash; page forward, backward, reload, close,  open another page in same pageid,left right middle modify in click, scroll page, 
# Left &mdash; fix click, check uncheck, select from list,

@mcp.tool()
async def previous_page(pageId: int) -> str:
    """
    Navigates the specified page back to the previous URL in its browsing history.

    This is equivalent to clicking the browser's back button. If there is no
    previous page in the history, the navigation will have no effect.

    Args:
        pageId (int): The ID of the page to navigate back (returned by open_page).
    """

    global session
    if f"Page{pageId}" not in session:
        return "Invalid Page ID"
    
    try:
        page=session.get(f"Page{pageId}")
        await page.go_back()
        return "success"
    except Exception as e:
        
        return f"Unable to go back{e}"
    
@mcp.tool()
async def next_page(pageId: int) -> str:
    """
    Navigates the specified page forward to the next URL in its browsing history.

    This is equivalent to clicking the browser's forward button. If there is no
    next page in the history (i.e., the user has not navigated back previously),
    the navigation will have no effect.

    Args:
        pageId (int): The ID of the page to navigate forward (returned by open_page).
    
    """

    global session
    if f"Page{pageId}" not in session:
        return "Invalid Page ID"
    
    try:
        page=session.get(f"Page{pageId}")
        await page.go_forward()
        return "success"
    except Exception as e:
        
        return f"Unable to go forward{e}"
    

@mcp.tool()
async def reload_page(pageId: int) -> str:

    """
        Reloads the specified page, refreshing its content from the server.

        Args:
            pageId (int): The ID of the page to reload (returned by open_page).

    """



    global session
    if f"Page{pageId}" not in session:
        return "Invalid Page ID"
    
    try:
        page=session.get(f"Page{pageId}")
        await page.reload()
        return "success"
    except Exception as e:
        
        return f"Unable to go forward{e}"
    
@mcp.tool()
async def close_page(pageId: int) -> str:
    """
    Closes the specified browser page/tab and removes it from the active session.

    This permanently closes the page associated with the given pageId. Once closed,
    the pageId becomes invalid and cannot be used for further interactions. The
    browser itself remains open and other pages in the session are unaffected.

    Args:
        pageId (int): The ID of the page to close (returned by open_page).
    
    """
    global session
    if f"Page{pageId}" not in session:
        return "Invalid Page ID"
    
    try:
        page=session.get(f"Page{pageId}")
        await page.close()
        return "success"
    except Exception as e:
        
        return f"Unable to close page{e}"


@mcp.tool()
async def navigate_to(pageId: int, url: str) -> str:
    """
    Navigates an existing page to a new URL, replacing the current page content.

    Unlike open_page, this does not open a new tab. Instead, it loads the given
    URL within the same page identified by pageId, similar to typing a new address
    in the browser's address bar and pressing Enter. The pageId remains valid and
    can continue to be used after navigation.

    Args:
        pageId (int): The ID of the existing page to navigate (returned by open_page).
        url (str): The full URL to navigate to (e.g., "https://example.com")
    """

    global session
    if f"Page{pageId}" not in session:
        return "Invalid Page ID"
    
    try:
        page=session.get(f"Page{pageId}")
        await page.goto(url)
        return "success"
    except Exception as e:
        
        return f"Unable to load new url{e}"

@mcp.tool()
async def scroll_screen(pageId: int, deltaX: float = 0.0, deltaY: int=0.0) -> str:
    """
    Scrolls the page by the specified number of pixels in the horizontal and/or vertical direction.

    This simulates a mouse wheel scroll event on the page. Positive values scroll
    right and down, while negative values scroll left and up. Both axes can be
    scrolled simultaneously by providing non-zero values for both deltaX and deltaY.

    Args:
        pageId (int): The ID of the page to scroll (returned by open_page).
        deltaX (int): The number of pixels to scroll horizontally.
                      Positive values scroll right, negative values scroll left.
                      Defaults to 0 (no horizontal scroll).
        deltaY (int): The number of pixels to scroll vertically.
                      Positive values scroll down, negative values scroll up.
                      Defaults to 0 (no vertical scroll).
    """
     
    global session
    if f"Page{pageId}" not in session:
        return "Invalid Page ID"
    
    
    page=session.get(f"Page{pageId}")
    await page.mouse.wheel(deltaX, deltaY)
    return "success"
    
     
@mcp.tool()
async def select_option_by_text(pageId: int, text: str, labels:List[str] = []) -> str:
    """
    Selects one or more options in a <select> dropdown, located by its visible text content.

    This tool finds a <select> element by matching its visible text on the page and
    selects the specified option(s) by their display label. Supports both single
    and multi-select dropdowns.

    Args:
        pageId (int): The ID of the page to interact with (returned by open_page).
        text (str): The visible text used to locate the <select> element on the page.
                    Example: "Sort by", "Filter", "Select country"
        labels (List[str]): A list of option display labels to select.
                    - Single selection: ["Newest"]
                    - Multiple selections: ["Flights", "Hotels"]
                    Defaults to [] (no selection).
    """
    global session
    if f"Page{pageId}" not in session: 
        return "Invalid Page Id"
    
    try:
        page=session[f"Page{pageId}"]
        await page.get_by_text(text).select_option(label=labels)
        return "success"

    except Exception as e:
        
        return f"Unable to click input f{e}ield"
    
@mcp.tool()
async def select_option_by_label(pageId: int, label: str, labels:List[str] = []) -> str:
    """
    Selects one or more options in a <select> dropdown, located by its associated label text.

    This tool finds a <select> element using its visible label (e.g., a <label> tag
    or aria-label attribute) and selects the specified option(s) by their display label.
    Supports both single and multi-select dropdowns.

    Args:
        pageId (int): The ID of the page to interact with (returned by open_page).
        label (str): The label text associated with the <select> element.
                     Example: "Choose a color", "Country", "Sort by"
        labels (List[str]): A list of option display labels to select.
                     - Single selection: ["Blue"]
                     - Multiple selections: ["Red", "Green", "Blue"]
                     Defaults to [] (no selection).
    """
    global session
    if f"Page{pageId}" not in session: 
        return "Invalid Page Id"
    
    try:
        page=session[f"Page{pageId}"]
        await page.get_by_label(label).select_option(label=labels)
        return "success"

    except Exception as e:
        
        return f"Unable to click element{e}"

@mcp.tool()
async def select_option_by_placeholder(pageId: int, placeholder: str, labels:List[str] = []) -> str:
    """
    Selects one or more options in a <select> dropdown, located by its placeholder text.

    This tool finds a <select> element using its placeholder attribute and selects
    the specified option(s) by their display label. Useful for dropdowns that show
    a placeholder hint like "Select an option..." before a value is chosen.

    Args:
        pageId (int): The ID of the page to interact with (returned by open_page).
        placeholder (str): The placeholder text of the <select> element.
                     Example: "Select a country", "Choose an option"
        labels (List[str]): A list of option display labels to select.
                     - Single selection: ["India"]
                     - Multiple selections: ["India", "USA"]
                     Defaults to [] (no selection).
    """
    global session
    if f"Page{pageId}" not in session: 
        return "Invalid Page Id"
    
    try:
        page=session[f"Page{pageId}"]
        await page.get_by_placeholder(placeholder).select_option(label=labels)
        return "success"

    except Exception as e:
        
        return f"Unable to click element{e}"

@mcp.tool()
async def select_option_by_title(pageId: int, title: str, labels:List[str] = []) -> str:
    """
    Selects one or more options in a <select> dropdown, located by its title attribute.

    This tool finds a <select> element using its HTML title attribute and selects
    the specified option(s) by their display label. Useful when the dropdown has a
    descriptive title attribute but no visible label or accessible name.

    Args:
        pageId (int): The ID of the page to interact with (returned by open_page).
        title (str): The title attribute value of the <select> element.
                     Example: "Select your country", "Choose currency"
        labels (List[str]): A list of option display labels to select.
                     - Single selection: ["INR"]
                     - Multiple selections: ["USD", "EUR"]
                     Defaults to [] (no selection).
    """
    global session
    if f"Page{pageId}" not in session: 
        return "Invalid Page Id"
    
    try:
        page=session[f"Page{pageId}"]
        await page.get_by_title(title).select_option(label=labels)
        return "success"
    except Exception as e:
        
        return f"Unable to click element{e}"

@mcp.tool()
async def select_option_by_role(pageId: int, role: str, labels:List[str] = [], name: str = "") -> str:
    """
    Selects one or more options in a <select> dropdown, located by its ARIA role
    and optional accessible name.

    This tool finds a dropdown element using its accessibility role (typically
    "combobox" or "listbox") and selects the specified option(s) by their display
    label. Supplying the accessible name is strongly recommended when multiple
    elements share the same role.

    Parameters:
        pageid (int):
            Identifier of the browser page or session where the element should be found.
        labels (List[str]): A list of option display labels to select.
                            - Single selection: ["Blue"]
                            - Multiple selections: ["Red", "Green"]
                            Defaults to [] (no selection).
        role (str):
            Accessibility role used to locate the target element.

            Allowed role values:
            - alert
            - alertdialog
            - application
            - article
            - banner
            - blockquote
            - button
            - caption
            - cell
            - checkbox
            - code
            - columnheader
            - combobox
            - complementary
            - contentinfo
            - definition
            - deletion
            - dialog
            - directory
            - document
            - emphasis
            - feed
            - figure
            - form
            - generic
            - grid
            - gridcell
            - group
            - heading
            - img
            - insertion
            - link
            - list
            - listbox
            - listitem
            - log
            - main
            - marquee
            - math
            - meter
            - menu
            - menubar
            - menuitem
            - menuitemcheckbox
            - menuitemradio
            - navigation
            - none
            - note
            - option
            - paragraph
            - presentation
            - progressbar
            - radio
            - radiogroup
            - region
            - row
            - rowgroup
            - rowheader
            - scrollbar
            - search
            - searchbox
            - separator
            - slider
            - spinbutton
            - status
            - strong
            - subscript
            - superscript
            - switch
            - tab
            - table
            - tablist
            - tabpanel
            - term
            - textbox
            - time
            - timer
            - toolbar
            - tooltip
            - tree
            - treegrid
            - treeitem

            Important:
            Not all roles represent elements that can accept text input. This tool is
            intended for editable or value-settable controls. The most appropriate roles
            for filling are usually:
            - textbox
            - searchbox
            - combobox
            - spinbutton

            In some applications, filling may also be meaningful for custom widgets that
            behave like editable controls, but roles such as `button`, `link`, `heading`,
            `image`, `list`, or `table` are generally not valid text-fill targets.

        

        name (str | None, optional):
            Accessible name used to narrow the role match to a specific element.
            This is typically the user-facing label announced by assistive technology,
            such as "Email", "Search", or "Age".
            
        """
    
    global session
    if f"Page{pageId}" not in session: 
        return "Invalid Page Id"
    
    try:
        page=session.get(f"Page{pageId}")
        if name == "":
            await page.get_by_role(role).select_option(label=labels)
        else:
            await page.get_by_role(role, name=name).select_option(label=labels)
        
        return "succes"
    except Exception as e:
        
        return f"Unable to click element{e}"



@mcp.tool()
async def select_checked_by_text(pageId: int, text: str, checked: bool = True) -> str:
    """
    Checks or unchecks a checkbox or radio button, located by its visible text content.

    This tool finds a checkbox or radio button by matching its visible text on the page
    and sets its checked state. Useful when the element has visible text but no formal
    label or ARIA attribute.

    Args:
        pageId (int): The ID of the page to interact with (returned by open_page).
        text (str): The visible text used to locate the <select> element on the page.
                    Example: "Sort by", "Filter", "Select country"
        checked (bool): The desired checked state.
                     - True  → Check the checkbox / Select the radio button (default)
                     - False → Uncheck the checkbox
    """
    global session
    if f"Page{pageId}" not in session: 
        return "Invalid Page Id"
    
    try:
        page=session[f"Page{pageId}"]
        await page.get_by_text(text).set_checked(checked)
        return "success"

    except Exception as e:
        
        return f"Unable to click input f{e}ield"
    
@mcp.tool()
async def select_checked_by_label(pageId: int, label: str, checked: bool = True) -> str:
    """
    Checks or unchecks a checkbox or radio button, located by its associated label text.

    This tool finds a checkbox or radio button using its visible label (e.g., a <label>
    tag or aria-label attribute) and sets its checked state. Use checked=True to check
    or select, and checked=False to uncheck. Radio buttons can only be checked (not unchecked).


    Args:
        pageId (int): The ID of the page to interact with (returned by open_page).
        label (str): The label text associated with the <select> element.
                     Example: "Choose a color", "Country", "Sort by"
        checked (bool): The desired checked state.
                     - True  → Check the checkbox / Select the radio button (default)
                     - False → Uncheck the checkbox
    """
    global session
    if f"Page{pageId}" not in session: 
        return "Invalid Page Id"
    
    try:
        page=session[f"Page{pageId}"]
        await page.get_by_label(label).set_checked(checked)
        return "success"

    except Exception as e:
        
        return f"Unable to click element{e}"


@mcp.tool()
async def select_checked_by_title(pageId: int, title: str, checked: bool = True) -> str:
    """
    Checks or unchecks a checkbox or radio button, located by its title attribute.

    This tool finds a checkbox or radio button using its HTML title attribute and
    sets its checked state. Useful when the element has a descriptive title attribute
    but no visible label or accessible name.

    Args:
        pageId (int): The ID of the page to interact with (returned by open_page).
        title (str): The title attribute value of the <select> element.
                     Example: "Select your country", "Choose currency"
        checked (bool): The desired checked state.
                     - True  → Check the checkbox / Select the radio button (default)
                     - False → Uncheck the checkbox
    """
    global session
    if f"Page{pageId}" not in session: 
        return "Invalid Page Id"
    
    try:
        page=session[f"Page{pageId}"]
        await page.get_by_title(title).set_checked(checked)
        return "success"
    except Exception as e:
        
        return f"Unable to click element{e}"

@mcp.tool()
async def select_checked_by_role(pageId: int, role: str, checked: bool = True, name: str = "") -> str:
    """
    Checks or unchecks a checkbox or radio button, located by its ARIA role
    and optional accessible name.

    This tool finds a checkbox or radio button using its accessibility role and
    sets its checked state. Supplying the accessible name is strongly recommended
    when multiple elements share the same role.

    Parameters:
        pageid (int):
            Identifier of the browser page or session where the element should be found.
        checked (bool): The desired checked state.
                     - True  → Check / Select / Turn on (default)
                     - False → Uncheck / Deselect / Turn off
        
        role (str):
            Accessibility role used to locate the target element.

            Allowed role values:
            - alert
            - alertdialog
            - application
            - article
            - banner
            - blockquote
            - button
            - caption
            - cell
            - checkbox
            - code
            - columnheader
            - combobox
            - complementary
            - contentinfo
            - definition
            - deletion
            - dialog
            - directory
            - document
            - emphasis
            - feed
            - figure
            - form
            - generic
            - grid
            - gridcell
            - group
            - heading
            - img
            - insertion
            - link
            - list
            - listbox
            - listitem
            - log
            - main
            - marquee
            - math
            - meter
            - menu
            - menubar
            - menuitem
            - menuitemcheckbox
            - menuitemradio
            - navigation
            - none
            - note
            - option
            - paragraph
            - presentation
            - progressbar
            - radio
            - radiogroup
            - region
            - row
            - rowgroup
            - rowheader
            - scrollbar
            - search
            - searchbox
            - separator
            - slider
            - spinbutton
            - status
            - strong
            - subscript
            - superscript
            - switch
            - tab
            - table
            - tablist
            - tabpanel
            - term
            - textbox
            - time
            - timer
            - toolbar
            - tooltip
            - tree
            - treegrid
            - treeitem

            Important:
            Not all roles represent elements that can accept text input. This tool is
            intended for editable or value-settable controls. The most appropriate roles
            for filling are usually:
            - textbox
            - searchbox
            - combobox
            - spinbutton

            In some applications, filling may also be meaningful for custom widgets that
            behave like editable controls, but roles such as `button`, `link`, `heading`,
            `image`, `list`, or `table` are generally not valid text-fill targets.

        

        name (str | None, optional):
            Accessible name used to narrow the role match to a specific element.
            This is typically the user-facing label announced by assistive technology,
            such as "Email", "Search", or "Age".
            
        """
    
    global session
    if f"Page{pageId}" not in session: 
        return "Invalid Page Id"
    
    try:
        page=session.get(f"Page{pageId}")
        if name == "":
            await page.get_by_role(role).set_checked(checked)
        else:
            await page.get_by_role(role, name=name).set_checked(checked)
        
        return "succes"
    except Exception as e:
        
        return f"Unable to click element{e}"



    
    



if __name__ == "__main__":
    mcp.run()




'