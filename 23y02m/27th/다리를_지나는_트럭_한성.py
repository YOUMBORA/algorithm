from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    # bridge_length 는 트럭이 들어갈 수 있는 개수
    # weight 는 트럭이 최대 들어갈 수 있는 무게
    queue = deque(truck_weights)
    bridge = [0 for _ in range(bridge_length)]
    while queue:
        kg = queue.popleft()
        waiting = 0
        print('kg',kg)
        for _ in range(min(bridge_length,len(queue))):
            tmp = queue.popleft()
            print('for', _)
            if kg +tmp < weight:
                waiting += 1
                kg +=tmp
            elif kg + tmp == weight:
                waiting +=1
                kg +=tmp
                break
            else:
                queue.appendleft(tmp)
                print('break')
                break
        print(queue)
        print('wait', waiting)
        # 묶음을 정의하고 waiting + bridge_length 로 초를 정의하면 된다. 
        answer += bridge_length + waiting
        print('answer',answer)
    return answer
# waiting time 에 대한 정의가 필요한듯 하나 어떻게 정의해야할 지 모르겠음.
if __name__== '__main__':
    bridge_length = 2
    weight = 10
    truck_weights = [7,4,5,6]
    print(solution(bridge_length,weight,truck_weights))
    # bridge_length = 100
    # weight = 100
    # truck_weights = [10]
    # print(solution(bridge_length,weight,truck_weights))
    # bridge_length = 100
    # weight = 100
    # truck_weights = [10,10,10,10,10,10,10,10,10,10]
    # print(solution(bridge_length,weight,truck_weights))