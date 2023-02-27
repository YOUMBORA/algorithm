from collections import deque
def solution(bridge_length, weight, truck_weights):
    cnt = 0

    result = [0] * bridge_length
    
    truck_weights = deque(truck_weights)
    result = deque(result)

    while result:
        cnt += 1
        result.popleft()

        if truck_weights:
            if sum(result) + truck_weights[0] <= weight:
                result.append(truck_weights.popleft())

            else:
                result.append(0)
        

    return cnt
