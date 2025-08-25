def solution(d, budget):
    answer = 0
    possible = 0
    d.sort()
    for i, v in enumerate(d):
        if possible + v > budget:
            break
        possible += v
        answer += 1
    return answer