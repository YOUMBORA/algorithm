import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, a, b, visit):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    o = 0
    v = 0
    
    queue = deque([(a, b)])
    visit[a][b] = True
    
    if graph[a][b] == "o":
        o += 1
    elif graph[a][b] == "v":
        v += 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if (0 <= nx < n) and (0 <= ny < m):
                if not visit[nx][ny] and graph[nx][ny] != "#":
                    visit[nx][ny] = True
                    queue.append((nx, ny))
                    
                    if graph[nx][ny] == "o":
                        o += 1
                    elif graph[nx][ny] == "v":
                        v += 1
    
    return o, v


n, m = map(int, input().split())

graph = []
visit = [[False]*m for _ in range(n)]
sheep = 0
wolf = 0

for _ in range(n):
    graph.append(list(input().strip()))

for i in range(n):
    for t in range(m):
        if graph[i][t] != "#" and visit[i][t] == False:
            sh, wo = bfs(graph, i, t, visit)
            if sh > wo:
                sheep += sh
            elif wo >= sh:
                wolf += wo
                
                
print(f"{sheep} {wolf}")
