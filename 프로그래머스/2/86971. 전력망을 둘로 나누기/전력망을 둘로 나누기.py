from collections import deque

def get_node_count(start_node, n, adj, broken_edge):
    visited = [False] * (n+1)
    visited[start_node] = True
    queue = deque([start_node])
    count = 1
    
    while queue:
        curr = queue.popleft()
        for neighbor in adj[curr]:
            if (curr, neighbor) == broken_edge or (neighbor, curr) == broken_edge:
                continue
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    return count

def solution(n, wires):
    answer = n
    
    adj = [[] for _ in range(n+1)]
    for v1, v2 in wires:
        adj[v1].append(v2)
        adj[v2].append(v1)
        
    for v1, v2 in wires:
        cnt = get_node_count(v1, n, adj, (v1, v2))
        
        diff = abs(cnt - (n - cnt))
        answer = min(answer, diff)
        
    return answer