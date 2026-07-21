"""
main.py - Harshit Tyagi Bot Unified Application Launcher
Allows launching the Localhost Web Server, Desktop Tkinter GUI, or both simultaneously.
"""

import sys
import time
import threading
import argparse

# Windows console encoding fix
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass


def run_web_server():
    """Launches Localhost Web Server on port 5000."""
    from server import start_server
    start_server(host="127.0.0.1", port=5000)


def run_desktop_gui():
    """Launches Tkinter Desktop GUI."""
    from gui_app import launch_gui
    launch_gui()


def main():
    parser = argparse.ArgumentParser(description="Harshit Tyagi Bot - Multi-Type Problem Solver Launcher")
    parser.add_argument(
        "mode",
        nargs="?",
        default="both",
        choices=["web", "desktop", "both"],
        help="Mode to run: 'web' (Localhost Server), 'desktop' (Tkinter GUI), or 'both' (default)"
    )

    args = parser.parse_args()

    print("==================================================")
    print("      🤖 HARSHIT TYAGI BOT - LAUNCHER")
    print("==================================================")

    if args.mode == "web":
        print("🌐 Mode: Localhost Web Server (http://localhost:5000)")
        run_web_server()

    elif args.mode == "desktop":
        print("💻 Mode: Desktop Tkinter GUI Application")
        run_desktop_gui()

    elif args.mode == "both":
        print("🚀 Mode: Launching BOTH Localhost Web Server & Desktop Tkinter GUI!")
        print("👉 Localhost URL: http://localhost:5000")
        
        # Start Web server in daemon background thread
        web_thread = threading.Thread(target=run_web_server, daemon=True)
        web_thread.start()
        
        # Give server a moment to bind to port
        time.sleep(1.5)

        # Start Desktop GUI on main thread
        run_desktop_gui()


if __name__ == "__main__":
    main()
