def solution(food):
    answer = ''
    li = []
    for i in range(1, len(food)):
        if food[i] % 2 != 0:
            food[i] -= 1
        food[i] //= 2
        li.append(str(i)*food[i])
    answer += ''.join(li) + '0' + ''.join(reversed(li))
    return answer