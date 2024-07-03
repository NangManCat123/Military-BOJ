a,b=input().split()
a=list(map(int,a))
b=list(map(int,b))
print(a,b)
alist,blist=[],[]
for i in range(1,10):
    alist.append(a.count(i))
    blist.append(b.count(i))
sum=0
for i in range(1,10):
    for j in range(1,10):
        sum+=j*blist[j-1]*i*alist[i-1]
print(sum)