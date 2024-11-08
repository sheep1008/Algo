import sys
input = sys.stdin.read

data = input().splitlines()
a, b = map(int, data[0].split())

s = []
index_map = {}

for i in range(1, a + 1):
    c = data[i]
    s.append(c)
    index_map[c] = i

for i in range(a + 1, a + b + 1):
    c = data[i]
    if c.isdigit():
        c = int(c)
        print(s[c - 1])
    else:
        print(index_map[c])
