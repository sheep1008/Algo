def solution(people, limit):
    people.sort() # 1. 몸무게순 정렬 (필수)
    
    left = 0 # 가장 가벼운 사람의 인덱스
    right = len(people) - 1 # 가장 무거운 사람의 인덱스
    boats = 0
    
    while left <= right:
        # 2. 가장 무거운 사람 + 가장 가벼운 사람 조합 확인
        if people[left] + people[right] <= limit:
            left += 1 # 가벼운 사람도 태움
        
        # 3. 무거운 사람은 무조건 이번 보트에 탐
        right -= 1
        boats += 1
        
    return boats