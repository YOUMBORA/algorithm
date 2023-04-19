N, M, x, y, K = map(int, input().split())
graph = [[0]*M for _ in range(N)]
for i in range(N):
    temp = map(int,input().split())
    for j, t in enumerate(temp):
        graph[i][j] = t 
graph[x][y] = 0
move = list(map(int,input().split()))
direction = {1:(0,1),2:(0,-1),3:(-1,0),4:(1,0)}
dice =[0,0,0,0,0,0]

def turn(dir):
    a,b,c,d,e,f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d,b,a,f,e,c
    elif dir == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c,b,f,a,e,d
    elif dir == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e,a,c,d,f,b
    elif dir == 4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b,f,c,d,a,e

for m in move:
    dx, dy = direction[m]
    nx, ny = x+dx, y+dy 
    if not 0<=x+dx<N or not 0<=y+dy<M:
        continue 
    turn(m)
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[-1]
    else:
        dice[-1] = graph[nx][ny]
        graph[nx][ny] = 0
    x, y = nx, ny
    print(dice[0])
