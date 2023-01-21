n=int(input())
sum1=0
pro=1
while n>0:
    r=n%10
    sum1=r+sum1
    pro=pro*r
    n=n//10
print(pro-sum1)
