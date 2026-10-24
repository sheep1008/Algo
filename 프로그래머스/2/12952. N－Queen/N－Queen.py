def getAns(end, row, width, right_up, left_down):
    if row == end:
        return 1
    ans = 0
    
    for col in range(len(width)):
        if width[col] or right_up[row+col] or left_down[row-col+end]:
            continue
        width[col] = right_up[row+col] = left_down[row-col+end] = True
        ans += getAns(end, row+1, width, right_up, left_down)
        width[col] = right_up[row+col] = left_down[row-col+end] = False
    
    return ans

def solution(n):
    ans = getAns(n, 0, [False]*n, [False]*(n*2), [False]*(n*2))
    
    return ans