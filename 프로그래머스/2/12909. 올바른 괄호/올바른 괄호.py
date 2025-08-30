def solution(s):
    li = []
    for c in s:
        if c == '(':
            li.append(c)
        else:
            if not li:
                return False
            elif li[-1] == '(':
                li.pop()
                
    return not li