# dfs 로 풀어야 되는 거 알겠어
# up, down, left, right 할 때 커서도 활용해야 되는 것도 알겠어 한번 해볼게


# def dfs(graph,cnt):
#     if cnt == 5:
#         return max([max(i) for i in graph])
#     return max(dfs(swing(deepcopy(graph),0),cnt+1),dfs(swing(deepcopy(graph),1),cnt+1),dfs(swing(deepcopy(graph),2),cnt+1),dfs(swing(deepcopy(graph),3),cnt+1))
from copy import deepcopy
def dfs(graph,cnt):
    global max_num
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                max_num = max(max_num, graph[i][j])
        return
    for i in range(4):
        new_map = swing(deepcopy(graph),i)
        # print(f'{cnt+1}번째 시도 {i} 방향으로 ')
        # for k in new_map:
        #     print(k)
        dfs(new_map,cnt+1)

from collections import deque
def bfs(graph):
    max_num = max([max(i) for i in graph])
    queue = deque()
    for i in range(4):
        queue.append((graph,i,0))
    while queue:
        tmp, way,cnt = queue.popleft()
        if cnt ==5:
            continue
        else:
            next_tmp = swing(tmp,way)
            tmp_max = max([max(i) for i in next_tmp])
            if max_num < tmp_max:
                max_num = tmp_max
            for i in range(4):
                queue.append((next_tmp,i,cnt+1))
    return max_num


def swing(zido, way):
    if way == 0:
        for y in range(n):
            cursor = 0
            for x in range(1, n):
                if zido[x][y]:
                    tmp = zido[x][y]
                    zido[x][y] = 0
                    if zido[cursor][y] == 0:
                        zido[cursor][y] = tmp

                    elif zido[cursor][y] == tmp:
                        zido[cursor][y] *= 2
                        cursor += 1
                    else: # 서로 다른 경우
                        cursor +=1
                        zido[cursor][y] = tmp
    if way == 1:
        for y in range(n):
            cursor = n-1
            for x in range(n - 2, -1, -1):
                if zido[x][y]:
                    tmp = zido[x][y]
                    zido[x][y] = 0
                    if zido[cursor][y] == 0:
                        zido[cursor][y] = tmp

                    elif zido[cursor][y] == tmp:
                        zido[cursor][y] *= 2
                        cursor -= 1
                    else: # 서로 다른 경우
                        cursor -=1
                        zido[cursor][y] = tmp
    if way == 2:
        for x in range(n):
            cursor = 0
            for y in range(1,n):
                if zido[x][y]:
                    tmp = zido[x][y]
                    zido[x][y] = 0
                    if zido[x][cursor] == 0:
                        zido[x][cursor] = tmp

                    elif zido[x][cursor] == tmp:
                        zido[x][cursor] *= 2
                        cursor += 1
                    else: # 서로 다른 경우
                        cursor +=1
                        zido[x][cursor] = tmp
    if way == 3:
        for x in range(n):
            cursor = n-1
            for y in range(n-2,-1,-1):
                if zido[x][y]:
                    tmp = zido[x][y]
                    zido[x][y] = 0
                    if zido[x][cursor] == 0:
                        zido[x][cursor] = tmp

                    elif zido[x][cursor] == tmp:
                        zido[x][cursor] *= 2
                        cursor -= 1
                    else:  # 서로 다른 경우
                        cursor -= 1
                        zido[x][cursor] = tmp
    return zido
if __name__=='__main__':
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    dx = [-1,1,0,0]
    dy = [0, 0, -1, 1]
    max_num = 0
    # print(bfs(graph))
    dfs(graph,0)
    print(max_num)