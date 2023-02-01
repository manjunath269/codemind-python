n=int(input())
lst=list(map(int,input().split()))
flag=0
b=[]
for i in lst:
    cnt=0
    for j in lst:
        if i==j:
            cnt+=1
    if cnt==1:
        b.append(i)
        flag=1
if flag!=0:
    print(max(b))
else:
        print("-1")
