n = int(input())
words = sorted([input() for _ in range(n)])
print(n-[words[i+1].startswith(words[i]) for i in range(n-1)].count(True))