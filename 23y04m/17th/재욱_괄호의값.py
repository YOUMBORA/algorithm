import sys
from collections import deque

input = sys.stdin.readline

bracket = deque(list(input().strip()))

open = deque([])
open_count = 1

result = 0

while bracket:
    bracket_pop = bracket.popleft()
    
    if bracket_pop == "(":
        open.append("(")
        open_count *= 2
    
    elif bracket_pop == "[":
        open.append("[")
        open_count *= 3
    
    elif bracket_pop == ")":
        if not open or open[-1] != "(":
            print(0)
            exit()
        if open[-1] == "(":
            result += open_count
            open.pop()
            open_count //= 2
                
    elif bracket_pop == "]":
        if not open or open[-1] != "[":
            print(0)
            exit()
        if open[-1] == "[":
            result += open_count
            open.pop()
            open_count //= 3
    
    print(open_count)
    print(result)
    print("-------")
            
            
if not open:
    print(result)


# import sys
# input = sys.stdin.readline
# arr = input().rstrip()
# stack = []
# cnt = 1
# res = 0
# for i in range(len(arr)):
#     if arr[i] == '(':
#         stack.append(arr[i])
#         cnt *= 2
#     elif arr[i] == '[':
#         stack.append(arr[i])
#         cnt *= 3
#     elif arr[i] == ')':
#         if stack == [] or stack[-1] == '[':
#             print(0)
#             break
#         else:
#             if arr[i-1] =='(':
#                 res+=cnt
#             stack.pop()
#             cnt //= 2
#     elif arr[i] == ']':
#         if stack == [] or stack[-1] == '(':
#             print(0)
#             break
#         else:
#             if arr[i-1] =='[':
#                 res+=cnt
#             stack.pop()
#             cnt //= 3
# else:
#     if stack:
#         print(0)
#     else:
#         print(res)
