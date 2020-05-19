arr=[]
for _ in range(int(input('Enter number of vote: '))):
	arr.append(input('Enter name of candidates to vote: '))
narr=[]
for i in set(arr):
	narr.append([arr.count(i),i])
narr.sort()
h = narr[-1][0]
winner=[]
for i in narr:
	if i[0]==h:
		winner.append(i[1])
print('The winner is :',sorted(winner)[0])