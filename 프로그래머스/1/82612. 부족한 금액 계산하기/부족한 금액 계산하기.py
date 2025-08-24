def solution(price, money, count):
    fee = 0
    a = price
    for i in range(count):
        fee += a
        a = (i+2) * price
    if fee > money:
        answer = fee - money
    else:
        answer = 0
        
    return answer