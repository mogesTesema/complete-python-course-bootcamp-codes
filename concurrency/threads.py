import time
from threading import Thread
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
print(f"Singe thread total time: {time.time()-start}\n")



thread_one = Thread(target=complex_calculation)
thread_two = Thread(target=ask_user)

start = time.time()

thread_one.start()
thread_two.start()

thread_one.join()
thread_two.join()
print(f"Two thread total time:{time.time()-start} \n")
