import sys
from collections import deque
input = sys.stdin.readline

# 입력 받기
n, m, start_engine = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
start_y, start_x= map(int, input().split())
people = []
for i in range(m):
    people.append(list(map(int, input().split())))

# 최단 거리에 있는 승객 찾기
def passenger(x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()



# 손님 목적지까지 가기
def destination():
    pass


# 조건에 맞게 승객 태우고 목적지까지 가보기
for _ in range(m):
    pass