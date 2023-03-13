import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, x, y, visit):
    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    
    queue = deque([(x, y)])
    graph[x][y] = 0
    visit[x][y] = True
    
    while queue:
        l, r = queue.popleft()
        
        for i in range(8):
            nx = l + dx[i]
            ny = r + dy[i]
            
            if 0 <= nx < h and 0 <= ny < w and not visit[nx][ny] and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                visit[nx][ny] = False

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
    
    graph = []
    land = []
    cnt = 0
    visit = [[False] * w for _ in range(h)]
    
    print(graph)
    print(visit)
    print(land)
    
    for i in range(h):
        x = list(map(int, input().split()))
        graph.append(x)
        
        for t in range(len(x)):
            if x[t] == 1:
                land.append([i, t])
    
    for x, y in land:
        if graph[x][y] == 1:
            bfs(graph, x, y, visit)
            cnt += 1
    
    print(cnt)
