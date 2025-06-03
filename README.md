# 🤖 GitHub Auto-Responder Bot (FastAPI + AWS EC2)

A FastAPI-powered bot that listens to GitHub issue events, automatically applies labels, posts helpful comments, and optionally sends real-time notifications to Slack or Discord. Designed to streamline open-source contribution management and hosted on an AWS EC2 instance with full CI/CD integration.

---

## 🚀 Features

- **Webhook Listener** – Receives and processes GitHub issue events securely.
- **Auto Labeling** – Applies predefined labels based on issue content or repo context.
- **Auto Commenting** – Posts a helpful response or contribution guide on new issues.
- **Slack/Discord Notifications** – Sends live alerts when issues are opened (optional).
- **CI/CD Pipeline** – Auto-deploy on push to `main` using GitHub Actions + SSH.
- **Systemd Integration** – Runs as a persistent background service on EC2.
- **Docker Support** – Fully containerized setup for clean deployment.

---

## ☁️ Hosted on AWS

- **Compute**: AWS EC2 (Ubuntu)
- **Web Server**: FastAPI with Uvicorn
- **Deployment**: GitHub Actions → EC2 via SSH
- **Security**: Webhook secret + GitHub PAT stored in `.env`

---

## 🛠️ Project Structure

```bash
github-auto-responder-bot/
│
├── app/
│   ├── main.py              # FastAPI app entrypoint
│   ├── webhook_handler.py   # GitHub webhook logic
│   └── utils.py             # Label/comment helpers
│
├── .github/workflows/
│   └── deploy.yml           # GitHub Actions CI/CD
│
├── .env.example             # Sample environment config
├── requirements.txt         # Python dependencies
├── Dockerfile               # Optional container support
├── Makefile                 # Project command shortcuts
└── README.md                # You're here


---

🔧 Setup

1. Clone the Repo

git clone https://github.com/your-username/github-auto-responder-bot.git
cd github-auto-responder-bot

2. Create and Activate Virtual Environment

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Create a .env File

GITHUB_TOKEN=ghp_YourTokenHere
WEBHOOK_SECRET=your_webhook_secret
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...

4. Run Locally

uvicorn app.main:app --host 0.0.0.0 --port 8000


---

🛡️ Deploy to AWS EC2

1. SSH into EC2:



ssh -i your-key.pem ubuntu@your-ec2-ip

2. Clone and set up:



git clone https://github.com/your-username/github-auto-responder-bot.git
cd github-auto-responder-bot
cp .env.example .env
# Add your real keys to .env

3. Install dependencies and run:



pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000

4. Or register as a service with systemd.




---

🧪 Webhook Setup

Go to your GitHub repo → Settings → Webhooks

Payload URL: http://your-server-ip/webhook

Content type: application/json

Secret: (same as WEBHOOK_SECRET in .env)

Events: Just the “Issues” event



---

🔄 CI/CD with GitHub Actions

Auto-deploy every time you push to main:

Set secrets in GitHub:

EC2_SSH_KEY

EC2_HOST


Push code → Bot redeploys automatically



---

📈 Future Enhancements

GPT-powered label classification

Contributor leaderboard dashboard

MongoDB/DynamoDB webhook event logging

OAuth integration for multi-repo support



---

📄 License

MIT License. Feel free to fork and customize.


---

🤝 Contributing

Pull requests are welcome. Please format with ruff, check with mypy, and test before committing.


---

Author

Elliot Nzei – Python developer, AWS intern, automation enthusiast

LinkedIn: https://www.linkedin.com/in/elliot-nzei-ba771025b?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app 

GitHub: 

Twitter: 

Portfolio: 
