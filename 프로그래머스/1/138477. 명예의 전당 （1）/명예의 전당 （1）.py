def solution(k, score):
    answer = []
    legend = []
    for s in score:
        if len(legend) >= k:
            if legend[-1] < s:
                legend[-1] = s
        else:
            legend.append(s)
        legend.sort(reverse = True)
        answer.append(legend[-1])
    return answer