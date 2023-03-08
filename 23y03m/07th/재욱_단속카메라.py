def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x : x[1])
    x = -30001
    
    for inputs, outputs in routes:
        if x < inputs:
            answer += 1
            x = outputs

    return answer
