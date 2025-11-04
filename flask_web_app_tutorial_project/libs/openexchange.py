import requests
import os
# import functools
from cachetools import cached,TTLCache
class OpenExchangeClient:
    ENDPOINT = os.getenv("ENDPOINT")
    # print(f"base_url: {ENDPOINT}")
    def __init__(self):
        self.app_id = os.getenv("APP_ID")
        # print(f"app_id: {self.app_id}")
    @property
    # @functools.lru_cache(maxsize=2)
    @cached(cache=TTLCache(maxsize=2,ttl=900))
    def latest(self):
        return requests.get(f"{self.ENDPOINT}?app_id={self.app_id}").json()

    def convert(self,from_amount,from_currency,to_currency):
        rates = self.latest["rates"]
        # print(f"rates:{rates}")
        to_rate = rates[to_currency]
        # print(f"to rate: {to_rate}")

        if from_currency == 'USD':
            return from_amount * to_rate
        else:
            from_in_usd = from_amount/rates[from_currency]
            return from_in_usd * to_rate



