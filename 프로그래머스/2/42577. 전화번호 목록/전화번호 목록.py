def solution(phone_book):
    data = dict()
    
    for p in phone_book:
        data[p] = True
    
    for d in data:
        prefix = ''
        for c in d:
            prefix += c
            if prefix in data and prefix != d:
                return False
    return True