# 효율성 1번 통과 못하면 deque 사용하면 통과됨!
# deque 안에서는 sort안됨

from collections import deque

def solution(people, limit):
    answer = 0
    
    # 몸무게 오름차순으로 정렬 후, deque에 넣어주기
    people.sort()
    people = deque(people)
    
    # 가장 몸무게가 적은 사람과 가장 몸무게가 많이 나가는 사람을 짝지어 무게 제한에 걸리는지 확인해보자
    while people:
        if people[0] + people[-1] > limit:
            people.pop()
            answer += 1
        elif len(people) == 1:
            people.pop()
            answer += 1
        else:
            people.pop()
            people.popleft()
            answer += 1
    
    return answer