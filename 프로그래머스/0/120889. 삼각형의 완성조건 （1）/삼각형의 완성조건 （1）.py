def solution(sides):
    answer = 0
    max_num = max(sides)
    left = sum(sides) - max_num
    if (max_num >= left):
        answer = 2
    else:
        answer = 1
    return answer