n=int(input())
lst=list(map(int,input().split()))
flag=1
for i in lst:
    cnt=0
    for j in lst:
        if i==j:
            cnt+=1
    if cnt==1:
        print(i, end=" ")
        flag=0
if flag:
    print("-1")