import sys
from collections import deque 

input = lambda : sys.stdin.readline().strip()

n, k = map(int, input().split())
p = [i for i in input().split()]

def bfs(v):
    string_v = "".join(v)
    visited = set()
    queue = deque([[string_v,0]])
    while queue:
        value, cnt = queue.popleft()
        if list(value) == sorted(list(value)):
            return cnt
        for i in range(n-k+1):
            new_value = list(value)
            temp = new_value[i:i+k]
            temp.reverse()
            for j in range(k):
                new_value[i+j] = temp[j]
            new_v = "".join(new_value)
            if new_v not in visited:
                visited.add(new_v)
                queue.append([new_v,cnt+1])
    return -1 

print(bfs(p))