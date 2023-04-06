N = int(input())
K = int(input())

apple_list = []
for i in range(K):
    apple_list.append(list(map(int, input().split())))

total_move = int(input())
snake_list = []
for j in range(total_move):
    snake_list.append(input().split())

graph = [[0 for _ in range(N)] for _ in range(N)]

for apple in apple_list:
    graph[apple[0]-1][apple[1]-1] = 1


def change_dir(new_dir, coor):

    if new_dir == 0:
        coor[1] += 1
    elif new_dir == 1:
        coor[0] += 1
    elif new_dir == 2:
        coor[1] -= 1
    elif new_dir == 3:
        coor[0] -= 1

    return coor


snake_head = [0, 0]
snake_tail = [0, 0]

# E,S,W,N -> [0,1,2,3]
snake_dir = 0
dir_dict = {(0, 0): 0}

time = 0

while True:
    time += 1
    # print(snake_dir)
    # go forward as right direction
    snake_head = change_dir(snake_dir, snake_head)

    # check game over condition
    if (snake_head[0] not in range(N)) or (snake_head[1] not in range(N)):
        print(time)
        break

    if graph[snake_head[0]][snake_head[1]] == 2:
        print(time)
        break
    elif graph[snake_head[0]][snake_head[1]] == 1:
        graph[snake_head[0]][snake_head[1]] = 2
    elif graph[snake_head[0]][snake_head[1]] == 0:
        graph[snake_head[0]][snake_head[1]] = 2
        graph[snake_tail[0]][snake_tail[1]] = 0
        snake_tail = change_dir(
            dir_dict[(snake_tail[0], snake_tail[1])], snake_tail)
    if snake_list:
        if time == int(snake_list[0][0]):
            # print("direction changed")
            temp = snake_list.pop(0)
            if temp[1] == 'D':
                snake_dir = (snake_dir + 1) % 4
            elif temp[1] == 'L':
                snake_dir = (snake_dir - 1) % 4
            # print(temp, snake_dir)

    dir_dict[(snake_head[0], snake_head[1])] = snake_dir

    # print("time = ", time)
    # print("graph = ", graph)
