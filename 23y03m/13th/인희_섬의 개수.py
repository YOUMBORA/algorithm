# dfs 사용하려면 python 재귀 깊이 늘려주기
import sys
sys.setrecursionlimit(10**6)

# dfs 함수
def dfs(x, y):
    
    # 상하좌우대각선까지 고려하면 8가지 방향으로 나갈 수 있음
    dx = [-1, 1, 0, 0, 1, -1, -1, 1]
    dy = [0, 0, -1, 1, 1, -1, 1, -1]
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (0 <= nx < h) and (0 <= ny < w):
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                dfs(nx, ny)
    

while True:
    # 입력 받기
    w, h = map(int, input().split())
    
    # 입력 마지막 줄에는 0이 두 개 주어진다.
    if w == 0 and h == 0:
        break
    # 입력 받기
    else:
        graph = []
        cnt = 0
        for _ in range(h):
            lists = list(map(int, input().split()))
            graph.append(lists)
        
        # 지도를 돌면서 안 본 땅이 존재하면, dfs로 연결된 땅들 전부 찾기(섬 하나로 취급)
        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    dfs(i, j)
                    cnt += 1
    
    # 섬의 개수 출력
    print(cnt)