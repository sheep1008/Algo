dr = [-1, -1, 0, 1]
dc = [0, 1, 1, 1]

def check_omok(N, board):
    for r in range(N):
        for c in range(N):
            if board[r][c] == 'o':
                for i in range(4):
                    cnt = 1
                    for k in range(1, 5):
                        nr = r + dr[i] * k
                        nc = c + dc[i] * k
                        if 0<=nr<N and 0<=nc<N and board[nr][nc] == 'o':
                            cnt+=1
                        else:
                            break
                    if cnt >= 5:
                        return "YES"
    return "NO"
T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    
    answer = check_omok(N, board)
    print(f"#{t} {answer}")