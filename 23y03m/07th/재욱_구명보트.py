from collections import deque

def solution(people, limit):
    answer = 0
    result = limit
    people.sort()

    people = deque(people)

    while True:
        if len(people) == 0:
            break
        
        if len(people) >= 2:
            if people[0] + people[-1] <= limit:
                people.popleft()
                people.pop()
                answer += 1
            else:
                people.pop()
                answer += 1
        
        else:
            people.pop()
            answer += 1

    return answer
