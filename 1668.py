n=int(input())
ilist=[int(input()) for _ in range(n)]
jlist=ilist[::-1]
a=0
leftcnt,rightcnt=0,0
for i in ilist:
    if i>a:
        leftcnt+=1
        a=i
a=0
for i in jlist:
    if i>a:
        rightcnt+=1
        a=i
print(leftcnt)
print(rightcnt)