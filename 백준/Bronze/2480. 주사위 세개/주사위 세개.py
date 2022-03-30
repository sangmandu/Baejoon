import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a*1000)
elif a != b and a != c and b != c:
    print(max([a, b, c]) * 100)
else:
    total = a + b + c - sum(list(set([a, b, c])))
    print(1000 + total*100)