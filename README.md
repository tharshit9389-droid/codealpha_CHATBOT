# 🤖 Harshit Tyagi Bot Pro v2.0 - Multilingual AI Assistant & Problem Solver

**Harshit Tyagi Bot Pro v2.0** is a professional-grade, supercharged AI assistant and multi-type problem solver comparable to ChatGPT & Google Gemini. It offers both a **Desktop Tkinter Application** and a **Localhost Web Application (`http://localhost:5000`)** equipped with full Markdown rendering, code syntax highlighting, copy-code buttons, multilingual language detection, AI personas, and contextual conversation memory.

---

## 📁 Complete Project Files Directory

Below is the complete list of all files included in this project:

| File Name | Description / Role |
| :--- | :--- |
| 📄 **[`bot_engine.py`](file:///c:/Users/Dell/OneDrive/Desktop/New%20folder/bot_engine.py)** | Core AI engine for `Harshit Tyagi Bot Pro v2.0`. Features multilingual language detection (English, Hindi, Hinglish, Spanish, French, German, etc.), AI personas, context memory, physics & math solver, full-stack software code generator, and Google Gemini 2.5 Flash API integration. |
| 📄 **[`gui_app.py`](file:///c:/Users/Dell/OneDrive/Desktop/New%20folder/gui_app.py)** | Professional Desktop GUI built with `tkinter` and `ttk`. Includes AI persona selector, multithreaded fast response stream, dark glassmorphism theme, quick solver toolbar, and dynamic API Key settings. |
| 📄 **[`server.py`](file:///c:/Users/Dell/OneDrive/Desktop/New%20folder/server.py)** | Localhost Web Server built with `FastAPI` and `Uvicorn` (`http://localhost:5000`). Serves the web interface and REST API endpoints (`/api/chat`, `/api/personas`, `/api/status`). |
| 📄 **[`templates/index.html`](file:///c:/Users/Dell/OneDrive/Desktop/New%20folder/templates/index.html)** | Web interface with `Marked.js` markdown parser, `Highlight.js` syntax highlighting, 1-click **Copy Code** buttons, AI persona dropdown, quick action chips, and glowing dark UI. |
| 📄 **[`main.py`](file:///c:/Users/Dell/OneDrive/Desktop/New%20folder/main.py)** | Unified entry point launcher script to run Localhost Server, Desktop Tkinter App, or both simultaneously. |
| 📄 **[`requirements.txt`](file:///c:/Users/Dell/OneDrive/Desktop/New%20folder/requirements.txt)** | Python package dependencies (`fastapi`, `uvicorn`, `requests`, `google-genai`, `pillow`, `jinja2`). |
| 📄 **[`README.md`](file:///c:/Users/Dell/OneDrive/Desktop/New%20folder/README.md)** | Full project documentation, file overview, setup instructions, and feature guide. |

---

## ✨ Key Capabilities & Features

1. 🌐 **Multilingual Language Engine:**
   - Detects and responds natively in **English, Hindi (हिंदी), Hinglish, Spanish (Español), French (Français), German (Deutsch)**, and programming languages.
2. 🎭 **AI Persona System:**
   - **General Assistant:** All-round intelligent companion.
   - **Coding Expert:** Production-grade code, debugging, and architecture.
   - **Math & Science Tutor:** Calculus, algebra, quadratic equations, and physics formulas ($F=ma$, $E=mc^2$).
   - **Polyglot Translator:** Accurate multilingual translations.
3. 🧠 **Contextual Conversation Memory:**
   - Maintains multi-turn context so users can ask follow-up questions.
4. 💻 **Markdown & 1-Click Code Copy UI:**
   - Code blocks with syntax highlighting and 1-click copy buttons.
5. 🔑 **Gemini 2.5 Flash Integration:**
   - Connects to Google Gemini API when `GEMINI_API_KEY` is provided, with built-in supercharged offline AI reasoning fallback.

---

## 🚀 How to Launch

To run **BOTH** the Localhost Web Server (`http://localhost:5000`) and the Desktop Tkinter GUI simultaneously:

```bash
py main.py
```

### Launch Options
- **Localhost Web Server only:** `py main.py web` (Access `http://localhost:5000` in browser)
- **Desktop Tkinter GUI only:** `py main.py desktop`
