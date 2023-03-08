R,C = list(map(int,input().split()))
graph = []
for i in range(R):
    graph.append(list(input()))

#safe => answer == 1
#unsafe => answer == 0
answer = 1
checklist = [[1,0],[-1,0],[0,1],[0,-1]]
for x in range(R):
    for y in range(C):
        if graph[x][y] == 'W':
            for delta in checklist:
                new_x = x+delta[0]
                new_y = y+delta[1]
                if (0<=new_x<R) and (0<=new_y<C):
                    if graph[new_x][new_y] == 'S':
                        answer = 0
                        print(answer)
                        exit()
                    elif graph[new_x][new_y] == '.':
                        graph[new_x][new_y] = 'D'

print(answer)
if answer:
    for i in range(R):
        print(''.join(graph[i]))
