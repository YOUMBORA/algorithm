import sys
from collections import deque 

input = lambda : sys.stdin.readline().strip()

n = int(input())
i, j = map(int, input().split())
m = int(input())

graph = [[]]*(n+1)
visited = [False]*(n+1)

for _ in range(m):
    f, t = map(int, input().split())
    if graph[f] == []:
        graph[f] = [t]
    else:
        graph[f].append(t)
    if graph[t] == []:
        graph[t] = [f]
    else:
        graph[t].append(f)

def bfs(i):
    queue = deque([[i,0]])
    while queue:
        v, cnt = queue.popleft()
        if v == j:
            return cnt
        if not visited[v]:
            visited[v] = True
            for k in graph[v]:
                queue.append([k,cnt+1])
    return -1
print(bfs(i))

