def dfs(current_k, cnt, dungeons, visited):
    answer_max = cnt
    
    for idx in range(len(dungeons)):
        if current_k < dungeons[idx][0] or visited[idx]:
            continue
        visited[idx] = True
        answer_max = max(
            answer_max,
            dfs(current_k - dungeons[idx][1], cnt+1, dungeons, visited)
        )
        visited[idx] = False
    
    return answer_max

def solution(k, dungeons):
    visited = [False] * len(dungeons)
    answer = dfs(k, 0, dungeons, visited)
    return answer