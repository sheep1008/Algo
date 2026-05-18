def dfs(idx, curr_sum):
    global K, ans
    if curr_sum > K:
        return
    if curr_sum == K:
        ans+=1
        return
    for j in range(idx, N):
        if not visited[j]:
            visited[j] = True
            dfs(j+1, curr_sum+arr[j])
            visited[j] = False
    
T = int(input())
for t in range(1,T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [False] * N
    ans = 0
    dfs(0, 0)
    print(f"#{t} {ans}")