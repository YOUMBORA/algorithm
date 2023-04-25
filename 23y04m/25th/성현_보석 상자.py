N , M = map(int, input().split())
J = [int(input()) for _ in range(M)]

s = 1
e = max(J)
answer = e

while s<=e:
    mid = (s+e)//2

    p = 0
    for j in J:
        if j%mid:
            p += j//mid + 1
        else:
            p += j//mid
    if p > N:
        s = mid +1
    else:
        answer = min(answer,mid)
        e = mid -1

print(answer)