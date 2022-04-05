import sys
input = sys.stdin.readline

M, N = max(int(input()), 2), int(input())
sieve = [0] * M + [k for k in range(M, N+1)]
for i in range(2, N+1):
    for j in range(i+i, N+1, i):
        sieve[j] = 0

if sum(sieve) == 0:
    print(-1)
else:
    print(sum(sieve))
    print(sorted(list(set(sieve)))[1])
