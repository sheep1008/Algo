def solution(participant, completion):
    data = dict()
    for p in participant:
        if p not in data:
            data[p] = 1
        else:
            data[p] += 1
    
    for c in completion:
        data[c] -= 1
        
    for key, val in data.items():
        if val == 1:
            return key