from itertools import permutations

lists = list(map(int,input('Enter elements of a list ').split()))
sset = set(lists)
sset.add(sum(lists))

for i in range(2,len(lists)):
	for j in permutations(lists,i):
		sset.add(sum(j))
num=1
while 1:
	if num not in sset:
		print('the least integer is ',num)
		break

	num+=1