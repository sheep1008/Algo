import heapq
from collections import defaultdict

INF = float('inf')

def solution(N, road, K):
    answer = 0
    graph = defaultdict(list)
    for node1, node2, weight in road:
        graph[node1].append((node2, weight))
        graph[node2].append((node1, weight))
    distances = [INF] * (N+1)
    distances[1] = 0
    visited = [False] * (N+1)
    
    priority_queue = [(0, 1)]
    
    while priority_queue:
        distance, current_node = heapq.heappop(priority_queue)
        if visited[current_node]:
            continue
        visited[current_node] = True
        
        for next_node, weight in graph[current_node]:
            new_distance = weight + distance
            if new_distance < distances[next_node]:
                distances[next_node] = new_distance
            
            heapq.heappush(priority_queue, (distances[next_node], next_node))
            
    for idx in range(1, N+1):
        if distances[idx] <= K:
            answer += 1
            
    return answer