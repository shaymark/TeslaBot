# 📈 Tesla Stock Price Bot – Daily WhatsApp Updates

This project is a Python-based automation bot that fetches the **Tesla (TSLA)** stock price every day at **17:00 (Israel Time)** and sends it to your **WhatsApp** using **Twilio's WhatsApp Sandbox** and **GitHub Actions**.

## 🚀 Features

- ✅ Fetches real-time TSLA stock price from Yahoo Finance
- ✅ Sends daily update to your WhatsApp number
- ✅ Uses Twilio API and GitHub Actions (free tier)
- ✅ Runs entirely in the cloud – no local machine needed

---

## 🛠 Requirements

- Python 3.8+
- A [Twilio](https://www.twilio.com/) account (free)
- GitHub account (for scheduled actions)

---

## 📦 Installation (Local Dev)

1. **Clone the repo**

```bash
git clone https://github.com/your-username/tesla-stock-bot.git
cd tesla-stock-bot
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2. **Create `.env` file**

```env
TWILIO_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
MY_WHATSAPP=whatsapp:+9725XXXXXXX
```

> 💡 Make sure you’ve joined the Twilio WhatsApp Sandbox by sending a code like `join great-iguana` to `+14155238886` from your WhatsApp.

3. **Run it manually**

```bash
python send_tesla_price.py
```

---

## ☁️ Cloud Automation with GitHub Actions

1. Go to **Settings > Secrets and variables > Actions** in your repo
2. Add the following **repository secrets**:

| Secret Name          | Value                                   |
|----------------------|-----------------------------------------|
| `TWILIO_SID`         | Your Twilio Account SID                 |
| `TWILIO_AUTH_TOKEN`  | Your Twilio Auth Token                  |
| `MY_WHATSAPP`        | Your WhatsApp number with `whatsapp:` prefix (e.g., `whatsapp:+9725XXXXXXX`) |

3. GitHub Actions will automatically run the bot daily at **17:00 Israel Time** (14:00 UTC)

To run it manually from GitHub:
- Go to the **Actions** tab → select workflow → **Run workflow**

---

## 📁 Project Structure

```
tesla-stock-bot/
├── send_tesla_price.py           # Main Python script
├── .env                          # Your local environment variables (optional)
├── requirements.txt              # Python dependencies
└── .github/
    └── workflows/
        └── send_whatsapp.yml     # GitHub Actions workflow file
```

---

## 🧪 Example Output

A typical WhatsApp message will look like this:

```
📈 Tesla (TSLA) closing price on 2025-06-07: $187.23
```

---

## 🔐 Notes

- You can only send WhatsApp messages to numbers you’ve verified in Twilio Sandbox (for free accounts).
- Want multiple stocks? Add more tickers using `yfinance`.

---

## 📃 License

MIT License – free to use and modify.

---

## 🙌 Acknowledgments

- [Twilio](https://www.twilio.com/whatsapp)
- [Yahoo Finance API via yfinance](https://pypi.org/project/yfinance/)
- [GitHub Actions](https://docs.github.com/en/actions)

---
