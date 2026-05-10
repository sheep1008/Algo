n = int(input())
for i in range(n):
    day = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    last = arr[-1]
    for idx in range(day-1, -1, -1):
        if arr[idx] > last:
            last = arr[idx]
        else:
            answer += last-(arr[idx])
    print(f"#{i+1} {answer}")