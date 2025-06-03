from fastapi import FastAPI, Request
import hmac, hashlib
import os

app = FastAPI()

GITHUB_SECRET = os.getenv("webhook_secret")

@app.post("/webhook")
async def webhook_handler(request: Request):
    body = await request.body()
    signature = request.headers.get("X-Hub-Signature-256")
    expected_signature = 'sha256=' + hmac.new(GITHUB_SECRET.encode(), body, hashlib.sha256).hexdigest()

    if not hmac.compare_digest(signature, expected_signature):
        return {"status": "unauthorized"}

    payload = await request.json()
    # Handle GitHub issue event here...
    return {"status": "ok"}