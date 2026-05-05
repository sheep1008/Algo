from collections import deque

def solution(priorities, location):
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    answer = 0
    
    while queue:
        first = queue.popleft()
        if any(first[0] < item[0] for item in queue):
            queue.append(first)
        else:
            answer+=1
            if location == first[1]:
                return answer