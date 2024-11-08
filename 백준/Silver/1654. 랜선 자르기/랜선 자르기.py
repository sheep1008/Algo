def find_sub(main_list, need):
    low = 1
    high = max(main_list)
    while low <= high:
        mid = (low + high) // 2
        l = [x // mid for x in main_list]
        if sum(l) >= need:
            low = mid + 1
        else:
            high = mid - 1
    return high

def find_max(main_list, mid, need):
    while True:
        l = [x // mid for x in main_list]
        if sum(l) < need:
            return mid - 1
        mid += 1

a, need = map(int, input().split())
main_list = [int(input()) for _ in range(a)]

mid = find_sub(main_list, need)
answer = find_max(main_list, mid, need)
print(answer)