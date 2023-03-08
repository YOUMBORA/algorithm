def solution(card):
    mi, ma = 0, 0
    for c in card:
        mi = max(min(c),mi)
        ma = max(max(c),ma)
    return mi * ma