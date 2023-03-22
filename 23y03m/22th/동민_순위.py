def solution(n, results):
    INF = 1e9
    graph = [[INF for _ in range(n)] for _ in range(n)]
    
    for result in results:
        winner = result[0] - 1
        loser = result[1] - 1
        graph[winner][loser] = 1
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
                
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j], graph[j][i])
            
    cnt = 0
    for i in graph:
        if sum(i) < INF:
            cnt += 1
    return cnt
