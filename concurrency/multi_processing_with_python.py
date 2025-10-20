from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor

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
with ProcessPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(ask_user)
# process = Process(target=complex_calculation)
# process_two = Process(target=ask_user)
# process.start()
# process_two.start()

# process_two.join()
# process.join()
print(f"Two process total time: {time.time()-start}")