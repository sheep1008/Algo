def solution(brown, yellow):
    for y_height in range(1, int(yellow ** 0.5) + 1):
        if yellow % y_height != 0:
            continue
        y_width = yellow // y_height
        if y_width < y_height:
            break
        
        if (y_width + 2) * (y_height + 2) == yellow + brown:
            return [y_width + 2, y_height + 2]