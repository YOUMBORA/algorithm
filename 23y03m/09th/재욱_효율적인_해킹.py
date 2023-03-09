import sys
from collections import deque

def bfs(graph, v, visited):
    cnt = 0

    queue = deque([v])
    visited[v] = True

    while queue:
        r = queue.popleft()
        
        for i in graph[r]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1

    return cnt

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
hacking = [0] * (n+1)
hacker = 0

for _ in range(m):
    x, y = map(int, input().split())
    graph[y].append(x)

for i in range(1, n+1):
    visited = [False] * (n+1)
    result = bfs(graph, i, visited)

    hacker = max(result, hacker)
    hacking[i] = result

for i in range(1, n+1):
    if hacking[i] == hacker:
        print(i, sep=" ")

