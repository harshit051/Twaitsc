for i in range(8):
	h=' '*i+'*'+' '*(7-i)
	print(h+h[::-1])
for i in range(n):
	h=' '*(7-i)+'*'+' '*i
	print(h+h[::-1])