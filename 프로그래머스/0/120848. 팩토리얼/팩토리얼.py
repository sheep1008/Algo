def solution(n):
    answer = 1
    a = 1
    while True:
        answer *= a 
        if answer > n:
            return a-1
        a+=1