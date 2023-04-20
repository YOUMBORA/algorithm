import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, robot_x, robot_y, robot_direction):
    queue = deque([(robot_x, robot_y, robot_direction)])
    graph[robot_x][robot_y] = 2
    cnt = 1
    
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    
    back_move = {0 : [1, 0], 1 : [0, -1], 2: [-1, 0], 3 : [0, 1]}
    turn_move = {0 : [0, -1, 3], 1 : [1, 0, 0], 2 : [0, 1, 1], 3 : [-1, 0, 2]}
    
    while queue:
        x, y, direction = queue.popleft()
        boolean = False
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if graph[nx][ny] == 0:
                boolean = True
                break
                
        if boolean:
            nx = x + turn_move[direction][0]
            ny = y + turn_move[direction][1]
            
            if graph[nx][ny] == 0:
                queue.append((nx, ny, turn_move[direction][2]))
                graph[nx][ny] = 2
                cnt += 1
            else:
                queue.append((x, y, turn_move[direction][2]))
                

        if not boolean:
            nx = x + back_move[direction][0]
            ny = y + back_move[direction][1]
            
            if graph[nx][ny] == 1:
                print(nx,ny)
                print(x, y)
                for i in range(n):
                    print(graph[i])
                break
            else:
                queue.append((nx, ny, direction))
    
    print(cnt)

n, m = map(int, input().split())

robot_x, robot_y, robot_direction = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

bfs(graph, robot_x, robot_y, robot_direction)
