n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    ho = c//a + 1
    if c%a == 0:
        print(a, end = "")
        ho -= 1
    else:
        print(c%a, end="")

    if ho >=10:
        print(ho)
    else:
        print("0" + str(ho))