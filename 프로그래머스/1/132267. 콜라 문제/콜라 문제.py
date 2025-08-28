def solution(a, b, n):
    answer = 0
    bin_juice = n
    while bin_juice >= a:
        answer += (bin_juice//a) * b
        bin_juice = (bin_juice//a)*b + (bin_juice%a)
    return answer