import hmac
import hashlib
from fastapi.responses import JSONResponse
from app.issue_classifier import classify_issue
from app.github_api import comment_on_issue, add_label_to_issue
from app.config import settings

async def handle_webhook(payload, headers):
    # Verify GitHub signature
    signature = headers.get("X-Hub-Signature-256")
    if not verify_signature(payload, signature):
        return JSONResponse(status_code=403, content={"error": "Invalid signature"})

    if payload.get("action") == "opened" and "issue" in payload:
        issue = payload["issue"]
        repo = payload["repository"]["full_name"]
        issue_number = issue["number"]
        body = issue.get("body", "")

        category = classify_issue(body)
        await add_label_to_issue(repo, issue_number, category)
        await comment_on_issue(repo, issue_number, category)

    return {"status": "OK"}

def verify_signature(payload, signature):
    if not signature:
        return False
    mac = hmac.new(settings.webhook_secret.encode(), msg=str(payload).encode(), digestmod=hashlib.sha256)
    return hmac.compare_digest(f"sha256={mac.hexdigest()}", signature)
# This function verifies the signature of the incoming webhook payload
# using the secret configured in the settings.