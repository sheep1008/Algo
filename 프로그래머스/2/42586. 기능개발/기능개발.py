"""
1. 제일 앞에 있는 작업이 며칠 걸리는지 계산
2. 앞에 거를 그 일수안에 뒤의 작업이 끝나는지 확인
3. 그렇다면 뽑고 그렇지 않을 때까지 반복
4. 1~3을 progresses가 빌 때까지 반복
"""
from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    
    queue = deque(progresses)
    speed_queue = deque(speeds)
    duration = 0
    while queue:
        count = 0
        duration = int(math.ceil((100 - queue[0]) / speed_queue[0]))
        while queue and queue[0] + duration * speed_queue[0] >= 100:
            count += 1
            queue.popleft()
            speed_queue.popleft()
        answer.append(count)
        
    return answer