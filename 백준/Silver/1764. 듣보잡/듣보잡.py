import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = set([input().strip() for _ in range(N)])
B = set([input().strip() for _ in range(M)])
ret = [i for i in A.intersection(B)]
print('\n'.join([str(len(ret))]+sorted(ret)))