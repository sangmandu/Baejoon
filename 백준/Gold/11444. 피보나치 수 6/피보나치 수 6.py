import sys
input = sys.stdin.readline

mod = [1000000007]
factorial = {0: 0, 1: 1}


def dOcagne(n):
    if factorial.get(n, -1) == -1:
        if n % 2:
            oprd1 = dOcagne(n//2)
            oprd2 = dOcagne(n//2 + 1)
            factorial[n] = (oprd1*oprd1 + oprd2*oprd2) % mod[0]
        else:
            oprd1 = dOcagne(n//2)
            oprd2 = dOcagne(n//2 - 1)
            factorial[n] = (oprd1*(oprd1 + 2 * oprd2)) % mod[0]
    return factorial[n]

# sys.setrecursionlimit(2000)
print(dOcagne(int(input())))
