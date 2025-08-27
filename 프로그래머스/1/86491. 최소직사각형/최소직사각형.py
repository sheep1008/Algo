def solution(sizes):
    w = 0
    h = 0
    for v in sizes:
        if max(v) > w:
            w = max(v)
        if min(v) > h:
            h = min(v)
    answer = w*h
    return answer