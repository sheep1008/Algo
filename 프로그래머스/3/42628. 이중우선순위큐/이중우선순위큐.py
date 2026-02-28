import heapq

def solution(operations):
    min_h, max_h = [], []
    counts = {}
    
    for op in operations:
        command, val = op.split()
        num = int(val)
        
        if command == 'I':
            heapq.heappush(min_h, num)
            heapq.heappush(max_h, -num)
            counts[num] = counts.get(num, 0) + 1
        elif num == 1:
            while max_h and counts.get(-max_h[0], 0) == 0:
                heapq.heappop(max_h)
            if max_h:
                target = -heapq.heappop(max_h)
                counts[target] -= 1
        else:
            while min_h and counts.get(min_h[0], 0) == 0:
                heapq.heappop(min_h)
            if min_h:
                target = heapq.heappop(min_h)
                counts[target] -= 1
    while max_h and counts.get(-max_h[0], 0) == 0: heapq.heappop(max_h)
    while min_h and counts.get(min_h[0], 0) == 0: heapq.heappop(min_h)
    if not min_h or not max_h:
        return [0,0]
    return [-max_h[0], min_h[0]]