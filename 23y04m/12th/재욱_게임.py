import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, visit):
    queue = deque([(0, 0, 0)])
    visit[0][0] = True
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y, cnt = queue.popleft()
        
        if x == 500 and y == 500:
            print(cnt)
            exit()
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 501 and 0 <= ny < 501 and not visit[nx][ny] and graph[nx][ny] != 2:
                if graph[nx][ny] == 0:
                    visit[nx][ny] = True
                    queue.appendleft((nx, ny, cnt))
                else:
                    visit[nx][ny] = True
                    queue.append((nx, ny, cnt+1))
    
    
    print(-1)
    
graph = [[0] * 501 for _ in range(501)]
visit = [[False] * 501 for _ in range(501)]
   
n = int(input())

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    
    for i in range(min(x1, x2), max(x1, x2) +1):
        for t in range(min(y1, y2), max(y1, y2)+1):
            graph[i][t] = 1
    
m = int(input())

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    
    for i in range(min(x1, x2), max(x1, x2) +1):
        for t in range(min(y1, y2), max(y1, y2)+1):
            graph[i][t] = 2

bfs(graph, visit)
