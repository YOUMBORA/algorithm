from collections import deque 

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] *(N+1)
answer = [0]*(N+1)

for i in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs():
    queue = deque()
    queue.append(1)
    while queue:
        v = queue.popleft()
        visited[v] = True
        for c in graph[v]:
            if not visited[c]:
                answer[c] = v
                queue.append(c)
bfs()
for i in range(2, N+1):
    print(answer[i])