from collections import deque 

N = int(input())
K = int(input())
# 게임 맵
graph = [[0]*N for _ in range(N)]

for _ in range(K):
    x,y = map(int,input().split())
    graph[x-1][y-1] = 2

L = int(input())
move = {}
for _ in range(L):
    movet, moved = input().split()
    move[int(movet)] = moved

# 오른쪽, 위쪽, 왼쪽, 아래쪽
d = [(0,1),(1,0),(0,-1),(-1,0)]

# 시작 위치
nx, ny = 0, 0
dcount = 0
curd = d[0]
queue = deque()
queue.append((0,0))
graph[nx][ny] = 1
i = 0

while True:
    nx, ny = nx+ curd[0], ny+ curd[1]
    i += 1

    if nx<0 or nx>=N or ny<0 or ny>=N:
        break
    if graph[nx][ny] == 1:
        break
    if graph[nx][ny] == 2:
        graph[nx][ny] = 1
        queue.append((nx,ny))
    if graph[nx][ny] == 0:
        graph[nx][ny] = 1
        queue.append((nx,ny))
        tx,ty= queue.popleft()
        graph[tx][ty] = 0

    if i in move:
        if move[i] == 'L':
            curd = d[(dcount-1)%4]
            dcount -= 1
        if move[i] == 'D':
            curd = d[(dcount+1)%4]
            dcount += 1
print(i)