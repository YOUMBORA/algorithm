from collections import deque

def solution(maps):
    answer = 0
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    
    queue = deque()
    queue.append((0,0))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or nx >= len(maps) or ny<0 or ny>=len(maps[0]):
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] +1
                queue.append((nx,ny))
    answer = maps[len(maps)-1][len(maps[0])-1]
    return -1 if answer == 1 else answer