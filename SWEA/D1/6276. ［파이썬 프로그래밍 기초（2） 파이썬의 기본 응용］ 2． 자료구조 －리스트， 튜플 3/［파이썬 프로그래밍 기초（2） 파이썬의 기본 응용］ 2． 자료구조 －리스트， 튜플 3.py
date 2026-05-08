answer = []
for i in range(2, 10):
    arr = []
    for j in range(1, 10):
        num = i * j
        if num % 3 != 0 and num % 7 != 0:
        	arr.append(num)
    answer.append(arr)
print(answer)