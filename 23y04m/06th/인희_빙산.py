import sys
from collections import deque
input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# BFS 알고리즘
def bfs(x, y, visit, melt):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = True

    while queue:
        x, y = queue.popleft()
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m):
                # 이어진 빙산임을 확인하기 위한 bfs 알고리즘
                if not visit[nx][ny] and graph[nx][ny] != 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                # 현재 위치한 곳에서 주변에 바다가 몇 개 있는지 확인
                if graph[nx][ny] == 0:
                    cnt += 1
        # 현재 위치한 곳과 주변에 위치한 바다를 표시
        melt.append((x, y, cnt))


answer = 0
while True:
    melt = []
    visited = [[False for _ in range(m)] for _ in range(n)] 
    cnt_island = 0

    # 좌표평면을 순서대로 돌기
    for i in range(n):
        for j in range(m):
            # 현재 위치가 빙산에 해당하며, 방문한 적 없다면 BFS 알고리즘 실행
            if graph[i][j] != 0 and not visited[i][j]:
                bfs(i, j, visited, melt)
                cnt_island += 1   # bfs로 이어진 섬 개수 세기

    # 빙산이 2개 이상으로 나뉘어지면 while문 탈출
    if cnt_island >= 2:
        break
    # 빙산이 한 개도 존재하지 않으면 0을 내보내고 while문 탈출
    elif cnt_island == 0:
        answer = 0
        break
    # 빙산이 1개 이하이면 계속해서 빙산 녹이기
    else:
        answer += 1

    # 앞에서 구했던, 빙산의 위치와 주변의 바다 개수를 통해 1년이 지난 후 빙산의 변화를 graph에 다시 적어놓기
    for x, y, melt_cnt in melt:
        ans = graph[x][y] - melt_cnt
        if ans < 0:
            graph[x][y] = 0
        else:
            graph[x][y] = ans

# 빙산이 2개 이상으로 분리되는 년수 출력
print(answer)