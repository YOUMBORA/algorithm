answer = -1

def dfs(n, pos, num, number, s):
    global answer
    if pos > 8:
        return
    if num==number:
        if pos < answer or answer == -1:
            answer = pos
        return
    nn=0
    for i in range(8):
        nn = nn*10+n
        dfs(n, pos+1+i, num+nn, number, s+'+')
        dfs(n, pos+1+i, num-nn, number, s+'-')
        dfs(n, pos+1+i, num*nn, number, s+'*')
        dfs(n, pos+1+i, num/nn, number, s+'/')

def solution(N, number):    
    dfs(N, 0, 0, number, '')    
    return answer