arr=[]
for _ in range(8):
    arr.append(list(input()))
count=0
for j in range(8):
    for i in range(j%2,8,2):
        if arr[j][i]=="F":
            count+=1
print(count)