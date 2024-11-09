max_n = 1000000

is_prime = [True] * (max_n+1)
is_prime[0] = is_prime[1] = False 

for i in range(2, int(max_n**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, max_n+1, i):
            is_prime[j] = False

def find_case(n):
    answer=0
    half = n//2
    for i in range(2, half+1):
        if is_prime[i] and is_prime[n-i]:
            answer+=1
    return answer

t = int(input())
for i in range(t):
    n = int(input())
    answer = find_case(n)
    print(answer)