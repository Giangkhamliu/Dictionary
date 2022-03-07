a=['Class-V','Class-VI','Class-VII','Class-VIII']
b=[1, 2, 2, 3]
from collections import defaultdict
temp = defaultdict(set)
for c, i in zip(a, b):
    temp[c].add(i)
print(temp)                                               