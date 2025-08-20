def solution(array):
    answer = 0
    count_arr = [0]*1000
    for i in array:
        count_arr[i] += 1
    m = max(count_arr)
    c = 0
    for index, n in enumerate(count_arr):
        if m == n:
            c += 1
            answer = index 
        
        if c > 1:
            answer = -1
    return answer