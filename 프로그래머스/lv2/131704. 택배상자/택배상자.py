def solution(order):
    answer = 0
    container = list(range(1, len(order)+1))[::-1]
    stack = []
    while container:
        stack.append(container.pop())
        while stack and order[answer] == stack[-1]:
            stack.pop()
            answer += 1
    return answer