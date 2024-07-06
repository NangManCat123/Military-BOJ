n=int(input())
arr=list(map(int,input().split()))
sorted_arr=list(sorted(arr))
ilist=[]
for i in arr:
    x=sorted_arr.index(i)
    ilist.append(x)
    sorted_arr[x]=False
print(*ilist)