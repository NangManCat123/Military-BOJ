n,k=map(int,input().split())
arr=list(map(int,input().split(",")))
for _ in range(k):
    for i in range(n-1):
        arr[i]=arr[i+1]-arr[i]
    arr.pop()
    n-=1
print(",".join(map(str,arr)))