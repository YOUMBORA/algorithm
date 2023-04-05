from collections import deque

def word_check(w1,w2):
    c = len(w1)
    for r1, r2 in zip(w1,w2):
        if r1 == r2:
            c -= 1
    return c 

def solution(begin, target, words):
    answer = 0
    visited = []
    queue = deque()
    queue.append((begin,0))
    visited.append(begin)
    while queue:
        cword, cnt = queue.popleft()
        if cword not in visited:
            visited.append(cword)
        if cword == target:
            return cnt
        for nword in words:
            if word_check(cword,nword) == 1:
                if word_check(target,nword) <= word_check(target,cword):
                    if nword not in visited:
                        queue.append((nword,cnt+1))
    return 0