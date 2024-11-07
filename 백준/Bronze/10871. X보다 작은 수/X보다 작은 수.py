a, b = map(int, input().split())
c = list(map(int, input().split()))
answer = []
count = 0
for i in c:
    if i < b:
        answer.append(i)
for n in answer:
    print(n, end=' ')