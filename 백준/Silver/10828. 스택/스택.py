import sys
input = sys.stdin.read

stk = []
data = input().splitlines()
a = int(data[0])

for i in range(1, a + 1):
    b = data[i]
    if "push" in b:
        _, d = b.split()
        stk.append(d)
    elif b == "pop":
        if len(stk) == 0:
            print(-1)
        else:
            print(stk.pop())
    elif b == "size":
        print(len(stk))
    elif b == "empty":
        print(1 if len(stk) == 0 else 0)
    elif b == "top":
        if len(stk) == 0:
            print(-1)
        else:
            print(stk[-1])