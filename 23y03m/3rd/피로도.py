def solution(k, dungeons):
    result = [0]
    for id in range(len(dungeons)):
        if k >= dungeons[id][0]:
            new_dungeons = dungeons[:id] + dungeons[id+1:]
            delta_cnt = solution(k - dungeons[id][1], new_dungeons)
            result.append(1+delta_cnt)
    return max(result)
