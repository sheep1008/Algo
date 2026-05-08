results = []
for n in range(100, 301):
    s = str(n)
    count = 0
    for c in s:
        c = int(c)
        if c % 2 != 0:
            break
        count += 1
    if count == 3:
        results.append(s)
print(','.join(results))