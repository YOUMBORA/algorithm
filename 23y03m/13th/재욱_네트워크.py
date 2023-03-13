from collections import deque

def bfs(graph, x, visit):
    queue = deque([x])
    visit[x] = True
    
    while queue:
        r = queue.popleft()
        
        for i in graph[r]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True
        
    
    
    
    return


def solution(n, computers):
    answer = 0
    
    graph = [[] for _ in range(n)]
    visit = [False] * (n+1)
    
    for i in range(len(computers)):
        for idx, com in enumerate(computers[i]):
            if com == 1 and i != idx:
                graph[i].append(idx)
                graph[idx].append(i)

    for i in range(n):
        if not visit[i]:
            bfs(graph, i, visit)
            answer += 1
    
    
    return answer
