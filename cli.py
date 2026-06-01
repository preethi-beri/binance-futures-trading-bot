import argparse
from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--qty", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.qty)

        if args.type.upper() == "LIMIT":
            validate_price(args.price)

        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.qty}")

        if args.price:
            print(f"Price    : {args.price}")

        if args.type.upper() == "MARKET":
            response = place_market_order(
                args.symbol,
                args.side,
                args.qty
            )

        else:
            response = place_limit_order(
                args.symbol,
                args.side,
                args.qty,
                args.price
            )

        print("\n========== ORDER RESPONSE ==========")
        print(f"Order ID      : {response.get('orderId')}")
        print(f"Status        : {response.get('status')}")
        print(f"Avg Price     : {response.get('avgPrice')}")
        print(f"Executed Qty  : {response.get('executedQty')}")
        print("\nSUCCESS")

    except Exception as e:
        print(f"\nERROR: {e}")


if __name__ == "__main__":
    main()