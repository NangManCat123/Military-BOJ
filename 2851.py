ilist=[]
for _ in range(10):
    ilist.append(int(input()))
sum=0
for i in ilist:
    if sum+i<=100:
        sum+=i
    else:
        if abs(sum-100)<abs(sum+i-100):
            print(sum)
            sum+=100
            break
        else:
            print(sum+i)
            sum+=100
            break
if sum<=100:
    print(sum)