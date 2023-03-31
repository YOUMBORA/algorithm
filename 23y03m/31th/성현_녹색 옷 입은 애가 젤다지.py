import heapq as hq 
count = 0
while True:
    N = int(input())
    count += 1
    if N == 0:
        break
    INF = int(1e9)
    graph = [list(map(int,input().split())) for _ in range(N)]
    distance = [[INF]*N for _ in range(N)]

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    
    queue = []
    hq.heappush(queue, (graph[0][0],0,0))
    
    while queue :
        cnt,x,y = hq.heappop(queue)
        if x == N-1 and y == N-1:
            print("Problem {}: {}".format(count,distance[x][y]))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            cost = cnt + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                hq.heappush(queue,(cost,nx,ny))