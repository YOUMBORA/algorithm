import sys
sys.setrecursionlimit(100000)
from collections import deque

def dfs(graph, v, visited):
    print(v, end = " ")
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        r = queue.popleft()
        print(r, end=" ")
        for i in graph[r]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    i, t = map(int, input().split())
    graph[i].append(t)
    graph[t].append(i)

for i in range(N+1):
    graph[i].sort()

dfs_visit = [False] * (N+1)

bfs_visit = [False] * (N+1)

dfs(graph, R, dfs_visit)
print()
bfs(graph, R, bfs_visit)
