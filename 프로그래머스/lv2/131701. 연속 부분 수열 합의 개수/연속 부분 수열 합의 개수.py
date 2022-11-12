from itertools import permutations
def solution(elements):
    dup = set()
    for _ in range(len(elements)):
        total = 0
        for e in elements:
            total += e
            dup.add(total)
        elements = elements[1:] + [elements[0]]
    return len(dup)
    