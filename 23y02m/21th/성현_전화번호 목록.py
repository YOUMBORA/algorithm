def solution(p):
    p.sort(key=lambda x: (x,len(x)))
    for i in range(len(p)-1):
        if p[i] == p[i+1][:len(p[i])]:
            return False
    return True