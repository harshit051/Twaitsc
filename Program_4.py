from itertools import permutations
l=(["".join(x) for x in permutations('218765')])
l=sorted(l)
for i  in l:
    if i>'218765':
        print(i)
        break;
