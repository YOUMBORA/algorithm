def solution(arr):
    queue = []
    for a in arr:
        if queue == []:
            queue.append(a)
        if queue[-1] == a:
            continue
        else:
            queue.append(a)
    return queue