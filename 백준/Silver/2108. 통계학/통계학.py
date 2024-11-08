from collections import Counter

def find_most(l):
    counter = Counter(l)
    max_frequency = counter.most_common(1)[0][1]
    most_common_values = [num for num, freq in counter.items() if freq == max_frequency]
    most_common_values.sort()
    if len(most_common_values) == 1:
        return most_common_values[0]
    else:
        return most_common_values[1]

import sys
input = sys.stdin.read
data = input().splitlines()
n = int(data[0])
l = [int(data[i]) for i in range(1, len(data))]

print(round(sum(l) / len(l)))
l.sort()
print(l[len(l) // 2])
print(find_most(l))
print(max(l) - min(l))
