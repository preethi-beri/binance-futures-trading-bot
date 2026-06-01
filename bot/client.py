from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

client = Client(
    os.getenv("API_KEY"),
    os.getenv("API_SECRET"),
    testnet=True
)

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"