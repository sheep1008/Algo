def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a< b:
        parent[b] = a
    else:
        parent[a] = b
        
def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    
    parent = [i for i in range(n)]
    total_cost = 0
    bridge_count = 0
    
    for u, v, cost in costs:
        if find_parent(parent, u) != find_parent(parent, v):
            union_parent(parent, u, v)
            total_cost += cost
            bridge_count += 1
            
            if bridge_count == n-1:
                break
                
    return total_cost