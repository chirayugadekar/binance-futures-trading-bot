import logging
from typing import Any, Dict, Optional

from binance.exceptions import BinanceAPIException
from requests.exceptions import RequestException

from .validators import OrderSide, OrderType


logger = logging.getLogger(__name__)


class OrderExecutionError(Exception):
    """Raised when order execution fails."""


class OrderManager:
    """
    Handles order placement logic.
    """

    def __init__(self, client) -> None:
        self.client = client

    def place_order(
        self,
        symbol: str,
        side: OrderSide,
        order_type: OrderType,
        quantity: float,
        price: Optional[float] = None,
        stop_price: Optional[float] = None,
    ) -> Dict[str, Any]:

        order_payload = {
            "symbol": symbol.upper(),
            "side": side.value,
            "type": order_type.value,
            "quantity": quantity,
        }

        if order_type == OrderType.LIMIT:
            order_payload.update(
                {
                    "price": price,
                    "timeInForce": "GTC",
                }
            )

        if order_type == OrderType.STOP_LIMIT:
            order_payload.update(
                {
                    "type": "STOP",
                    "price": price,
                    "stopPrice": stop_price,
                    "timeInForce": "GTC",
                }
            )

        logger.info(f"Order Request Payload: {order_payload}")

        try:
            response = self.client.futures_create_order(**order_payload)
            logger.info(f"API Response: {response}")
            return response

        except BinanceAPIException as e:
            logger.exception("Binance API error occurred.")
            raise OrderExecutionError(f"Binance API Error: {e.message}")

        except RequestException as e:
            logger.exception("Network error occurred.")
            raise OrderExecutionError("Network error. Please check connection.")

        except Exception as e:
            logger.exception("Unexpected error occurred.")
            raise OrderExecutionError(str(e))