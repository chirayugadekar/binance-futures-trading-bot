import argparse
import logging

from bot.client import BinanceFuturesClient
from bot.logging_config import setup_logging
from bot.orders import OrderManager, OrderExecutionError
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
    ValidationError,
    OrderType,
)


def main() -> None:
    setup_logging()
    logger = logging.getLogger("CLI")

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)
    parser.add_argument("--stop-price", type=float)

    args = parser.parse_args()

    try:
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        if order_type == OrderType.STOP_LIMIT and not args.stop_price:
            raise ValidationError("STOP_LIMIT requires --stop-price.")

        client = BinanceFuturesClient().get_client()
        manager = OrderManager(client)

        print("\n📌 Order Summary:")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {side.value}")
        print(f"Type: {order_type.value}")
        print(f"Quantity: {quantity}")
        if price:
            print(f"Price: {price}")
        if args.stop_price:
            print(f"Stop Price: {args.stop_price}")

        response = manager.place_order(
            symbol=args.symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
            stop_price=args.stop_price,
        )

        print("\n✅ Order Placed Successfully!")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice')}")

    except ValidationError as e:
        logger.error(str(e))
        print(f"\n❌ Validation Error: {e}")

    except OrderExecutionError as e:
        logger.error(str(e))
        print(f"\n❌ Order Failed: {e}")

    except Exception as e:
        logger.exception("Unhandled error.")
        print("\n❌ Unexpected error occurred.")


if __name__ == "__main__":
    main()