import sys
input=sys.stdin.readline
n=int(input())
iset=set(input().strip() for _ in range(n))
resset=set()
for i in iset:
    count=0
    for j in iset:
        if i[0] == j[0]:
            count+=1
    if count>=5:
            resset.add(i[0])
if len(resset)==0:
    print("PREDAJA")
else:
    print("".join(sorted(list(resset))))