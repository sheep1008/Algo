import sys
input = sys.stdin.read
data = input().splitlines()

my_dict = {}

for key in map(int, data[1].split()):
    if key in my_dict:
        my_dict[key] += 1
    else:
        my_dict[key] = 1

result = []
for key in map(int, data[3].split()):
    if key in my_dict:
        result.append(str(my_dict[key]))
    else:
        result.append("0")

print(" ".join(result))
