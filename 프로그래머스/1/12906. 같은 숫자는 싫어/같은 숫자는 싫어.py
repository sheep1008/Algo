def solution(arr):
    answer = []
    last = 0
    for i, v in enumerate(arr):
        if answer:
            if v != answer[last]:
                answer.append(v)
                last += 1
        else:
            answer.append(v)
    return answer