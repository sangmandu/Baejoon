from collections import deque

def solution(queue1, queue2):
    s1, s2 = sum(queue1), sum(queue2)
    if (s1 + s2) % 2:
        return -1
    
    answer = 0
    q1, q2 = deque(queue1), deque(queue2)
    size = len(q1) + len(q2)
    
    while s1 != s2:
        if s1 > s2:
            item = q1.popleft()
            q2.append(item)
            s1 -= item
            s2 += item
        else:
            item = q2.popleft()
            q1.append(item)
            s2 -= item
            s1 += item
        answer += 1
        if answer > size * 2:
            return -1
            
    return answer