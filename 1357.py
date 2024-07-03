def rev(x):
    x=list(str(x))
    while not x[-1]:
        x.pop()
    return int("".join(reversed(x)))
x,y=map(int,input().split())
print(rev(rev(x)+rev(y)))