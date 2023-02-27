import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    if K == 0 or K <= scoville[0]:
        return 0

    while(1):
        if len(scoville) == 1:
            return -1
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)

        answer += 1

        if scoville[0] >= K:
            return answer
