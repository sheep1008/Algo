def solution(my_string):
    answer = ''
    l = list(my_string)
    a = []
    for i, v in enumerate(l):
        if v not in a:
            answer += v
            a.append(v)
        else:
            continue
    return answer