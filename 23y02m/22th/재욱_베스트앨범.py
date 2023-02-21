from collections import defaultdict

def solution(genres, plays):
    answer = defaultdict(list)
    play = {}
    result = []
    
    for idx, g in enumerate(genres):
        answer[g].append([idx, plays[idx]])
        
        try:
            if play[g]:
                play[g] += plays[idx]
        except:
            play[g] = plays[idx]
    
    play = dict(sorted(play.items(), key=lambda x:x[1], reverse=True))
    
    for gen in play.keys():
        x = sorted(answer[gen], key=lambda x:x[1], reverse=True)
        
        if len(x) == 1:
            result.append(x[0][0])
        
        else:
            result.append(x[0][0])
            result.append(x[1][0])
        
    return result
