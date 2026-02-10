from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    
    days = deque([math.ceil((100-p)/s) for p, s in zip(progresses, speeds)])
    
    while days:
        first_job = days.popleft()
        count = 1
        
        while days and days[0] <= first_job:
            days.popleft()
            count += 1
        
        answer.append(count)
    return answer