from collections import deque

while True:
    m = int(input())
    
    if m == 0:
        break
    
    sentence = list(input())

    queue = deque()
    queue.append(sentence[0])

    ans = 0
    for i in range(1, len(sentence)):
        ans = max(len(queue), ans)
        word = sentence[i]

        queue.append(word)

        while len(set(queue)) > m:
            queue.popleft()

    print(ans)