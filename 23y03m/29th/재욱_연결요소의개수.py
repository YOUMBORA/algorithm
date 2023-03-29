import sys
from collections import deque

input = sys.stdin.readline


def bfs(graph, i, visit):
    queue = deque([i])
    
    while queue:
        r = queue.popleft()
        
        for t in graph[r]:
            if not visit[t]:
                queue.append(t)
                visit[t] = True 

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

count = 0
for i in range(1, n+1):
    if visit[i] == False:
        count+=1
        bfs(graph, i, visit)

print(count)
