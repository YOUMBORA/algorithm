import sys 
from collections import deque

input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

def dfs(v, i):
    global result
    val = 0
    if v==m:
        for h in house:
            hx, hy = h[0], h[1]
            dist = 2*n
            for s in select:
                sx, sy = s[0], s[1]
                tmp = abs(hx-sx) + abs(hy-sy)
                dist = min(dist,tmp)
            val += dist
        if val < result:
            result = val
            return 
    for idx in range(i, k):
        select.append(chicken[idx])
        dfs(v+1, idx+1)
        select.pop()

chicken = deque([])
house = deque([])

select = deque([])
for a in range(n):
    for b in range(n):
        if graph[a][b] == 1:        # 집 위치 추가
            house.append((a, b))
        elif graph[a][b] == 2:      # 치킨집 위치 추가
            chicken.append((a, b))
            
k = len(chicken)
result = n*2*len(house)

for t in range(k):
    dfs(0, t)

print(result)