from collections import deque

def solution(s):
    answer = True
    
    open = deque([])
    
    x = deque(s)
    
    while x:
        T = x.popleft()
        
        if T == "(":
            open.append("(")
        else:
            if len(open) == 0:
                return False
            else:
                open.pop()
            

    if len(open) == 0:
        return True
    else:
        return False
