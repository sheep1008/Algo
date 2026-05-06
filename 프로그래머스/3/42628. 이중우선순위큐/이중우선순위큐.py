import heapq

def solution(operations):
    min_h, max_h = [], []
    counts = {}

    for op in operations:
        command, num = op.split()
        val = int(num)

        if command == 'I':
            heapq.heappush(min_h, val)
            heapq.heappush(max_h, -val)
            counts[val] = counts.get(val, 0) + 1

        elif val == 1:
            while max_h and counts.get(-max_h[0], 0) == 0:
                heapq.heappop(max_h)
            if max_h:
                n = -heapq.heappop(max_h)
                counts[n] -= 1

        else:
            while min_h and counts.get(min_h[0], 0) == 0:
                heapq.heappop(min_h)
            if min_h:
                n = heapq.heappop(min_h)
                counts[n] -= 1

    while max_h and counts.get(-max_h[0], 0) == 0:
        heapq.heappop(max_h)
    while min_h and counts.get(min_h[0], 0) == 0:
        heapq.heappop(min_h)

    if not min_h or not max_h:
        return [0, 0]

    return [-max_h[0], min_h[0]]