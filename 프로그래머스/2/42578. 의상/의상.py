def solution(clothes):
    data = dict()
    for k, p in clothes:
        data[k] = p
        
    data2 = dict()
    
    for key, value in data.items():
        data2[value] = data2.get(value, 0) + 1
    
    answer = 1
    for key, value in data2.items():
        answer *= (value+1)
    return answer -1 