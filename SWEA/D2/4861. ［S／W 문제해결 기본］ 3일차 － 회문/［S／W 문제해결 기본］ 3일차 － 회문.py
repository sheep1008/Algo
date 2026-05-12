T = int(input())
for t in range(1, T+1):
    board = []
    N, M = map(int, input().split())
    answer = ""
    for n in range(N):
        s = input()
        board.append(s)

    for i in range(N):
        if answer:
            break
        for j in range(N-M+1):
            s = board[i][j:j+M]
            if s==s[::-1]:
                answer = s
                break

    for j in range(N):
        if answer:
            break
        
        for i in range(N-M+1):
            target = ""
            for k in range(i, i+M):
                target += board[k][j]

            if target == target[::-1]:
                answer = target
                break
    print(f"#{t} {answer}")