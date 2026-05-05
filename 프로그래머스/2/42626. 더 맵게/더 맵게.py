import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville[0] < K:
        count += 1
        if len(scoville) < 2:
            return -1
        
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        
        new = a + 2*b
        
        heapq.heappush(scoville, new)
    return count