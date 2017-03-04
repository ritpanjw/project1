"""
template==
Take 2 list randomly and then remove the matching integers and then remove the duplicates.
"""

import random
a=random.sample(range(10), 6)
b=random.sample(range(10), 7)
k=[]

"""
for i in a:
	for j in b:
		if i!=j:
			continue
		else:
			k.append(i)

k=set(k)
k=list(k)
print k
"""

[k.append(i) for i in a for j in b if i==j]
k=set(k)
k=list(k)
print k
