# dfs 쓸거니까 재귀 깊이 늘려주기
import sys
sys.setrecursionlimit(10**6)

# 입력 받기
n = int(input())
per1, per2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    parents, child = map(int, input().split())
    graph[parents].append(child)
    graph[child].append(parents)

# dfs 함수
def dfs(v):
    for i in graph[v]:
        if ans[i] == 0:
            ans[i] = ans[v] + 1
            dfs(i)

ans = [0] * (n+1)

dfs(per1)

# 친척 관계면 촌수 출력, 아니면 -1 출력
if ans[per2] > 0:
    print(ans[per2])
else:
    print(-1)