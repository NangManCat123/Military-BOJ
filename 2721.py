for _ in range(int(input())):
    n=int(input())
    print(sum(k*sum(range(k+2)) for k in range(1,n+1)))
    