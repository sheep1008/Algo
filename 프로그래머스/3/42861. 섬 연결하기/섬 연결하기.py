def find(x, parents):
    if x!= parents[x]:
        parents[x] = find(parents[x], parents)
    return parents[x]

def union(answer, cost, parents):
    root1 = find(cost[0], parents)
    root2 = find(cost[1], parents)
    
    if root1 != root2:
        parents[root2] = root1
        answer += cost[2]
    
    return answer

def solution(n, costs):
    # 비용 순으로 오름차순 정렬
    costs.sort(key=lambda x: x[2])
    parents = list(range(n+1))
    answer = 0
    # 하나씩 돌면서 연결이 안되어 있으면 비용 추가
    for cost in costs:
        answer = union(answer, cost, parents)
        
    return answer