dic={"0":4,"1":2}
for i in range(2,10):
    dic[str(i)]=3
while True:
    ilist=list(input())
    if ilist[0]=="0" and len(ilist)==1:
        break
    sum=len(ilist)+1
    for i in ilist:
        sum+=dic[i]
    print(sum)