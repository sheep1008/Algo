def f(start, end, k):
    c = (start+end)//2
    if c == k:
        return 1
    elif c>k:
        return 1 + f(start, c, k)
    else:
        return 1 + f(c, end, k)

T = int(input())
for t in range(1, T+1):
    END, A, B = map(int, input().split())
    answer1 = f(1,END, A)
    answer2 = f(1, END, B)
    answer = 0
    if answer1 < answer2:
        answer = 'A'
    elif answer1 > answer2:
        answer = 'B'
    print(f"#{t} {answer}")