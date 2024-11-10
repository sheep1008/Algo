from collections import deque
import sys
input = sys.stdin.read
data = input().splitlines()
d = deque()
n = int(data[0])
for i in range(1, len(data)):
    if "push" in data[i]:
        _, b = data[i].split()
        d.append(b)
    elif data[i] == "pop":
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif data[i] == "size":
        print(len(d))
    elif data[i] == "empty":
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif data[i] == "front":
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif data[i] == "back":
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])