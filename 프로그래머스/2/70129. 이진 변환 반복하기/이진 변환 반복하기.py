def solution(s):
    answer = [0, 0]
    while not (s == '1'):
        answer[0] += 1
        answer[1] += s.count('0')
        rm = s.replace('0', '')
        length = len(rm)
        li = []
        while length > 1:
            li.append(str(length%2))
            length //= 2
        li.append(str(length))
        li.reverse()
        s = ''.join(li)
    return answer