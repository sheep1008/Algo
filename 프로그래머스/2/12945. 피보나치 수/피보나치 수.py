def solution(n):
    answer = 0
    a = 0
    b = 1
    for i in range(n+1):
        if i == 0:
            answer = 0
        elif i == 1:
            answer = 1
        else:
            answer = a + b
            a = b
            b = answer
    return answer % 1234567