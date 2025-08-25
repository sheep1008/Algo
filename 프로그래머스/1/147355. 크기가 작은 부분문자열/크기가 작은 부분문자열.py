def solution(t, p):
    answer = 0
    length_t = len(t)
    length_p = len(p)
    for i in range(length_t-length_p + 1):
        if int(p) >= int(t[i:i+length_p]):
            answer += 1
    return answer