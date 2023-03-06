def solution(name):
    answer = 0
    last = 0
    ln = len(name)
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for n in name:
        p = alphabet.index(n)
        pl = abs(p - last)
        pr = len(alphabet) - pl
        answer += min(pl,pr)
    
    move = ln - 1
    for idx in range(ln):
        next_idx = idx + 1
        while (next_idx < ln) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, ln - next_idx)
        move = min(move, idx + ln - next_idx + distance)
    answer += move
    
    return answer