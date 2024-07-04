n=int(input())
for i in range(1,n):
    print("*"*i,end="")
    print(" "*((2*n)-2*i),end="")
    print("*"*i)
print("*"*(2*n))
for i in range(n-1,0,-1):
    print("*"*i,end="")
    print(" "*((2*n)-2*i),end="")
    print("*"*i)