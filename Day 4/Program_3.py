di=dict()
for _ in range(int(input('Enter the Number of values you want:'))):
	key = input('Enter The key : ')
	di[key] = int(input('Enter the value: '))
lists=list(di.values())
for i in (sorted(lists))[::-1]:
	if i<max(lists):
		print('Second highest value is ',i)
		break