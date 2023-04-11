import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, visit, K):
    queue = deque([(0, 0, 0, K)])
    visit[0][0][0] = True
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    hx = [-1, -2, -2, -1, 1, 2, 2, 1]
    hy = [-2, -1, 1, 2, -2, -1, 1, 2]
    
    while queue:
        x, y, cnt, k = queue.popleft()
        
        if x == m-1 and y == n-1:
            print(cnt)
            exit()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and not visit[nx][ny][k] and graph[nx][ny] == 0:
                queue.append((nx, ny, cnt+1, k))
                visit[nx][ny][k] = True
                
        if k > 0 :
            for t in range(8):
                nx = x + hx[t]
                ny = y + hy[t]
                    
                if 0 <= nx < m and 0 <= ny < n and not visit[nx][ny][k-1] and graph[nx][ny] == 0:
                    queue.append((nx, ny, cnt+1, k-1))
                    visit[nx][ny][k-1] = True
                
    print(-1)

K = int(input())

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(m)]
visit = [[[False] * (K+1) for _ in range(n)] for _ in range(m)]

bfs(graph, visit, K)

