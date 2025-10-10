import math
import random
ceils = math.ceil(2.8)
print(ceils)
my_list = list(range(0,21))
print(random.choice(my_list))
print(random.choices(population=my_list,k=10))
print(my_list)
random.shuffle(my_list)
print(my_list)
random_uniform = random.uniform(a=0,b=100)
random_normal = random.gauss(mu=0,sigma=1)
print(random_uniform,random_normal)