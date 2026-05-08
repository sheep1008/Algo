def is_prime(n):
    if n <2: return "소수가 아닙니다."
    for i in range(2, int(n**0.5)+1):
        if n%i == 0: return "소수가 아닙니다."
    return "소수입니다."

n = int(input())
print(is_prime(n))