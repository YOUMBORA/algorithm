from itertools import permutations

def solution(k, dungeons):
    
    # 방문할 순서 조합 만들기
    num = [x for x in range(len(dungeons))]
    lst = list(permutations(num, len(dungeons)))
    
    # 각 조합이 가능한 개수 담는 list 생성
    result = []
    # 각각의 조합들을 하나씩 실행해보기
    for case in lst:
        ans = 0
        cur_k = k
        # 한 조합을 실제로 실행해보면서 유저가 탐험할 수 있는 최대 던전 수 찾아서 list에 저장하기
        for idx in case:
            if cur_k >= dungeons[idx][0]:
                cur_k -= dungeons[idx][1]
                ans += 1
            else:
                break
        result.append(ans)
    
    return max(result)