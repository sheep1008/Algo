from collections import deque
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

def bfs(maps):
    start_row, start_col, distance = 0, 0, 1
    destination = (len(maps)-1, len(maps[0])-1)
    
    queue = deque([(start_row, start_col, distance)])
    visited = set()
    visited.add((start_row, start_col))

    while queue:
        curr_row, curr_col, distance = queue.popleft()
        
        if (curr_row, curr_col) == destination:
            return distance
        
        for idx in range(4):
            nr = curr_row + dr[idx]
            nc = curr_col + dc[idx]
            
            if nr < 0 or nr >= len(maps) or nc < 0 or nc >= len(maps[0]):
                continue
            if (nr, nc) in visited or maps[nr][nc] == 0:
                continue
            queue.append((nr, nc, distance+1))
            visited.add((nr, nc))
    return -1

def solution(maps):
    answer = bfs(maps)
    
    return answer