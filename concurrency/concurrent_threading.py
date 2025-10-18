from concurrent.futures import ThreadPoolExecutor
import time

def ask_user():
    start = time.time()
    user_input  = input("Enter you name: ")
    greet = f"Hello,{user_input}"
    print(greet)
    print(f"ask user, {time.time()-start}")

def complex_calculation():
    start = time.time()
    print("Started calculation...\n")
    [x**2 for x in range(29990000)]
    print(f"complex calculation, {time.time()-start}\n")

start = time.time()
ask_user()
complex_calculation()
print(f"sequential execution time: {time.time()-start}")

start = time.time()
with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(ask_user)
    pool.submit(complex_calculation)

print(f"pool thread total time: {time.time()-start}\n")
