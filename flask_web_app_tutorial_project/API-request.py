from libs.openexchange import OpenExchangeClient
import time
client = OpenExchangeClient()
start_time = time.time()
usd_etb = client.convert(1000,'GBP','ETB')
end_time = time.time()
print(f"time taken: {end_time - start_time}")
print(usd_etb)


start_time = time.time()
usd_etb = client.convert(1000,'GBP','ETB')
end_time = time.time()
print(f"time taken: {end_time - start_time}")
print(usd_etb)


start_time = time.time()
usd_etb = client.convert(1000,'GBP','ETB')
end_time = time.time()
print(f"time taken: {end_time - start_time}")
print(usd_etb)


start_time = time.time()
usd_etb = client.convert(1000,'GBP','ETB')
end_time = time.time()
print(f"time taken: {end_time - start_time}")
print(usd_etb)

