while(1):
    li = list(map(int, input().split()))
    if (li[0], li[1], li[2]) == (0, 0, 0):
        break
    li.sort()
    if li[0]**2 + li[1]**2 == li[2]**2:
        print("right")
    else: print("wrong")