import sys
input = sys.stdin.readline

N = int(input())
preds = sorted([int(input()) for _ in range(N)])
print(sum([abs(prize-pred) for prize, pred in zip(range(1, N+1), preds)]))