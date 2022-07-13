import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = set([input().strip() for _ in range(N)])
B = [input().strip() for _ in range(M)]
print(sum([int(b in A) for b in B]))