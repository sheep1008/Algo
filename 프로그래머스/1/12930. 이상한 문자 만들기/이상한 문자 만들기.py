def solution(s):
    answer = ''
    idx = 0  # 단어 내에서의 인덱스 (0부터 시작)

    for c in s:
        if c == ' ':  # 공백이면 그대로 추가 + 단어 인덱스 리셋
            answer += ' '
            idx = 0
        else:
            if idx % 2 == 0:
                answer += c.upper()
            else:
                answer += c.lower()
            idx += 1

    return answer