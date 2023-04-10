import sys
from itertools import combinations

input = sys.stdin.readline

def check(graph):
    for i in range(1, N+1):
        move = i
        
        for t in range(1, H+1):
            if graph[t][move] == True:
                move += 1
            elif graph[t][move-1] == True:
                move -= 1
        
        if move != i:
            return False
    
    return True

N, M, H = map(int, input().split())

if M == 0:
    print(0)
    exit()

first_graph = [list(map(int, input().split())) for _ in range(M)]

graph = [[False] * (N+1) for _ in range(H+1)]

for a, b in first_graph:
    graph[a][b] = True

combination = []

for i in range(1, H+1):
    for t in range(1, N):
        if graph[i][t] == False and graph[i][t-1] == False and graph[i][t+1] == False:
            combination.append([i, t])

if check(graph):
    print(0)
    
else:
    for count in range(1, 4):
        for i in combinations(combination, count):
            for x, y in i:
                graph[x][y] = True
            
            if check(graph):
                print(count)
                exit()
            else:
                for x, y in i:
                    graph[x][y] = False

    print(-1)

