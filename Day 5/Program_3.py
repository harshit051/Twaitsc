house = list(map(int,input('Enter house values : ').split()))
print(house)
size = len(house)
i=0
maxv=0
while i<size:
	maxv+=house[i]
	i+=2
print(maxv)