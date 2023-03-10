from collections import deque
import sys

input = lambda : sys.stdin.readline().strip()

n, k = map(int, input().split())
v = "".join(input().split())

def bfs(v):
    visited = set(v)
    queue = deque([[v,0]])
    while len(queue) > 0:
        value, cnt = queue.popleft()
        temp = list(value)
        if temp == sorted(temp):
            return cnt
        else:
            for i in range(n-k+1):
                new_value = list(value)
                target = new_value[i:i+k]
                target.reverse()
                for j in range(k):
                    new_value[i+j] = target[j]
                new_word = "".join(new_value)
                if new_word not in visited:
                    visited.add(new_word)
                    queue.append([new_word,cnt+1])
    return -1
print(bfs(v))