ar = list(map(int,input('Enter number : ').split()))
size = len(ar)
for i in range(size-1):
	ar[i]=max(ar[i+1:])
ar[-1]=-1
print(ar)