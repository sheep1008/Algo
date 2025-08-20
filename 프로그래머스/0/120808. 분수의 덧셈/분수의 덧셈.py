def lcm(a,b):
    for i in range(max(a,b), a*b+1):
        if i % a == 0 and i % b == 0:
            return i
        
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(numer1, denom1, numer2, denom2):
    answer = []
    m = lcm(denom1, denom2)
    n1 = numer1 * (m//denom1)
    n2 = numer2 * (m//denom2)
    s = n1 + n2
    g = gcd(m, s)
    m //= g
    s //=g
    answer.append(s)
    answer.append(m)
    return answer