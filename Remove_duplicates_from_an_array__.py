n=int(input())
a=map(int,input().split())
b=[]
for i in a:
    if i not in b:
        b.append(i)
        print(i,end=" ")
        
