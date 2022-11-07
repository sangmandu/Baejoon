def solution(want, number, discount):
    from collections import defaultdict
    count = defaultdict(int)
    
    for i in range(9):
        count[discount[i]] += 1
    discount = ["nothing"] + discount

    i = 10
    answer = 0
    while i < len(discount):
        old, new = discount[i-10], discount[i]
        count[old] -= 1
        count[new] += 1
        i += 1
        
        for w, n in zip(want, number):
            if count[w] < n:
                break
        else:
            answer += 1
    
    return answer