from heapq import heappop, heappush

T = int(input())

total_result = []
INF = int(1e9)


def dijkstra(graph, start_node):
    # visited = [False] * (len(graph))
    dist = [INF] * (len(graph))
    heap = []
    heappush(heap, (0, start_node))
    dist[start_node] = 0

    while heap:
        cost, cur_node = heappop(heap)
        # visited[cur_node] = True
        if cost > dist[cur_node]:
            continue
        for node in graph[cur_node]:
            temp = node[0] + cost
            if dist[node[1]] > temp:
                dist[node[1]] = temp
                heappush(heap, (dist[node[1]], node[1]))
    return dist


for i in range(T):
    ## input
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    target_list = []
    graph = [[] for _ in range(n + 1)]
    for j in range(m):
        x, y, w = map(int, input().split())
        graph[x].append((w, y))
        graph[y].append((w, x))
    for k in range(t):
        target_list.append(int(input()))

    result = []

    ## main
    start_dist = dijkstra(graph, s)
    # print(start_dist)
    for node in graph[g]:
        if node[1] == h:
            gh_edge = node[0]
    # print(gh_edge)
    for target in target_list:
        target_dist = dijkstra(graph, target)
        # print(target_dist)
        if start_dist[g] + target_dist[h] + gh_edge == start_dist[target]:
            result.append(target)
            continue
        if start_dist[h] + target_dist[g] + gh_edge == start_dist[target]:
            result.append(target)

    total_result.append(sorted(result))

for some in total_result:
    print(*some)
