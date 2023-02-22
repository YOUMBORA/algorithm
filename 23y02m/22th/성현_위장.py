def solution(clothes):
    answer = 0
    d={}
    for cloth, category in clothes:
        d[category] = d.get(category,[]) + [cloth]
    for k, v in d.items():
        ic = len(v)
        if answer > 0:
            answer += answer * ic
        answer += ic
    return answer