T = int(input())
for t in range(1, T+1):
    target = list(input())
    curr = '0'
    answer = 0
    for n in target:
        if curr != n:
            answer += 1
            curr = str(n)
    print(f"#{t} {answer}")