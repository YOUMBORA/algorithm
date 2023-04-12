import sys
input = sys.stdin.readline

# 입력 받기
n, m, k = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
tree = []
for _ in range(m):
    x, y, z = map(int, input().split())
    tree.append([x-1, y-1, z])

# 가장 처음에 양분은 모든 칸에 5만큼씩 들어있음
food = [[5 for _ in range(n)] for _ in range(n)]


def spring(food, tree):
    # 만약, 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다.
    tree.sort(key=lambda x: x[2])
    death = []
    idx = []
    # print("food", food)
    for i in range(len(tree)):
        # 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다.
        if food[tree[i][0]][tree[i][1]] >= tree[i][2]:
            food[tree[i][0]][tree[i][1]] -= tree[i][2]
            tree[i][2] += 1
        # 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
        else:
            death.append(tree[i])
            idx.append(i)

    for j in range(len(idx)-1, -1, -1):
        del tree[idx[j]]

    return death


def summer(food, death):
    # 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 
    for i in range(len(death)):
        food[death[i][0]][death[i][1]] += int(death[i][2] / 2)


def autumn(tree):
    new_trees = []
    for i in range(len(tree)):
        # 번식하는 나무는 나이가 5의 배수, 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
        if tree[i][2] % 5 == 0:
            dx = [-1, -1, -1, 0, 0, 1, 1, 1]
            dy = [-1, 0, 1, -1, 1, -1, 0, 1]

            for j in range(8):
                nx = tree[i][0] + dx[j]
                ny = tree[i][1] + dy[j]

                if (0 <= nx < n) and (0 <= ny < n):
                    new_trees.append([nx, ny, 1])

    tree += new_trees
    return tree


def winter(A, food):
    # S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다.
    for i in range(len(A)):
        for j in range(len(A[i])):
            food[i][j] += A[i][j]


for year in range(k):
    death = spring(food, tree)
    summer(food, death)
    tree = autumn(tree)
    winter(A, food)

print(len(tree))