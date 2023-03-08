def solution(n, lost, reserve):
    answer = 0
    total = [1]*n
    for l in lost:
        total[l-1] -= 1
    for r in reserve:
        total[r-1] += 1
    for i, t in enumerate(total):
        if t == 0:
            if i>0 and total[i-1] > 1:
                total[i-1] -= 1
                total[i] += 1
            elif i< len(total)-1 and total[i+1] > 1:
                total[i+1] -= 1
                total[i] += 1
        if total[i] > 0:
            answer += 1
    return answer