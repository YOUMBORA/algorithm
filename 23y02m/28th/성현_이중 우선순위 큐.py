import heapq
def solution(operations):
    answer = []
    q = []
    heapq.heapify(q)
    for o in operations:
        order, num = o.split()
        if order == "I":
            heapq.heappush(q, int(num))
        else:
            if len(q) >0 :
                if num == "-1":
                    heapq.heappop(q)
                else:
                    q.pop()
    if len(q)>0:
        answer = [max(q), min(q)]
    else:
        answer = [0,0]
    return answer
                