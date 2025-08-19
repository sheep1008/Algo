def solution(my_string):
    answer = ''
    l = ['a', 'e', 'i', 'o', 'u']
    c =[]
    for v in my_string:
        if v not in l:
            c.append(v)
            
    answer = "".join(c)
    return answer