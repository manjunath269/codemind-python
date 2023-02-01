n=int(input())
ar=list(map(int,input().split()))
even=0
odd=0
for i in range(0,len(ar),2):
    even=even+ar[i]
for j in range(1,len(ar),2):
    odd=odd+ar[j]
if (odd-even)==0:
    print("YES")
else:
        print("NO")