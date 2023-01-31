n,d=map(int,input().split())
dig = 0
cnt=0
for i in str(n):
         dig=dig*10+int(i)
         cnt=cnt+1
         if cnt==d:
             break
pow1=10**d
rem=n%pow1
print(abs(rem-dig))