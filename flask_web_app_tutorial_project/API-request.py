from libs.openexchange import OpenExchangeClient
client = OpenExchangeClient()
usd_etb = client.convert(1000,'GBP','ETB')
print(usd_etb)
