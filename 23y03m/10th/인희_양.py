# dfs의 재귀 사용하니까 재귀 깊이 늘려주기
import sys
sys.setrecursionlimit(10**6)

# dfs 함수
def dfs(x, y):
    global W, S

    # 울타리 안의 양의 수, 늑대의 수를 센 후, 울타리로 채워 넣기(다신 안볼거니까)
    if graph[x][y] == '.':
        graph[x][y] = '#'

    elif graph[x][y] == 'v':
        W += 1
        graph[x][y] = '#'

    elif graph[x][y] == 'o':
        S += 1
        graph[x][y] = '#'

    # 상하좌우 살펴보기
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # graph 안에 있으며 울타리 안쪽으로만 돌면서 살펴보기
        if (0 <= nx < c) and (0 <= ny < r):
            if graph[nx][ny] != '#':
                dfs(nx, ny)



# 입력 받기
r, c = map(int, input().split())
graph = []
for i in range(r):
    graph.append(list(input()))

wolf, sheep = 0, 0

# graph를 돌면서
for p in range(r):
    for q in range(c):
        # 울타리가 없으면 해당 필드 안의 늑대와 양의 수를 파악하기
        if graph[p][q] != '#':
            W, S = 0, 0
            dfs(p, q)
            
            # 늑대가 양보다 많으면 늑대만 존재, 반대면 양만 존재
            if W >= S:
                wolf += W
            else:
                sheep += S

# 최종 결과 값 출력
print(sheep, wolf)