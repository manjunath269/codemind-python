def fun(n):
    d=0
    while n:
        r=n%10
        d=d*10+r
        n=n//10
    return d
n=int(input())
if n<0:
    pos=n*-1
    neg=fun(pos)
    print(-neg)
else:
    rev=fun(n)
    print(rev)
