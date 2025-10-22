from types import coroutine
from collections import deque
friends = deque(("Rolf","Jose","Charlie","Jen","Anna"))

def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f"{greeting} {friend}")

async def greet_two(g):
    # yield from g
    # print("starting...")
    await g
    # print("ending>")


greeter = greet_two(friend_upper())
greeter.send(None)
greeter.send("Ello")
greeter.send("Hi")
greeter.send("good Moring")
print("Ello! multitasking...")
greeter.send("good afternoon")
