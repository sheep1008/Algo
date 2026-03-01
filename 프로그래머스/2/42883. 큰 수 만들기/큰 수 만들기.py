def solution(number, k):
    stack = []
    
    for num in number:
        # 1. 보충 포인트: 스택에 숫자가 있고, 아직 지울 횟수(k)가 남았을 때
        # 현재 숫자(num)가 스택 맨 위의 숫자보다 크면, 스택 안의 작은 숫자를 계속 제거
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1 # 숫자를 하나 지웠으므로 k 감소
            
        stack.append(num)
    
    # 2. 보충 포인트: 루프가 끝났는데도 k가 남은 경우 (예: "987", k=1)
    # 이미 내림차순 정렬된 상태이므로 뒤에서부터 남은 k만큼 잘라냄
    if k > 0:
        stack = stack[:-k]
        
    return "".join(stack)