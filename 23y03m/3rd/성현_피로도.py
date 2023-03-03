from itertools import permutations
def solution(k, dungeons):
    answer =0
    for p in permutations(dungeons,len(dungeons)):
        kp = k
        dc = 0
        for mp, ep in p:
            if kp >= mp:
                kp -= ep
                dc += 1
        answer = max(answer,dc)
    return answer