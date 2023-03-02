def solution(sizes):
    arr = [0, 0]
    
    for i, t in sizes:
        if i < t:
            i, t = t, i
        arr[0] = max(arr[0], i)
        arr[1] = max(arr[1], t)
    
    return arr[0] * arr[1]
