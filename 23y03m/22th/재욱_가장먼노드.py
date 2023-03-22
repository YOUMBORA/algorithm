from collections import deque

def bfs(graph, v, visit):
    queue = deque([(1, 0)])
    visit[v] = True
    count = 0
    check = 0
    
    while queue:
        r, cnt = queue.popleft()

        for i in graph[r]:
            if not visit[i]:
                queue.append((i, cnt+1))
                visit[i] = True
                if count < cnt:
                    check = 1
                    count = cnt
                elif count == cnt:
                    check += 1
    
    return check

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visit = [False] * (n+1)
    
    for i, t in edge:
        graph[i].append(t)
        graph[t].append(i)
    
    return bfs(graph, 1, visit)
