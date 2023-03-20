import sys
N, K = map(int,input().split())
thing_list = [0]

for _ in range(N):
    thing_list.append(list(map(int,sys.stdin.readline().split())))
    
## 2차원 dp table을 만들 것임. K*N
dp_list = [[0 for _ in range(K+1)] for _ in range(N+1)]

for x in range(1, N+1):
    for y in range(1, K+1):
        if y >= thing_list[x][0]:
            dp_list[x][y] = max(dp_list[x-1][y], dp_list[x-1][y-thing_list[x][0]]+thing_list[x][1])
        else:
            dp_list[x][y] = dp_list[x-1][y]
print(dp_list[N][K])
