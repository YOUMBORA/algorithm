from itertools import combinations

# 입력 받기
n, m = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

# 집과 치킨집이 각각 어느 위치에 존재하는지 list에 담기
house = []
chicken = []

for i in range(len(city)):
    for j in range(len(city[i])):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

ans = []
# 조합을 사용하여 총 치킨집 개수 중 m개의 치킨집 고르기 
for chicken_list in combinations(chicken, m):
    cnt = 0
    # 집이 존재하는 좌표를 하나 선택해서
    for h in house:
        lst = []
        # m개 고른 치킨집 리스트 중 앞에서 선택한 집의 좌표에서 가장 가까운 치킨집에서의 거리 더해주기
        for c in chicken_list:
            lst.append(abs(c[0] - h[0]) + abs(c[1] - h[1]))
        cnt += min(lst)
    # 고른 m개의 치킨집에서 집으로부터의 거리의 최솟값을 ans에 담기
    ans.append(cnt)

# 담긴 리스트에서 도시의 치킨 거리의 최솟값 출력하기
print(min(ans))