def solution(n, words):
    stack = []
    count = 0
    s = set()
    for start in range(0, len(words), n):
        count += 1
        for idx in range(start, start+n):
            if not stack:
                stack.append(words[idx])
                s.add(words[idx])
                continue
            if stack[-1][-1] == words[idx][0]:
                stack.append(words[idx])
                if words[idx] in s:
                    return [idx%n+1, count]
                s.add(words[idx])
            else:
                return [idx%n+1, count]

    return [0, 0]