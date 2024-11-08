a = input()
b = input()
c = input()
if a.isdigit():
    d = int(a)+3
    if d%5 ==0 and d%3 == 0:
        print("FizzBuzz")
    elif d %3 ==0:
        print("Fizz")
    elif d % 5 ==0:
        print("Buzz")
    else:
        print(d)
elif b.isdigit():
    d = int(b)+2
    if d%5 ==0 and d%3 == 0:
        print("FizzBuzz")
    elif d %3 ==0:
        print("Fizz")
    elif d % 5 ==0:
        print("Buzz")
    else:
        print(d)
elif c.isdigit():
    d = int(c)+1
    if d%5 ==0 and d%3 == 0:
        print("FizzBuzz")
    elif d %3 ==0:
        print("Fizz")
    elif d % 5 ==0:
        print("Buzz")
    else:
        print(d)