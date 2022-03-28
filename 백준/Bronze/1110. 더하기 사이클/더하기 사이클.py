n = input()
if len(n) == 1:
    n = '0'+n
tmp, cnt = n, 0
while True:
    a, b = tmp
    c = str(int(a) + int(b))
    d = c[-1]
    tmp = b+d
    cnt += 1
    if tmp == n:
        break
print(cnt)
    