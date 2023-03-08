from collections import deque 
import sys 

input = lambda : sys.stdin.readline().strip()

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    matrix = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int,input().split())
        matrix[x][y] = 1

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    visited = []
    answer = 0 
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                queue = deque()
                queue.append((i,j))
                matrix[i][j] = 0 
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx <0 or nx>=n or ny <0 or ny >=m:
                            continue
                        if matrix[nx][ny] ==1 :
                            matrix[nx][ny] = 0 
                            queue.append((nx,ny))
                answer +=1 
    print(answer)





