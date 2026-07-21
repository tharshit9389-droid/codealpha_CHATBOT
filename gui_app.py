"""
gui_app.py - Tkinter Desktop Interface for Harshit Tyagi Bot Pro v2.0
Features a modern glassmorphism dark UI, persona switching, multithreaded fast response delivery,
chat bubbles, quick prompt actions, and API settings.
"""

import sys
import threading
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from bot_engine import HarshitTyagiBot

# Windows stdout encoding safeguard
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass


class HarshitTyagiBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Harshit Tyagi Bot Pro v2.0 - Multilingual AI Assistant")
        self.root.geometry("950x720")
        self.root.minsize(800, 580)

        # Apply dark color theme palette
        self.bg_color = "#090d16"      # Deep Dark 950
        self.card_bg = "#161e2e"       # Slate Dark 900
        self.user_bubble = "#2563eb"    # Blue 600
        self.bot_bubble = "#1e293b"     # Slate 800
        self.text_color = "#f8fafc"     # Slate 50
        self.muted_text = "#94a3b8"     # Slate 400
        self.accent_color = "#38bdf8"   # Sky 400
        self.input_bg = "#334155"       # Slate 700

        self.root.configure(bg=self.bg_color)
        self.bot = HarshitTyagiBot()

        self._setup_ui()
        self._send_welcome_message()

    def _setup_ui(self):
        # 1. Header Frame
        header_frame = tk.Frame(self.root, bg=self.card_bg, height=70, relief=tk.FLAT)
        header_frame.pack(fill=tk.X, side=tk.TOP)

        avatar_label = tk.Label(
            header_frame,
            text="🤖",
            font=("Segoe UI Emoji", 24),
            bg=self.card_bg,
            fg="#ffffff"
        )
        avatar_label.pack(side=tk.LEFT, padx=(15, 5), pady=10)

        title_sub_frame = tk.Frame(header_frame, bg=self.card_bg)
        title_sub_frame.pack(side=tk.LEFT, pady=10)

        title_label = tk.Label(
            title_sub_frame,
            text="Harshit Tyagi Bot Pro v2.0",
            font=("Segoe UI", 15, "bold"),
            bg=self.card_bg,
            fg=self.text_color
        )
        title_label.pack(anchor="w")

        subtitle_label = tk.Label(
            title_sub_frame,
            text="● Online | Multilingual AI Assistant & Problem Solver",
            font=("Segoe UI", 8),
            bg=self.card_bg,
            fg="#4ade80" # Green online dot
        )
        subtitle_label.pack(anchor="w")

        # Header Controls (Persona Selector, API Key, Clear Chat)
        controls_frame = tk.Frame(header_frame, bg=self.card_bg)
        controls_frame.pack(side=tk.RIGHT, padx=15)

        # Persona Dropdown
        persona_label = tk.Label(controls_frame, text="Persona:", font=("Segoe UI", 9, "bold"), bg=self.card_bg, fg=self.muted_text)
        persona_label.pack(side=tk.LEFT, padx=(0, 4))

        self.persona_var = tk.StringVar(value=self.bot.persona)
        persona_dropdown = ttk.Combobox(
            controls_frame,
            textvariable=self.persona_var,
            values=list(HarshitTyagiBot.PERSONAS.keys()),
            state="readonly",
            width=18,
            font=("Segoe UI", 9)
        )
        persona_dropdown.pack(side=tk.LEFT, padx=(0, 10))
        persona_dropdown.bind("<<ComboboxSelected>>", self._on_persona_change)

        api_btn = tk.Button(
            controls_frame,
            text="🔑 API Key",
            font=("Segoe UI", 9, "bold"),
            bg="#3b82f6",
            fg="white",
            activebackground="#2563eb",
            activeforeground="white",
            relief=tk.FLAT,
            bd=0,
            padx=10,
            pady=4,
            cursor="hand2",
            command=self._open_api_settings
        )
        api_btn.pack(side=tk.LEFT, padx=3)

        clear_btn = tk.Button(
            controls_frame,
            text="🗑️ Clear",
            font=("Segoe UI", 9),
            bg="#475569",
            fg="white",
            activebackground="#334155",
            activeforeground="white",
            relief=tk.FLAT,
            bd=0,
            padx=10,
            pady=4,
            cursor="hand2",
            command=self._clear_chat
        )
        clear_btn.pack(side=tk.LEFT, padx=3)

        # 2. Main Chat Display Area
        chat_container = tk.Frame(self.root, bg=self.bg_color)
        chat_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        self.chat_display = tk.Text(
            chat_container,
            bg=self.card_bg,
            fg=self.text_color,
            font=("Segoe UI", 10),
            wrap=tk.WORD,
            bd=0,
            padx=15,
            pady=15,
            state=tk.DISABLED,
            insertbackground=self.text_color
        )
        self.chat_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(chat_container, orient=tk.VERTICAL, command=self.chat_display.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_display.configure(yscrollcommand=scrollbar.set)

        # Tags for formatting
        self.chat_display.tag_configure("user_header", font=("Segoe UI", 10, "bold"), foreground="#60a5fa", justify="right")
        self.chat_display.tag_configure("user_msg", font=("Segoe UI", 10), foreground="#ffffff", justify="right")
        self.chat_display.tag_configure("bot_header", font=("Segoe UI", 10, "bold"), foreground="#38bdf8", justify="left")
        self.chat_display.tag_configure("bot_msg", font=("Segoe UI", 10), foreground="#f8fafc", justify="left")

        # 3. Quick Action Chips Toolbar
        quick_frame = tk.Frame(self.root, bg=self.bg_color)
        quick_frame.pack(fill=tk.X, padx=15, pady=(0, 5))

        chip_label = tk.Label(quick_frame, text="Quick Solvers:", font=("Segoe UI", 9, "bold"), bg=self.bg_color, fg=self.muted_text)
        chip_label.pack(side=tk.LEFT, padx=(0, 5))

        chips = [
            ("🌐 Hindi/Hinglish", "Aap kaise ho bhai? Mujhe ek Python program likhkar batao."),
            ("🧮 Solve Math", "Solve quadratic equation 1x^2 - 5x + 6 = 0"),
            ("💻 Python Code", "Write a python function to scrape website titles"),
            ("⚛️ Physics Formula", "Explain Newton's second law F=ma with example"),
            ("📝 Summarize Text", "Summarize: Artificial Intelligence and Machine Learning are transforming modern software.")
        ]

        for label_text, prompt_text in chips:
            btn = tk.Button(
                quick_frame,
                text=label_text,
                font=("Segoe UI", 8),
                bg="#334155",
                fg="#e2e8f0",
                activebackground="#475569",
                activeforeground="#ffffff",
                relief=tk.FLAT,
                bd=0,
                padx=8,
                pady=3,
                cursor="hand2",
                command=lambda p=prompt_text: self._use_quick_prompt(p)
            )
            btn.pack(side=tk.LEFT, padx=3)

        # 4. Input Controls Frame
        input_frame = tk.Frame(self.root, bg=self.card_bg, height=60)
        input_frame.pack(fill=tk.X, side=tk.BOTTOM, padx=15, pady=(0, 15))

        self.input_entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 11),
            bg=self.input_bg,
            fg=self.text_color,
            bd=0,
            insertbackground=self.text_color,
            relief=tk.FLAT
        )
        self.input_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.input_entry.bind("<Return>", lambda event: self.send_message())
        self.input_entry.focus_set()

        self.send_btn = tk.Button(
            input_frame,
            text="Send 🚀",
            font=("Segoe UI", 10, "bold"),
            bg="#3b82f6",
            fg="white",
            activebackground="#2563eb",
            activeforeground="white",
            relief=tk.FLAT,
            bd=0,
            padx=18,
            pady=8,
            cursor="hand2",
            command=self.send_message
        )
        self.send_btn.pack(side=tk.RIGHT, padx=10, pady=10)

        # 5. Status Bar
        self.status_bar = tk.Label(
            self.root,
            text=f"Ready | Active Persona: {self.bot.persona}",
            font=("Segoe UI", 8),
            bg=self.bg_color,
            fg=self.muted_text,
            anchor="w"
        )
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM, padx=15, pady=(0, 2))

    def _send_welcome_message(self):
        welcome_text = (
            f"👋 Welcome to **Harshit Tyagi Bot Pro v2.0**!\n\n"
            f"I am your supercharged Multilingual AI Assistant & Multi-Type Problem Solver.\n"
            f"I understand **English, Hindi (हिंदी), Hinglish, Spanish, French, German**, and code languages.\n\n"
            f"• 🌐 **Multilingual Polyglot:** Ask questions in any language or request translations.\n"
            f"• 🧮 **Math & Physics:** Step-by-step calculus, algebra, geometry & physics formulas.\n"
            f"• 💻 **Coding & Web Architecture:** Python, JS/TS, React, HTML/CSS, SQL, C++, Java.\n"
            f"• 🎭 **AI Personas:** Change persona above (Coding Expert, Math Tutor, Polyglot, General).\n\n"
            f"Type your problem below or select a Quick Solver above!"
        )
        self._append_message("Harshit Tyagi Bot", welcome_text, is_user=False)

    def _on_persona_change(self, event):
        new_persona = self.persona_var.get()
        msg = self.bot.set_persona(new_persona)
        self.status_bar.config(text=f"Ready | Active Persona: {self.bot.persona}", fg=self.accent_color)
        self._append_message("Harshit Tyagi Bot", msg, is_user=False)

    def _use_quick_prompt(self, prompt: str):
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, prompt)
        self.send_message()

    def send_message(self):
        query = self.input_entry.get().strip()
        if not query:
            return

        self.input_entry.delete(0, tk.END)
        self._append_message("You", query, is_user=True)
        self.status_bar.config(text="Harshit Tyagi Bot is processing & reasoning...", fg=self.accent_color)
        self.send_btn.config(state=tk.DISABLED)

        # Threading for non-blocking UI
        threading.Thread(target=self._process_bot_response, args=(query,), daemon=True).start()

    def _process_bot_response(self, query: str):
        try:
            response_text = self.bot.get_response(query)
        except Exception as e:
            response_text = f"❌ Error processing query: {e}"

        self.root.after(0, self._handle_bot_response, response_text)

    def _handle_bot_response(self, text: str):
        self._append_message("Harshit Tyagi Bot", text, is_user=False)
        self.status_bar.config(text=f"Ready | Active Persona: {self.bot.persona}", fg=self.muted_text)
        self.send_btn.config(state=tk.NORMAL)

    def _append_message(self, sender: str, text: str, is_user: bool):
        self.chat_display.configure(state=tk.NORMAL)
        self.chat_display.insert(tk.END, "\n")
        
        if is_user:
            header = f"👤 {sender}\n"
            self.chat_display.insert(tk.END, header, "user_header")
            self.chat_display.insert(tk.END, f"{text}\n", "user_msg")
        else:
            header = f"🤖 {sender} ({self.bot.persona})\n"
            self.chat_display.insert(tk.END, header, "bot_header")
            self.chat_display.insert(tk.END, f"{text}\n", "bot_msg")

        self.chat_display.configure(state=tk.DISABLED)
        self.chat_display.see(tk.END)

    def _clear_chat(self):
        self.bot.clear_history()
        self.chat_display.configure(state=tk.NORMAL)
        self.chat_display.delete("1.0", tk.END)
        self.chat_display.configure(state=tk.DISABLED)
        self._send_welcome_message()

    def _open_api_settings(self):
        current_key = self.bot.api_key or ""
        new_key = simpledialog.askstring(
            "Gemini API Key Settings",
            "Enter your Google Gemini API Key (Optional for Gemini 2.5 Flash reasoning):\n(Leave blank to use built-in supercharged offline AI engine)",
            initialvalue=current_key,
            parent=self.root
        )
        if new_key is not None:
            self.bot.set_api_key(new_key)
            if new_key.strip():
                messagebox.showinfo("Harshit Tyagi Bot", "🔑 Gemini API Key updated successfully!")
            else:
                messagebox.showinfo("Harshit Tyagi Bot", "ℹ️ Using built-in supercharged offline AI engine.")


def launch_gui():
    root = tk.Tk()
    app = HarshitTyagiBotGUI(root)
    root.mainloop()


if __name__ == "__main__":
    launch_gui()
