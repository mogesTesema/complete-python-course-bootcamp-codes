import time
from datetime import datetime,timezone,timedelta
print(datetime.now(timezone.utc))
today = datetime.now(tz=timezone.utc)

tomorrow = today + timedelta(days=1)
print(today,"\n",tomorrow,"\n", tomorrow-today)
print(today.strftime("%d-%m-%Y %H:%M:%S"))

# user_date = input("Enter the date in YYYY-mm-dd format: ")
# user_date = datetime.strptime(user_date,'%Y-%m-%d')
# print(user_date)

def powers(limit):
    return [x**2 for x in range(limit)]

start = time.time()
powers(991223)
end = time.time()
print(start,end,end-start)

def measure_runtime(func) -> float:
    start = time.time()
    func()
    end = time.time()
    return end-start

measured_time = measure_runtime(lambda:powers(1000000)), # why we pass powerfunction itself? well it don't allow us to pass argument.
print("time taked in second: ",measured_time)

import timeit

print(timeit.timeit("[x**2 for x in range(10)]"))