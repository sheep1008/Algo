from collections import deque

def bfs(start, n, adj):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    count = 1
    
    while queue:
        curr = queue.popleft()
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    return count

def solution(n, wires):
    answer = n
    
    # 1. 모든 전선을 하나씩 끊어보기
    for i in range(len(wires)):
        # i번째 전선을 제외한 인접 리스트 구성
        adj = [[] for _ in range(n + 1)]
        for j, (v1, v2) in enumerate(wires):
            if i == j: continue # 선택된 전선은 무시 (끊기)
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        # 2. 한쪽 전력망의 송전탑 개수 세기
        res = bfs(1, n, adj)
        
        # 3. 두 전력망 개수 차이의 최솟값 갱신
        # |한쪽 개수 - 다른쪽 개수| = |res - (n - res)|
        answer = min(answer, abs(res - (n - res)))
        
    return answer