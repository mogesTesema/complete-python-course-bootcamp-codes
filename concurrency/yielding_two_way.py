from collections import deque
friends = deque(("Rolf","Jose","Charlie","Jen","Anna"))

def get_friend():
    yield from friends
# c = get_friend()
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))

def greet(g):
    index = 0
    while True:
        try:
            friend = next(g)
            yield f"Hello {friend}"
            print(f"{index} done")
            index += 1
        except StopIteration:
            pass

friends_generator = get_friend()
g = greet(friends_generator)
print(next(g))
print(next(g))
print(next(g))
