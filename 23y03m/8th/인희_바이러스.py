n = int(input())
m = int(input())

# graph에서 i번째 컴퓨터가 몇 번째 컴퓨터와 연결되어 있는지 list 추가
graph = [[]*n for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
# dfs를 통해 연결되어 있는 노드들 방문하기
def dfs(v): 
    global cnt
    visited[v] = True 
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            cnt += 1


visited = [False] * (n+1)      

dfs(1)
print(cnt)