from collections import Counter
my_list = [1,2,2,2,3,3,3,3,4,4,4,5,6,6,6,6,6,6,6,5,5,3]
my_freq = Counter(my_list)
print(my_freq,my_list)
top_three = my_freq.most_common(3)
print(top_three)