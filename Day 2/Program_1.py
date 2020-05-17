n=(int)(input('Enter the nummber'))
if n%2:
  print('Number is EVEN')
else:
  print('Number is ODD')
for i in range(2,n):
  if n%i==0:
    break
else:
  print('Number is prime')

num=n
rev=0
rem=0
while num>0:
  rem=num%10
  rev=rev*10+rem
  num=num//10
if rev==n:
  print('palindrome')
else:
  print('Not palindrome')
num1=n
rev=0
while num1>0:
  rem=num1%10
  rev+=rem**3
  num1=num1//10

if rev==n:
  print('Armstrong')
else:
  print('Not Armstrong')
