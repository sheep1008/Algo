from collections import defaultdict

def solution(tickets):
    # 1. 인접 리스트 그래프 생성
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)
    
    # 2. 알파벳 역순 정렬 (pop()으로 알파벳 순서대로 꺼내기 위함)
    for key in graph:
        graph[key].sort(reverse=True)
    
    stack = ["ICN"]
    path = []
    
    while stack:
        top = stack[-1]
        
        # 해당 공항에서 출발하는 티켓이 남아있다면
        if top in graph and graph[top]:
            stack.append(graph[top].pop())
        # 더 이상 갈 곳이 없다면 경로에 추가 (역순으로 쌓임)
        else:
            path.append(stack.pop())
            
    # 3. 역순으로 담긴 경로를 뒤집어서 반환
    return path[::-1]