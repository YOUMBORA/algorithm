from collections import deque

def bfs():

    dx = [0, 1, -1]

    while queue:
        x = queue.popleft()

        for i in range(len(dx)):
            if dx[i] == 0:
                nx = x * 2
                if 0 <= nx < t and l[nx] == -1:
                    l[nx] = l[x]
                    queue.appendleft(nx)

            else:
                nx = x + dx[i]
                if 0 <= nx < t and l[nx] == -1:
                    l[nx] = l[x] + 1
                    queue.append(nx)


n, k = map(int, input().split())

l = [-1 for i in range(100000+1)]
t = len(l)
l[n] = 0

queue = deque()
queue.append(n)

if n == k:
    print(0)

else:
    bfs()

    print(l[k])
