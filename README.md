# Binance Futures Trading Bot

## Overview

A modular Python-based command-line trading bot designed to interact with the Binance Futures Testnet (USDT-M). The application allows users to place MARKET and LIMIT orders through a simple CLI interface while maintaining clean code architecture, robust validation, structured logging, and comprehensive error handling.

The bot not only places orders but also retrieves the final order status after execution, providing accurate execution details such as status, executed quantity, and average execution price.

This project was developed as part of a technical assessment to demonstrate API integration, software design principles, and Python development best practices.

---

## Key Features

### Trading Functionality

* Place MARKET orders on Binance Futures Testnet
* Place LIMIT orders on Binance Futures Testnet
* Support for both BUY and SELL order sides
* Real-time order submission through Binance Futures API
* Retrieve final order execution details after placement

### Input Validation

* Validates order side (BUY / SELL)
* Validates order type (MARKET / LIMIT)
* Validates quantity values
* Validates price input for LIMIT orders

### Logging & Monitoring

* Logs API requests and responses
* Records successful order placements
* Tracks final order execution status
* Captures exceptions and API failures
* Stores logs in a dedicated log file for auditing and debugging

### Error Handling

* Handles invalid user inputs
* Handles Binance API exceptions
* Handles network and connectivity issues
* Provides meaningful user-friendly error messages

### Command Line Interface

* Simple and intuitive CLI-based interaction
* Supports parameterized command execution using command-line arguments

---

## Technology Stack

* Python 3.x
* Binance Futures API
* python-binance
* python-dotenv
* requests
* argparse
* logging

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py             # Binance API client configuration
│   ├── orders.py             # Order placement and tracking logic
│   ├── validators.py         # Input validation utilities
│   └── logging_config.py     # Logging configuration
│
├── logs/
│   └── trading_bot.log       # Application logs
│
├── sample_logs/
│   ├── market_order.log
│   └── limit_order.log
│
├── cli.py                    # Command-line entry point
├── requirements.txt          # Project dependencies
├── README.md                 # Project documentation
├── .env                      # API credentials (excluded from Git)
└── .gitignore
```

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd trading_bot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## API Configuration

Create a `.env` file in the project root directory and add your Binance Futures Testnet API credentials:

```text
API_KEY=your_api_key
API_SECRET=your_api_secret
```

> Note: Never commit your API credentials to a public repository.

---

## Usage Examples

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001
```

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 90000
```

---

## Sample Output

```text
========== ORDER REQUEST ==========
Symbol   : BTCUSDT
Side     : BUY
Type     : MARKET
Quantity : 0.001

========== ORDER RESPONSE ==========
Order ID      : 13711471895
Status        : FILLED
Executed Qty  : 0.0010
Avg Price     : 70936.700000

SUCCESS
```

---

## Logging Example

```text
2026-06-01 21:04:05,943 - INFO - MARKET ORDER: BUY 0.001 BTCUSDT
2026-06-01 21:04:06,984 - INFO - Response: {...}
2026-06-01 21:04:08,121 - INFO - Final Order Status: FILLED
```

---

## Assumptions

* Binance Futures Testnet or Demo Trading environment is accessible.
* Valid API credentials are configured in the `.env` file.
* User has the required permissions to create orders on the testnet account.

---

## Future Enhancements

* Stop-Limit Order Support
* OCO Order Support
* Interactive CLI Menus
* Portfolio Monitoring
* Position Management
* Trade History Dashboard
* Web-Based User Interface

---

## Author

**Preethi Beri**

Python Developer Assessment Submission
