import heapq

def solution(scoville, K):
    heap = []
    count = 0
    for s in scoville:
        heapq.heappush(heap, s)
    
    while True:
        if len(heap) == 1 and heap[0] < K:
            return -1
        
        else:
            if heap[0] < K:
                a = heapq.heappop(heap)
                b = heapq.heappop(heap)
                new_s = a+b*2
                heapq.heappush(heap, new_s)
                count+=1
            else:
                break
    return count