def solution(s):
    answer = 0
    dic = {'zero' : 0, 'one' : 1, 'two' : 2, 'three':3, 'four':4, 'five' : 5,
          'six' : 6, 'seven':7, 'eight':8, 'nine':9}
    check = ''
    for c in s:
        if c.isdigit():
            answer *= 10
            answer += int(c)
        else:
            check += c
            if check in dic:
                answer *= 10
                answer += dic[check]
                check = ''
        
    return answer