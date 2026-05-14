T = int(input())
for t in range(1, T+1):
    arr = list(input().split())
    stack = []
    answer = 0
    for a in arr:
        if a.isdigit():
            stack.append(int(a))
        elif a == '.':
            if len(stack) == 1:
                answer = stack.pop()
            else:
                answer= 'error'
            break
        else:
            if len(stack) <2:
                answer = 'error'
                break
            beta = stack.pop()
            alpha = stack.pop()
            if a == '+':
                stack.append(alpha + beta)
            elif a == '-':
                stack.append(alpha-beta)
            elif a == '/':
                stack.append(alpha//beta)
            else:
                stack.append(alpha*beta)

    print(f"#{t} {answer}")