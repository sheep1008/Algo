def post_fix(s):
    stk=[]
    answer=""
    for i in range(len(s)):
        if 'A'<=s[i]<='z':
            answer+=s[i]
            continue
        if not stk:
            stk.append(s[i])
        else: 
            if s[i] =='(':
                stk.append(s[i])
            elif s[i]==')':
                while True:
                    a = stk.pop()
                    if a== '(':
                        break
                    answer+=str(a)
            elif s[i] =='*' or s[i] == '/':
                while stk:
                    a = stk.pop()
                    if a =='*' or a == '/':
                        answer+=a
                    else:
                        stk.append(a)
                        break
                stk.append(s[i])
            else:
                while stk:
                    a = stk.pop()
                    if a == '(':
                        stk.append(a)
                        break
                    answer+=a
                stk.append(s[i])
    while stk:
        answer+=stk.pop()
    return answer

s = input()
print(post_fix(s))