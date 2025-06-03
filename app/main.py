from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import hmac, hashlib, os, json

app = FastAPI()

# Load secrets
GITHUB_SECRET = os.getenv("webhook_secret", "")
LOG_FILE_PATH = "logs/output.log"

# Mount frontend
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
async def serve_dashboard():
    return FileResponse("frontend/index.html")


# Webhook Handler
@app.post("/webhook")
async def webhook_handler(request: Request):
    body = await request.body()
    signature = request.headers.get("X-Hub-Signature-256")
    expected_signature = 'sha256=' + hmac.new(GITHUB_SECRET.encode(), body, hashlib.sha256).hexdigest()

    if not hmac.compare_digest(signature, expected_signature):
        log_event("Unauthorized access attempt.")
        return {"status": "unauthorized"}

    payload = await request.json()
    # Do GitHub bot logic here...
    issue = payload.get("issue", {}).get("title", "unknown")
    action = payload.get("action", "unknown")

    log_event(f"Received webhook: action={action}, issue={issue}")
    return {"status": "ok"}


# Logs API
@app.get("/api/logs")
async def get_logs():
    if not os.path.exists(LOG_FILE_PATH):
        return "No logs found."
    with open(LOG_FILE_PATH, "r") as f:
        return f.read()


# Stats API (stubbed for now)
@app.get("/api/stats")
async def get_stats():
    return {
        "issues_handled": count_log_entries("Received webhook"),
        "labels_applied": count_log_entries("Label applied")
    }


# Internal Logging Helper
def log_event(message: str):
    os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)
    with open(LOG_FILE_PATH, "a") as log:
        log.write(f"{message}\n")


# Simple parser to count events
def count_log_entries(keyword: str) -> int:
    if not os.path.exists(LOG_FILE_PATH):
        return 0
    with open(LOG_FILE_PATH, "r") as f:
        return sum(1 for line in f if keyword in line)