def solution(participant, completion):
    data = dict()

    for p in participant:
        data[p] = data.get(p, 0) + 1

    for c in completion:
        if c in data.keys():
            data[c] -= 1

    for p in participant:
        if data[p] != 0:
            return p