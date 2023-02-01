n=int(input())
lst=list(map(int,input().split()))
for i in lst:
    cnt=0
    for j in lst:
        if i>j:
            cnt+=1
    print(cnt ,end=" ")
