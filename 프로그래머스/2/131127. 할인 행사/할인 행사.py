"""
1. 첫째날부터 하나씩 뺀다.
2. 그렇지 않다면 둘째날
3. 그래서 10일을 만들 수 있는 날까지 체크하며 가능한지 체크
4. 제일 앞에 있는 것만 추가하고 다시 복원하면
"""
def solution(want, number, discount):
    want_dict = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
        
    answer = 0
    
    for i in range(len(discount) - 9):
        discount_10d = {}
        
        for j in range(i, i+10):
            if discount[j] in want_dict:
                discount_10d[discount[j]] = discount_10d.get(discount[j], 0) + 1
        if discount_10d == want_dict:
            answer += 1
    return answer