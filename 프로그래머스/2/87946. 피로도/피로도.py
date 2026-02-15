from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for p in permutations(dungeons, len(dungeons)):
        current_k = k
        count = 0
        
        for min_need, spend in p:
            if current_k >= min_need:
                current_k -= spend
                count += 1
            else:
                break
                
        answer = max(answer, count)
    return answer