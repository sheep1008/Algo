import heapq

def solution(jobs):
    jobs_with_idx = []
    for i in range(len(jobs)):
        jobs_with_idx.append([jobs[i][0], jobs[i][1], i])
    jobs_with_idx.sort()
    
    answer, now, i = 0, 0, 0
    wait_queue = [] # 힙(우선순위)
    count = 0 # 마친 작업 수
    
    while count < len(jobs):
        while i < len(jobs) and jobs_with_idx[i][0] <= now:
            heapq.heappush(wait_queue, [jobs_with_idx[i][1], jobs_with_idx[i][0], jobs_with_idx[i][2]])
            i += 1
            
        if wait_queue:
            duration, request_time, idx = heapq.heappop(wait_queue)
            now += duration
            answer += (now - request_time)
            count += 1
        
        else:
            now = jobs_with_idx[i][0]
            
    return answer // len(jobs)