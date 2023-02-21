from collections import Counter as ct

def solution(clothes):
    result = 1

    wear = []

    for i in clothes:
        wear.append(i[1])
    
    wearing = list(ct(wear).values())

    for i in wearing:
        result *= (i+1)
        
    return result-1
