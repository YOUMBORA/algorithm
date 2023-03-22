from collections import deque
def bfs(graph, v, visit, cnt):
    queue = deque([v])

    visit[v] = True

    while queue:
        r = queue.popleft()

        for i in graph[r]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True
                cnt += 1
    return visit, cnt
    
def solution(n, results):
    answer = 0
    graph1 = [[] for _ in range(n+1)]
    graph2 = [[] for _ in range(n+1)]
    
    for i, t in results:
        graph1[i].append(t)
        graph2[t].append(i)
        
        
    for i in range(1, n+1):
        visit = [False] * (n+1)
        cnt = 0
        
        visit, cnt = bfs(graph1, i, visit, cnt)
        visit, cnt = bfs(graph2, i, visit, cnt)
        
        if cnt == (n-1):
            answer += 1
        
    return answer
