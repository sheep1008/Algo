def solution(n):
    answer = 0
    a = 6
    while True:
        if a % n == 0:
            answer += 1
            break
        else:
            answer +=1
            a+=6
    return answer