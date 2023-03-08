import sys 

input = lambda : sys.stdin.readline().strip()
r,c  = map(int, input().split())
graph = []

for _ in range(r):
    graph.append(list(input()))

move = [(-1,0),(1,0),(0,-1),(0,1)]
safe = True
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'W':
            for k in range(4):
                nx = i + move[k][0]
                ny = j + move[k][1]
                if 0<=nx<r and 0<=ny<c and graph[nx][ny] == 'S':
                    safe = False
        elif graph[i][j] == 'S':
            continue
        else:
            graph[i][j] = "D"

if safe:
    print(1)
    for i in graph:
        print("".join(i))
else:
    print(0)
