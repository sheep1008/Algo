a = int(input())
b = int(input())
c = int(input())
gob = str(a*b*c)
for i in range(10):
    print(gob.count(str(i)))