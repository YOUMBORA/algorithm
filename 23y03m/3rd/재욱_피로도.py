from itertools import permutations as pt

def solution(k, dungeons):
    answer = 0
    
    for i in pt(dungeons, len(dungeons)):
        Fatigue = k
        result = 0
        
        for Fatigue_min, Fatigue_cons in i:
            if Fatigue >= Fatigue_min:
                Fatigue -= Fatigue_cons
                result += 1
        
        if result > answer:
            answer = result
            
    
    
    return answer
