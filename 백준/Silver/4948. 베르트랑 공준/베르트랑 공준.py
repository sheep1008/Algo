import sys
input = sys.stdin.read
data = input().splitlines()
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

setting = set()
for i in range(123456*2, 0, -1):
    if is_prime(i):
        setting.add(i)

for i in range(len(data)):
    n = int(data[i])
    if n == 0: break
    answer = 0
    for j in range(n+1, 2*n+1):
        if j in setting:
            answer+=1
    print(answer)