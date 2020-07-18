l=list(map(int,input().split()))
l=sorted(l)
x=[]
for i in l:
    if i>0:
        x.append(i)
for i in range(len(x)):
    if x[i]==x[i+1]:
        continue
    if x[i]!=(x[i+1]-1):
        print('Missing smallst number is: ',(x[i]+1))
        break
