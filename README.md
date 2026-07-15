# 📈 Automated Stock & News Alert Bot

A Python-based cloud automation script that monitors daily stock performance and sends SMS alerts via Twilio if there is a significant price change (greater than 5%).

This project is fully automated using **GitHub Actions**, running silently every day at 4:30 PM IST (11:00 UTC).

## ✨ Features

* **Live Stock Data:** Integrates with the [Alpha Vantage API](https://www.alphavantage.co/) to track daily market performance.

* **Market News:** Fetches relevant company news headlines via the [NewsAPI](https://newsapi.org/) if the stock price moves significantly.

* **SMS Notifications:** Utilizes the [Twilio API](https://www.twilio.com/docs/sms) to instantly deliver text messages to your phone.

* **Cloud Automation:** Fully automated via a Cron job scheduled through GitHub Actions.

## 🛠️ Tech Stack

* **Language:** Python 3

* **Libraries:** `requests`, `twilio`, `os`

* **APIs:** Alpha Vantage API, NewsAPI, Twilio SMS API

* **CI/CD / Automation:** GitHub Actions (configured to run at 4:30 PM IST daily)

## 🚀 Local Setup and Testing

### 1. Prerequisites

You will need free API keys for the following:

* [Alpha Vantage](https://www.alphavantage.co/) (`STOCK_API_KEY`)

* [NewsAPI](https://newsapi.org/) (`NEWS_API_KEY`)

* [Twilio](https://www.twilio.com/) (`TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN`)

### 2. Run the Script

Ensure you have your environment variables set, then:
