from collections import deque
import math

def solution(progresses, speeds):
    days = deque([math.ceil((100-p)/s) for p, s in zip(progresses, speeds)])
    
    answer = []
    while days:
        first = days.popleft()
        count = 1
        
        while days and days[0] <= first:
            count += 1
            days.popleft()
        
        answer.append(count)
    return answer