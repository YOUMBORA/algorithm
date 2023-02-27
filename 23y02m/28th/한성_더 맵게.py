import heapq
def solution(scoville, k):
    answer = 0
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)
    while heap[0] < k:
        if len(heap) <2:
            return -1
        else:
            tmp1, tmp2 = heapq.heappop(heap), heapq.heappop(heap)
            heapq.heappush(heap, (tmp1 + tmp2*2))
            answer +=1
        
    return answer