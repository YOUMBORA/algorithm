from collections import deque 

# 위험 구역의 수
N = int(input())
# 위험 구역 정보
danger = [list(map(int, input().split())) for _ in range(N)]
# 죽음 구역 정보
# 죽음 구역의 수
M = int(input())
death = [list(map(int, input().split())) for _ in range(M)]

graph = [[0]*501 for _ in range(501)]

for i in range(501):
    for j in range(501):
        # 위험 영역
        for a1, b1, a2, b2 in danger:
            if (min(a1, a2) <= i <= max(a1, a2)) and (min(b1, b2) <= j <= max(b1, b2)):
                graph[i][j] = 1
        # 죽음 영역
        for a1, b1, a2, b2 in death:
            if (min(a1, a2) <= i <= max(a1, a2)) and (min(b1, b2) <= j <= max(b1, b2)):
                graph[i][j] = -1

d = [(0,1),(1,0),(-1,0),(0,-1)]

def bfs(bx,by):
    queue = deque()
    visited = [[False]*501 for _ in range(501)]
    queue.append((bx,by))
    visited[bx][by] = True 
    graph[bx][by] = 0
    while queue:
        qx, qy = queue.popleft()
        if (qx,qy) == (500,500):
            return graph[qx][qy]
        for dx, dy in d:
            nx = qx+dx 
            ny = qy+dy 
            if 0<=nx<501 and 0<=ny<501 and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[qx][qy]
                    visited[nx][ny] = True 
                    queue.appendleft((nx,ny))
                elif graph[nx][ny] == 1:
                    graph[nx][ny] += graph[qx][qy]
                    visited[nx][ny] = True 
                    queue.append((nx,ny))
    return -1
print(bfs(0,0))
