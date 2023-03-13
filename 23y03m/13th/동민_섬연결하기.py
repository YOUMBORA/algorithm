def dfs():
    
    delta_list = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
    total_graph = []

    while True:
        R,C = map(int, input().split())
        if (R,C) == (0,0):
            break
        graph = []
        for i in range(C):
            graph.append(list(map(int, input().split())))
        total_graph.append([R,C,graph])

    # visited == 1 , unvisited == 0
    for R,C,graph in total_graph:
        visited = [[0 for i in range(R)] for j in range(C)]
        stack = []
        island_cnt = 0
        for x in range(C):
            for y in range(R):
                if (visited[x][y] == 0) and (graph[x][y] == 1):
                    visited[x][y] = 1
                    stack.append([x,y])
                    while stack:
                        xi, yi = stack.pop()
                        for delta in delta_list:
                            xf = xi+delta[0]
                            yf = yi+delta[1]
                            if (0<=(xf)<C) and (0<=(yf)<R):
                                if (graph[xf][yf] == 1) and (visited[xf][yf] == 0):
                                    visited[xf][yf] = 1
                                    stack.append([xf,yf])
                    island_cnt += 1
        print(island_cnt)                     
dfs()
