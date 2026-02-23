import os
from binance.client import Client
from dotenv import load_dotenv


class BinanceFuturesClient:
    """
    Wrapper for Binance Futures Testnet client.
    """

    BASE_URL = "https://testnet.binancefuture.com"

    def __init__(self) -> None:
        load_dotenv()

        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise EnvironmentError(
                "API keys not found. Please configure .env file."
            )

        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = self.BASE_URL

    def get_client(self) -> Client:
        return self.client