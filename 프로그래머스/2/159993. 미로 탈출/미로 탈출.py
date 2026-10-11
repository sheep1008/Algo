dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

from collections import deque

def find_lever(row, col, board):
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    visited[row][col] = True
    queue = deque([(row, col, 0)])
    
    while queue:
        curr_row, curr_col, curr_time = queue.popleft()
        for idx in range(4):
            nr = curr_row + dr[idx]
            nc = curr_col + dc[idx]
            if nr < 0 or nr >=len(board) or nc < 0 or nc >= len(board[0]):
                continue
            if visited[nr][nc]:
                continue
            
            if board[nr][nc] == 'L':
                return nr, nc, curr_time+1
            
            if board[nr][nc] != 'X':
                visited[nr][nc] = True
                queue.append((nr, nc, curr_time+1))
            
    return False

def find_exit(row, col, board, time):
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    visited[row][col] = True
    queue = deque([(row, col, time)])
    
    while queue:
        curr_row, curr_col, curr_time = queue.popleft()
        
        for idx in range(4):
            nr = curr_row + dr[idx]
            nc = curr_col + dc[idx]
            if nr < 0 or nr >=len(board) or nc < 0 or nc >= len(board[0]):
                continue
            if visited[nr][nc]:
                continue
            
            if board[nr][nc] == 'E':
                return nr, nc, curr_time+1
            
            if board[nr][nc] != 'X':
                visited[nr][nc] = True
                queue.append((nr, nc, curr_time+1))
            
    return False

def solution(maps):
    answer = 0
    curr_row, curr_col = 0, 0
    board = []
    
    for row in range(len(maps)):
        array = list(maps[row])
        if 'S' in array:
            curr_row, curr_col = row, array.index('S')

        board.append(array)
    
    lever_inform = find_lever(curr_row, curr_col, board)
    if not lever_inform:
        return -1
    
    exit_inform = find_exit(lever_inform[0], lever_inform[1], board, lever_inform[2])
    
    if not exit_inform:
        return -1
    
    return exit_inform[2]