def solution(number, k):
    stack = []
    for num in number:
        while k>0 and len(stack) != 0 and stack[-1] < num:
            stack.pop()
            k-=1
        stack.append(num)
    return ''.join(stack[:len(stack)-k])