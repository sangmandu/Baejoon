n = int(input())
answer = input().split()
dic = {val : idx for idx, val in enumerate(answer)}
result = input().split()
print([dic[result[i]] < dic[result[j]] for i in range(n) for j in range(i, n)].count(1),'/',(n*(n-1)//2),sep='')