n = int(input())
house = [list(map(int,input().split())) for _ in range(n)]

dist = {0:house[0]}

for i in range(1,n):
    dist[i] = [0,0,0]
    dist[i][0] = house[i][0] + min(dist[i-1][1], dist[i-1][2])
    dist[i][1] = house[i][1] + min(dist[i-1][0], dist[i-1][2])
    dist[i][2] = house[i][2] + min(dist[i-1][1], dist[i-1][0])
    
print(min(dist[n-1][0],dist[n-1][1],dist[n-1][2]))
