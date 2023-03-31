import sys
import heapq
input = sys.stdin.readline
INF = 1e9

# 입력 받기
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
start, end = map(int, input().split())

near = [start] * (n+1)
distance = [INF] * (n+1)


q = [(0, start)]

while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    
    for next, nextDist in graph[now]:
        cost = nextDist + dist
        if cost < distance[next]:
            distance[next], near[next] = cost, now
            heapq.heappush(q, (cost, next))

path = [end]
now = end
while now != start:
    now = near[now]
    path.append(now)

path.reverse()

print(len(path))
print(' '.join(map(str, path)))