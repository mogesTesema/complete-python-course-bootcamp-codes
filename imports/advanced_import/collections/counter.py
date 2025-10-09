from collections import Counter
from collections import defaultdict
my_list = [1,2,2,2,3,3,3,3,4,4,4,5,6,6,6,6,6,6,6,5,5,3]
my_freq = Counter(my_list)
print(my_freq,my_list)
top_three = my_freq.most_common(3)
print(top_three)
# python default dictionary
default_d = defaultdict(lambda:10)
default_d["correct"] = 100
print(default_d["correct"])
print(default_d["wrong_key"])
