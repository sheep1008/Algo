"""
1. 연산할 때는 홀수이면 1을 더하고 2를 나눈 몫을 이용한다.
"""
def solution(n,a,b):
    answer = 0
    
    while a != b:
        a = (a+1) // 2
        b = (b+1) // 2
        answer += 1
        
    return answer