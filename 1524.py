import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    input()
    s,b=map(int,input().split())
    slist=list(sorted(map(int,input().split())))
    blist=list(sorted(map(int,input().split())))
    while slist and blist:
        if slist[-1]>=blist[-1]:
            blist.pop()
        else:
            slist.pop()
    if slist:
        print("S")
    elif blist:
        print("B")
    else:
        print("C")