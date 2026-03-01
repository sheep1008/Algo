def solution(m, n, puddles):
    ma = [[0] * (m+1) for _ in range(n+1)]
    
    puddles_set = {(y, x) for x, y in puddles}
    
    ma [1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i==1 and j==1:
                continue
                
            if (i, j) in puddles_set:
                ma[i][j] = 0
            else:
                ma[i][j] = (ma[i][j-1] + ma[i-1][j]) % 1000000007
            
    return ma[n][m]