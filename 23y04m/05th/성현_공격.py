from collections import deque 

N, R, D, X, Y = map(int,input().split())
T = {tuple(map(int,input().split())) for _ in range(N)}

queue = deque()
queue.append((X,Y,0))
answer = 0
while queue:
    x, y, d = queue.popleft()
    if d:
        answer += D / (2**(d-1))
    candidate = []
    for t in T:
        if (x - t[0])**2 + (y-t[1])**2 <= R**2:
            candidate.append(t)
    for c in candidate:
        queue.append((c[0],c[1],d+1))
    T -= set(candidate)

print(round(answer, 2)) if int(answer) != answer else print(f'{int(answer)}.0')

