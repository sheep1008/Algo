a = int(input())
b = int(input())
one = a * (b%10)
b = b//10
two = a * (b%10)
b = b//10
three = a*(b%10)
print(one)
print(two)
print(three)
print(one+two*10+three*100)