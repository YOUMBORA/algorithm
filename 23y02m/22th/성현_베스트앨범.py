def solution(genres, plays):
    d1 = {}
    d2 = {}
    for i, (g,p) in enumerate(zip(genres, plays)):
        d1[g] = d1.get(g,[])+[(i,p)]
        d2[g] = d2.get(g,0)+p
    answer = []
    for k, v in sorted(d2.items(), key= lambda x : x[1], reverse=True):
        for a in sorted(d1[k], key= lambda x : x[1], reverse=True)[:2]:
            answer.append(a[0])
    return answer