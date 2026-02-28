import heapq

def solution(jobs):
    jobs_with_idx = []
    for i in range(len(jobs)):
        jobs_with_idx.append([jobs[i][0], jobs[i][1], i])
    jobs_with_idx.sort()
    
    now, i, answer = 0, 0, 0
    count = 0
    wait_jobs = []
    
    while count < len(jobs):
        while i < len(jobs) and jobs_with_idx[i][0]<=now:
            heapq.heappush(wait_jobs, [jobs_with_idx[i][1], jobs_with_idx[i][0], jobs_with_idx[i][1]])
            i+=1
        
        if wait_jobs:
            d, r, index = heapq.heappop(wait_jobs)
            now += d
            answer += (now - r)
            count += 1
        else:
            now = jobs_with_idx[i][0]
            
    return answer//len(jobs)