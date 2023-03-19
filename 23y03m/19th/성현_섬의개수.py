from collections import deque

while True:
    w, h = map(int,input().split())
    if w==0 and h==0:
        break 
    graph = [list(map(int,input().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    answer = 0

    dx = [-1,0,1,0,-1,-1,1,1]
    dy = [0,-1,0,1,-1,1,-1,1]

    for a in range(h):
        for b in range(w):
            if graph[a][b] == 1 and not visited[a][b]:
                queue = deque()
                queue.append((a,b))
                visited[a][b] = True 
                while queue:
                    x, y = queue.popleft()
                    for i in range(8):
                        nx = x+dx[i]
                        ny = y+dy[i]
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and graph[nx][ny]==1:
                            visited[nx][ny] = True 
                            queue.append((nx,ny))
                answer +=1
    print(answer)
