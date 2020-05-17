for i in range(5):
	h='* '*(5-i)+'  '*i
	print(h+h[::-1])

for i in range(1,6):
	h='* '*i+'  '*(5-i)
	print(h+h[::-1])