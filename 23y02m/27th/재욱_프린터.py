from collections import deque
def solution(priorities, location):

    count = deque([i for i in range(len(priorities))])
    priorities = deque(priorities)

    result = []
    test= []

    while count:
        t = max(priorities)
        
        if priorities[0] == t:
            test.append(priorities.popleft())
            result.append(count.popleft())
    
        else:
            priorities.append(priorities.popleft())
            count.append(count.popleft())


    return result.index(location) + 1
