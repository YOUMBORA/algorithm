import sys
from collections import deque
input = sys.stdin.readline

# 상어가 최소 거리의 물고기를 먹기 위해 bfs 사용
def shark_bfs(x, y):
    distance = [[0 for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    fish = []

    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < n) and not visited[nx][ny]:
                # 자신보다 큰 물고기가 아니라면 지나갈 수 있음
                if graph[nx][ny] <= shark_size:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1

                    # 자신보다 크기가 작은 물고기가 있는 곳의 정보를 저장하기
                    if graph[nx][ny] < shark_size and graph[nx][ny] != 0:
                        fish.append((nx, ny, graph[nx][ny], distance[nx][ny]))
    
    return fish

# 입력 받기, 처음 상어 크기는 2, 현재 상어의 좌표값 저장하기
n = int(input())
graph = []
shark_size = 2
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(len(lst)):
        if lst[j] == 9:
            shark = (i, j)
    graph.append(lst)

cnt = 0
answer = 0

while True:
    # 상어가 먹을 수 있는 물고기를 탐색해보자
    fish = shark_bfs(shark[0], shark[1])

    # graph에 물고기가 존재하지 않는다면 반복문 종료
    if len(fish) == 0:
        break

    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
    fish.sort(key=lambda x: (x[3], x[0], x[1]))

    # 먹은 물고기 횟수 +1, 먹은 물고기까지의 거리 더해주기
    cnt += 1
    answer += fish[0][3]

    # 먹힌 물고기 자리는 0으로, 상어가 있던 자리도 0으로
    graph[shark[0]][shark[1]] = 0
    graph[fish[0][0]][fish[0][1]] = 0

    # 상어의 현재 위치 갱신
    shark = (fish[0][0], fish[0][1])

    # 상어의 크기가 먹은 물고기 횟수와 같다면, 상어의 크기 +1 해주기
    if shark_size == cnt:
        shark_size += 1
        cnt = 0

# 물고기를 다 먹고, 이동한 거리들의 합 출력
print(answer)
    