di=dict()
di1=dict()
for _ in range(int(input('Enter the Number of values you want:'))):
	key = input('Enter The key : ')
	value = int(input('Enter the value: '))
	di[key]=value
	if value not in di1.values():
		di1[key]=value

print('New dictionary :',di1)