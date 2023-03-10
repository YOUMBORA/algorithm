def solution(n, computers):
    # dfs 함수
    def dfs(v):
        visited[v] = True
        
        for j in range(n):
            # 방문한 적 없는 컴퓨터이며 연결되어 있으면 dfs 재귀
            if not visited[j] and computers[v][j] == 1:
                dfs(j)
        
    cnt = 0
    visited = [False] * (n+1)

    # 모든 computer에서 네트워크 검사하기
    for i in range(n):
        if not visited[i]:
            dfs(i)
            cnt += 1

    return cnt