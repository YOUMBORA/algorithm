answer = 0

def dfs(idx, numbers, target, value):
    global answer 
    N = len(numbers)
    if (idx==N and target==value):
        answer+=1
        return 
    if (idx==N):
        return 
    dfs(idx+1, numbers, target, value+numbers[idx])
    dfs(idx+1, numbers, target, value-numbers[idx])

def solution(numbers, target):
    global answer 
    dfs(0,numbers,target,0)
    return answer

# def solution(numbers, target):
#     answer = 0 
#     stack = [[0,numbers[0]], [0, -1*numbers[0]]]
#     n = len(numbers)
#     while stack:
#         idx, temp = stack.pop()
#         idx +=1
#         if idx<n:
#             stack.append([idx, temp+numbers[idx]])
#             stack.append([idx, temp-numbers[idx]])
#         else:
#             if temp == target:
#                 answer +=1
#     return answer