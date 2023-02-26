from collections import deque

def solution(priorities, location):
    answer = 1
    
    # priorities에 idx 정보 추가
    idx_priorities = deque((num, idx) for idx, num in enumerate(priorities))

    while True:
        # 조건 1
        now = idx_priorities.popleft()
        # 조건 2
        if len(idx_priorities) > 1 and max(idx_priorities, key=lambda x: x[0])[0] > now[0]:
            idx_priorities.append(now)
        else:
            # 조건 3
            if now[1] != location:
                answer += 1
            else:
                break
                
    return answer