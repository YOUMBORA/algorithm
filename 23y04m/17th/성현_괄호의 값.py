import sys 
input = lambda : sys.stdin.readline().strip()

N = list(input())

stack = []
answer = 0
temp = 1
for i, n in enumerate(N):
    if n == '(':
        stack.append(n)
        temp *= 2
    elif n == '[':
        stack.append(n)
        temp *= 3
    elif n == ')':
        if len(stack)==0 or stack[-1]=='[':
            answer = 0
            break 
        if N[i-1] =='(':
            answer += temp 
        stack.pop()
        temp = temp//2
    elif n == ']':
        if len(stack)==0 or stack[-1]=='(':
            answer = 0
            break 
        if N[i-1] =='[':
            answer += temp 
        stack.pop()
        temp = temp//3

if len(stack) > 0 :
    print(0)
else:
    print(answer)
                    

