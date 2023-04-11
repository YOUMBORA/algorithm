from collections import deque

def bfs(graph, visit, CX, CY, IX, IY):
    queue = deque([(CX, CY, 0)])
    visit[CX][CY] = True
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y, cnt = queue.popleft()
        
        if x == IX and y == IY:
            return cnt // 2
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 102 and 0 <= ny < 102 and not visit[nx][ny] and graph[nx][ny] == 1:
                queue.append((nx, ny, cnt+1))
                visit[nx][ny] = True

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[0] * 102 for _ in range(102)]
    visit = [[False] * 102 for _ in range(102)]
    
    for z in rectangle:
        x1, y1, x2, y2 = map(lambda x:x*2, z)
        
        for i in range(x1, x2+1):        
            for t in range(y1, y2+1):
                if x1 < i < x2 and y1 < t < y2:
                    graph[i][t] = 2
                    
                elif graph[i][t] != 2:
                    graph[i][t] = 1
            
    return bfs(graph, visit, characterX * 2, characterY * 2, itemX * 2, itemY * 2)
