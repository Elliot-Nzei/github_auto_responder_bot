def classify_issue(body: str) -> str:
    text = body.lower()
    if "crash" in text or "error" in text or "bug" in text:
        return "bug"
    elif "feature" in text or "request" in text:
        return "enhancement"
    elif "how" in text or "help" in text or "?" in text:
        return "question"
    else:
        return "needs triage"
