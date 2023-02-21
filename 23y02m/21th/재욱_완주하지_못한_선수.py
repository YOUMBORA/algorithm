from collections import Counter as ct

def solution(participant, completion):
    answer = ct(participant) - ct(completion)
    return list(answer.keys())[0]
