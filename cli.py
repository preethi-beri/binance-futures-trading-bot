import argparse
import sys

from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


def get_interactive_input():
    print("\n========== Binance Futures Trading Bot ==========\n")

    symbol = input("Enter Symbol (e.g. BTCUSDT): ").upper()
    side = input("Enter Side (BUY/SELL): ").upper()
    order_type = input("Enter Order Type (MARKET/LIMIT): ").upper()
    quantity = float(input("Enter Quantity: "))

    price = None

    if order_type == "LIMIT":
        price = float(input("Enter Price: "))

    return symbol, side, order_type, quantity, price


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Trading Bot"
    )

    parser.add_argument("--symbol")
    parser.add_argument("--side")
    parser.add_argument("--type")
    parser.add_argument("--qty", type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        # Interactive Mode
        if len(sys.argv) == 1:
            symbol, side, order_type, quantity, price = (
                get_interactive_input()
            )

        # CLI Argument Mode
        else:
            if not all([
                args.symbol,
                args.side,
                args.type,
                args.qty
            ]):
                raise ValueError(
                    "Missing required command-line arguments."
                )

            symbol = args.symbol
            side = args.side
            order_type = args.type
            quantity = args.qty
            price = args.price

        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)

        if order_type.upper() == "LIMIT":
            validate_price(price)

        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {quantity}")

        if price:
            print(f"Price    : {price}")

        if order_type.upper() == "MARKET":
            response = place_market_order(
                symbol,
                side,
                quantity
            )

        else:
            response = place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        print("\n========== ORDER RESPONSE ==========")
        print(f"Order ID      : {response.get('orderId')}")
        print(f"Status        : {response.get('status')}")
        print(f"Executed Qty  : {response.get('executedQty')}")
        print(f"Avg Price     : {response.get('avgPrice')}")
        print("\nSUCCESS")

    except Exception as e:
        print("\n❌ ORDER FAILED")
        print(f"Reason: {e}")


if __name__ == "__main__":
    main()