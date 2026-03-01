def solution(arr):
    # 1. 숫자와 연산자 분리
    nums = [int(x) for x in arr[::2]]
    ops = arr[1::2]
    n = len(nums)
    
    # 2. 최댓값과 최솟값을 저장할 DP 테이블 초기화
    max_dp = [[-float('inf')] * n for _ in range(n)]
    min_dp = [[float('inf')] * n for _ in range(n)]
    
    # 3. 길이가 1인 구간(자기 자신) 초기화
    for i in range(n):
        max_dp[i][i] = min_dp[i][i] = nums[i]
        
    # 4. 구간 길이를 늘려가며 DP (d는 구간의 길이 차이)
    for d in range(1, n):
        for i in range(n - d):
            j = i + d
            # i부터 j 사이의 연산자 위치 k
            for k in range(i, j):
                if ops[k] == '+':
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k+1][j])
                elif ops[k] == '-':
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j])
                    
    return max_dp[0][n-1]