from collections import Counter
def solution(p,c):
    d = Counter(p)
    for m in c:
        d[m] -= 1
    for k in d:
        if d[k] == 1:
            return k