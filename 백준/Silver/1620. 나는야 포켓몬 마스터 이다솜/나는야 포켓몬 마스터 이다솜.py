import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
for i in range(1, N+1):
    s = str(i)
    dic[s] = input().strip()
    dic[dic[s]] = s
for _ in range(M):
    print(dic[input().strip()])