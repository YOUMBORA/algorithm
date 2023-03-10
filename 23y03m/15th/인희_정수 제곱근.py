# 정수 입력 받기
n = int(input())

# n 조건에 따른 start, end 값 설정하기
start = 0
end = 2**63

ans = 0

# 이진 탐색
while start <= end:

    mid = (start + end) // 2

    # n의 정수 제곱근이 될 수 있는 가장 작은 mid를 구하자 
    if mid**2 >= n:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)