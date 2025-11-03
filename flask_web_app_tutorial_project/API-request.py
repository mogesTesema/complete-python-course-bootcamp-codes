import requests
import os


APP_ID = os.getenv("APP_ID")
ENDPOINT = os.getenv("ENDPOINT")
print("Endpoint and app_id: ",ENDPOINT,APP_ID,"\n"*5)

response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
exchange_rate = response.json()["rates"]
usd_amount = 10000
gbp_amount = usd_amount * exchange_rate["GBP"]
eth_amount = usd_amount * exchange_rate["ETB"]
print(f"Ethipia:{eth_amount}")
print(f"GBP: {gbp_amount}")