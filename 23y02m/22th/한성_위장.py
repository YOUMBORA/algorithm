from collections import Counter
def solution(clothes):
    # key*nums들의 곱 -1 = answer
    keys = [i[1] for i in clothes]
    sol = Counter(keys)
    ans = 1
    for i in sol:
        ans *= (1+sol[i])
    return ans-1