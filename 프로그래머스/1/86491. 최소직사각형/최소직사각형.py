def solution(sizes):
    maximum = []
    minimum = []
    for w, h in sizes:
        maximum.append(max(w, h))
        minimum.append(min(w, h))
        
    return max(maximum)*max(minimum)