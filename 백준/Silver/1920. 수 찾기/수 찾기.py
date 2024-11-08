import sys
input = sys.stdin.read
data = input().splitlines()
n = int(data[0])
a = set(map(int, data[1].split()))
m = int(data[2])
check = list(map(int, data[3].split()))

for i in range(len(check)):
    if check[i] in a:
        print(1)
    else:
        print(0)