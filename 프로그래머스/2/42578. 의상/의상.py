def solution(clothes):
    data = {}
    
    for k, v in clothes:
        data[v] = data.get(v, 0) + 1
    
    answer = 1
    
    for n in data.values():
        answer *= (n+1)
    
    return answer - 1