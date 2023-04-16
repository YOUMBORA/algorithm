import sys
input = sys.stdin.readline

answer = 0
s = list(input())
stack = []
tmp = 1

for i in range(len(s)):

    if s[i] == '(':
        tmp *= 2
        stack.append(s[i])
    
    elif s[i] == '[':
        tmp *= 3
        stack.append(s[i])

    elif s[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if s[i-1] == '(':
            answer += tmp
        stack.pop()
        tmp //= 2

    elif s[i] == ']':
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if s[i-1] == '[':
            answer += tmp
        stack.pop()
        tmp //= 3
        
if stack:
    print(0)
else:
    print(answer)