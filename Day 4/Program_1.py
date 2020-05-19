from collections import Counter

lists = tuple(input('Enter elements of a tuple').split())
h = Counter(lists)
for i in set(lists):
	print('Element',i,'occured',h[i])