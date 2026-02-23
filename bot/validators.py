from enum import Enum


class OrderSide(str, Enum):
    BUY = "BUY"
    SELL = "SELL"


class OrderType(str, Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"
    STOP_LIMIT = "STOP_LIMIT"


class ValidationError(Exception):
    """Raised when user input validation fails."""


def validate_side(side: str) -> OrderSide:
    try:
        return OrderSide(side.upper())
    except ValueError:
        raise ValidationError("Invalid side. Must be BUY or SELL.")


def validate_order_type(order_type: str) -> OrderType:
    try:
        return OrderType(order_type.upper())
    except ValueError:
        raise ValidationError(
            "Invalid order type. Must be MARKET, LIMIT, or STOP_LIMIT."
        )


def validate_quantity(quantity: float) -> float:
    if quantity <= 0:
        raise ValidationError("Quantity must be greater than 0.")
    return quantity


def validate_price(price: float | None, order_type: OrderType) -> float | None:
    if order_type == OrderType.LIMIT and price is None:
        raise ValidationError("Price is required for LIMIT orders.")
    return price