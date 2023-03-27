from collections import deque 
N, K = map(int, input().split())

queue =deque()
queue.append((N,0))
MAX_V = 100001
visited = [False]*(100001)
visited[N] = True 

while queue:
    node, cnt = queue.popleft()
    if node == K:
        print(cnt)
        break 
    if 0 < node*2 < MAX_V and not visited[node*2]:
        visited[node*2] = True 
        queue.appendleft((node*2,cnt))
    if 0 <= node+1 < MAX_V and not visited[node+1]:
        visited[node+1] = True 
        queue.append((node+1,cnt+1))
    if 0 <= node-1 < MAX_V and not visited[node-1]:
        visited[node-1] = True 
        queue.append((node-1,cnt+1))
    