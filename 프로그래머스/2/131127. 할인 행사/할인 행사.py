"""
1. 첫째날부터 하나씩 뺀다.
2. 그렇지 않다면 둘째날
3. 그래서 10일을 만들 수 있는 날까지 체크하며 가능한지 체크
4. 제일 앞에 있는 것만 추가하고 다시 복원하면
"""
def solution(want, number, discount):
    answer = 0
    dic = dict()
    for idx in range(len(number)):
        dic[want[idx]] = number[idx]
        
    for idx in range(10):
        if discount[idx] in dic:
            dic[discount[idx]] -= 1
    
    start_idx = 0
    for idx in range(10, len(discount)):
        count = 0
        for value in dic.values():
            if value == 0:
                count += 1
        
        if count == len(number):
            answer += 1
        
        if discount[start_idx] in dic:
            dic[discount[start_idx]] += 1
        
        if discount[idx] in dic:
            dic[discount[idx]] -= 1
            
        start_idx += 1
        
    count = 0
    for value in dic.values():
        if value == 0:
            count += 1
    if count == len(number):
        answer += 1
    return answer