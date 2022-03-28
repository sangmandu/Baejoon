exp = input()
idx = exp.find('-')
if idx == -1: a, b = exp, '0'
else: a, b = exp[:idx], exp[idx+1:]
a = list(map(int, a.split('+')))
b = list(map(int, b.replace('-', '+').split('+')))
print(sum(a) - sum(b))