import sys
import copy

input = sys.stdin.readline

def dfs(graph, depth):
    global answer
    if depth == len(cctv):
        answer = min(answer, count_zero(graph))
        return
    else:
        graph_copy = copy.deepcopy(graph)
        x, y, cctv_type = cctv[depth]
        for cctv_dir in cctv_move[cctv_type]:
            watch(x, y, cctv_dir, graph_copy)
            dfs(graph_copy, depth + 1)
            graph_copy = copy.deepcopy(graph)

def watch(x, y, direction, graph):
    for d in direction:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 6:
                    break
                elif graph[nx][ny] == 0:
                    graph[nx][ny] = '#'
            else:
                break

def count_zero(graph):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    return cnt


N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
cctv = []

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

cctv_move = {
    1: [[0], [1], [2], [3]],
    2: [[0, 1], [2, 3]],
    3: [[0, 2], [0, 3], [1, 2], [1, 3]],
    4: [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    5: [[0, 1, 2, 3]]
}
x = []

for i in range(N):
    for t in range(M):
        if 1 <= graph[i][t] < 6:
            cctv.append((i, t, graph[i][t]))

answer = 1e9

dfs(graph, 0)

print(answer)