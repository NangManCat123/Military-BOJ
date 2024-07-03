n=int(input())
for i in range(1,n+1):
    if i**2>100:
        print("*"*100+"...")
    else:
        print("*"*(i**2))