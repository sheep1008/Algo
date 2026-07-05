# 시계 방향 90도 회전 함수
def rotate_90(matrix, n):
    result = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            result[c][n - 1 - r] = matrix[r][c]
    return result

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    board = [input().split() for _ in range(N)]
    
    # 순차적으로 회전 적용
    r90 = rotate_90(board, N)
    r180 = rotate_90(r90, N)
    r270 = rotate_90(r180, N)
    
    print(f"#{t}")
    
    for i in range(N):
        print(f"{''.join(r90[i])} {''.join(r180[i])} {''.join(r270[i])}")