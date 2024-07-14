n=int(input())
data=input().replace(" ","")
count=data.count('L')

if count==0:
    print(n)
else:
    print(n-(count//2-1))