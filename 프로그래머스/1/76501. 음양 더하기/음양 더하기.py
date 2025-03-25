def solution(absolutes, signs):
    answer=0
    index = 0
    for bool in signs:
        if bool:
            answer += absolutes[index]
        else:
            answer -= absolutes[index]
        index+=1
    return answer