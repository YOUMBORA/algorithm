from itertools import product as pd

def solution(numbers, target):
    cnt = 0

    number = [[x, -x] for x in numbers]

    list_ = list(pd(*number))

    for i in list_:
        if sum(i) == target:
            cnt += 1

    return cnt
