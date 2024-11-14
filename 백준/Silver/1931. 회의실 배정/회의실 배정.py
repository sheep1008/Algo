n = int(input())
work =[]
for i in range(n):
    k = list(map(int, input().split()))
    work.append(k)

work.sort(key = lambda x: (x[1], x[0]))
possible = []

for i in range(n):
    if not possible:
        possible.append(work[i])
    
    else:
        if possible[-1][1] <= work[i][0]:
            possible.append(work[i])
print(len(possible))