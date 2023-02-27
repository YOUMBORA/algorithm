def solution(operations):
    answer = []
    
    for oper in operations:
        # 큐에 주어진 숫자를 삽입
        if oper[0] == 'I':
            lst = oper.split()
            answer.append(int(lst[1]))
            answer.sort()
        # 큐에서 최댓값을 삭제
        if oper == 'D 1':
            if answer:
                answer.pop()
        # 큐에서 최솟값을 삭제    
        if oper == 'D -1':
            if answer:
                answer.pop(0)
    
    if len(answer) > 1:
        return [max(answer), min(answer)]
    else:
        return [0, 0]