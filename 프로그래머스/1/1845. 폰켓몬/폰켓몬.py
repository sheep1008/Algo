def solution(nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1
        
    return min(len(nums)//2, len(dic))