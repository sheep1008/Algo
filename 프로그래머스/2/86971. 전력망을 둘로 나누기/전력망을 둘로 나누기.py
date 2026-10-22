def dfs(current, skip, graph, visited, count):
    visited[current] = True
    for next_node in graph[current]:
        if visited[next_node] or next_node == skip:
            continue
        count += 1
        count = dfs(next_node, skip, graph, visited, count)
    
    return count

from collections import defaultdict

def solution(n, wires):
    answer = float('inf')
    graph = defaultdict(list)
    
    for node1, node2 in wires:
        graph[node1].append(node2)
        graph[node2].append(node1)
        
    for wire in wires:
        visited = [False] * (n+1)
        count1 = dfs(wire[0], wire[1], graph, visited, 0)
        count2 = dfs(wire[1], wire[0], graph, visited, 0)
        
        answer = min(answer, abs(count1-count2))
        
    return answer