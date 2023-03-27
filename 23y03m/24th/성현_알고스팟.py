from collections import deque
N, M = map(int, input().split())
graph = [list(map(int,list(input()))) for _ in range(M)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

visited = [[False]*N for _ in range(M)]

def bfs():
    queue = deque()
    queue.append((0,0,0))
    visited[0][0] = True 
    while queue:
        x, y, cnt = queue.popleft()
        if x == M-1 and y == N-1:
            print(cnt)
            break 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<M and 0<=ny<N and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    queue.appendleft((nx,ny,cnt))
                    visited[nx][ny] = True 
                else:
                    queue.append((nx, ny, cnt+1))
                    visited[nx][ny] = True

bfs()

        
