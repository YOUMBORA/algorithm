from itertools import permutations
def solution(numbers):
    answer = 0
    tmp = set()
    for i in range(len(numbers)):
        tmp |= set(map(int,map(''.join,(list(permutations(list(numbers),i+1))))))
    tmp -= set(range(0,2))
    for t in tmp:
        q = 0
        for r in range(2,t):
            if t%r == 0:
                q = 1
                break
        if q == 0:
            answer += 1
    return answer