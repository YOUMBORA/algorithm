from collections import deque 

N,M,K = map(int,input().split())
G = [[5]*N for _ in range(N)]
A = [list(map(int,input().split())) for _ in range(N)]
T = [[deque() for _ in range(N)] for _ in range(N)]
for i in range(M):
    tx,ty,tz = map(int,input().split())
    T[tx-1][ty-1].append(tz)

d = [(-1,0),(0,1),(0,-1),(1,0),(1,1),(-1,-1),(1,-1),(-1,1)]

while K > 0:
    for i in range(N):
        for j in range(N):
            t_len = len(T[i][j])
            for l in range(t_len):
                if G[i][j] >= T[i][j][l]:
                    G[i][j] -= T[i][j][l]
                    T[i][j][l] += 1
                else:
                    for _ in range(l, t_len):
                        G[i][j] += T[i][j].pop() //2 
                    break 
    for a in range(N):
        for b in range(N):
            for c in T[a][b]:
                if c % 5 == 0:
                    for dx, dy in d:
                        nx = a + dx 
                        ny = b + dy 
                        if 0<=nx<N and 0<=ny<N:
                            T[nx][ny].appendleft(1)
            G[a][b] += A[a][b]
    K -= 1 

result = 0
for i in range(N):
    for j in range(N):
        result += len(T[i][j])
print(result)