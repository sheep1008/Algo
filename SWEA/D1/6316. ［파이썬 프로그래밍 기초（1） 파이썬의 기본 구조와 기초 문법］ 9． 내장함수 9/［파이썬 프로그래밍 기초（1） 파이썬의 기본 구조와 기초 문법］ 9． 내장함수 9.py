arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr1 = filter(lambda x: x%2==0, arr)
arr2 = list(map(lambda x:x**2, arr1))
print(arr2)