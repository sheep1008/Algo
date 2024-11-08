def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

a, b = map(int, input().split())
if b > a:
    a, b = b,a
g = gcd(a,b)
print(g)
print(int(a*b/g))