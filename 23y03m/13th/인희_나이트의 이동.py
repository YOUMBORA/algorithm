from collections import deque

# bfs 함수
def bfs(a, b, move_x, move_y):
    global chess

    queue = deque()
    queue.append([a, b])
    chess[a][b] = 1

    # 나이트가 한 번에 이동할 수 있는 칸은 총 8개
    dx = [2, -2, 2, -2, 1, -1, 1, -1]
    dy = [1, -1, -1, 1, 2, -2, -2, 2]

    while queue:
        x, y = queue.popleft()

        # 나이트가 이동하려는 칸으로 가면 몇 번만에 이동했는지 출력 후 break
        if x == move_x and y == move_y:
            print(chess[x][y] - 1)
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < L) and (0 <= ny < L):
                if chess[nx][ny] == 0:
                    queue.append([nx, ny])
                    # 몇 번만에 이동하는지 적어놓기
                    chess[nx][ny] = chess[x][y] + 1

# 입력 받기
T = int(input())
for _ in range(T):
    L = int(input())
    now_x, now_y = map(int, input().split())
    move_x, move_y = map(int, input().split())

    chess = [[0] * L for _ in range(L)]

    bfs(now_x, now_y, move_x, move_y)
