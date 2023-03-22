import heapq

def dijkstra(adj_list, start, n):
    INF = 1e9
    dist = [INF] * n
    
    heap_list = []
    heapq.heappush(heap_list,(0,0))
    
    dist[0] = 0
    
    while heap_list:
        cur_dist, cur_node = heapq.heappop(heap_list)

        for id in adj_list[cur_node]:
            if (dist[id] > 1 + cur_dist):
                dist[id] = 1 + cur_dist
                heapq.heappush(heap_list, (dist[id],id))

    max_cnt = dist.count(max(dist))
    return max_cnt

def solution(n, edges):
    ## 1~n번까지 노드 존재 => 0~n-1로 치환
    ## may use dijkstra

    graph = [[] for _ in range(n)]
    
    for edge in edges:
        start_node = edge[0]-1
        end_node = edge[1]-1
        graph[start_node].append(end_node)
        graph[end_node].append(start_node)
    
    answer = dijkstra(graph, 0, n)
    return answer
