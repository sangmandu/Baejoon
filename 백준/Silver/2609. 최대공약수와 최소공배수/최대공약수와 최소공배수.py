import sys
input = sys.stdin.readline

import math
n, m = map(int, input().split())
print(math.gcd(n, m), math.lcm(n, m), sep='\n')