#2
n=[5,8,6,11,7]
result=[]
for i in range(len(n)):
    count_small=0
    for j in range(i):
        if n[j]<n[i]:
            count_small+=1
    result.append(count_small)
print(result)
