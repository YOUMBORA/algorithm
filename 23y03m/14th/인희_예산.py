# 입력 받기
n = int(input())
money = list(map(int, input().split()))
m = int(input())

# 이진 탐색에 필요한 start, end 값 설정
start, end = 0, max(money)

# 이진 탐색
while start <= end:
    # 중앙값 설정
    mid = (start + end) // 2
    total = 0

    # money 탐색하면서 
    for i in money:
        if i > mid:
            total += mid
        else:
            total += i
    
    # total이 예산보다 작으면 start 값을 높이고, 아니면 end 값을 낮추기
    if total <= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)