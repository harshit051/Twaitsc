from itertools import permutations

n = input('Enter a String :')
for i in permutations(n):
  print(''.join(i))
  