import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y, visit, arr_x, arr_y):
    dx = [2, 1, 2, 1, -2, -1, -2, -1]
    dy = [1, 2, -1, -2, 1, 2, -1, -2]
    
    queue = deque([(x, y, 0)])
    visit[x][y] = True
    cnt = 0
    
    while queue:
        xx, yy, cnt = queue.popleft()
        
        if xx == arr_x and yy == arr_y:
            return cnt
        
        for i in range(len(dx)):
            nx = xx + dx[i]
            ny = yy + dy[i]
            
            if 0 <= nx < l and 0 <= ny < l and not visit[nx][ny]:
                queue.append((nx, ny, cnt+1))
                visit[nx][ny] = True

T = int(input().strip())

for _ in range(T):
    l = int(input())
    x, y = map(int, input().split())
    arr_x, arr_y = map(int, input().split())
    
    visit = [[False] * l for _ in range(l)]
    
    print(bfs(x, y, visit, arr_x, arr_y))
    
    
