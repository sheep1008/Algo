def solution(n):
    answer = 0
    sq = int(n**0.5)
    if sq * sq == n:
        answer = 1
    else:
        answer = 2
    return answer