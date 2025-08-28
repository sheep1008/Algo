def solution(array, commands):
    answer = []
    for c in commands:
        start = c[0]
        end = c[1]
        k = c[2]
        li = array[start-1:end]
        li.sort()
        answer.append(li[k-1])
    return answer