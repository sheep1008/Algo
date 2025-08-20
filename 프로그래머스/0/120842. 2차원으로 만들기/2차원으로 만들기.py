def solution(num_list, n):
    answer = []
    i = 0
    length = len(num_list)
    while i < length:
        answer.append(num_list[i:i+n])
        i+=n
    return answer