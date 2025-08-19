def solution(numbers):
    answer = 0
    numbers.sort()
    length = len(numbers)
    s1 = numbers[0]*numbers[1]
    s2 = numbers[length-2] * numbers[length-1]
    if s1 > s2:
        answer = s1
    else:
        answer = s2
    return answer