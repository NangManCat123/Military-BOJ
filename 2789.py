cambridge=set("CAMBRIDGE")
ilist=list(input())
reslist=[]
for i in ilist:
    if i not in cambridge:
        reslist.append(i)
print("".join(reslist))