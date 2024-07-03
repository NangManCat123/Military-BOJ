n,m=map(int,input().split())
arr=[]
width=[]
length=[]
for i in range(n):
    x=list(input())
    if not "X" in x:
        width.append(i)
    arr.append(x)
for i in range(m):
    stack=[]
    for l in arr:
        stack.append(l[i])
    if "X" not in stack:
        length.append(i)
print(max(len(width),len(length)))