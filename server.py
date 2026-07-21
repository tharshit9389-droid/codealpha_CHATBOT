"""
server.py - Localhost Web Application Server for Harshit Tyagi Bot Pro v2.0
Serves the web application showcase on http://localhost:5000 with REST API endpoints.
"""

import os
import sys
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn

from bot_engine import HarshitTyagiBot

# Windows stdout encoding safeguard
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

app = FastAPI(title="Harshit Tyagi Bot Pro Localhost Server", version="2.0.0")

# Central bot instance
bot_instance = HarshitTyagiBot()


class ChatRequest(BaseModel):
    message: str
    api_key: str = None
    persona: str = "General Assistant"


@app.get("/", response_class=HTMLResponse)
def read_root():
    """Serves the web application showcase for Harshit Tyagi Bot."""
    html_path = os.path.join(os.path.dirname(__file__), "templates", "index.html")
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Harshit Tyagi Bot Pro Localhost Server Running! (index.html missing)</h1>"


@app.post("/api/chat")
def chat_endpoint(request: ChatRequest):
    """API Endpoint to process queries with Harshit Tyagi Bot."""
    if not request.message or not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    if request.api_key and request.api_key.strip():
        bot_instance.set_api_key(request.api_key)

    if request.persona:
        bot_instance.set_persona(request.persona)

    response_text = bot_instance.get_response(request.message)
    return {
        "bot_name": bot_instance.bot_name,
        "version": bot_instance.version,
        "persona": bot_instance.persona,
        "query": request.message,
        "response": response_text,
        "status": "success"
    }


@app.get("/api/personas")
def get_personas():
    """Returns list of available AI personas."""
    return {"personas": list(HarshitTyagiBot.PERSONAS.keys())}


@app.get("/api/status")
def status_endpoint():
    """Health check endpoint."""
    return {
        "status": "online",
        "bot_name": bot_instance.bot_name,
        "version": bot_instance.version,
        "persona": bot_instance.persona,
        "api_key_configured": bool(bot_instance.api_key)
    }


def start_server(host: str = "127.0.0.1", port: int = 5000):
    print(f"\n🚀 Starting Harshit Tyagi Bot Pro Localhost Server...")
    print(f"👉 Access your bot in browser at: http://localhost:{port} or http://{host}:{port}\n")
    uvicorn.run(app, host=host, port=port, log_level="info")


if __name__ == "__main__":
    start_server()
