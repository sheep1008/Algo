from collections import deque
import sys
input = sys.stdin.read
data = input().splitlines()
a= int(data[0])

for i in range(a):
    count=1
    n, check = map(int, data[2 * i + 1].split())
    li = list(map(int, data[2*i+2].split()))
    q = deque((li[j], j) for j in range(n))

    while q:
        if q[0][0] != max(q, key=lambda x: x[0])[0]:
            q.append(q.popleft())

        else:
            priority, idx = q.popleft()
            if idx == check:
                print(count)
                break
            count += 1