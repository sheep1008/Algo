def solution(n):
    answer = 0
    li = []
    while n >= 3:
        li.append(n%3)
        n //= 3
    li.append(n)
    li.reverse()
    for i, v in enumerate(li):
        answer += v*(3**i)
    return answer