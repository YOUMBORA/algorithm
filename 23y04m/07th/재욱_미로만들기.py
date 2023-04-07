import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, visit):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque([(0, 0, 0)])
    visit[0][0] = True

    while queue:
        x, y, cnt = queue.popleft()
        
        if x == n-1 and y == n-1:
            print(cnt)
            break

        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                if graph[nx][ny] == 1:
                    queue.appendleft((nx, ny, cnt))
                    visit[nx][ny] = True
                else:
                    queue.append((nx, ny, cnt+1))
                    visit[nx][ny] = True

n = int(input())

graph = [list(map(int, input().strip())) for _ in range(n)]
visit = [[False] * n for _ in range(n)]

bfs(graph, visit)
