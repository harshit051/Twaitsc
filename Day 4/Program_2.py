lists=[]
for _ in range(int(input('enter number of elements '))):
	lists.append(tuple(input('Enter elements').split()))
n=int(input('Enter index value to sort the list:'))
print(lists)
print(sorted(lists[n-1:])+sorted(lists[:n-1]))