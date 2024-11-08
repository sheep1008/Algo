import sys
input = sys.stdin.read
data = input().splitlines()

for i in data:
    if i[0] == '.':
        break
    
    stk = []
    balanced = True
    
    for j in i:
        if j == '(' or j == '[':
            stk.append(j)
        elif j == ')':
            if stk and stk[-1] == '(':
                stk.pop()
            else:
                balanced = False
                break
        elif j == ']':
            if stk and stk[-1] == '[':
                stk.pop()
            else:
                balanced = False
                break

    if balanced and not stk:
        print("yes")
    else:
        print("no")
