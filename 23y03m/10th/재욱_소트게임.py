import sys
from collections import deque

input = sys.stdin.readline

def bfs(number, collect, check):
    
    queue = deque([("".join(number), 0)])
    
    check["".join(number)] = 0
    
    while queue:
        r, cnt = queue.popleft()
        
        if r == collect:
            return cnt
        
        for i in range(n-k+1):
            num = list(r)
            
            change = num[i:i+k]
            change.reverse()
            
            for t in range(k):
                num[i+t] = change[t]
            
            try:
                if check["".join(num)]:
                    pass
            except:
                check["".join(num)] = 1
                queue.append(("".join(num), cnt+1))
    
    return -1

n, k = map(int,input().split())

num = list(map(str, input().split()))
collect = "".join(sorted(num))
check = dict()

print(bfs(num, collect, check))
