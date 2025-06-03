import httpx
from app.config import settings

headers = {
    "Authorization": f"token {settings.github_token}",
    "Accept": "application/vnd.github+json"
}

async def add_label_to_issue(repo, issue_number, label):
    async with httpx.AsyncClient() as client:
        await client.post(
            f"https://api.github.com/repos/{repo}/issues/{issue_number}/labels",
            json={"labels": [label]},
            headers=headers
        )

async def comment_on_issue(repo, issue_number, label):
    message = {
        "bug": "Thanks for reporting a bug! Please include reproduction steps.",
        "enhancement": "Feature request noted! We'll review it soon.",
        "question": "Thanks for your question! Someone will answer shortly.",
        "needs triage": "Thanks! We'll triage your issue soon.",
    }[label]

    async with httpx.AsyncClient() as client:
        await client.post(
            f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments",
            json={"body": message},
            headers=headers
        )
