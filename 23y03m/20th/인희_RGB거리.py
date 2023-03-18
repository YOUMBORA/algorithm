import sys
input = sys.stdin.readline

# 입력 받기
lst = []
n = int(input())
for i in range(n):
    lst.append(list(map(int, input().split())))

# 2번째 줄부터 시작
# R에서는 앞의 줄의 B, G 중에서 작은 값을 선택하고, 현재의 R값을 다시 더해줌
# G에서는 앞의 줄의 R, B 중에서 작은 값을 선택하고, 현재의 G값을 다시 더해줌
# B도 마찬가지
# 마지막 줄에는 각각 가장 작은 값들로 더한 최종 값들이 존재할 것 -> min을 통해 이들 중 작은 값을 구해주기
for j in range(1, n):
    lst[j][0] = min(lst[j-1][1], lst[j-1][2]) + lst[j][0]
    lst[j][1] = min(lst[j-1][0], lst[j-1][2]) + lst[j][1]
    lst[j][2] = min(lst[j-1][0], lst[j-1][1]) + lst[j][2]

print(min(lst[-1][0], lst[-1][1], lst[-1][2]))