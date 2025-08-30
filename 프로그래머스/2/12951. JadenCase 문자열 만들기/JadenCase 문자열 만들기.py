def solution(s):
    answer = ''
    li = s.split(' ')
    for w in li:
        for i, v in enumerate(w):
            if i == 0:
                if v.islower():
                    answer += v.upper()
                else:
                    answer += v
            else:
                if v.isupper():
                    answer += v.lower()
                else:
                    answer += v
        answer += ' '
    answer = answer[:-1]
    return answer