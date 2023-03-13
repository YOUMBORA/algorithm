from collections import deque 
dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]

N = int(input())
for _ in range(N):
    I = int(input())
    visited = [[False]*I for _ in range(I)]

    start_x, start_y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    if start_x == target_x and start_y == target_y:
        print(0)
        continue
    
    queue = deque([[start_x, start_y, 0]])
    visited[start_x][start_y]=True
    while queue:
        x, y, cnt = queue.popleft()
        if x == target_x and y == target_y:
            print(cnt)
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<I and 0<=ny<I and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx,ny,cnt+1])
