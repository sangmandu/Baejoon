import sys
input = sys.stdin.readline

N, K = map(int, input().split())
mod = 1000000007

# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=a4gkyum&logNo=220768006509
ret = 1
for r in range(max(K, N-K)+1, N+1):
    ret *= r
    ret %= mod

ret2 = 1
for r in range(1, min(K, N-K)+1):
    ret2 *= r
    ret2 %= mod

rest = []
div = mod-2
while div > 1:
    if div % 2:
        rest.append(ret2)
    ret2 *= ret2
    ret2 %= mod
    div //= 2

for r in rest:
    ret2 *= r
    ret2 %= mod

print(ret * ret2 % mod)
