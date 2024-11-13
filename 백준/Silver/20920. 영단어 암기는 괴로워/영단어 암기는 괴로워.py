import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())  # O(1)
li = [data[i] for i in range(1, n + 1) if len(data[i]) >= m]  # O(n)

# 각 단어의 빈도를 사전에 저장
frequency = {}
for word in li:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# 가장 높은 빈도수를 구하고, 빈도별로 단어를 분류
max_count = 0
dictionary = {}
for word, count in frequency.items():
    if count > max_count:
        max_count = count
    if count in dictionary:
        dictionary[count].append(word)
    else:
        dictionary[count] = [word]

# 가장 높은 빈도부터 출력
for i in range(max_count, 0, -1):
    if i in dictionary:
        len_li = {}
        max_len = 0

        # 단어 길이를 기준으로 분류
        for word in dictionary[i]:
            length = len(word)
            if length > max_len:
                max_len = length
            if length in len_li:
                len_li[length].append(word)
            else:
                len_li[length] = [word]

        # 가장 긴 길이부터 사전순 출력
        for j in range(max_len, 0, -1):
            if j in len_li:
                len_li[j].sort()
                for k in len_li[j]:
                    print(k)
