def power(a, b):
    if b == 1:
        return a
    return a*power(a, b-1)

for _ in range(10):
    t = input()
    a, b = map(int, input().split())
    answer = power(a, b)
    print(f"#{t} {answer}")