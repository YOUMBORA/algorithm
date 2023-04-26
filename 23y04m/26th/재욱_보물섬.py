import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, visit, start_x, start_y):
    queue = deque([(start_x, start_y, 0)])
    visit[start_x][start_y] = True
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    answer = 0
    
    while queue:
        x, y, cnt = queue.popleft()

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]=="L" and not visit[nx][ny]:
                queue.append((nx, ny, cnt+1))
                visit[nx][ny] = True
                answer = max(answer, cnt+1)
 
    return answer

n, m = map(int, input().split())

graph = [list(map(str, input().strip())) for _ in range(n)]

result = 0
for i in range(n):
    for t in range(m):
        if graph[i][t] == "L":
            
            visit = [[False] * m for _ in range(n)]
            result = max(result, bfs(graph, visit, i, t))
            
print(result)