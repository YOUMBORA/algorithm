import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())
lst = list(map(int, input().split()))

# 이진탐색을 사용하기 위해 오름차순 정렬하기
lst.sort()

ans = 0
# x는 좋은 수인지 판별되는 대상(index)
for x in range(n):
    # tmp는 x(index)를 제외한 나머지로 구성된 list
    tmp = lst[:x] + lst[x+1:]
    
    start = 0
    end = n - 2
    cnt = 0
    # start + end = x 가 되는 값을 찾기 위한 이분탐색
    while start < end:
        sum_ = tmp[start] + tmp[end]

        if sum_ == lst[x]:
            cnt += 1
            break
        elif sum_ > lst[x]:
            end -= 1
        else:
            start += 1
            
    # 좋은 수라면, ans에 1추가
    if cnt > 0:
        ans += 1

print(ans)