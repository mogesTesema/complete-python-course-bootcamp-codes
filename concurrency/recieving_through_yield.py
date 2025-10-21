def greet():
    friend = yield
    print(f"Hello,  {friend}")

# g = greet()
# g.send(None) # priming the genrator
# g.send("Adam")

from collections import deque
friends = deque(("Rolf","Jose","Charlie","Jen","Anna"))

def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f"{greeting} {friend}")

def greet_two(g):
    # g.send(None)
    # while True:
    #     greeting = yield
    #     g.send(greeting)
    yield from g

greeter = greet_two(friend_upper())
greeter.send(None)
greeter.send("Ello")
greeter.send("Hi")
greeter.send("good Moring")
print("Ello! multitasking...")
greeter.send("good afternoon")
