n, m = map(int, input().split(','))
answer = []

for i in range(n):
    a = []
    for j in range(m):
        a.append(i*j)
    answer.append(a)
print(answer)