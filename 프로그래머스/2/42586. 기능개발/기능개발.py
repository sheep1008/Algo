from collections import deque

def solution(progresses, speeds):
    # 1. 각 기능별 남은 일수 계산하여 큐에 저장
    # (100 - p) / s 를 올림한 값
    days = deque([-( (p - 100) // s ) for p, s in zip(progresses, speeds)])
    
    answer = []
    
    while days:
        # 2. 현재 배포의 기준이 되는 '가장 앞선 작업' 꺼내기
        first = days.popleft()
        count = 1
        
        # 3. 뒤의 작업들이 기준(first)보다 빨리 끝난다면 같이 배포
        while days and days[0] <= first:
            days.popleft()
            count += 1
            
        # 4. 이번 배포에 포함된 기능 개수 저장
        answer.append(count)
        
    return answer