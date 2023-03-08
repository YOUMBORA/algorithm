uf = []

def find(a):
    global uf
    if uf[a] < 0: 
        return a
    uf[a] = find(uf[a])
    return uf[a]

def merge(a, b):
    global uf
    pa = find(a)
    pb = find(b)
    if pa == pb: 
        return
    uf[pa] += uf[pb]
    uf[pb] = pa
    
def solution(n, wires):
    global uf
    answer = int(1e9)
    k = len(wires)
    for i in range(k):
        uf = [-1 for _ in range(n+1)]
        tmp = [wires[x] for x in range(k) if x != i]
        print(tmp)
        for a, b in tmp: 
            merge(a, b)
            print(uf)
        v = [x for x in uf[1:] if x < 0]
        print(v)
        answer = min(answer, abs(v[0]-v[1]))
    return answer

# def solution(n, wires):
#     answer = 100
#     for i in range(1, len(wires)-1):
#         connected = 1
#         wl = wires[:i]
#         wr = wires[i+1:]
#         if len(wl) > 1:
#             for l in range(len(wl)-1):
#                 if wl[l][0] == wl[l+1][0]:
#                     connected =1
#                 elif wl[l][0] == wl[l+1][1]:
#                     connected =1
#                 elif wl[l][1] == wl[l+1][0]:
#                     connected =1
#                 elif wl[l][1] == wl[l+1][1]:
#                     connected =1
#                 else:
#                     connected = 0
                    
#         if wl[-1][0] == wr[0][0]:
#             connected = 0
#         elif wl[-1][0] == wr[0][1]:
#             connected = 0
#         elif wl[-1][1] == wr[0][0]:
#             connected = 0
#         elif wl[-1][1] == wr[0][1]:
#             connected = 0
#         if connected == 1:
#             if len(wl) >= len(wr):
#                 answer = min(len(wl)-len(wr),answer)
#             else:
#                 answer = min(len(wr)-len(wl),answer)       
#     return answer