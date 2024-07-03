a,b=map(int,input().split())
ilist=[]
x=1
while len(ilist)<=b:
    for _ in range(x):
        ilist.append(x)
    x+=1
print(sum(ilist[a-1:b]))