n=(int)(input('Enter Nth term of fabonacci series'))
def fabi(n):
  if n==0 or n==1:
    return n
  return (fabi(n-1)+fabi(n-2))
for i in range(n+1):
  print(fabi(i),end=' ')
