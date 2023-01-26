n=int(input())
lst=list(map(int,input().split()))
for i in lst:
    print(lst.pop(),end=" ")
for j in lst:
    print(j,end=" ")
