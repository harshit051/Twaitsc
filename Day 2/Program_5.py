def add_star(h):
	d=''
	for i in h:
		d+=i+'*'
	return d[:-1]

for i in range(3,0,-1):
	print(add_star(str(i)*i))

for i in range(1,4):
	print(add_star(str(i)*i))
