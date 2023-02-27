################# 효율성 통과 X ######################
def solution(scoville, K):
    answer = 0
    
    scoville.sort()
    
    while scoville[0] < K:
        if len(scoville) > 1:
            score = scoville.pop(0)
            scoville[0] = scoville[0] * 2 + score
            answer += 1
            scoville.sort()
        else:
            return -1
             
    return answer
#####################################################

################# 모두 통과 O ########################
import heapq

def solution(scoville, K):
    answer = 0
    
    # list를 heapq으로 변환 -> 자동 정렬(오름차순)
    heapq.heapify(scoville)
    
    # 조건 : 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복
    while scoville[0] < K:
        if len(scoville) > 1:
            # heap에서 가장 작은 원소를 pop & 리턴
            min_score = heapq.heappop(scoville)
            min2_score = heapq.heappop(scoville)
            mix_score = min_score + min2_score * 2
            heapq.heappush(scoville, mix_score)
            answer += 1
        else:
            # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
            return -1
             
    return answer