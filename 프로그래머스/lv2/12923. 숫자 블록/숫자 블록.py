def solution(begin, end):
    answer = []
    if begin == 1:
        answer.append(0)
        begin += 1
        
    for n in range(begin, end+1):
        for i in range(2, int(n**0.5)+1):
            if not n % i and n // i <= 1e+7:
                answer.append(n // i)
                break
        else:
            answer.append(1)
    return answer