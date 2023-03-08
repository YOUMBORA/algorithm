import sys
from collections import deque

def bfs(graph, v, visited):
    global cnt
    queue = deque([v])

    visited[v] = True

    while queue:
        r = queue.popleft()

        for i in graph[r]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1


input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    i, t = map(int, input().split())
    graph[i].append(t)
    graph[t].append(i)
    

visit = [False] * (n+1)
cnt = 0

bfs(graph, 1, visit)

print(cnt)

