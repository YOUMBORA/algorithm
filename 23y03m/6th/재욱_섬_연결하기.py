# 다익스트라로 접근하였으나 틀림..

import heapq

def dijkstra(start, graph, visited, distance, answer):
    
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                answer += cost - dist
                print(cost-dist)
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
                
    return answer

def solution(n, costs):
    
    graph = [[] for i in range(n+1)]
    # visited = [False] * (n+1)
    # distance =  [1e9] * (n+1)

    answer = 0
    
    for i, t, z in costs:
        graph[i].append((t, z))
    
    result = 1e9
    
    for i in range(n):
        visited = [False] * (n+1)
        distance =  [1e9] * (n+1)
        # result = dijkstra(0, graph, visited, distance, answer)
        min_dis = dijkstra(i, graph, visited, distance, answer)
        print(min_dis)
        result = min(result, min_dis)
    
    return result
