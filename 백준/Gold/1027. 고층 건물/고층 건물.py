n = int(input())
lst = list(map(int, input().split()))
cnt = [1] + [2] * (n-2) + [1]
for src in range(n):
    for i, drt in enumerate([range(src-2, -1, -1), range(src+2, n, 1)]):
        sign = 2*i-1
        if not drt:
            continue
        max_grad = -(lst[src]-lst[src+sign])
        for dst in drt:
            #print(i, src, dst, max_grad, sign * (lst[src]-lst[dst])/(src-dst))
            if max_grad < sign * (lst[src]-lst[dst])/(src-dst):
                max_grad = sign * (lst[src]-lst[dst])/(src-dst)
                cnt[src] += 1
print(max(cnt) if n > 1 else 0)