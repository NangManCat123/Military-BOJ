n=int(input())
x=1
for i in range(n):
    print(" "*(n-i-1),end="")
    print("*"*x)
    x+=2