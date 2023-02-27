from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    now_weight = weight
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    
    cnt = 0
    while truck_weights:
        answer += 1
        bridge.popleft()
        if sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)

    for i in range(-1, len(bridge), -1):
        if bridge[i] == 0:
            cnt += 1
            break
        else:
            cnt += 1
    answer += len(bridge) - cnt
    
    
            
    
    
    return answer
