import sys
from collections import deque

input = sys.stdin.readline


def bfs(graph, a, b):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if (0 <= nx < M) and (0 <= ny < N):
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    cnt = 0
    
    graph = [[0] * N for _ in range(M)]
    
    for _ in range(K):
        i, t = map(int, input().split())
        graph[i][t] = 1
        
    for i in range(M):
        for t in range(N):
            if graph[i][t] == 1:
                bfs(graph, i, t)
                cnt += 1
    print(cnt)
