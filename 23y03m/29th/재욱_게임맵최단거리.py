from collections import deque
def bfs(graph, visit, target_x, target_y):
    queue = deque([(0, 0, 1)])
    visit[0][0] = True
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y, cnt = queue.popleft()
        
        if x == target_x and y == target_y:
            return cnt
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < target_x+1 and 0<= ny < target_y+1 and not visit[nx][ny] and graph[nx][ny] == 1:
                visit[nx][ny] = True
                queue.append((nx, ny, cnt+1))
    
    return -1


def solution(maps):
    n =  len(maps)
    m = len(maps[0])
    visit = [[False] * m for _ in range(n)]
    
    return bfs(maps, visit, n-1, m-1)
