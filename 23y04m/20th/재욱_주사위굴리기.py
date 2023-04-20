import sys
from collections import deque

input = sys.stdin.readline

def roll(roll_dice, direct):
    if direct == 1: #동
        dice = [roll_dice[2], roll_dice[4], roll_dice[1], roll_dice[3], roll_dice[0], roll_dice[5]]
        return dice
    
    elif direct == 2: #서
        dice = [roll_dice[4], roll_dice[2], roll_dice[0], roll_dice[3], roll_dice[1], roll_dice[5]]
        return dice
    
    elif direct == 3: #북
        dice = [roll_dice[3], roll_dice[5], roll_dice[2], roll_dice[1], roll_dice[4], roll_dice[0]]
        return dice
    
    elif direct == 4: #남
        dice = [roll_dice[5], roll_dice[3], roll_dice[2], roll_dice[0], roll_dice[4], roll_dice[1]]
        return dice

def bfs(graph, check_list, start_x, start_y):
    queue = deque(check_list)
    
    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]
    dice = [0, 0, 0, 0, 0, 0] # 1, 6, 4, 5, 3, 2 위, 아래, 왼쪽, 앞, 오른쪽, 뒤
    
    while queue:
        direction = queue.popleft()
        
        if 0 <= start_x + dx[direction] < N and 0 <= start_y + dy[direction] < M:
            start_x += dx[direction]
            start_y += dy[direction]
            dice = roll(dice, direction)
            if graph[start_x][start_y] == 0:
                graph[start_x][start_y] = dice[1]
            else:
                dice[1] = graph[start_x][start_y]
                graph[start_x][start_y] = 0
            
            print(dice[0])
   

N, M, X, Y, K = map(int,input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

check_list = list(map(int, input().split()))

bfs(graph, check_list, X, Y)