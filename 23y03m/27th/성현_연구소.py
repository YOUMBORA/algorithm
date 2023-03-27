from collections import deque
import copy 

def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph)    
    for i in range(N):
        for j in range(M):
            if tmp_graph[i][j] == 2:
                queue.append((i,j))
    while queue:
        x, y =queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
        
            if 0 <= nx < N and 0 <= ny < M and tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny]=2
                queue.append((nx,ny))
    
    global answer
    cnt = 0

    for i in range(N):
        cnt += tmp_graph[i].count(0)

    answer = max(answer, cnt)


def makeWall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1)
                graph[i][j] = 0


N,M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = 0
makeWall(0)
print(answer)