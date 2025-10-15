
"""
* counter
* defaultdict
* ordereddict
* namedtuple
* deque
"""
from collections import Counter,defaultdict,OrderedDict,namedtuple,deque
nums = [12,2,32,3,3,3,1,2]
counted = Counter(nums)
print(counted)
student = defaultdict(int,10)
print(student["hello"])