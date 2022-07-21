import sys
input = sys.stdin.readline

K = int(input())
que = []
order = ''
for _ in range(6):
    d, size = map(int, input().split())
    que.append((d, size))
    order += str(d)

for o in ['314232', '231424', '142313', '423141']:
    if o not in (order * 2):
        continue
    st = (order * 2).index(o)
    a, b, c, d, e, f = [que[(st+idx) % 6][1] for idx in range(6)]
    print(K * (b * c - e * f))
    
# 314232 ㄱ
# 231424 ㄴ/
# 142313 ㄱ/
# 423141 ㄴ
