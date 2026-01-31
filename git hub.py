#2
n=[3,1,4,2]
result=[]
for i in range(len(n)):
    count_small=0
    for j in range(i):
        if n[j]<n[i]:
            count_small+=1
    result.append(count_small)
print(result)
