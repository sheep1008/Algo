def explore(info, children, sheep_count, wolf_count, candidates):
    max_sheep = sheep_count
    
    for candidate in candidates:
        next_sheep = sheep_count
        next_wolf = wolf_count
        
        if info[candidate] == 0:
            next_sheep += 1
        else:
            next_wolf += 1
        
        if next_wolf >= next_sheep:
            continue
            
        next_candidates = [node for node in candidates if node != candidate]
        next_candidates.extend(children[candidate])
        max_sheep = max(max_sheep, explore(info, children, next_sheep, next_wolf, next_candidates))
    
    return max_sheep

from collections import deque

def solution(info, edges):
    children = [[] for _ in range(len(info))]
    
    for parent_node, child_node in edges:
        children[parent_node].append(child_node)
        
    return explore(info, children, 1, 0, list(children[0]))