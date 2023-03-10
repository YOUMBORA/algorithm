# 입력 받기
x, y = map(int, input().split())
# 형택이의 승률
z = 100 * y // x

cnt = 0
# 게임 횟수 제한 조건
start = 1
end = 1000000000

# 이진 탐색
while start <= end:

    # 승률이 절대 변하지 않는 경우
    if z == 100:
        break
    
    # 게임 횟수 중간값
    mid = (start + end) // 2

    # 게임을 mid판 더 했을 때의 승률과 입력으로 받은 값으로 나온 승률 비교하기
    if (y + mid) * 100 // (x + mid) <= z:
        start = mid + 1
    else:
        cnt = mid
        end = mid - 1

# 승률이 변하지 않는다면 -1, 아니라면 최소 게임 몇 판 더 해야하는지 출력하기
if cnt == 0:
    print(-1)
else:
    print(cnt)