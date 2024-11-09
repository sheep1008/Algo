n, k = map(int, input().split())
li = []
answer =0
for i in range(n):
    a = int(input())
    li.append(a)
index = len(li)-1
while (k>0):
    if k - li[index] >= 0:
        answer += k//li[index]
        k -= li[index]*(k//li[index])
    index-=1
print(answer)