def solution(prices):
    n = len(prices)
    # 1. 결과를 담을 배열을 0으로 초기화
    answer = [0] * n
    
    # 2. 각 시점의 가격을 하나씩 검사
    for i in range(n):
        # 3. 현재 시점(i) 이후의 가격들을 확인
        for j in range(i + 1, n):
            # 일단 1초가 흐른 것으로 간주
            answer[i] += 1
            # 4. 만약 가격이 떨어졌다면? 더 이상 검사하지 않고 중단!
            if prices[i] > prices[j]:
                break
                
    return answer