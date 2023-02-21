from collections import Counter
def solution(clothes):
    # key*nums들의 곱 -1 = answer
    keys = [i[1] for i in clothes]
    sol = Counter(keys)
    ans = 1
    for i,v in sol.items():
        ans *= (1+v)
    return ans-1