a, b = map(int, input().split())
s_1 = set(list(map(int, input().split())))
s_2 = set(list(map(int, input().split())))
answer = 0
answer += len(s_1-s_2)
answer += len(s_2-s_1)
print(answer)