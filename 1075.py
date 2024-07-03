n=list(input())
f=int(input())
n[-1],n[-2]="0","0"
n=int("".join(n))
while True:
    if n%f==0:
        print(str(n)[-2]+str(n)[-1])
        break
    n+=1