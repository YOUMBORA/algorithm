###################### Python3은 시간초과, PyPy3은 메모리초과 남 ######################

# 런타임 에러 (RecursionError) 뜨니까 최대재귀깊이를 다시 지정해주길...
import sys
sys.setrecursionlimit(10**6)

# 입력 받기
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

# dfs 구현
def dfs(v):
    global cnt

    visited[v] = True
    cnt += 1

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

# 1부터 n까지 몇 개의 컴퓨터를 신뢰할 수 있는지 확인
ans = []
for j in range(1, n+1):
    cnt = 0
    visited = [False] * (n+1)
    dfs(j)
    ans.append([cnt, j])

# 가장 많이 신뢰하는 컴퓨터 순서대로 정렬
ans.sort(key=lambda x: (-x[0], x[1]))

# 정답 출력하기
max = ans[0][0]
for k in range(len(ans)):
    if k == 0:
        print(ans[k][1], end = ' ')
    else:
        if ans[k][0] == max:
            print(ans[k][1], end = ' ')