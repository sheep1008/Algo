def solution(s, n):
    answer = ''
    for c in s:
        if c ==' ':
            answer += ' '
        elif 'A'<=c<='Z':
            word = ord(c) + n
            if word > ord('Z'):
                word -= 26
            answer += chr(word)
        elif 'a' <=c<= 'z':
            word = ord(c) + n
            if word > ord('z'):
                word -= 26
            answer += chr(word)
        
    return answer