def solution(n, info):
    answer = []
    stack = [(n, 0, '', 0)]
    best_score = 0
    
    while stack:
        num_arrow, cur_pos, score_board, win = stack.pop()
        if cur_pos == len(info):
            if best_score < win:
                best_score = win
                answer = [score_board]
            elif best_score != 0 and best_score == win:
                answer.append(score_board)
            continue
            
        if num_arrow >= info[cur_pos] + 1:
            stack.append((num_arrow - info[cur_pos] - 1 , cur_pos+1, score_board + str(info[cur_pos] + 1), win + (10 - cur_pos)))
        
        score = (10 - cur_pos) if info[cur_pos] > 0 else 0
        stack.append((num_arrow, cur_pos+1, score_board + ('0' if cur_pos < len(info)-1 else str(num_arrow)), win - score))

    if not answer:
        return [-1]
    
    return list(map(int, sorted([a[::-1] for a in answer])[-1][::-1]))
