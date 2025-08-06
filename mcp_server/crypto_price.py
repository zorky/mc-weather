import requests

from langchain.tools import tool

import logging
from logger import init_logger
logger = init_logger(level=logging.DEBUG)

@tool
def get_crypto_price(symbol: str) -> str:
    """Donne le cours actuel d'une crypto (ex: BTC, ETH)."""
    logger.debug(f"Crypto price pour {symbol}")
    # https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR&e=CCCAGG
    url = f"https://min-api.cryptocompare.com/data/price?fsym={symbol.lower()}&tsyms=EUR,USD&e=CCCAGG"
    # params = {"fsym": symbol.lower(), "tsyms": "EUR,USD", "e": "CCCAGG"}
    logger.debug(f"url: {url}")
    # logger.debug(f"params: {params}")
    try:
        # r = requests.get(url, params=params)
        r = requests.get(url)
        data = r.json()
        price = data.get(symbol, {}).get("EUR")
        if price:
            return_response = f"Le cours de {symbol.upper()} est de {price} €"
            logger.debug(return_response)
            return return_response
        return f"Crypto non trouvée : {symbol}"
    except Exception as e:
        return f"Erreur crypto : {str(e)}"
