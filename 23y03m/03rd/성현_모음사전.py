from itertools import product

def solution(word):
    dict = []
    for i in range(5):
        for p in product("AEIOU",repeat=i+1):
            dict.append("".join(p))
    dict.sort()
    return dict.index(word)+1