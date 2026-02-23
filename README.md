Designed with clean architecture principles and production-level error handling suitable for scaling into automated trading systems

# Binance Futures Testnet Trading Bot

Production-ready CLI trading bot for Binance USDT Futures Testnet.

---

## Features

- MARKET orders
- LIMIT orders
- STOP-LIMIT orders (advanced feature)
- BUY / SELL support
- Structured modular architecture
- Centralized logging
- Environment-based credentials
- Proper validation & error handling

---

## Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd trading_bot
2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
Binance Futures Testnet Setup
Create Testnet Account

Go to:
https://testnet.binancefuture.com

Login using your Binance account.

Generate API Keys

Go to API Management

Create API Key

Enable Futures permission

Copy API Key and Secret

Create .env file
cp .env.example .env

Edit .env:

BINANCE_API_KEY=your_key_here
BINANCE_API_SECRET=your_secret_here
Example Commands
MARKET BUY
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
LIMIT SELL
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 65000
STOP-LIMIT BUY
python cli.py --symbol BTCUSDT --side BUY --type STOP_LIMIT --quantity 0.001 --price 64000 --stop-price 64500
Architecture Explanation

client.py → Binance client wrapper

orders.py → Order execution logic

validators.py → Input validation & enums

logging_config.py → Central logging setup

cli.py → CLI entry point

logs/ → Rotating log files

Logging

Logs stored at:

logs/trading_bot.log

Includes:

Order payload

API response

Error traceback

Assumptions

User has Binance Testnet account

Futures trading enabled

USDT-M Futures used

Proper testnet balance available

Security

No credentials hardcoded

Uses .env

.env ignored via .gitignore