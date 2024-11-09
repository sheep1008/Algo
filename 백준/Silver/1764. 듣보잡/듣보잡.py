a, b = map(int, input().split())
s_1 = set()
s_2 = set()
for i in range(a):
    name = input()
    s_1.add(name)
for i in range(b):
    name = input()
    s_2.add(name)
intersection_set = s_1 & s_2
li = list(intersection_set)
li.sort()
print(len(li))
for i in range(len(li)):
    print(li[i])