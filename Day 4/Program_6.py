h=[]
for _ in range(int(input('Enter number of words: '))):
	h.append(input('Enter word: '))
d = input('Enter character set seperated by a space: ').split()
ha=[]
for word in h:
	if set(word).issubset(set(d)):
		ha.append(word)
print(", ".join(ha),end='.')