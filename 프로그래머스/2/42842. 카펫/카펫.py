def solution(brown, yellow):
    total_area = brown + yellow
    
    for h in range(3, int(total_area**0.5+1)):
        if total_area % h == 0:
            w = total_area // h
            
            if (w-2) * (h-2) == yellow:
                return [w, h]