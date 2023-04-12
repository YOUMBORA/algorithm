from collections import deque 
N = int(input())
graph = []
for i in range(N):
    temp = list(map(int,(input().split())))
    graph.append(temp)
    for j, t in enumerate(temp):
        if t == 9:
            sx,sy = i,j
size = 2
d = [(0,-1),(-1,0),(0,1),(1,0)]

def bfs(bx,by,bs):
    queue = deque()
    queue.append((bx,by))
    distance = [[0]*N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    visited[bx][by] = True
    temp = []
    while queue:
        qx, qy = queue.popleft()
        for dx, dy in d:
            nx = qx + dx 
            ny = qy + dy 
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if graph[nx][ny] <= bs:
                    queue.append((nx,ny))
                    visited[nx][ny] = True 
                    distance[nx][ny] = distance[qx][qy] +1
                    if graph[nx][ny] < bs and graph[nx][ny] !=0:
                        temp.append((nx,ny,distance[nx][ny]))
    return sorted(temp,key=lambda x: (-x[2],-x[0],-x[1]))      

cnt = 0
result = 0
while True:
    shark = bfs(sx,sy,size)
    if len(shark) == 0:
        break 
    nx,ny,dist = shark.pop()

    result += dist 
    graph[sx][sy], graph[nx][ny] = 0, 0

    sx, sy = nx, ny 
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0

print(result)
