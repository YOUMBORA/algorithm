def solution(s):
    stack = []
    for ss in s:
        if ss == "(":
            stack.append(ss)
        elif ss == ")":
            if len(stack)>0 and stack[-1]=="(":
                stack.pop(-1)
            else:
                stack.append(ss)
    if len(stack)==0:
        return True
    return False