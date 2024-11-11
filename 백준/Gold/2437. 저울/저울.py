n = int(input())
weight = list(map(int, input().split()))
weight.sort()
sum = 0
flag = 0
if weight[0] != 1:
    print(1)
elif len(weight) == 1:
    print(2)
else:
    for i in range(0, n):
        if sum+1>=weight[i]:
            sum+=weight[i]
        else:
            print(sum+1)
            break

        if i == n-1:
            flag = 1

if flag == 1:
    print(sum+1)