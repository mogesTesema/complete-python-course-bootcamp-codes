friends_last_seen = {
    "Rolf":31,
    "Jen":1,
    "Anne":7
}
print(id(friends_last_seen))
another_var = friends_last_seen
print(id(another_var)==id(friends_last_seen ))

"""
Immutable data structure function returns new object instead of updatining themself. for example num += 1, in this expression buit in __add__ return 6 new integer instance instead of updating itself. but in mutable object _iadd__, add value to the current values e.g [21,21] + [2,1]
"""
def see_friend(friends,name):
    print(id(friends))
    friends[name] = 0
print(id(friends_last_seen))
print(id(friends_last_seen["Rolf"]))
see_friend(friends_last_seen,"Rolf")
print(id(friends_last_seen))
print(id(friends_last_seen["Rolf"]))

print("IMMUTABLE OBJECT IN PYTHON BEHAVES")

age = 20 
def add_one(current_num):
    current_num += 1

print(id(age))
add_one(age)
print(id(age))

print("MUTABLE OBJECT IN PYTHON BEHAVES")

primes = [2,3,5]
print(id(primes))
primes += [7,11]
print(id(primes))

def mutable(nums):
    print(id(nums))
    nums += [2,2,42,2]
    print(id(nums))

no = [1,2,3,4]
print("mutablity test")
print(id(no),no)
mutable(no)
print(id(no),no)