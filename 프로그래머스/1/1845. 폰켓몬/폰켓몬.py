import math

def solution(nums):
    data = dict()
    select = len(nums)//2
    count = 0
    
    for n in nums:
        data[n] = data.get(n, 0) + 1
        
    for key in data:
        count+=1
    
    if select <= count:
        answer = select
    else:
        answer = count
    
    return answer