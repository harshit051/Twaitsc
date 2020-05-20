from itertools import combinations

weight = list(map(int,input("enter weights:").split()))
value = list(map(int,input("enter values:").split()))
maxweight = int(input("Enter Max Weight: "))
dict={}
h=[]
for i in range(len(weight)):
	dict[weight[i]]=value[i]
	for j in combinations(weight,i+1):
		if sum(j)<=maxweight:
			h.append(j)
mvalue=0
for i in h:
	temp=0
	for j in i:
		temp+=dict[j]
	if temp>mvalue:
		mvalue=temp
print(mvalue)