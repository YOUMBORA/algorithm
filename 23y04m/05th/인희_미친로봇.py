import sys
input = sys.stdin.readline

# 동서남북 방향
dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)

# dfs 알고리즘
def dfs(depth, r, c, percentage):
    global result
    # N번의 횟수만큼 이동하면 만들어둔 percentage list에 저장하기
    if depth == N:
        result += percentage
        return
    
    # 4가지 방향으로 이동
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        # 이동한 적 있으면 돌아가
        if check[nr][nc]:
            continue

        # 이동한 적 없으면 1을 넣어주기
        check[nr][nc] = 1
        
        # dfs로 재귀
        dfs(depth+1, nr, nc, percentage*dirInfo[i])
        check[nr][nc] = 0

# main
N, east, west, south, north = map(int, input().split())
# 동서남북 방향별 percentage를 100으로 나누어 리스트에 저장
dirInfo = [east/100, west/100, south/100, north/100]

result = 0
# 갈 수 있는 위치 배열
check = [[0] * (2*N+1) for _ in range(2*N+1)]
check[N][N] = 1
dfs(0, N, N, 1)
print(result)