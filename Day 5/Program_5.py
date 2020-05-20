array = list(map(int,input('Enter number : ').split()))

odd=[]
even=[]
for i in array:
	if i%2==0:
		even.append(i)
	else:
		odd.append(i)
array=sorted(odd,reverse=True)+sorted(even)
print(array)