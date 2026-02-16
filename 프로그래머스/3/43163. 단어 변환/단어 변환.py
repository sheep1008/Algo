from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = set()
    
    while queue:
        current_word, step = queue.popleft()
        
        if current_word == target:
            return step
        
        for word in words:
            if word not in visited:
                diff_count = 0
                for i in range(len(begin)):
                    if current_word[i] != word[i]:
                        diff_count += 1
                        
                if diff_count == 1:
                    visited.add(word)
                    queue.append((word, step + 1))
    return 0