def solution(clothes):
    hash_map = {}
    arr = []
    answer = 1
    for c in clothes:
        a, b = c
        
        hash_map[b] = hash_map.get(b, 0) + 1
        
    for n in hash_map.values():
        arr.append(n)
        
    for a in arr:
        answer *= (a+1)
    
    return answer - 1