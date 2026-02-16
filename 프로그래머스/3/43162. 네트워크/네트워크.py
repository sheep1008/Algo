def solution(n, computers):
    answer = 0
    visited = [False] * n

    def dfs(i):
        visited[i] = True
        for neighbor in range(n):
            # i번 컴퓨터와 연결되어 있고, 아직 방문하지 않은 컴퓨터라면 탐색
            if computers[i][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    for i in range(n):
        # 아직 방문하지 않은 컴퓨터라면 새로운 네트워크 시작점
        if not visited[i]:
            dfs(i)
            answer += 1 # 네트워크 개수 추가
            
    return answer