import sys
input = sys.stdin.read
from functools import reduce

def gcd(a,b):
    if b>a :
        a,b = b,a
    if b == 0:
        return a
    return gcd(b, a % b)

def gcd_multiple(li):
    return reduce(gcd, li)

data = input().splitlines()
count = 0
n = int(data[0])
tree = [int(data[i]) for i in range(1, n+1)]
li=set()
for i in range(n-1):
    li.add(tree[i+1]- tree[i])
gap = gcd_multiple(list(li))

print((tree[n-1]-tree[0]) // gap + 1 - len(tree) )