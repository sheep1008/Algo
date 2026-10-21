def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(i):
        visited[i] = True
        for neighbor in range(n):
            if computers[i][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)
                
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
            
    return answer