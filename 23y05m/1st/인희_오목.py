import sys
input = sys.stdin.readline

graph = []
for _ in range(19):
    graph.append(list(map(int, input().split())))

ans = []
for i in range(19):
    for j in range(19):
        # 바둑돌 있으면 시작
        if graph[i][j] != 0:
            stone = graph[i][j]

            # 가장 왼쪽에 있는 바둑돌부터 나아갈 수 있는 방향
            dx = [-1, 0, 1, 1]
            dy = [1, 1, 1, 0]

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                # 현재 바둑돌로부터(가장 왼쪽에 있음) 오목이 되는지 같은 방향으로 쭉 가보면서 검사하기
                cnt = 1
                while (0 <= nx < 19) and (0 <= ny < 19) and graph[nx][ny] == stone:
                    cnt += 1

                    # 육목 체크
                    if (0 <= i - dx[k] < 19) and (0 <= j - dy[k] < 19) and graph[i-dx[k]][j-dy[k]] == stone:
                        break
                    
                    nx += dx[k]
                    ny += dy[k]

                # 오목이라면, 값 저장하기
                if cnt == 5:
                    ans.append([stone, i, j])

if not ans:
    print(0)
else:
    ans.sort(key=lambda x:(x[2], x[1]))
    print(ans[0][0])
    print(ans[0][1]+1, ans[0][2]+1)