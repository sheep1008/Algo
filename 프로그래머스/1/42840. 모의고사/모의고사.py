def solution(answers):
    student = [0, 0, 0]
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    r = []
    for i, answer in enumerate(answers):
        if answer == a[i%len(a)]:
            student[0] += 1
        if answer == b[i%len(b)]:
            student[1] += 1
        if answer == c[i%len(c)]:
            student[2] += 1
    max_score = max(student)
    for i in range(len(student)):
        if student[i] == max_score:
            r.append(i+1)
    return r