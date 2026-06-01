from binance.enums import *
from bot.client import client
from bot.logging_config import logger


def place_market_order(symbol, side, quantity):
    try:
        logger.info(f"MARKET ORDER: {side} {quantity} {symbol}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_MARKET,
            quantity=quantity
        )

        logger.info(f"Response: {order}")
        return order

    except Exception as e:
        logger.error(f"Error placing market order: {e}")
        raise


def place_limit_order(symbol, side, quantity, price):
    try:
        logger.info(
            f"LIMIT ORDER: {side} {quantity} {symbol} at {price}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_LIMIT,
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"Response: {order}")
        return order

    except Exception as e:
        logger.error(f"Error placing limit order: {e}")
        raise