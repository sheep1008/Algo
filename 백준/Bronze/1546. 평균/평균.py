a = int(input())
arr = list(map(int,input().split()))
max_score=max(arr)
new = []
for i in range(a):
    new.append(arr[i]/max_score*100)
print(sum(new)/a)