while True:
    m = int(input())
    if m == 0:
        break
    s = input()
    value = 0
    for i in range(len(s)):
        start = i
        end = len(s)-1
        mid = (start+end)//2
        sett = len(set(list(s[start:mid])))
        if  sett> m:
            end = mid -1
        else:
            if sett >= value:
                value = max(len(list(s[start:mid])),value)
            start = mid +1
    print(value)

    

