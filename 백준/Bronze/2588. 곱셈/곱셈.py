a, b = map(int, [input(), input()])
d = 0
for i, c in enumerate(str(b)[::-1]):
    print(a*int(c))
    d += (a * int(c)) * (10 ** i)
print(d)