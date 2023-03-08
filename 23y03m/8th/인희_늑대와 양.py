# 입력 받아오기
r, c = map(int, input().split())
graph = []
for i in range(r):
    lst = list(map(str, input()))
    graph.append(lst)

ans = 1
# 목장 한 칸씩 돌기
for i in range(len(graph)):
    for j in range(len(graph[i])):
        # 아무것도 없으면 울타리를 설치하기
        if graph[i][j] == '.':
            graph[i][j] = 'D'
        # 양이 나오면 지나가기
        elif graph[i][j] == 'S':
            continue
        # 늑대가 있을 때, 상하좌우에 양이 존재하면 0 출력, 아니라면 빈 곳에 울타리 설치하기
        else:
            dx = [-1, 1, 0, 0]
            dy = [0, 0, 1, -1]

            for q in range(4):
                x = i + dx[q]
                y = j + dy[q]

                if (0 <= x < r) and (0 <= y < c):
                    if graph[x][y] == 'S':
                        ans -= 1
                        break

# 늑대의 상하좌우에 양이 존재할 경우
if ans != 1:
    print(0)
# 늑대가 양이 있는 칸과 인접해 있지 않은 경우
else:
    print(1)
    for p in range(len(graph)):
        print(''.join(graph[p]))