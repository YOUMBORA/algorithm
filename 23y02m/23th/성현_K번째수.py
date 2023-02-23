def solution(array, commands):
    answer = []
    for c in commands:
        s, e, i = c
        answer.append(sorted(array[s-1:e])[i-1])
    return answer