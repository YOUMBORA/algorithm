from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:

        cnt = 0
        t = prices.popleft()

        for i in prices:
            cnt += 1
            if t > i:
                break

        answer.append(cnt)

    return answer
