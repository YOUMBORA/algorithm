import sys
import copy

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
time = 0


def dfs(board, time):

    node_cnt = 0
    visited = [[1 for _ in range(len(board[0]))] for _ in range(len(board))]
    next_board = copy.deepcopy(board)
    for x in range(1, len(board)-1):
        for y in range(1, len(board[0])-1):
            if board[x][y] != 0:
                start_node = [x, y]
                visited[x][y] = 0
                node_cnt += 1
                dec_cnt = 0
                for j in range(4):
                    nx = x+dx[j]
                    ny = y+dy[j]
                    if nx >= N or ny >= M or nx < 0 or ny < 0:
                        continue
                    else:
                        if board[nx][ny] == 0:
                            dec_cnt += 1
                next_board[x][y] = max(0, board[x][y] - dec_cnt)

    if node_cnt == 0:
        return (0, next_board, time)

    stack = [start_node]
    while stack:
        cur = stack.pop()
        if visited[cur[0]][cur[1]] == 0:
            visited[cur[0]][cur[1]] = 1
            for j in range(4):
                nx = cur[0]+dx[j]
                ny = cur[1]+dy[j]
                if nx >= N or ny >= M or nx < 0 or ny < 0:
                    continue
                else:
                    if visited[nx][ny] == 0:
                        stack.append([nx, ny])

    if sum([sum(visit) for visit in visited]) < N*M:
        return (1, next_board, time)
    return (2, next_board, time+1)


while time >= 0:

    # 분리된걸 알려면 dfs 이용
    result, graph, time = dfs(graph, time)
    # print(result, graph, time)
    if result == 0:
        print("0")
        break
    elif result == 1:
        print(time)
        break
