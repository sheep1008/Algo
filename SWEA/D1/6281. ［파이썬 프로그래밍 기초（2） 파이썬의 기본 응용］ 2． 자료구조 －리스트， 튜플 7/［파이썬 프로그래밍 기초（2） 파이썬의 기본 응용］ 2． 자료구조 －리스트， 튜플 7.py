num = int(input())
answer = [k for k in range(1, num+1) if num%k==0]
print(answer)