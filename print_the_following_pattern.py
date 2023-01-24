def fun(row):
    for i in range(1,row+1):
        print(chr(64+row),end=" ")
    print()
row=int(input())
while row:
  fun(row)
  row=row-1
